import CommandRunner


def run(force):
    timeout = 10*60
    if not force:
        CommandRunner.run_command(
            "hashcat --benchmark -m 1000 | tee -a Tests/results.txt", 
            silent=False, 
            return_value=True)
        return CommandRunner.run_command(
            "python3 SmartHashCat.py -n Example -u https://www.example.com -f Tests/hibp_subset.txt -m 1000 | tee -a Tests/results.txt", 
            silent=False, 
            return_value=True, 
            time_out=timeout)
    else:
        CommandRunner.run_command(
            "hashcat --benchmark --force -m 1000 | tee -a Tests/results.txt", 
            silent=False, 
            return_value=True)
        return CommandRunner.run_command(
        "python3 SmartHashCat.py -n Example -u https://www.example.com -f Tests/hibp_subset.txt -m 1000 --force | tee -a Tests/results.txt", 
        silent=False, 
        return_value=True, 
        time_out=timeout)
