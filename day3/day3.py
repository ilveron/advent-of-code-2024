#!/usr/bin/python3
import os
import re

# part1 regex: mul\(([0-9]{1,3}),([0-9]{1,3})\)
# part2 regexes: 
#   (.*?)do
#   do\(\)(.*?)don't


def get_part1_result(memory_dump):
    result = 0
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    matches = [match for match in re.finditer(pattern, memory_dump)]
    for match in matches:
        result += int(match.group(1)) * int(match.group(2))
    return result


def get_part2_result(memory_dump):
    result = 0

    # we use this pattern to get the first part of the memory, before any do(s) or don't(s)
    first_part_pattern = r"(.*?)do" 

    enabled_parts_pattern = r"do\(\)(.*?)don't"
    
    # here we get all the substrings which contain the enabled parts of the memory
    enabled_substrings = [match.group(1) for match in re.finditer(enabled_parts_pattern, memory_dump)]
    enabled_substrings.append(re.match(first_part_pattern, memory_dump).group(1))

    # we consider any instance of the enabled_substrings as a part1 problem
    for sub in enabled_substrings:
        result += get_part1_result(sub)
    return result


def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        memory_dump = ''
        for line in f:
            memory_dump += line.strip()

        print(f"part1: {get_part1_result(memory_dump)}")    
        print(f"part2: {get_part2_result(memory_dump)}")



if __name__ == '__main__':
    main()