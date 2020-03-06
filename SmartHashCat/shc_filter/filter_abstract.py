class FilterAbstract:

    def __init__(self, previous_input):
        self.previous_input = previous_input
        
    def get_results(self):
        raise NotImplementedError("Not yet implemented!")
