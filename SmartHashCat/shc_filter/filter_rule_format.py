from shc_filter.filter_rule_abstract import FilterRuleAbstract
import misc


class Filter(FilterRuleAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)

    def get_results(self):
        yield ":"
        for l in self.previous_input.get_results():
            yield f"{self.transform_to_prepend_hashcat_format(l)} :"
            yield f": {self.transform_to_apend_hashcat_format(l)}"
