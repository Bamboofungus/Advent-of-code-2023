import re

def boat_race(file_path):
    with open(file_path, 'r') as file:
        memo = boat_race_serialize(file)
        # assume always possible to win one way in any race
        memo["ways"] = 1
        for i, distance in enumerate(memo['distances']):
            valid_hold_times = []
            max_time = memo['times'][i]
            for press_time in range(1, max_time + 1):
                remaining_time = max_time - press_time
                if(remaining_time * press_time >=  distance):
                    valid_hold_times.append(press_time)
            memo["ways"] *= len(valid_hold_times)
        return memo["ways"]
            


def boat_race_serialize(file) -> dict:
    serialized = {}
    find_numbers = lambda line: re.findall(r'\d+', line)
    serialized['times'] = list(map(int, find_numbers(file.readline())))
    serialized['distances'] = list(map(int, find_numbers(file.readline())))
    return serialized


if __name__ == "__main__":
    res = boat_race("boat_race.txt")
    print(res)