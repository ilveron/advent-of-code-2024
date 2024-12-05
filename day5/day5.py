import os
from math import ceil

def parse_input(successors, updates):
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            if '|' in line:
                split = line.strip().split('|')
                predecessor, successor = split[0], split[1]
                if predecessor not in successors:
                    successors[predecessor] = [successor]
                else:
                    successors[predecessor].append(successor)
            elif ',' in line:
                updates.append(line.strip().split(','))


def is_update_correct(successors, update):
    for prec in range(len(update)-1):
        for succ in range(prec+1, len(update)):
            if update[succ] not in successors[update[prec]]:
                return False
    return True  


def get_part1(successors, updates):
    result = 0

    for update in updates:
        update_len = len(update)
        if is_update_correct(successors, update):
            middle_page = int(update[update_len//2])
            print(middle_page)
            result += middle_page
    return result


def main():
    successors = {}
    updates = []

    parse_input(successors, updates)

    print(f"part1: {get_part1(successors, updates)}")
    

if __name__ == '__main__':
    main()