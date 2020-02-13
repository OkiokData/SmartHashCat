import CommandRunner


class Phase:

    def __init__(self, hashes_file, session, final_output_file, smart_file,
                 show_when_done, hashcat_hash_option, is_add_force_flag):
        self.hashes_file = hashes_file
        self.session = session
        self.final_output_file = final_output_file
        self.smart_file = smart_file
        self.show_when_done = show_when_done
        self.hashcat_hash_option = hashcat_hash_option
        self.is_add_force_flag = is_add_force_flag
        self.hashcat_path = "/usr/bin/hashcat"

    def run(self):
        self.print_date_time()
        self.run_child()
        self.print_date_time()

    def run_child(self):
        raise NotImplementedError("Not yet implemented!")

    def log_actual_phase_in_output_file(self, phase):
        CommandRunner.run_command('echo ' + str(phase) +
                                  ' > $HOME/.hashcat/sessions/' +
                                  self.session.replace('--session ', '') +
                                  '.phase', silent=True)
        CommandRunner.run_command(
            "echo Phase " + str(phase) + " starting " +
            self.return_formated_date_time() +
            " >> " + self.final_output_file, silent=True)

    def send_content_to_file(self, command, content, file_out, append=True):
        if append:
            CommandRunner.run_command(command + " " + content + " >> " +
                                      file_out, silent=True)
        else:
            CommandRunner.run_command(command + " " + content + " > " +
                                      file_out, silent=True)

    def copy_file_content_to_other_file(self, file_in, file_out, append=True):
        self.send_content_to_file("cat", file_in, file_out, append)

    def write_text_to_file(self, text, file_out, append=True):
        self.send_content_to_file("echo", text, file_out, append)

    def print_date_time(self):
        print(self.return_formated_date_time())

    def return_formated_date_time(self):
        import datetime
        return "Time: " + str(datetime.datetime.now())
