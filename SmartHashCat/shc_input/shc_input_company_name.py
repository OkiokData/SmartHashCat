from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters, final_output_file):
        super(SHCInput, self).__init__(final_output_file)
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_combinaison']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        return
    
    def get_results(self):
        for val in [self.company_name]:
            yield val