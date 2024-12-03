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


def main():
    safe_reports = safe_reports_with_problem_dampener = 0

    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            levels = [int(num) for num in line.split(" ")]
            if is_safe(levels):
                safe_reports += 1
                safe_reports_with_problem_dampener += 1
            else:
                dampened = False
                for i in range(0,len(levels)):
                    if is_safe(levels[:i]+levels[i+1:]):
                        dampened = True
                if dampened:
                    safe_reports_with_problem_dampener += 1
                
    print(f"part1: {safe_reports}")
    print(f"part2: {safe_reports_with_problem_dampener}")


if __name__ == '__main__':
    main()
