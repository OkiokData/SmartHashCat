class SHCInputAbstract:

    def __init__(self):
        self.filters = []

    def need_filters(self):
        return len(self.filters) > 0

    def run(self):
        self.run_child()

    def run_child(self):
        raise NotImplementedError("Not yet implemented!")
    
    def get_results(self):
        raise NotImplementedError("Not yet implemented!")