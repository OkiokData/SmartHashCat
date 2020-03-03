from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def get_results(self):
        '''
        This function returns the result(s) of the execution.
        It is preferable to use yield instead of return to avoid heavy memory usage
        '''
        raise NotImplementedError("Not yet implemented!")