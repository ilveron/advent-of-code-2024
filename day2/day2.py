#!/usr/bin/python3
import os

def is_safe(levels):
    previous_difference = 0
    couple_remove_idx = 0
    for i in range(len(levels)-1):
        couple = (levels[i], levels[i+1])

        difference = couple[0] - couple[1]
        if previous_difference*difference < 0:  # if the ordering reverses
            return False
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        previous_difference = difference
    return True

def is_safe_with_problem_dampener(levels):
    previous_difference = 0
    couple_remove_idx = -1
    for i in range(len(levels)-1):
        couple = (levels[i], levels[i+1])

        difference = couple[0] - couple[1]
        if previous_difference*difference < 0:  # if the ordering reverses
            return is_safe(levels[0:i]+levels[i+1:])
        if abs(difference) < 1 or abs(difference) > 3:
            return is_safe(levels[0:i]+levels[i+1:]) or is_safe(levels[0:i+1]+levels[i+2:])
        previous_difference = difference
    return True

'''
def is_safe_with_problem_dampener(levels):
    is_increasing = True
    problem = False

    for i in range(len(levels)-1):
        couple = (levels[i], levels[i+1])

        if i == 0: 
            if couple[1] < couple[0]:
                is_increasing = False
        elif (couple[1] < couple[0] and is_increasing) or (couple[1] > couple[0] and not is_increasing):
            problem = True

        difference = abs(couple[0] - couple[1])
        if difference < 1 or difference > 3:
            problem = True
            
        if problem:
            first_idx = levels.index(couple[0])
            second_idx = levels.index(couple[1])
            levels_first_in_couple_removed = levels.copy()
            levels_second_in_couple_removed = levels.copy()
            del levels_first_in_couple_removed[first_idx]
            del levels_second_in_couple_removed[second_idx]
            if not is_safe(levels_first_in_couple_removed) or is_safe(levels_second_in_couple_removed):
                print(f"{levels} - {levels_first_in_couple_removed} - {levels_second_in_couple_removed}")
            return is_safe(levels_first_in_couple_removed) or is_safe(levels_second_in_couple_removed)
    return True
'''

def main():
    safe_reports = safe_reports_with_problem_dampener = 0

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            levels = [int(num) for num in line.split(" ")]
            if is_safe(levels):
                safe_reports += 1
                safe_reports_with_problem_dampener += 1
            elif is_safe_with_problem_dampener(levels):
                safe_reports_with_problem_dampener += 1

    print(f"part1: {safe_reports}")
    print(f"part2: {safe_reports_with_problem_dampener}")


if __name__ == '__main__':
    main()
