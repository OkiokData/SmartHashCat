class FilterAbstract:

    def __init__(self, previous_input):
        self.need_to_clean_after_use = True
        self.previous_input = previous_input
        
    def get_results(self):
        raise NotImplementedError("Not yet implemented!")
