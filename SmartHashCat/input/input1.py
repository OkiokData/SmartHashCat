from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCompanyName", "tmp/company_name_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['unique'],
            filters['write_to_smart_file'],
            filters['combinaison'],
            filters['write_to_smart_file']
        ]
        self.company_name = attacker.company_name
    
    def run_child(self):
        misc.write_text_to_file(self.company_name, self.filter_transit_file, append=False)
        return True