'''
This is a mask template to design more masks.
Refer to this documentation: https://hashcat.net/wiki/doku.php?id=mask_attack
The mask is dynamically created with a for loop arround the middle mask for the
repeat_middle_min number up to the repeat_middle_max number.

Pseudo-code:
    for i each numbers in range(repeat_middle_min, repeat_middle_max):
        mask = start
        for j each numbers in range(0, i):
            mask += middle
        mask += end

Because of this logic, the total password length is equal to:
    the number of "?" in the start
    + the number of "?" in the middle for the actual j in the for loop (line 8)
    + the number of "?" in the end
'''
start = "-1 '?d~!@#$%&?' -2 ?u -3 ?l -4 ?d ?1?2"
middle = "?3"
end = "?4"
length_groups = {
    "quick": {"repeat_middle_min": 5, "repeat_middle_max": 7},
    "slow": {"repeat_middle_min": 7, "repeat_middle_max": 8},
    "slower": {"repeat_middle_min": -1, "repeat_middle_max": -1},
    "desesperate": {"repeat_middle_min": 8, "repeat_middle_max": 9}
}
