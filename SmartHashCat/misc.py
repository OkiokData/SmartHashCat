import datetime
import command_runner
import string


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

def get_rule_format_utf_8_letter(letter, is_append):
    hashcat_code = "$" if is_append else "^"
    if letter in string.ascii_letters:
        return f"{hashcat_code}{letter}"
    
    letter_bytes = letter.encode()
    
    if not is_append:
        letter_bytes = letter_bytes[::-1]
    
    to_return = []
    for i in letter_bytes:
        to_return.append(f"{hashcat_code}\\x{hex(i)[2:]}")
        
    return "".join(to_return)
