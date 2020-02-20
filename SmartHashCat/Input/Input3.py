from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCustomList", "tmp/custom_list_out.txt")
        self.filters = [
            filters['FilterWriteToSmartFileTemp'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartFile']
        ]
        self.custom_list = attacker.custom_list
    
    def run_child(self):
        if self.custom_list:
            Misc.copy_file_content_to_other_file(
                    self.custom_list, self.filter_transit_file, append=False)
            return True
        return False
