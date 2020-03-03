from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_write_to_smart_file']
        ]
        self.user_list = attacker.user_list
        self.most_common_pass = attacker.most_common_pass
        self.modifier_list = attacker.modifier_list
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.user_list, 'r') as f:
            for line in f:
                yield line
        with open(self.modifier_list, 'r') as f:
            for line in f:
                yield line
        with open(self.most_common_pass, 'r') as f:
            for line in f:
                yield line