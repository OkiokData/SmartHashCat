from Phases.Phase import Phase
import CommandRunner
import sys


class Phase0(Phase):

    def __init__(self, hashes_file, custom_list, company_name, url, cewl_depth,
                 smart_file, session, final_output_file, show_when_done,
                 hashcat_hash_option, is_add_force_flag):
        super(Phase0, self).__init__(hashes_file, session, final_output_file,
                                     smart_file, show_when_done,
                                     hashcat_hash_option, is_add_force_flag)
        self.phase = 0
        self.custom_list = custom_list
        self.company_name = company_name
        self.url = url
        self.smart_file_temp = "tmp/SmartHCDict_temp.txt"
        self.custom_dict_en = "/usr/share/SmartHashCat/dict/words_en.txt"
        self.custom_dict_fr = "/usr/share/SmartHashCat/dict/words_fr.txt"
        self.user_list = "/usr/share/SmartHashCat/lists/user_list.txt"
        self.most_common_pass = "/usr/share/SmartHashCat/lists/"\
            "most_common_pass.txt"
        self.modifier_list = "/usr/share/SmartHashCat/lists/modifier_list.txt"
        self.cewl_file_output = "tmp/cewl_out.txt"
        self.cewl_depth = cewl_depth

    def run_child(self):
        print("Sending default data to dictionary")
        self.log_actual_phase_in_output_file(0)

        self.copy_file_content_to_other_file(
            self.user_list, self.smart_file_temp, append=False)
        self.copy_file_content_to_other_file(
            self.modifier_list, self.smart_file_temp)
        self.copy_file_content_to_other_file(
            self.most_common_pass, self.smart_file_temp)

        if self.custom_list:
            self.copy_file_content_to_other_file(
                self.custom_list, self.smart_file_temp)

        if not self.company_name:
            print("NO COMPANY NAME GIVEN (-n), WILL APPEND NOTHING TO THE "
                  "DICT FILE!!")
        else:
            self.write_text_to_file(self.company_name, self.smart_file_temp)

        self.copy_file_content_to_other_file(
            self.custom_dict_en, self.smart_file_temp)

        self.copy_file_content_to_other_file(
            self.custom_dict_fr, self.smart_file_temp)

        if self.url:
            print('Starting cewl. You can force stop anytime with '
                  '"CTRL+C"')
            CommandRunner.run_command("cewl -d " + self.cewl_depth +
                                      " -e -v " + self.url + " -w " +
                                      self.cewl_file_output,
                                      interuptable=True)
            self.print_date_time()
            self.copy_file_content_to_other_file(
                self.cewl_file_output, self.smart_file_temp)
        else:
            print("NO URL GIVEN (-u), SKIPPING CEWL!!")

        # Append everything to finish file
        self.copy_file_content_to_other_file(
            self.smart_file_temp, self.smart_file)

        with open(self.smart_file_temp, "r") as file:
            lines_1 = list(set([l.strip().lower() for l in file.readlines()]))
        with open(self.user_list, "r") as file:
            lines_2 = list(set([l.strip().lower() for l in file.readlines()]))
        with open(self.modifier_list, "r") as file:
            lines_3 = list(set([l.strip().lower() for l in file.readlines()]))

        total = 2 * len(lines_1) * len(lines_2) + 2 * len(lines_1) * \
            len(lines_3) + 2 * len(lines_2) * len(lines_3) \
            + 6 * len(lines_1) * len(lines_2) * len(lines_3)
        count = 0
        self.print_date_time()
        print("Starting combinations")
        sys.stdout.write("{} / {}\r".format(count, total))
        sys.stdout.flush()
        with open(self.smart_file, "a", 10000000) as file_smart:
            for l1 in lines_1:
                for l2 in lines_2:
                    file_smart.write("{}{}\n".format(l1, l2))
                    file_smart.write("{}{}\n".format(l2, l1))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l1 in lines_1:
                for l3 in lines_3:
                    file_smart.write("{}{}\n".format(l1, l3))
                    file_smart.write("{}{}\n".format(l3, l1))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l2 in lines_2:
                for l3 in lines_3:
                    file_smart.write("{}{}\n".format(l2, l3))
                    file_smart.write("{}{}\n".format(l3, l2))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l1 in lines_1:
                for l2 in lines_2:
                    for l3 in lines_3:
                        file_smart.write("{}{}{}\n".format(l1, l2, l3))
                        file_smart.write("{}{}{}\n".format(l1, l3, l2))
                        file_smart.write("{}{}{}\n".format(l2, l1, l3))
                        file_smart.write("{}{}{}\n".format(l2, l3, l1))
                        file_smart.write("{}{}{}\n".format(l3, l1, l2))
                        file_smart.write("{}{}{}\n".format(l3, l2, l1))
                        count += 6
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
        sys.stdout.write("{} / {}\n".format(count, total))
        sys.stdout.flush()
