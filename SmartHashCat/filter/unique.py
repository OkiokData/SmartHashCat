import command_runner
from filter.filter_abstract import FilterAbstract
import misc


class Filter(FilterAbstract):

    def __init__(self, attacker):
        super(Filter, self).__init__()
        self.filter_unique = self.get_new_tempfile_name()

    def get_new_tempfile_name(self):
        return "tmp/unique_out.txt"

    def run_child(self, filter_transit_file):
        misc.write_text_to_file("", self.filter_unique, False)
        for l1 in open(filter_transit_file):
            count = 0
            for l2 in open(self.filter_unique):
                if l1 == l2:
                    count += 1
            if count == 0:
                with open(self.filter_unique, 'a') as f:
                    f.write(l1)
        return self.filter_unique
                
