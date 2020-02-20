from Input.InputAbstract import InputAbstract
import Misc
import CommandRunner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputCeWL", "tmp/cewl_out.txt")
        self.filters = [
            filters['FilterWriteToSmartFileTemp'],
            filters['FilterUnique'],
            filters['FilterWriteToSmartFile'],
            filters['FilterCombinaison'],
            filters['FilterWriteToSmartFile']
        ]
        self.cewl_depth = attacker.cewl_depth
        self.url = attacker.url
    
    def run_child(self):
        print('Starting cewl. You can force stop anytime with '
                  '"CTRL+C"')
        CommandRunner.run_command("cewl -d " + self.cewl_depth +
                                    " -e -v " + self.url + " -w " +
                                    self.filter_transit_file,
                                    interuptable=True)
        Misc.print_date_time()
        return True