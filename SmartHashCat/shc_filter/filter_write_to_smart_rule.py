from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.smart_rule = attacker.smart_rule
        self.has_been_written = False

    def get_results(self):
        if not self.has_been_written:
            self.has_been_written = True
            with open(self.smart_rule, 'a') as f:
                for line in self.previous_input.get_results():
                    f.write(f"{line}\n")
                    yield line
        else:
            for l in self.previous_input.get_results():
                yield l
