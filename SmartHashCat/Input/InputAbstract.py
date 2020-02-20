import CommandRunner


class InputAbstract:

    def __init__(self, input_name, filter_transit_file):
        self.filters = []
        self.name = input_name
        self.filter_transit_file = filter_transit_file
        self.initial_filter_transit_file = filter_transit_file
        self.need_to_clean_after_use = True

    def run_then_need_filters(self):
        return self.run_child()

    def run_child(self):
        raise NotImplementedError("Not yet implemented!")
    
    def cleanup_after_use(self):
        if self.need_to_clean_after_use:
            CommandRunner.run_command("rm " + self.initial_filter_transit_file, silent=True)
    