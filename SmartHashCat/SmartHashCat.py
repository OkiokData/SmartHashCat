#!/usr/bin/python3
'''
   _____                      _   _    _           _      _____      _
  / ____|                    | | | |  | |         | |    / ____|    | |
 | (___  _ __ ___   __ _ _ __| |_| |__| | __ _ ___| |__ | |     __ _| |_
  \___ \| '_ ` _ \ / _` | '__| __|  __  |/ _` / __| '_ \| |    / _` | __|
  ____) | | | | | | (_| | |  | |_| |  | | (_| \__ \ | | | |___| (_| | |_
 |_____/|_| |_| |_|\__,_|_|   \__|_|  |_|\__,_|___/_| |_|\_____\__,_|\__|

    Initially designed by people at Okiok - https://www.okiok.com/
    Special thanks to Tristan Dostaler - https://github.com/tristandostaler
    Release to the public with love by Okiok
    https://github.com/OkiokData/SmartHashCat/

'''
import Attacker
import argparse
from argparse import RawTextHelpFormatter
import CommandRunner
import os
import string
import random


def get_usage():
    return '''
    smarthashcat -p <attack phase number> \
    [arguments needed for the choosen phase]\
    \n\nExamples:\n\
    \nComplete attack:\n\t\
    SmartHashCat.py -n Example -u https://www.example.com -f hashes.txt\
    \nComplete attack without CEWL:\n\t\
    smarthashcat -n Example -f hashes.txt\n\
    Start at Dictionnary attack phase and continue all the way to desesperate \
    mask attacks:\n\t\
    smarthashcat -p 1 -f hashes.txt'''


def get_description():
    return 'Smart HashCat cracker. Dictio are in '\
           '/usr/share/SmartHashCat/dict. Lists are in '\
           '/usr/share/SmartHashCat/lists'


def get_phase_help():
    return '''The attack phase to proceed with.

Available options:
0 - Dictionary generation phase
1 - Dictionary attack phase
2 - Brute force attack 1-6 lenght phase
3 - Quick mask attack phase
4 - Slow mask attack phase
5 - Slower mask attack phase (Starts with brute force attack 7-length)
6 - Desesperate mask attack phase
-1 - Phase 0 to Phase 6

'''


def get_workload_profile_help():
    return '''Enable a specific workload profile, see pool below

- [ Workload Profiles ] -

  # | Performance | Runtime | Power Consumption | Desktop Impact
 ===+=============+=========+===================+=================
  1 | Low         |   2 ms  | Low               | Minimal
  2 | Default     |  12 ms  | Economic          | Noticeable
  3 | High        |  96 ms  | High              | Unresponsive
  4 | Nightmare   | 480 ms  | Insane            | Headless

'''


def parse_args():
    usage = get_usage()
    description = get_description()

    parser = argparse.ArgumentParser(
        usage=usage, description=description,
        formatter_class=RawTextHelpFormatter)

    parser.add_argument('-n', '--company_name',
                        action='store', type=str, required=False,
                        help="The name of the company")
    parser.add_argument('-u', '--url',
                        action='store', type=str, required=False,
                        help='The URL of the company website to crawl with '
                             'cewl. (Skip CEWL if empty)')
    parser.add_argument('-m', '--hashcat_hash_type',
                        action='store', type=str, required=False,
                        help="The hash type to brute force. See hashcat doc.")
    parser.add_argument('-p', '--phase',
                        action='store', type=int, required=False,
                        help=get_phase_help(), default=-1)
    parser.add_argument('-o', '--smart_dict',
                        action='store', type=str, required=False,
                        help='The path to the dictionary to use for the phase '
                             '1. (default="tmp/SmartHCDict.txt")',
                        default="tmp/SmartHCDict.txt")
    parser.add_argument('--custom_list',
                        action='store', type=str, required=False,
                        help='The path to the custom list to use for the '
                             'phase 0.',
                        default="")
    parser.add_argument('-d', '--cewl_depth',
                        action='store', type=str, required=False,
                        help='The "depth" argument to pass to cewl. '
                             '(default="1")',
                        default='1')
    parser.add_argument('-f', '--hash_file', type=str, required=False,
                        help='The path to the file with the hashes to crack.')
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="Increase output verbosity (default=0)")
    parser.add_argument("-s", "--show", action="count", default=0,
                        help='If enabled, show the content of the output_file '
                             'when finished.')
    parser.add_argument("--clear", action="count", default=0,
                        help='If enabled, clear every temporary files.')
    parser.add_argument("--hashes", action="count", default=0,
                        help='If enabled, show all the hashes IDs (like 5600 '
                             'for NetNTLMv2).')
    parser.add_argument("--force", action="count", default=0,
                        help="If enabled, add's the --force flag to hashcat.")
    parser.add_argument('--session',
                        action='store', type=str, required=False,
                        help='Use this option to restore a previous session '
                             'from it session ID',
                        default='')
    parser.add_argument('--hashcat_path',
                        action='store', type=str, required=False,
                        help='Used when the default hashcat binary path is '
                             'not standard.',
                        default='/usr/bin/hashcat')
    parser.add_argument("-w", "--workload_profile", action="store", type=int,
                        default=3,
                        help=get_workload_profile_help())
    parser.add_argument('--test', action='count', default=0, required=False,
                        help='Use this option to run the standardized 10 min test.')
    args = parser.parse_args()
    return args


