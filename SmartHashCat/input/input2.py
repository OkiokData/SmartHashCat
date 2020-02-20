from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultFiles", "tmp/default_lists_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['unique'],
            filters['write_to_smart_file'],
            filters['combinaison'],
            filters['write_to_smart_file']
        ]
        self.user_list = attacker.user_list
        self.most_common_pass = attacker.most_common_pass
        self.modifier_list = attacker.modifier_list
    
    def run_child(self):
        misc.copy_file_content_to_other_file(
            self.user_list, self.filter_transit_file, append=False)
        misc.copy_file_content_to_other_file(
            self.modifier_list, self.filter_transit_file)
        misc.copy_file_content_to_other_file(
            self.most_common_pass, self.filter_transit_file)
        return True