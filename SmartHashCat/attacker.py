import os
from phases.phase1 import Phase1
from phases.phase_mask import PhaseMask
import dynamic_loader
import misc


class SmartHCAttacker:

    def __init__(self):
        self.company_name = ""
        self.url = None
        self.hashcat_hash_option = None
        self.cewl_depth = '1'
        self.session = ""
        self.show_when_done = False
        self.is_add_force_flag = False
        self.workload_profile = 3
        self.hashes_file = ''

        self.custom_list = ""
        self.smart_file = "tmp/SmartHCDict.txt"
        self.rock_you_file = "/usr/share/SmartHashCat/lists/rockyou.txt"
        self.final_output_file = "outputs/final_output.txt"

        self.user_list = "/usr/share/SmartHashCat/lists/user_list.txt"
        self.most_common_pass = "/usr/share/SmartHashCat/lists/most_common_pass.txt"
        self.modifier_list = "/usr/share/SmartHashCat/lists/modifier_list.txt"

    def run_with_input(self):
        misc.write_text_to_file("", self.smart_file, False)
        self.filters = dynamic_loader.load_filter()
        self.inputs = dynamic_loader.load_input()
        for input_name in self.inputs:
            module = self.inputs[input_name]
            i = module.Input(self, self.filters)
            print("Runnin input and filters for " + i.name)
            if i.run_then_need_filters():
                for filter_module in i.filters:
                    f = filter_module.Filter(self)
                    i.filter_transit_file = f.run(i.filter_transit_file)
                for filter_module in i.filters:
                    f = filter_module.Filter(self)
                    f.cleanup_after_use()
            i.cleanup_after_use()

    def check_rockyou(self):
        is_rockyou_exists = os.path.exists(self.rock_you_file)

        if not is_rockyou_exists:
            print("The file " + self.rock_you_file +
                  " was not found! Maybe it is zipped?")
            exit(1)

    def check_smartfile(self):
        if not os.path.exists(self.smart_file):
            print("{} not present. Run Phase 0 to generate one or move on to "
                  "phase 2!".format(self.smart_file))
            exit(1)

    def phase_zero(self):
        self.check_rockyou()
        self.run_with_input()

    def attack_dictio(self):
        self.check_rockyou()
        self.check_smartfile()

        p1 = Phase1(self.hashes_file, self.workload_profile,
                    self.rock_you_file, self.smart_file, self.session,
                    self.final_output_file, self.show_when_done,
                    self.hashcat_hash_option, self.is_add_force_flag)
        p1.run()

    def attack_mask(self, phase_selection=2):
        pm = PhaseMask(self.hashes_file, phase_selection, self.smart_file,
                       self.session, self.final_output_file,
                       self.show_when_done, self.hashcat_hash_option,
                       self.is_add_force_flag)
        pm.run()
