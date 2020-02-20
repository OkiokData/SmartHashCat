from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputDefaultFiles", "tmp/default_lists_out.txt")
        self.filters = [
            filters['FilterWriteToSmartFileTemp'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartFile']
        ]
        self.user_list = attacker.user_list
        self.most_common_pass = attacker.most_common_pass
        self.modifier_list = attacker.modifier_list
    
    def run_child(self):
        Misc.copy_file_content_to_other_file(
            self.user_list, self.filter_transit_file, append=False)
        Misc.copy_file_content_to_other_file(
            self.modifier_list, self.filter_transit_file)
        Misc.copy_file_content_to_other_file(
            self.most_common_pass, self.filter_transit_file)
        return True