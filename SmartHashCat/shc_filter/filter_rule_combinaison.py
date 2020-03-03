from shc_filter.filter_abstract import FilterAbstract


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.new_run = False
        self.smart_file = attacker.smart_file
        self.user_list = attacker.user_list
        self.modifier_list = attacker.modifier_list
        #misc.print_date_time()
        print("Starting combinations")

    def get_lines_1(self):
        for l in self.previous_input.get_results():
            yield l
    
    def get_lines_2(self):
        for l in open(self.user_list, "r"):
            yield l.strip().lower()

    def get_lines_3(self):
        for l in open(self.modifier_list, "r"):
            yield l.strip().lower()

    def transform_to_prepend_hashcat_format(self, word):
        to_return = ""
        for c in word[::-1]:
            to_return += "^"+c
        return to_return

    def transform_to_apend_hashcat_format(self, word):
        to_return = ""
        for c in word:
            to_return += "$"+c
        return to_return

    def get_results(self):
        yield ":"
        for l1 in self.get_lines_1():
            yield f"{self.transform_to_prepend_hashcat_format(l1)} :"
            yield f": {self.transform_to_apend_hashcat_format(l1)}"

            for l2 in self.get_lines_2():
                yield f": {self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l2)}"
                yield f": {self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l1)}"

                yield f"{self.transform_to_prepend_hashcat_format(l1)} : {self.transform_to_apend_hashcat_format(l2)}"
                yield f"{self.transform_to_prepend_hashcat_format(l2)} : {self.transform_to_apend_hashcat_format(l1)}"

                yield f"{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l2)} :"
                yield f"{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l1)} :"

                for l3 in self.get_lines_3():
                    yield f": {self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l3)}"
                    yield f": {self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l2)}"
                    yield f": {self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l3)}"
                    yield f": {self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l1)}"
                    yield f": {self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l2)}"
                    yield f": {self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l1)}"

                    yield f"{self.transform_to_prepend_hashcat_format(l1)} : {self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l3)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l1)} : {self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l2)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)} : {self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l3)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)} : {self.transform_to_apend_hashcat_format(l3)}{self.transform_to_apend_hashcat_format(l1)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)} : {self.transform_to_apend_hashcat_format(l1)}{self.transform_to_apend_hashcat_format(l2)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)} : {self.transform_to_apend_hashcat_format(l2)}{self.transform_to_apend_hashcat_format(l1)}"
                    
                    yield f"{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l2)} : {self.transform_to_apend_hashcat_format(l3)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l3)} : {self.transform_to_apend_hashcat_format(l2)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l1)} : {self.transform_to_apend_hashcat_format(l3)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l3)} : {self.transform_to_apend_hashcat_format(l1)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l1)} : {self.transform_to_apend_hashcat_format(l2)}"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l2)} : {self.transform_to_apend_hashcat_format(l1)}"

                    yield f"{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l3)} :"
                    yield f"{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l2)} :"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l3)} :"
                    yield f"{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l1)} :"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l1)}{self.transform_to_prepend_hashcat_format(l2)} :"
                    yield f"{self.transform_to_prepend_hashcat_format(l3)}{self.transform_to_prepend_hashcat_format(l2)}{self.transform_to_prepend_hashcat_format(l1)} :"