from Phases.Phase import Phase
import CommandRunner


class Phase1(Phase):

    def __init__(self, hashes_file, workload_profile, rock_you_file,
                 smart_file, session, final_output_file, show_when_done,
                 hashcat_hash_option, is_add_force_flag):
        super(Phase1, self).__init__(hashes_file, session, final_output_file,
                                     smart_file, show_when_done,
                                     hashcat_hash_option, is_add_force_flag)
        self.workload_profile = workload_profile
        self.rock_you_file = rock_you_file
        self.is_add_force_flag = is_add_force_flag
        self.hash_cat_rules_path = "/usr/share/hashcat/rules/"
        self.rules_to_run = ["leetspeak.rule",
                             "best64.rule",
                             "InsidePro-PasswordsPro.rule",
                             "d3ad0ne.rule",
                             "OneRuleToRuleThemAll.rule"
                             ]
        self.files_to_run_rules_on = [self.smart_file, self.rock_you_file]

    def run_hashcat_with_rule_and_source_file(self, rule, source_file):
        CommandRunner.run_command(self.hashcat_path + " -m " +
                                  self.hashcat_hash_option + " -w " +
                                  str(self.workload_profile) + " " +
                                  self.session + " " + self.hashes_file +
                                  " " + source_file + " -r " +
                                  self.hash_cat_rules_path + rule +
                                  " -o " + self.final_output_file,
                                  interuptable=True,
                                  is_add_force_flag=self.is_add_force_flag)

    def run_hashcat_with_rule(self, rule):
        print("\nStarting hashcat " + rule +
              " attacks (on all defined files, including SmartHCDict and "
              "Rockyou)")
        for file_to_run_on in self.files_to_run_rules_on:
            self.run_hashcat_with_rule_and_source_file(rule, file_to_run_on)

    def run_child(self):
        self.log_actual_phase_in_output_file(1)

        print('Starting attack!')

        for rule in self.rules_to_run:
            self.run_hashcat_with_rule(rule)

        if self.show_when_done:
            CommandRunner.run_command("cat " + self.final_output_file)
