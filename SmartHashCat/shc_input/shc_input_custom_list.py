from shc_input.shc_input_abstract import SHCInputAbstract
import misc
import os


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters, final_output_file):
        super(SHCInput, self).__init__(final_output_file)
        self.attacker = attacker
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_unique'],
            filters['filter_combinaison']
        ]
    
    def run_child(self):
        if not self.attacker.custom_list or not os.path.exists(self.attacker.custom_list):
            misc.write_text_to_file('No custom list was specified or file not existent. Skipping...', self.final_output_file, append=True)
        return
    
    def get_results(self):
        if not self.attacker.custom_list or not os.path.exists(self.attacker.custom_list):
            return []
        with open(self.attacker.custom_list, 'r') as f:
            for line in f:
                yield line
