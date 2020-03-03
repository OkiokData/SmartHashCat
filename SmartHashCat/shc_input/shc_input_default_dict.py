from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_write_to_smart_file']
        ]
        self.custom_dict_en = "/usr/share/SmartHashCat/dict/1k_words_en.txt"
        self.custom_dict_fr = "/usr/share/SmartHashCat/dict/1k_words_fr.txt"
    
    def run_child(self):
        return
    
    def get_results(self):
        with open(self.custom_dict_en, 'r') as f:
            for line in f:
                yield line
        with open(self.custom_dict_fr, 'r') as f:
            for line in f:
                yield line