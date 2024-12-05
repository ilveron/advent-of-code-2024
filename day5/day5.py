import os

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


def separate_correct_and_incorrect_updates(successors, updates):
    correct, incorrect = [], []
    for update in updates:
        update_len = len(update)
        if is_update_correct(successors, update):
            correct.append(update)
        else:
            incorrect.append(update)

    return correct, incorrect


def calculate_middle_pages(successors, updates):
    result = 0
    for update in updates:
        middle_page = int(update[len(update)//2])
        result += middle_page
    return result


def reorder_incorrect_updates(successors, updates):
    for update in updates:
        is_ordered = False
        
        while not is_update_correct(successors, update):
            for prec in range(len(update)-1):
                for succ in range(prec+1, len(update)):
                    if update[succ] not in successors[update[prec]]:
                        temp = update[prec]
                        update[prec] = update[succ]
                        update[succ] = temp


def main():
    successors = {}
    updates = []

    parse_input(successors, updates)
    correct_updates, incorrect_updates = separate_correct_and_incorrect_updates(successors, updates)

    reorder_incorrect_updates(successors, incorrect_updates)

    print(f"part1: {calculate_middle_pages(successors, correct_updates)}")
    print(f"part2: {calculate_middle_pages(successors, incorrect_updates)}")
    

if __name__ == '__main__':
    main()