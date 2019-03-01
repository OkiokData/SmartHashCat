import os
from Phases.Phase0 import Phase0
from Phases.Phase1 import Phase1
from Phases.PhaseMask import PhaseMask


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

    def phase_zero(self):
        is_rockyou_exists = os.path.exists(self.rock_you_file)

        if not is_rockyou_exists:
            print("The file " + self.rock_you_file +
                  " was not found! Maybe it is zipped?")
            exit(1)

        p0 = Phase0(self.hashes_file, self.custom_list, self.company_name,
                    self.url, self.cewl_depth,
                    self.smart_file, self.session, self.final_output_file,
                    self.show_when_done, self.hashcat_hash_option,
                    self.is_add_force_flag)
        p0.run()

    def attack_dictio(self):
        if not os.path.exists(self.smart_file):
            print("{} not present. Run Phase 0 to generate one or move on to "
                  "phase 2!".format(self.smart_file))
            exit(1)

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
