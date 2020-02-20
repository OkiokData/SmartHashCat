import command_runner
from filter.filter_abstract import FilterAbstract
import misc
import sys


class Filter(FilterAbstract):

    def __init__(self, attacker):
        super(Filter, self).__init__()
        self.new_run = False
        self.smart_file = attacker.smart_file
        self.user_list = attacker.user_list
        self.modifier_list = attacker.modifier_list
        self.combinaison_file = self.get_new_tempfile_name()

    def get_new_tempfile_name(self):
        return "tmp/combinaison_out.txt"

    def get_lines_1(self, filter_transit_file):
        for l in open(filter_transit_file, "r"):
            yield l.strip().lower()
    
    def get_lines_2(self):
        for l in open(self.user_list, "r"):
            yield l.strip().lower()

    def get_lines_3(self):
        for l in open(self.modifier_list, "r"):
            yield l.strip().lower()

    def run_child(self, filter_transit_file):
        misc.write_text_to_file("", self.combinaison_file, False)
        lines_1_count = 0
        lines_2_count = 0
        lines_3_count = 0
        for l in self.get_lines_1(filter_transit_file):
            lines_1_count += 1
        for l in self.get_lines_2():
            lines_2_count += 1
        for l in self.get_lines_3():
            lines_3_count += 1
        
        total = 2 * lines_1_count * lines_2_count + 2 * lines_1_count * \
            lines_3_count + 2 * lines_2_count * lines_3_count \
            + 6 * lines_1_count * lines_2_count * lines_3_count
        count = 0
        misc.print_date_time()
        print("Starting combinations")
        sys.stdout.write("{} / {}\r".format(count, total))
        sys.stdout.flush()
        with open(self.combinaison_file, "a", 10000000) as file_smart:
            for l1 in self.get_lines_1(filter_transit_file):
                for l2 in self.get_lines_2():
                    file_smart.write("{}{}\n".format(l1, l2))
                    file_smart.write("{}{}\n".format(l2, l1))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l1 in self.get_lines_1(filter_transit_file):
                for l3 in self.get_lines_3():
                    file_smart.write("{}{}\n".format(l1, l3))
                    file_smart.write("{}{}\n".format(l3, l1))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l2 in self.get_lines_2():
                for l3 in self.get_lines_3():
                    file_smart.write("{}{}\n".format(l2, l3))
                    file_smart.write("{}{}\n".format(l3, l2))
                    count += 2
                sys.stdout.write("{} / {}\r".format(count, total))
                sys.stdout.flush()
            for l1 in self.get_lines_1(filter_transit_file):
                for l2 in self.get_lines_2():
                    for l3 in self.get_lines_3():
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

        return self.combinaison_file