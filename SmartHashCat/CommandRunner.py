import subprocess
from threading import Timer
import os
import signal


def run_command(command, silent=False, return_value=False, time_out=None,
                interuptable=False, is_add_force_flag=False):
    if is_add_force_flag:
        command = command + " --force"

    if not silent:
        print("You can interact normally with the program!")
        print("Executing Command: " + command)
        if interuptable:
            print('Interuptable! Stop anytime by pressing "CTRL+C"')
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)

    timeout = False

    def kill_proc(timeout):
        timeout = True

    timer = Timer(time_out, kill_proc, [timeout])
    out = ""
    try:
        if time_out:
            timer.start()
        for line in iter(p.stdout.readline, b''):
            if time_out and not timer.is_alive():
                timeout = True
                os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                break

            out += line.rstrip().decode() + "\n"
            if not silent:
                print(">>> " + line.rstrip().decode())
    except KeyboardInterrupt:
        if interuptable:
            if not silent:
                print("Keyboard Interrupt")
        else:
            raise
    finally:
        timer.cancel()

    if return_value:
        if timeout:
            return None

        return out
