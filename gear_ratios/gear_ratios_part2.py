# from collections import defaultdict

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
    res = []
    with open(file_path, 'r') as file:
        indices = []
        schematic = [[char for char in line.rstrip()] for line in file]
        row_length = len(schematic)
        col_length = len(schematic[0])

        for row in range(row_length):
            for col in range(col_length):
                if not schematic[row][col].isdigit() and schematic[row][col] != '.':
                    indices.append((row, col))
        
        for symbol_indices in indices:
            symbol_row, symbol_col = symbol_indices
            digits = []
            for direction in DIRECTIONS:
                x, y = direction
                if not_in_bounds(symbol_row + x, symbol_col + y, row_length, col_length):
                    continue
                if schematic[symbol_row + y][symbol_col + x].isdigit():
                    digits.append(scan_for_number(symbol_row + y, symbol_col + x, col_length, schematic))
            if len(digits) == 2:
                res.append(digits[0] * digits[1])
    return sum(res)

def not_in_bounds(row, col, max_row, max_col):
    if row >= max_row or row < 0 or col < 0 or col >= max_col:
        return True
    return False

# removes counted digits in-place to avoid double counting
def scan_for_number(row, col, max_col, schematic) -> int:
    l, r = col - 1, col + 1
    digit = [schematic[row][col]]
    while l >= 0 and schematic[row][l].isdigit():
        digit = [schematic[row][l]] + digit
        schematic[row][l] = '.'
        l -= 1
    while r < max_col and schematic[row][r].isdigit():
        digit = digit + [schematic[row][r]] 
        schematic[row][r] = '.'
        r += 1
    return int(''.join(digit))
    
        
if __name__ == "__main__":
    res = gear_ratios("gear_ratios.txt")
    print(res)