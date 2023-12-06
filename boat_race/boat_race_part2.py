import re

def boat_race(file_path):
    with open(file_path, 'r') as file:
        max_time, distance = boat_race_serialize(file)
        # assume always possible to win one way in any race
        # for i, distance in enumerate(memo['distances']):
        valid_hold_times = []
        for press_time in range(1, max_time + 1):
            remaining_time = max_time - press_time
            if(remaining_time * press_time >= distance):
                valid_hold_times.append(press_time)
        return len(valid_hold_times)
            
def boat_race_serialize(file) -> (int, int):
    find_numbers = lambda line: re.findall(r'\d+', line)
    time = int("".join(find_numbers(file.readline())))
    distance = int("".join(find_numbers(file.readline())))
    return (time, distance)


if __name__ == "__main__":
    res = boat_race("boat_race.txt")
    print(res)