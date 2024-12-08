import os
import copy as cp

def get_antennas_position(map: list) -> dict:
    antennas_position = dict()
    for r in range(len(map)):
        for c in range(len(map[0])):
            char = map[r][c]
            if char != '.' and char != '#':   
                if char not in antennas_position.keys():
                    antennas_position[char] = [(r,c)]
                else:
                    antennas_position[char].append((r,c))
    return antennas_position


def get_antennas_offsets(antennas_position: dict) -> dict:
    offsets = {}
    for antenna, positions in antennas_position.items():
        for i in range(len(positions)-1):
            for j in range(i+1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                offset = (pos1[0]-pos2[0], pos1[1]-pos2[1])
                offsets[(pos1,pos2)] = offset
    return offsets


def is_within_bounds(pos: tuple, map: list) -> bool:
    return pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])


def can_place_antinode(pos: tuple, positioned_antinodes: list) -> bool:
    return pos not in positioned_antinodes


def get_antinodes_position(pos1: tuple, pos2: tuple, offset: tuple, multiplier: int) -> list:
    r1, c1 = pos1
    r2, c2 = pos2
    return [(r1+offset[0]*multiplier,c1+offset[1]*multiplier), (r2-offset[0]*multiplier,c2-offset[1]*multiplier)]


def print_map(map, positioned_antinodes):
    map_copy = cp.deepcopy(map)
    for r in range(len(map_copy)):
        for c in range(len(map_copy[0])):
            if (r,c) in positioned_antinodes:
                if map_copy[r][c] == '.':
                    map_copy[r][c] = '#'
    
    for line in map_copy:
        print("".join(line))


def main():
    map = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            map.append(list(line.strip()))
    antennas_position = get_antennas_position(map)
    antennas_offsets = get_antennas_offsets(antennas_position)

    part1_result = 0
    part2_result = 0
    
    positioned_antinodes = []

    # part1
    for antenna, positions in antennas_position.items():
        for i in range(len(positions)-1):
            for j in range(i+1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                offset = antennas_offsets[(pos1,pos2)]
                antinodes_position = get_antinodes_position(pos1, pos2, offset, 1)                 
                for antinode in antinodes_position:
                    if is_within_bounds(antinode, map) and can_place_antinode(antinode,positioned_antinodes):
                        part1_result += 1
                        positioned_antinodes.append(antinode)

    part2_result += part1_result

    # part2
    for antenna, positions in antennas_position.items():
        for i in range(len(positions)-1):
            for j in range(i+1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                offset = antennas_offsets[(pos1,pos2)]

                # check whether the two antennas can also be antinodes of each other
                for pos in (pos1, pos2):
                    if can_place_antinode(pos, positioned_antinodes):
                        positioned_antinodes.append(pos)
                        part2_result += 1
                
                # here we propagate the antinodes in a straight line
                multiplier = 2
                while True:
                    at_least_one_in_bounds = False
                    antinodes_position = get_antinodes_position(pos1, pos2, offset, multiplier)

                    for antinode in antinodes_position:
                        if is_within_bounds(antinode, map):
                            at_least_one_in_bounds = True
                            if can_place_antinode(antinode, positioned_antinodes):
                                positioned_antinodes.append(antinode)
                                part2_result += 1

                    if not at_least_one_in_bounds:
                        break

                    multiplier += 1
                    
    print(f"part1: {part1_result}")
    print(f"part2: {part2_result}")


if __name__ == '__main__':
    main()