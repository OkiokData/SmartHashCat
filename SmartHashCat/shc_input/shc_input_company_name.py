from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_write_to_smart_file'],
            filters['filter_rule_combinaison'],
            filters['filter_write_to_smart_rule']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        return
    
    def get_results(self):
        for val in [self.company_name]:
            yield val