from phases.phase import Phase
import command_runner
import imp
import os
import fnmatch
import dynamic_loader


class PhaseMask(Phase):

    def __init__(self, hashes_file, phase_selection, smart_file, smart_rule, session,
                 final_output_file, show_when_done, hashcat_hash_option,
                 is_add_force_flag):
        super(PhaseMask, self).__init__(hashes_file, session,
                                        final_output_file, smart_file, smart_rule,
                                        show_when_done, hashcat_hash_option,
                                        is_add_force_flag)

        self.phase_selection = phase_selection

        self.pure_brute_force_mask_start = "-1 ?a -2 ?a -3 ?a ?1"
        self.pure_brute_force_mask_middle = "?2"
        self.pure_brute_force_mask_end = "?3"

        self.masks_list = {}

        self.phase_to_speed_name = {
            3: "quick",
            4: "slow",
            5: "slower",
            6: "desesperate"
        }

        self.masks_list = dynamic_loader.load_mask()

    def launch_hashcat(self, min_length, max_length, mask_start, mask_middle,
                       mask_end):
        for i in range(min_length, max_length + 1):
            mask_complete = mask_start
            for j in range(0, i):
                mask_complete += mask_middle
            mask_complete += mask_end
            command_runner.run_command(self.hashcat_path + " -a 3 -w 3 " +
                                      self.session + " -m " +
                                      self.hashcat_hash_option + " " +
                                      self.hashes_file +
                                      " " + mask_complete + " -o " +
                                      self.final_output_file,
                                      interuptable=True,
                                      is_add_force_flag=self.is_add_force_flag)

    def run_child(self):
        self.log_actual_phase_in_output_file(self.phase_selection)

        if self.phase_selection < 2 or self.phase_selection > 6:
            print("Phases can only be 2 <= phase <= 6")
            exit(1)

        print('Starting mask attack! Stop anytime by pressing "CTRL+C".')
        if self.phase_selection == 2 or self.phase_selection == 5:
            mask_start = self.pure_brute_force_mask_start
            mask_middle = self.pure_brute_force_mask_middle
            if self.phase_selection == 2:
                print("\nStarting Brute force attack of 1-6 lenght passwords")
                mask_end = ""  # Leave empty so it run passwords of 1 lenght
                min_length = 0
            else:
                print("\nStarting Brute force attack of 7 lenght passwords")
                mask_end = self.pure_brute_force_mask_end
                min_length = 5
            max_length = 6
            self.launch_hashcat(min_length, max_length,
                                mask_start, mask_middle, mask_end)

        if self.phase_selection not in self.phase_to_speed_name:
            return

        print("\nStarting " +
              self.phase_to_speed_name[self.phase_selection] +
              " mask attack mode")
        for mask in self.masks_list:
            mask_start = self.masks_list[mask].start
            mask_middle = self.masks_list[mask].middle
            mask_end = self.masks_list[mask].end
            repeat_middle_min = self.masks_list[mask].length_groups[
                self.phase_to_speed_name[
                    self.phase_selection]]["repeat_middle_min"]
            repeat_middle_max = self.masks_list[mask].length_groups[
                self.phase_to_speed_name[
                    self.phase_selection]]["repeat_middle_max"]

            if repeat_middle_min == -1:
                print(mask + " not applicable for current phase, skipping")
            else:
                self.launch_hashcat(
                    repeat_middle_min, repeat_middle_max, mask_start,
                    mask_middle, mask_end)

        if self.show_when_done:
            command_runner.run_command("cat" + self.final_output_file)
