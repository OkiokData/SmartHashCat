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
        self.hashcat_path = '/usr/bin/hashcat'
        self.with_phase_zero = False

        self.custom_list = ""
        self.smart_file = "tmp/SmartHCDict.txt"
        self.smart_rule = "tmp/SmartHC.rule"
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

        p1 = Phase1(self)
        
        if self.custom_list:
            p1.files_to_run_rules_on.append(self.custom_list)

        p1.run()

    def attack_mask(self, phase_selection=2):
        pm = PhaseMask(self, phase_selection)
        pm.run()
