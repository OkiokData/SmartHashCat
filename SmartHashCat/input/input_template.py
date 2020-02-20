from input.input_abstract import InputAbstract
import misc
import command_runner


class Input(InputAbstract):
    
    def __init__(self, attacker, filters):
        super(Input, self).__init__("InputName", "tmp/template_out.txt")
        self.filters = [
            filters['write_to_smart_file_temp'],
            filters['write_to_smart_file'],
            filters['combinaison']
        ]
        ''' Put this variable to false if you don't want the filter_transit_file to be deleted '''
        self.need_to_clean_after_use = True
    
    def run_child(self):
        '''
        This function needs to return a boolean that tells the caller if he needs to run filter after.
        It's also a good idea to either send some empty string to the self.filter_transit_file 
            or send data with append=False for the first call to make sure the file is 
            overwritten at the next run.
        '''
        raise NotImplementedError("Not yet implemented!")
