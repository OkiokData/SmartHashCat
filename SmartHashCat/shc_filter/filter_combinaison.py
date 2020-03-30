from shc_filter.filter_abstract import FilterAbstract
import misc


class Filter(FilterAbstract):

    def __init__(self, attacker, previous_input):
        super(Filter, self).__init__(previous_input)
        self.attacker = attacker
        lines_1_len = sum(1 for x in self.get_lines_1())
        lines_2_len = sum(1 for x in self.get_lines_2())
        lines_3_len = sum(1 for x in self.get_lines_3())
        self.aprox_len = lines_1_len * lines_2_len * lines_3_len
        if self.aprox_len == 0:
            self.aprox_len = 1
        self.counter = 0

    def get_lines_1(self):
        for l in self.previous_input.get_results():
            yield l
    
    def get_lines_2(self):
        for l in open(self.attacker.user_list, "r"):
            yield l.strip().lower()

    def get_lines_3(self):
        for l in open(self.attacker.modifier_list, "r"):
            yield l.strip().lower()

    def write_and_display_status(self):
        time = misc.return_formated_date_time()
        percentage = int(self.counter / self.aprox_len) * 100
        text_to_display = f"Combination status: {str(self.counter)}/{str(self.aprox_len)} ({percentage}%) {time}"
        print(text_to_display)
        misc.write_text_to_file(text_to_display, self.attacker.final_output_file_progress, append=True)

    def get_results(self):
        self.write_and_display_status()
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
                        self.write_and_display_status()
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
                yielded_3 = True # We need to yield all lines in the file 3, not just 1, hence not in the if after yield
            yielded_2 = True# We need to yield all lines in the file 2, not just 1, hence not in the if after yield
        self.write_and_display_status()
