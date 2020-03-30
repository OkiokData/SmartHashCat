from phases.phase import Phase
import command_runner
import os


class Phase1(Phase):

    def __init__(self, attacker, phase0):
        super(Phase1, self).__init__(attacker)
        self.phase0 = phase0
        self.workload_profile = attacker.workload_profile
        self.rock_you_file = attacker.rock_you_file
        self.smart_file = attacker.smart_file
        self.is_add_force_flag = attacker.is_add_force_flag
        self.with_phase_zero = attacker.with_phase_zero
        self.hash_cat_rules_path = "/usr/share/hashcat/rules/"
        self.rules_to_run = [
                             self.hash_cat_rules_path + "leetspeak.rule",
                             self.hash_cat_rules_path + "best64.rule",
                             self.hash_cat_rules_path + "InsidePro-PasswordsPro.rule",
                             self.hash_cat_rules_path + "d3ad0ne.rule",
                             self.hash_cat_rules_path + "OneRuleToRuleThemAll.rule"
                             ]
        
        self.files_to_run_rules_on = [self.rock_you_file]

    def run_hashcat_with_rule_and_source_file(self, rule, source_file):
        command_runner.run_command(self.hashcat_path + " -m " +
                                  self.hashcat_hash_option + " -w " +
                                  str(self.workload_profile) + " " +
                                  self.session + " " + self.hashes_file +
                                  " " + source_file + " " + rule +
                                  " -o " + self.final_output_file,
                                  interuptable=True,
                                  is_add_force_flag=self.is_add_force_flag)

    def run_hashcat_with_rule_and_phase0(self, rule):
        for l in self.phase0.run_with_input_and_has_more():
            command_runner.run_command(self.hashcat_path + " -m " +
                                    self.hashcat_hash_option + " -w " +
                                    str(self.workload_profile) + " " +
                                    self.session + " " + self.hashes_file +
                                    " " + self.smart_file  + " " + rule +
                                    " -o " + self.final_output_file,
                                    interuptable=True,
                                    is_add_force_flag=self.is_add_force_flag)

    def run_hashcat_with_rule(self, rule):
        print("\nStarting hashcat " + str(rule) +
              " attacks (on all defined files, including SmartHCDict and "
              "Rockyou)")
        for file_to_run_on in self.files_to_run_rules_on:
            self.run_hashcat_with_rule_and_source_file(rule, file_to_run_on)
        
        if self.with_phase_zero:
            self.run_hashcat_with_rule_and_phase0(rule)
        

    def run_child(self):
        self.log_actual_phase_in_output_file(1)

        print('Starting attack!')
        
        for rule in self.rules_to_run:
            self.run_hashcat_with_rule(rule)

        if self.show_when_done:
            command_runner.run_command("cat " + self.final_output_file)
