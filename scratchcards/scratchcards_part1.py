from collections import namedtuple
import re

ScratchcardNumbers = namedtuple('ScratchcardNumbers', ['winning', 'received'])

def scratchcards(file_path) -> int:
    total_points = []
    with open(file_path, 'r') as file:
        ser = serialize_scratchcard(file)
    for numbers in ser:
        matching_numbers = list(filter(lambda num: num in numbers.winning, numbers.received))
        points = 2 ** (len(matching_numbers) - 1) if len(matching_numbers) > 0 else 0
        total_points.append(points)
    return sum(total_points)


def serialize_scratchcard(file): 
    serialized = []
    for line in file.readlines():
        _, card_numbers = line.rstrip().split(':')
        winning_str, received_str = card_numbers.split('|')
        winning = []
        recieved = []
        # handle extra spaces from single digit #s using re
        for num in re.split(r'[\s]+', winning_str.strip()):
            winning.append(num)

        for num in re.split(r'[\s]+', received_str.strip()):
            recieved.append(num)

        serialized.append(ScratchcardNumbers(winning, recieved))
    return serialized

if __name__ == "__main__":
    res = scratchcards("scratchcards.txt")
    print(res)