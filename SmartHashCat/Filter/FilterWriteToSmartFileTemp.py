import CommandRunner
from Filter.FilterAbstract import FilterAbstract
import Misc


class Filter(FilterAbstract):

    def __init__(self, attacker):
        super(Filter, self).__init__()
        self.new_run = True
        self.smart_file_temp = self.get_new_tempfile_name()

    def get_new_tempfile_name(self):
        return "tmp/SmartHCDict_temp.txt"

    def run_child(self, filter_transit_file):
        if self.new_run:
            Misc.copy_file_content_to_other_file(
                filter_transit_file, self.smart_file_temp, append=False)
            self.new_run = False
        else:
            Misc.copy_file_content_to_other_file(
                filter_transit_file, self.smart_file_temp, append=True)
        return self.smart_file_temp