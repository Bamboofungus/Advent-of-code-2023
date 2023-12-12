from collections import namedtuple, Counter
from functools import cmp_to_key
HandToBid = namedtuple('HandToBid', ['hand', 'bid'])
hand_types_order = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card"
]
card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def camel_poker(file_path) -> int:
    with open(file_path, 'r') as file:
        hand_to_bids = camel_poker_serialize(file)
    sorted_hands = sorted(hand_to_bids, key=cmp_to_key(compare_hands))
    res = 0
    for i, hand_to_bid in enumerate(reversed(sorted_hands)):
        res += int(hand_to_bid.bid) * (i + 1)
    return res

def compare_hands(hand_to_bids1, hand_to_bids2) -> int:
    hand_types = []
    for hand_to_bid in iter([hand_to_bids1, hand_to_bids2]):
        hand_counts = Counter(hand_to_bid.hand)
        if len(hand_counts) == 1:
            hand_types.append("Five of a kind")
        elif len(hand_counts) == 2:
            values = sorted(list(hand_counts.values()))
            if values == [1, 4]:
                hand_types.append("Four of a kind")
            elif values == [2, 3]:
                hand_types.append("Full house")
        elif len(hand_counts) == 3:
            values = sorted(list(hand_counts.values()))
            if values == [1, 1, 3]:
                hand_types.append("Three of a kind")
            elif values == [1, 2, 2]:
                hand_types.append("Two pair")
        elif len(hand_counts) == 4:
            hand_types.append("One pair")
        elif len(hand_counts) == 5:
            hand_types.append("High card")
        else:
            raise ":("
    if hand_types[0] == hand_types[1]:
        for i in range(len(hand_to_bids1.hand)):
            card_value1 = card_order.index(hand_to_bids1.hand[i])
            card_value2 = card_order.index(hand_to_bids2.hand[i])
            if card_value1 == card_value2:
                continue
            else:
                return 1 if card_order.index(hand_to_bids1.hand[i]) > card_order.index(hand_to_bids2.hand[i]) else -1
    else:
        return 1 if hand_types_order.index(hand_types[0]) > hand_types_order.index(hand_types[1]) else -1


def camel_poker_serialize(file) -> list:
    ser = []
    for line in file.readlines():
        hand, bid = line.rstrip().split(' ')
        ser.append(HandToBid(hand, bid))
    return ser

if __name__ == "__main__":
    res = camel_poker("camel_poker.txt")
    print(res)
