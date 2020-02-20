from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCustomList", "tmp/custom_list_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['unique'],
            filters['write_to_smart_file'],
            filters['combinaison'],
            filters['write_to_smart_file']
        ]
        self.custom_list = attacker.custom_list
    
    def run_child(self):
        if self.custom_list:
            misc.copy_file_content_to_other_file(
                    self.custom_list, self.filter_transit_file, append=False)
            return True
        return False
