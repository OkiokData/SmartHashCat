import command_runner
from filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker):
        ''' Here, define the temp file to save the data after the function if needed. '''
        super(Filter, self).__init__()
        ''' Put this variable to false if you don't want the new temporary file to be deleted '''
        self.need_to_clean_after_use = True

    def run_child(self, filter_transit_file):
        '''
        This function should return the new filter_transit_file after changes has been made.
        For example, if you modify the input file to have only unique values and store the result
            in a separated file, return the name of the separated file.
        If you only check that the number of line in the file is OK (aka no modification),
            return filter_transit_file
        '''
        raise NotImplementedError("Not yet implemented!")
    
    def get_new_tempfile_name(self):
        ''' 
        Use this function to return the new temp file used if it's the case.
        If not, return empty.
        '''
        return ""