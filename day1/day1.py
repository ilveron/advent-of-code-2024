#!/usr/bin/python3
import os

def parse_input(l1, l2):
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            split = line.split("   ")
            l1.append(int(split[0]))
            l2.append(int(split[1]))


def get_total_distance(l1, l2):
    total_distance = 0
    for i in range(len(l1)):
        total_distance += abs(l1[i] - l2[i])
    return total_distance


def get_similarity_score(l1, l2):
    already_checked = {}
    similarity_score = 0
    for i in range(len(l1)):
        number_to_check = l1[i]
        occurrences = 0

        if number_to_check in already_checked.keys():
            similarity_score += already_checked[number_to_check]
        else:
            for j in range(len(l2)):
                if l2[j] == number_to_check:
                    occurrences += 1
                elif l2[j] > number_to_check:   # since the list was sorted before
                    break
            similarity_score += number_to_check * occurrences        
        
    return similarity_score

def main():
    l1 = []
    l2 = []
    
    parse_input(l1, l2)
    
    l1.sort()
    l2.sort()

    print(f"part1: {get_total_distance(l1,l2)}")
    print(f"part2: {get_similarity_score(l1,l2)}")
    

if __name__ == '__main__':
    main()
