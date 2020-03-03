from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def get_results(self):
        duplicates = []
        for l1 in self.previous_input.get_results():
            count = 0
            for l2 in self.previous_input.get_results():
                if l1 == l2:
                    count += 1
                    if count > 1:
                        break
            if count <= 1:
                yield l1
            elif l1 not in duplicates:
                duplicates.append(l1)
                yield l1
