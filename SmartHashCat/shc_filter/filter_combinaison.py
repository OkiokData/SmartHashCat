from shc_filter.filter_abstract import FilterAbstract
import misc


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.user_list = attacker.user_list
        self.modifier_list = attacker.modifier_list
        self.attacker = attacker
        #misc.print_date_time()
        #print("Starting combinations")
        lines_1_len = sum(1 for x in self.get_lines_1())
        lines_2_len = sum(1 for x in self.get_lines_2())
        lines_3_len = sum(1 for x in self.get_lines_3())
        self.aprox_len = lines_1_len * lines_2_len * lines_3_len
        self.counter = 0

    def get_lines_1(self):
        for l in self.previous_input.get_results():
            yield l
    
    def get_lines_2(self):
        for l in open(self.user_list, "r"):
            yield l.strip().lower()

    def get_lines_3(self):
        for l in open(self.modifier_list, "r"):
            yield l.strip().lower()

    def get_results(self):
        misc.write_text_to_file(f"{str(self.counter)}/{str(self.aprox_len)} " + misc.return_formated_date_time(),
            self.attacker.final_output_file_progress, append=True)
        yielded_2 = False
        yielded_3 = False
        for l1 in self.get_lines_1():
            yield f"{l1}"
            for l2 in self.get_lines_2():
                if not yielded_2:
                    yield f"{l2}"
                yield f"{l1}{l2}"
                yield f"{l2}{l1}"
                for l3 in self.get_lines_3():
                    self.counter += 1
                    if self.counter % 1000000 == 0:
                        misc.write_text_to_file(f"{str(self.counter)}/{str(self.aprox_len)} " + misc.return_formated_date_time(),
                            self.attacker.final_output_file_progress, append=True)
                    if not yielded_3:
                        yield f"{l3}"
                    yield f"{l1}{l3}"
                    yield f"{l3}{l1}"
                    yield f"{l2}{l3}"
                    yield f"{l3}{l2}"
                    yield f"{l1}{l2}{l3}"
                    yield f"{l1}{l3}{l2}"
                    yield f"{l2}{l1}{l3}"
                    yield f"{l2}{l3}{l1}"
                    yield f"{l3}{l1}{l2}"
                    yield f"{l3}{l2}{l1}"
                yielded_3 = True
            yielded_2 = True
        misc.write_text_to_file(f"{str(self.counter)}/{str(self.aprox_len)} " + misc.return_formated_date_time(),
            self.attacker.final_output_file_progress, append=True)
