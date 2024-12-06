import os
import copy as cp

def get_direction(char):
    if char == '^':
        return (-1,0)
    elif char == 'v':
        return (1,0)
    elif char == '<':
        return (0,-1)
    elif char == '>':
        return (0,1)
    raise(Exception("Can't assign direction"))


def get_next_direction_char_after_collision(char):
    if char == '^':
        return '>'
    elif char == 'v':
        return '<'
    elif char == '<':
        return '^'
    elif char == '>':
        return 'v'
    raise(Exception("Can't assign direction char"))


def is_pos_in_map(pos, map):
    return (pos[0] >= 0 and pos[0] < len(map)) and (pos[1] >= 0 and pos[1] < len(map[0]))


def get_next_pos(pos, direction):
    return (pos[0]+direction[0], pos[1]+direction[1])


def is_cell_free(map, r, c):
    return map[r][c] == '.'


def print_map(map):
    for row in map:
        print("".join(row))


def main():
    # take input
    map = []
    
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            map.append(list(line.strip()))
    
    map_part1 = cp.deepcopy(map)
    # get guard position
    guard_pos_part1 = guard_pos_part2 = og_guard_pos = (-1,-1)
    visited_in_part1 = []

    for r in range(len(map_part1)):
        for c in range(len(map_part1[0])):
            try:
                column_pos = map_part1[r].index('^')
                guard_pos_part1 = (r,column_pos)
            except ValueError:
                continue
        og_guard_pos = guard_pos_part2 = guard_pos_part1
    
    count_part1 = 1       # counter starts from 1 since the first cell is already visited
    
    while is_pos_in_map(guard_pos_part1, map_part1):
        direction_char = map_part1[guard_pos_part1[0]][guard_pos_part1[1]]
        direction = get_direction(direction_char)    
        next_pos = get_next_pos(guard_pos_part1, direction)

        if guard_pos_part1 not in visited_in_part1:
            visited_in_part1.append(guard_pos_part1)

        if not is_pos_in_map(next_pos, map_part1):
            break

        next_pos_char = map_part1[next_pos[0]][next_pos[1]]
        if next_pos_char == '#':    #                           position unchanged, direction changed
            map_part1[guard_pos_part1[0]][guard_pos_part1[1]] = get_next_direction_char_after_collision(direction_char)
        else:                       # either is an X or a .  -  position changed, direction unchanged, counter unchanged
            
            map_part1[guard_pos_part1[0]][guard_pos_part1[1]] = 'X'    
            map_part1[next_pos[0]][next_pos[1]] = direction_char
            guard_pos_part1 = next_pos
            
        if next_pos_char == ".":   # it is an unvisited cell - guard_pos_part1 marked, position changed, direction unchanged, counter incremented
            count_part1 += 1

    print(f"part1: {count_part1}")

    count_part2 = 0
    og_direction_char = map[og_guard_pos[0]][og_guard_pos[1]]
    map_part2 = cp.deepcopy(map)
    last_pos_tested = (-1,-1)
    max_steps = len(map)*len(map[0])
    for r,c in visited_in_part1[::-1]:
        if last_pos_tested != (-1,-1):
            # we make the previous one free again
            map_part2[last_pos_tested[0]][last_pos_tested[1]] = "."
        
        # we put the new obstacle
        map_part2[r][c] = 'O'
        map_part2[og_guard_pos[0]][og_guard_pos[1]] = og_direction_char
        guard_pos_part2 = og_guard_pos
        loop = False
        
        steps = 0
        # we mark the current position as visited
        while is_pos_in_map(guard_pos_part2, map_part2) and not loop:
            direction_char = map_part2[guard_pos_part2[0]][guard_pos_part2[1]]
            direction = get_direction(direction_char)  
            next_pos = get_next_pos(guard_pos_part2, direction)  
            
            if not is_pos_in_map(next_pos, map_part2):
                break

            next_pos_char = map_part2[next_pos[0]][next_pos[1]]
            if next_pos_char in ('#','O'):      #                           position unchanged, direction changed
                map_part2[guard_pos_part2[0]][guard_pos_part2[1]] = get_next_direction_char_after_collision(direction_char)
            else:                               # it is a .  -  position changed, direction unchanged
                steps+=1
                if steps > max_steps:
                    loop = True
                map_part2[next_pos[0]][next_pos[1]] = direction_char
                guard_pos_part2 = next_pos
        if loop:
            count_part2 += 1
        last_pos_tested = (r,c)

    '''
    BADDEST VERSION
    ### PART 2 ###
    # The (bad) idea is that we try to put the obstacle in every single cell we visited in the previous part, 
    # and in every test we use a queue to store already visited positions. If by chance the queue becomes empty,
    # we're stuck in a loop, hence we increment the counter. I expect this to be really time 
    # consuming

    count_part2 = 0
    og_direction_char = map[og_guard_pos[0]][og_guard_pos[1]]
    map_part2 = cp.deepcopy(map)
    last_pos_tested = (-1,-1)

    for r,c in visited_in_part1[::-1]:
        print(r,c)
        if last_pos_tested != (-1,-1):
            # we make the previous one free again
            map_part2[last_pos_tested[0]][last_pos_tested[1]] = "."
        
        # we put the new obstacle
        map_part2[r][c] = 'O'
        #print_map(map_part2)
        map_part2[og_guard_pos[0]][og_guard_pos[1]] = og_direction_char
        guard_pos_part2 = og_guard_pos
        loop = False
        visited = []
        # we mark the current position as visited
        while is_pos_in_map(guard_pos_part2, map_part2) and not loop:
            direction_char = map_part2[guard_pos_part2[0]][guard_pos_part2[1]]
            direction = get_direction(direction_char)  
            next_pos = get_next_pos(guard_pos_part2, direction)  
            
            
            if not is_pos_in_map(next_pos, map_part2):
                break

            next_pos_char = map_part2[next_pos[0]][next_pos[1]]
            if next_pos_char in ('#','O'):      #                           position unchanged, direction changed
                map_part2[guard_pos_part2[0]][guard_pos_part2[1]] = get_next_direction_char_after_collision(direction_char)
            else:                               # it is a .  -  position changed, direction unchanged
                if (guard_pos_part2, next_pos) in visited:
                    loop = True           # we already came along this path
                else:
                    visited.append((guard_pos_part2, next_pos))

                map_part2[next_pos[0]][next_pos[1]] = direction_char
                guard_pos_part2 = next_pos
        if loop:
            count_part2 += 1
        last_pos_tested = (r,c)


    '''
    print(f"part2: {count_part2}")
    
if __name__ == '__main__':
    main()