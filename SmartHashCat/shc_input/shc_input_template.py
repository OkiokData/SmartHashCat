from shc_input.shc_input_abstract import SHCInputAbstract


class SHCInput(SHCInputAbstract):
    
    def __init__(self, attacker, filters):
        super(SHCInput, self).__init__()
        self.filters = [
            filters['filter_strip_and_lower'],
            filters['filter_unique'],
            filters['filter_write_to_smart_file']
        ]
    
    def run_child(self):
        '''
        This function run any logic that's needed to generate it's result.
        Many functions do nothing here because they return something static.
        An example of something done here is the input for cewl
        '''
        raise NotImplementedError("Not yet implemented!")
    
    def get_results(self):
        '''
        This function returns the result(s) of the execution.
        It is preferable to use yield instead of return to avoid heavy memory usage
        '''
        raise NotImplementedError("Not yet implemented!")
