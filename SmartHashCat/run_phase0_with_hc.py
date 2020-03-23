import dynamic_loader
import misc
import sys


class Phase0Wrapper:

    def __init__(self, argv):
        self.smart_file = argv[0]
        self.final_output_file = argv[1]

    def phase_zero(self):
        self.run_with_input()

    def run_with_input(self):
        misc.write_text_to_file("", self.smart_file, False)
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