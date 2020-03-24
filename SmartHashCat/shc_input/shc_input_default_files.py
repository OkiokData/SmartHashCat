from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters, final_output_file):
        super(SHCInput, self).__init__(final_output_file)
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_combinaison']
        ]
        self.attacker = attacker
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.attacker.most_common_pass, 'r') as f:
            for line in f:
                yield line