from shc_input.shc_input_abstract import SHCInputAbstract
import misc
import command_runner
import os


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters, final_output_file):
        super(SHCInput, self).__init__(final_output_file)
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_unique'],
            filters['filter_combinaison'],
            #filters['filter_write_to_smart_file']
        ]
        self.cewl_depth = attacker.cewl_depth
        self.url = attacker.url
        self.cewl_file = "tmp/cewl_out.txt"
    
    def run_child(self):
        if not self.url:
            #print('No URL was specified. Skipping cewl...')
            misc.write_text_to_file('No URL was specified. Skipping cewl...', self.final_output_file, append=True)
            return
        
        misc.write_text_to_file('Starting cewl. You can force stop anytime with "CTRL+C"', self.final_output_file, append=True)
        if not os.path.exists(self.cewl_file):
            command_runner.run_command("cewl -d " + self.cewl_depth +
                                    " -e -v " + self.url + " -w " +
                                    self.cewl_file + " >> /dev/null",
                                    interuptable=True, silent=True)
        #misc.print_date_time()
    
    def get_results(self):
        if not self.url:
            return []
        with open(self.cewl_file, 'r') as f:
            for line in f:
                yield line
            
