from shc_input.shc_input_abstract import SHCInputAbstract
import misc
import command_runner


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_unique'],
            filters['filter_write_to_smart_file']
        ]
        self.cewl_depth = attacker.cewl_depth
        self.url = attacker.url
        self.cewl_file = "tmp/cewl_out.txt"
    
    def run_child(self):
        print('Starting cewl. You can force stop anytime with '
                  '"CTRL+C"')
        command_runner.run_command("cewl -d " + self.cewl_depth +
                                    " -e -v " + self.url + " -w " +
                                    self.cewl_file,
                                    interuptable=True)
        misc.print_date_time()
    
    def get_results(self):
        with open(self.cewl_file, 'r') as f:
            for line in f:
                yield line
            