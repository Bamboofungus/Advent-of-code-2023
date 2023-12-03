from collections import defaultdict 
from functools import reduce

def cube_conundrum(file_path) -> int:
    with open(file_path, 'r') as file:
        powers = map(lambda game: get_power(get_minimum_cubes_required(game)), file.readlines())
        return sum(powers)

def get_power(cube_colors: dict) -> int:
    return reduce(lambda val1, val2: val1 * val2, cube_colors.values())

def get_minimum_cubes_required(game: str) -> dict:
    game = game.split(':')[1]
    game_sets = game.split(';')
    max_cubes = defaultdict(int)

    for set in game_sets:
        cube_color_freqs = set.strip().split(', ')
        for cube_color_freq in cube_color_freqs:
            split = cube_color_freq.split(' ')
            freq = int(split[0])
            color = split[1]
            max_cubes[color] = max(max_cubes[color], freq)
    return max_cubes

if __name__ == "__main__":
    res = cube_conundrum("cube_conundrum.txt")
    print(res)
