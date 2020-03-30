import os
from phases.phase0 import Phase0
from phases.phase1 import Phase1
from phases.phase_mask import PhaseMask


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
        self.hashcat_path = '/usr/bin/hashcat'
        self.with_phase_zero = False
        self.smart_file = 'tmp/SmartFile.txt'
        self.buffer_line_count = int((1024*1024*1024) / (20)) # 1GB / 20 characters per line

        self.custom_list = ""
        self.rock_you_file = "/usr/share/SmartHashCat/lists/rockyou.txt"
        self.final_output_file = "outputs/final_output.txt"

        self.user_list = "/usr/share/SmartHashCat/lists/user_list.txt"
        self.most_common_pass = "/usr/share/SmartHashCat/lists/most_common_pass.txt"
        self.modifier_list = "/usr/share/SmartHashCat/lists/modifier_list.txt"

    def check_rockyou(self):
        is_rockyou_exists = os.path.exists(self.rock_you_file)

        if not is_rockyou_exists:
            print("The file " + self.rock_you_file +
                  " was not found! Maybe it is zipped?")
            exit(1)

    def attack_dictio(self):
        self.check_rockyou()
        p0 = Phase0(self)
        p1 = Phase1(self, p0)
        p1.run()

    def attack_mask(self, phase_selection=2):
        pm = PhaseMask(self, phase_selection)
        pm.run()
