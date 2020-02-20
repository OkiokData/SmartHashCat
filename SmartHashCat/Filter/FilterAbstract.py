import CommandRunner


class FilterAbstract:

    def __init__(self):
        self.need_to_clean_after_use = True
        
    def run(self, filter_transit_file):
        return self.run_child(filter_transit_file)

    def cleanup_after_use(self):
        if self.need_to_clean_after_use and self.get_new_tempfile_name():
            CommandRunner.run_command("rm " + self.get_new_tempfile_name(), silent=True)

    def run_child(self, filter_transit_file):
        raise NotImplementedError("Not yet implemented!")
    
    def get_new_tempfile_name(self):
        raise NotImplementedError("Not yet implemented!")