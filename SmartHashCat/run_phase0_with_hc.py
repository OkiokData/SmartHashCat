#!/usr/bin/python3
import dynamic_loader
import misc
import sys


class Phase0Wrapper:

    def __init__(self, argv):
        self.final_output_file = argv[0] # outputs/final_output.txt
        self.cewl_depth = argv[1] # 1
        self.url = argv[2] # https://www.exemple.com
        self.company_name = argv[3] # exemple
        self.user_list = argv[4] # "/usr/share/SmartHashCat/lists/user_list.txt"
        self.most_common_pass = argv[5] # "/usr/share/SmartHashCat/lists/most_common_pass.txt"
        self.modifier_list = argv[6] # "/usr/share/SmartHashCat/lists/modifier_list.txt"

    def phase_zero(self):
        self.run_with_input()

    def run_with_input(self):
        self.filters = dynamic_loader.load_filter()
        self.inputs = dynamic_loader.load_input()
        for input_name in self.inputs:
            module = self.inputs[input_name]
            i = module.SHCInput(self, self.filters, self.final_output_file)
            string_to_show = "Phase 0 - input and filters for " + input_name + " starting "
            #print(string_to_show)
            misc.write_text_to_file(string_to_show +
                misc.return_formated_date_time(), self.final_output_file, append=True)
            i.run()
            if i.need_filters():
                previous = i
                for filter_module in i.filters:
                    f = filter_module.Filter(self, previous)
                    previous = f
                for l in previous.get_results():
                    print(l)

if __name__ == "__main__":
    p0 = Phase0Wrapper(sys.argv[1:])
    p0.run_with_input()