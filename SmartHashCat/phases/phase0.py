#!/usr/bin/python3
import dynamic_loader
import misc
import sys
from phases.phase import Phase


class Phase0(Phase):

    def __init__(self, attacker):
        super(Phase0, self).__init__(attacker)
        self.final_output_file_progress = self.final_output_file.replace(".txt","") + "-progress.txt"
        self.cewl_depth = attacker.cewl_depth # 1
        self.url = attacker.url # https://www.exemple.com or "None" to skip cewl
        self.company_name = attacker.company_name # exemple
        self.user_list = attacker.user_list # "/usr/share/SmartHashCat/lists/user_list.txt"
        self.most_common_pass = attacker.most_common_pass # "/usr/share/SmartHashCat/lists/most_common_pass.txt"
        self.modifier_list = attacker.modifier_list # "/usr/share/SmartHashCat/lists/modifier_list.txt"
        self.custom_list = attacker.custom_list # ""
        self.smart_file = attacker.smart_file
        self.buffer_line_count = attacker.buffer_line_count

    def prepare_input_return_pipeline(self, input_name):
        module = self.inputs[input_name]
        i = module.SHCInput(self, self.filters, self.final_output_file)
        string_to_show = "Phase 0 - input and filters for " + input_name + " starting "
        print(string_to_show)
        misc.write_text_to_file(string_to_show +
            misc.return_formated_date_time(), self.final_output_file, append=True)
        misc.write_text_to_file(string_to_show +
            misc.return_formated_date_time(), self.final_output_file_progress, append=True)
        i.run()
        previous = i
        if i.need_filters():
            for filter_module in i.filters:
                f = filter_module.Filter(self, previous)
                previous = f
        return previous

    def run_buffered_pipeline_and_has_more(self, pipeline):
        line_counter = 0
        f = open(self.smart_file, 'w+')
        for l in pipeline.get_results():
            f.write(f'{l}\n')
            line_counter += 1
            if line_counter == self.buffer_line_count:
                f.flush()
                f.close()
                yield True
                f = open(self.smart_file, 'w+')
                line_counter = 0
        f.flush()
        f.close()
        
        yield line_counter != 0

    def run_with_input_and_has_more(self):
        self.filters = dynamic_loader.load_filter()
        self.inputs = dynamic_loader.load_input()
        for input_name in self.inputs:
            pipeline = self.prepare_input_return_pipeline(input_name)
            for yield_result in self.run_buffered_pipeline_and_has_more(pipeline):
                yield yield_result

        yield False

