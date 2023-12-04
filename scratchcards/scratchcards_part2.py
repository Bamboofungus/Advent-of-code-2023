from collections import namedtuple, defaultdict
import re

ScratchcardNumbers = namedtuple('ScratchcardNumbers', ['winning', 'received'])

def scratchcards(file_path) -> int:
    with open(file_path, 'r') as file:
        ser = serialize_scratchcard(file)
        scratchcards_won_memo = {i: 1 for i in range(1, len(ser) + 1)}
        for index, numbers in enumerate(ser):
            game_id = index + 1
            cards_won = len(list(filter(lambda num: num in numbers.winning, numbers.received)))
            for card in range(1, cards_won + 1):
                if(index + card >= len(ser)):
                    break
                scratchcards_won_memo[game_id + card] += scratchcards_won_memo[game_id]

    return sum(scratchcards_won_memo.values())


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