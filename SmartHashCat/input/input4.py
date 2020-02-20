from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultDict", "tmp/default_dict_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['unique'],
            filters['write_to_smart_file'],
            filters['combinaison'],
            filters['write_to_smart_file']
        ]
        self.custom_dict_en = "/usr/share/SmartHashCat/dict/1k_words_en.txt"
        self.custom_dict_fr = "/usr/share/SmartHashCat/dict/1k_words_fr.txt"
    
    def run_child(self):
        misc.copy_file_content_to_other_file(
            self.custom_dict_en, self.filter_transit_file, append=False)
        misc.copy_file_content_to_other_file(
            self.custom_dict_fr, self.filter_transit_file)
        return True