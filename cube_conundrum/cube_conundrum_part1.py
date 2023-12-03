def cube_conundrum(file_path) -> int:
    with open(file_path, 'r') as file:
        valid_games = filter(lambda game: is_valid_game(game), file.readlines())
        ids = map(lambda game: get_id_num(game), valid_games)
        return sum(ids)

def get_id_num(game: str) -> int:
    game_id = game.split(':')[0]
    return int(game_id.split(' ')[1])

def is_valid_game(game: str) -> bool:
    game = game.split(':')[1]
    game_sets = game.split(';')
    for set in game_sets:
        cube_color_freqs = set.strip().split(', ')
        for cube_color_freq in cube_color_freqs:
            split = cube_color_freq.split(' ')
            freq = int(split[0])
            color = split[1]

            if color == 'red' and freq > 12:
                return False
            elif color == 'green' and freq > 13:
                return False
            elif color == 'blue' and freq > 14:
                return False
    return True

if __name__ == "__main__":
    res = cube_conundrum("cube_conundrum.txt")
    print(res)
