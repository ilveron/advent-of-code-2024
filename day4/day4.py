import os
import numpy as np
from math import floor, ceil

def get_number_of_string_occurrences(text, string):
    return text.count(string) + text[::-1].count(string)


def get_xmas_occurrences(rows,cols,diags):
    occurrences = 0
    for i in range (max(len(rows), len(cols), len(diags))):
        if i < len(rows):
            occurrences += get_number_of_string_occurrences("".join(str(char) for char in rows[i]), "XMAS")
        if i < len(cols):
            occurrences += get_number_of_string_occurrences("".join(str(char) for char in cols[i]), "XMAS")
        if i < len(diags):
            occurrences += get_number_of_string_occurrences("".join(str(char) for char in diags[i]), "XMAS")
    return occurrences


def get_x_shaped_mas_occurrences(rows):
    occurrences = 0
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            char = rows[r,c]
            if char == 'A':
                x_shaped_neighborhood = []
                if r-1 >= 0 and r+1 < len(rows) and c-1 >= 0 and c+1 < len(rows[r]):
                    x_shaped_neighborhood.append(rows[r-1,c-1]+char+rows[r+1,c+1])
                    x_shaped_neighborhood.append(rows[r-1,c+1]+char+rows[r+1,c-1])
                    if get_number_of_string_occurrences(x_shaped_neighborhood[0], "MAS") + get_number_of_string_occurrences(x_shaped_neighborhood[1], "MAS") == 2:
                        occurrences += 1
    return occurrences
                    

def main():
    rows = []
    diags = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        for line in f:
            rows.append(list(line.strip()))

        rows = np.array(rows)
        cols = np.ndarray.transpose(rows)

        # get diags
        ## num of diags is given by m + n - 1
        num_of_diags = len(rows) + len(cols) - 1
        offset_lower_bound = - floor(num_of_diags / 2)
        offset_upper_bound = ceil(num_of_diags / 2)

        for off in range(offset_lower_bound, offset_upper_bound+1):
            # diagonal
            diags.append(np.diagonal(rows, offset=off))
            # anti-diagonal
            diags.append(np.diagonal(np.flipud(rows), offset=off))

        print(f"part1: {get_xmas_occurrences(rows,cols,diags)}")
        print(f"part2: {get_x_shaped_mas_occurrences(rows)}")
    

if __name__ == '__main__':
    main()