from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCompanyName", "tmp/company_name_out.txt")
        self.filters = [
            filters['FilterWriteToSmartFileTemp'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartFile']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        Misc.write_text_to_file(self.company_name, self.filter_transit_file, append=False)
        return True