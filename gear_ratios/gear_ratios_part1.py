from collections import defaultdict

DIRECTIONS = [
    (1,0), 
    (0,1), 
    (-1,0), 
    (0,-1),
    (1, 1),
    (-1,-1),
    (-1, 1),
    (1,-1)
]


def gear_ratios(file_path) -> int:
    with open(file_path, 'r') as file:
        res = []
        schematic = [[char for char in line.rstrip()] for line in file]
        row_length = len(schematic)
        col_length = len(schematic[0])

        for row in range(row_length):
            digits_to_col = defaultdict(list)
            
            col = 0
            # use while to skip indices and avoid double counting digits here
            while col < col_length:
                if schematic[row][col].isdigit():
                    indices = get_digit_indices(row, col, schematic)
                    digit = ''
                    for digit_col in indices:
                        digit += schematic[row][digit_col]
                    digit = int(digit)
                    digits_to_col[digit] = digits_to_col[digit] + [indices]
                    col = indices[-1] + 1
                else:
                    col += 1

            for d, index_list in digits_to_col.items():
                for indices in index_list:
                    symbol_found = False
                    for digit_col in indices:            
                        for direction in DIRECTIONS:
                            x, y = direction
                            if row + y >= row_length or row + y < 0 or digit_col + x < 0 or digit_col + x >= col_length:
                                continue
                            if (not schematic[row + y][digit_col + x].isdigit()) and schematic[row + y][digit_col + x] != '.':
                                res.append(d)
                                symbol_found = True
                                break
                        if symbol_found == True:
                            break
        return sum(res)


def get_digit_indices(i, j, schematic) -> list:
    digit_indices = []
    for curr_col in range(j, len(schematic[i])):
        if schematic[i][curr_col].isdigit():
            digit_indices.append(curr_col)
        else:
            break
    return digit_indices

if __name__ == "__main__":
    res = gear_ratios("gear_ratios.txt")
    print(res)
