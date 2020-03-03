import command_runner
import misc


class Phase:

    def __init__(self, hashes_file, session, final_output_file, smart_file, smart_rule,
                 show_when_done, hashcat_hash_option, is_add_force_flag):
        self.hashes_file = hashes_file
        self.session = session
        self.final_output_file = final_output_file
        self.smart_file = smart_file
        self.smart_rule = smart_rule
        self.show_when_done = show_when_done
        self.hashcat_hash_option = hashcat_hash_option
        self.is_add_force_flag = is_add_force_flag
        self.hashcat_path = "/usr/bin/hashcat"

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
