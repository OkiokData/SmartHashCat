import command_runner
import misc


class Phase:

    def __init__(self, attacker):
        self.attacker = attacker
        self.hashes_file = attacker.hashes_file
        self.session = attacker.session
        self.final_output_file = attacker.final_output_file
        self.show_when_done = attacker.show_when_done
        self.hashcat_hash_option = attacker.hashcat_hash_option
        self.is_add_force_flag = attacker.is_add_force_flag
        self.hashcat_path = attacker.hashcat_path # "/usr/local/bin/hashcat"

    def run(self):
        misc.print_date_time()
        self.run_child()
        misc.print_date_time()

    def run_child(self):
        raise NotImplementedError("Not yet implemented!")

    def log_actual_phase_in_output_file(self, phase):
        command_runner.run_command('echo ' + str(phase) +
                                  ' > $HOME/.hashcat/sessions/' +
                                  self.session.replace('--session ', '') +
                                  '.phase', silent=True)
        command_runner.run_command(
            "echo Phase " + str(phase) + " starting " +
            misc.return_formated_date_time() +
            " >> " + self.final_output_file, silent=True)
