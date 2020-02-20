import datetime
import command_runner


def print_date_time():
    print(return_formated_date_time())

def return_formated_date_time():
    return "Time: " + str(datetime.datetime.now())

def send_content_to_file(command, content, file_out, append=True):
    if not append:
        command_runner.run_command(command + " " + content + " > " +
                                    file_out, silent=True)
    else:
        command_runner.run_command(command + " " + content + " >> " +
                                    file_out, silent=True)

def copy_file_content_to_other_file(file_in, file_out, append=True):
    send_content_to_file("cat", file_in, file_out, append)

def write_text_to_file(text, file_out, append=True):
    send_content_to_file("echo", text, file_out, append)
