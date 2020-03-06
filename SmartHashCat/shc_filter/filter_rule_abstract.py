from shc_filter.filter_abstract import FilterAbstract
import misc


class FilterRuleAbstract(FilterAbstract):

    def __init__(self, previous_input):
        super(FilterRuleAbstract, self).__init__(previous_input)
        
    def get_results(self):
        raise NotImplementedError("Not yet implemented!")
    
    def transform_to_prepend_hashcat_format(self, word):
        to_return = []
        for c in word[::-1]:
            to_return.append(misc.prepend_rule_format_utf_8_letter(c))
        return ''.join(to_return)

    def transform_to_apend_hashcat_format(self, word):
        to_return = []
        for c in word:
            to_return.append(misc.append_rule_format_utf_8_letter(c))
        return ''.join(to_return)
