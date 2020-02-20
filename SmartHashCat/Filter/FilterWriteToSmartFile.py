import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc


class Filter(FilterAbstract):

    def __init__(self, attacker):
        super(Filter, self).__init__()
        self.smart_file = attacker.smart_file

    def get_new_tempfile_name(self):
        return ""

    def run_child(self, filter_transit_file):
        Misc.copy_file_content_to_other_file(
            filter_transit_file, self.smart_file)
        return filter_transit_file