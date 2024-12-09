import os
import numpy as np

def get_block_string_list(file_association):
    block_string_list = []
    
    for i in range(len(file_association)):
        file_size, free_space = file_association[i]
        block_string_list.extend([str(i)]*file_size)
        block_string_list.extend(['.']*free_space)
    return block_string_list


def is_compacted(block_string_list):
    found_free_space = False
    for char in block_string_list:
        if char == '.':
            found_free_space = True
        elif found_free_space:
            return False
    return True


def get_last_file_idx(block_string_list):
    for i in range(len(block_string_list)-1, -1, -1):
        char = block_string_list[i]
        if char != '.':
            return i


def get_first_free_cell_idx(block_string_list):
    for i in range(len(block_string_list)):
        char = block_string_list[i]
        if char == '.':
            return i
    

def get_compacted_string(block_string_list):
    while not is_compacted(block_string_list):  
        last_file_idx = get_last_file_idx(block_string_list)
        first_free_cell_idx = get_first_free_cell_idx(block_string_list)
        # swap
        block_string_list[first_free_cell_idx] = block_string_list[last_file_idx]
        block_string_list[last_file_idx] = '.'
    return block_string_list


def get_compacted_string_with_whole_blocks(block_string_list, max_id):
    for id in range(max_id, -1, -1):
        file_block_indexes = np.where(block_string_list == str(id)) 
        file_block = block_string_list[file_block_indexes]
        
        free_indices = np.where(block_string_list[:file_block_indexes[0][0]] == '.')[0]
        free_indices_split = np.split(free_indices, np.where(np.diff(free_indices) > 1)[0] + 1)

        swapped = False
        # scan free blocks from left to right
        for idx in range(len(free_indices_split)):
            if len(free_indices_split[idx]) >= len(file_block):
                # swap
                for k in file_block_indexes[0]:
                    block_string_list[k] = '.'
                for k in free_indices_split[idx][0:len(file_block_indexes[0])]:
                    block_string_list[k] = id
                swapped = True
            if swapped:
                break
        
      
    return block_string_list


def calculate_checksum(compacted_string):
    checksum = 0
    for i in range(len(compacted_string)):
        char = compacted_string[i]
        if char == '.':
            continue
        checksum += i*int(char)
    return checksum


# I swear that this works, just give it its (utterly long) time. Python ftw
def main():
    disk_map = ''
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        disk_map = f.readline().strip()
    
    file_association = [(int(disk_map[i]), int(disk_map[i+1])) for i in range(0,len(disk_map)-1,2)]
    # if the disk_map finishes with a file size (no free space)
    if len(disk_map) % 2 != 0:
        file_association.append((int(disk_map[-1]),0))

    block_string_list = np.array(get_block_string_list(file_association))
    compacted_string_part1 = get_compacted_string(np.copy(block_string_list))
    part1_result = calculate_checksum(compacted_string_part1)
    print(f"part1: {part1_result}")
    
    max_id = len(file_association)-1
    compacted_string_part2 = get_compacted_string_with_whole_blocks(np.copy(block_string_list), max_id)
    part2_result = calculate_checksum(compacted_string_part2)
    print(f"part2: {part2_result}")

if __name__ == '__main__':
    main()