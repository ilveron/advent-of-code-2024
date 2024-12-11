import os

lookup_table = {}

# classic recursion
def process_stone_part1(stone, counter):
    if counter > 25:
        return 1
    
    if stone == '0':
        return process_stone_part1('1', counter+1)
    if len(str(stone)) % 2 == 0:
        half = len(str(stone))//2
        return process_stone_part1(str(int(stone[:half])), counter+1) + process_stone_part1(str(int(stone[len(stone)-half:])), counter+1)
    return process_stone_part1(str(int(stone)*2024), counter+1)


# this one uses memoization
def process_stone_part2(stone, counter):
    if counter > 75:
        return 1

    key = (stone, counter)

    if key in lookup_table.keys():
        return lookup_table[key]
    
    if stone == '0':
        to_add = process_stone_part2('1', counter+1) 
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone))//2
        to_add = process_stone_part2(str(int(stone[:half])), counter+1) + process_stone_part2(str(int(stone[len(stone)-half:])), counter+1)
    else:
        to_add = process_stone_part2(str(int(stone)*2024), counter+1)
    lookup_table[key] = to_add
    return to_add


def main():
    stones = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        stones = f.readline().strip().split(' ')
    part1_result = part2_result = 0
    for stone in stones:
        part1_result += process_stone_part1(stone, 1)
        part2_result += process_stone_part2(stone, 1)
        
    print(f"part1: {part1_result}")
    print(f"part2: {part2_result}")

    
if __name__ == '__main__':
    main()