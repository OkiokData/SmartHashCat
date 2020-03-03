from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def get_results(self):
        for l in self.previous_input.get_results():
            yield l.strip().lower()