def print_hashcat_help_without_arguments(hashcat_path):
    help_text = CommandRunner.run_command(
        hashcat_path + " -h", silent=True, return_value=True)
    if not help_text:
        print("An error occured while getting hash modes. Please check your "
              "setup.")
    else:
        delimiter = '- [ Hash modes ] -'
        print(delimiter + (help_text.split(delimiter)
                           [1]).split('- [ Outfile Formats ] -')[0])


def get_random_token(length):
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(random.choice(alphabet) for i in range(length))


def print_error_and_usage_then_exit(error):
    print(get_usage())
    print(error)
    exit(1)


def main():
    args = parse_args()

    if args.clear and args.clear > 0:
        print("Clearing all unnecessary files!")
        CommandRunner.run_command("rm -R tmp/ > /dev/null", silent=True)
        CommandRunner.run_command("rm -R outputs/ > /dev/null", silent=True)
        CommandRunner.run_command(
            "rm -R $HOME/.hashcat > /dev/null", silent=True)
        CommandRunner.run_command("rmdir hashcat* > /dev/null", silent=True)
        CommandRunner.run_command("rm hashcat.* > /dev/null", silent=True)
        CommandRunner.run_command("rmdir hashcat* > /dev/null", silent=True)
        CommandRunner.run_command("rm hashcat.* > /dev/null", silent=True)
        CommandRunner.run_command("rm *.pyc > /dev/null", silent=True)
        CommandRunner.run_command(
            "rm custom_list.txt > /dev/null", silent=True)
        CommandRunner.run_command("rm -R __pycache__ > /dev/null", silent=True)
        print('Done!')
        exit(0)

    if args.test and args.test > 0:
        from Tests import RunTests
        result = RunTests.run((args.force and args.force > 0))
        print('Done!')
        exit(0)

    if args.hashes and args.hashes > 0:
        print_hashcat_help_without_arguments(args.hashcat_path)
        exit(1)

    if args.session:
        print("Restoring from session " + args.session)
        CommandRunner.run_command(
            args.hashcat_path + " --session " + args.session + " --restore",
            interuptable=True)
        phase = CommandRunner.run_command('cat $HOME/.hashcat/sessions/' +
                                          args.session + '.phase',
                                          interuptable=False,
                                          return_value=True, silent=True)
        args.phase = int(phase)

    attacker = Attacker.SmartHCAttacker()

    attacker.session = "--session " + get_random_token(8)

    if not os.path.exists('tmp'):
        CommandRunner.run_command("mkdir tmp", silent=True)
    if not os.path.exists('outputs'):
        CommandRunner.run_command("mkdir outputs", silent=True)

    if args.workload_profile < 0 or args.workload_profile > 4:
        print("The workload profile can only be 1 <= w <= 4")
        exit(1)
    else:
        attacker.workload_profile = args.workload_profile

    if args.company_name:
        attacker.company_name = args.company_name
    if args.url:
        attacker.url = args.url
    if args.cewl_depth:
        attacker.cewl_depth = args.cewl_depth
    if args.force and args.force > 0:
        attacker.is_add_force_flag = True

    if args.hashcat_hash_type:
        attacker.hashcat_hash_option = args.hashcat_hash_type
    else:
        hash_type = '5600'
        attacker.hashcat_hash_option = hash_type
        print("Using default hash type NetNTLMv2 (-m {})".format(
            hash_type))

    if args.show:
        attacker.show_when_done = args.show > 0

    if args.smart_dict:
        attacker.smart_file = args.smart_dict

    if args.custom_list:
        attacker.custom_list = args.custom_list

    if not args.hash_file:
        print_error_and_usage_then_exit(
            "Hash file path (-f) needed for phase 1 to 6!")
    else:
        attacker.hashes_file = args.hash_file

    if args.phase <= 0:
        if not args.company_name:
            print_error_and_usage_then_exit(
                "Company name (-n) needed for phase 0!")
        attacker.phase_zero()

    if args.phase <= 1:
        attacker.attack_dictio()

    for i in range(2, 7):
        if(args.phase <= i):
            attacker.attack_mask(phase_selection=i)


if __name__ == "__main__":
    main()
