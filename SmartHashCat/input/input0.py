from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCeWL", "tmp/cewl_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['unique'],
            filters['write_to_smart_file'],
            filters['combinaison'],
            filters['write_to_smart_file']
        ]
        self.cewl_depth = attacker.cewl_depth
        self.url = attacker.url
    
    def run_child(self):
        print('Starting cewl. You can force stop anytime with '
                  '"CTRL+C"')
        command_runner.run_command("cewl -d " + self.cewl_depth +
                                    " -e -v " + self.url + " -w " +
                                    self.filter_transit_file,
                                    interuptable=True)
        misc.print_date_time()
        return True