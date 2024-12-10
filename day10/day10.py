import os

def get_trailheads(map):
    trailheads = []
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 0:
                trailheads.append((r,c))
    return trailheads


def get_uphill_neighbors(pos, node, map):
    uphill_neighbors = []
    neighbors = []
    r, c = pos
    if r - 1 >= 0:
        neighbors.append((r-1,c))
    if r + 1 < len(map):
        neighbors.append((r+1,c))
    if c - 1 >= 0:
        neighbors.append((r,c-1))
    if c + 1 < len(map[0]):
        neighbors.append((r,c+1))
    
    for n_pos in neighbors:
        neighbor_node = map[n_pos[0]][n_pos[1]]
        if neighbor_node - node == 1:
            uphill_neighbors.append(n_pos)
    return uphill_neighbors


'''
    The exact same function works for both part1 and part2
    The only difference between the two parts, for this implementation
    is that part1 has an extra control to avoid what is insted asked in
    part2.
''' 
def get_trailhead_score(trailhead, map, is_part1):
    queue = [trailhead]
    reached_nines = []
    score = 0
    while len(queue) > 0:
        pos = queue.pop(0)
        expanded_node = map[pos[0]][pos[1]]
        if expanded_node == 9:
            if is_part1:
                if pos not in reached_nines:
                    reached_nines.append(pos)
                    score += 1
            else:
                score += 1
        else:
            queue.extend(get_uphill_neighbors(pos, expanded_node, map))
    return score



def main():
    map = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            map.append([int(x) for x in line.strip()])
    
    trailheads = get_trailheads(map)
    part1_result = part2_result = 0

    for trailhead in trailheads:
        part1_result += get_trailhead_score(trailhead, map, is_part1=True)
        part2_result += get_trailhead_score(trailhead, map, is_part1=False)

    print(f"part1: {part1_result}")
    print(f"part2: {part2_result}")
        


if __name__ == '__main__':
    main()