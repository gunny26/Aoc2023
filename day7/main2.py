#!/usr/bin/python3

# 12808797 is too low
# 251591612 is too high
# 250690017 is too low
# 250427288

# 250951660 - thatst the right answer

# mapping cards values to ASCII, so they are sortable
cards_to_char = {
    "A": "Z",
    "K": "Y",
    "Q": "X",
    "J": "W",
    "T": "V",
    "9": "U",
    "8": "T",
    "7": "S",
    "6": "R",
    "5": "Q",
    "4": "P",
    "3": "O",
    "2": "N",
    "1": "M",
}

# possible card types
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]  # 1 only for lowest value
cards = list(cards_to_char.values())
cards.reverse()  # so highest value is highest index
print(cards)

def hand_to_char(hand):
    ret_value = ""
    for card in hand:
        ret_value += cards_to_char[card]
    return ret_value

def five_of_a_kind(hand):
    return list(set([card for card in hand if hand.count(card) == 5]))

def four_of_a_kind(hand):
    return list(set([card for card in hand if hand.count(card) == 4]))

def three_of_a_kind(hand):
    return list(set([card for card in hand if hand.count(card) == 3]))

def two_of_a_kind(hand):  # there could be two in one hand
    return sorted(list(set([card for card in hand if hand.count(card) == 2])), key=cards.index)

def one_pair(hand):
    pairs = set([card for card in hand if hand.count(card) == 2])
    if len(pairs) == 1:
        return list(pairs)

def two_pairs(hand):
    pairs = set([card for card in hand if hand.count(card) == 2])
    if len(pairs) == 2:
        return sorted(list(pairs), key=cards.index)

def high_card(hand):
    ones = [hand.count(card) for card in hand]
    if sum(ones) == 5:
        return sorted(hand, key=cards.index)

def full_house(hand):
    # print(three_of_a_kind(hand))
    # print(two_of_a_kind(hand))
    if three_of_a_kind(hand) and two_of_a_kind(hand):
        return(three_of_a_kind(hand) + two_of_a_kind(hand))

with open("input1.txt", "rt") as infile:
    indata = [line.strip() for line in infile.read().split("\n") if line]

hands = {}  # hand to bid mapping
rank = {}  # rank to hand mapping

for this_hand, bid in [line.split() for line in indata]:

    hands[this_hand] = bid  # storing hand to bid map

    hand = hand_to_char(this_hand)  # transform hand to sortable characters
    print(this_hand, bid, hand)

    score = ["A"] * 6  # initial score

    if five_of_a_kind(hand):  # one kind
        kind = five_of_a_kind(hand)[0]  # A .. 2
        score[0] = "Z"
        print("- five of a kind ", kind, score)

    elif four_of_a_kind(hand):  # one kind
        kind = four_of_a_kind(hand)[0]
        print("- four of a kind ", kind, score)
        score[0] = "Y"

    elif full_house(hand):  # two kinds
        kinds = full_house(hand)
        kinds.reverse()
        score[0] = "X"
        print("- full house ", kinds, score)

    elif three_of_a_kind(hand):  # one kind
        kind = three_of_a_kind(hand)[0]
        score[0] = "W"
        print("- three of a kind ", kind, score)

    elif two_pairs(hand):  # two kinds
        kinds = two_pairs(hand)
        kinds.reverse()
        score[0] = "U"
        print("- two pairs ", kinds, score)

    elif one_pair(hand):  # one kind
        kind = one_pair(hand)[0]
        score[0] = "T"
        print("- one pair ", kind, score)


    if hand:  # are there some cards left, not in any other combination
        index = 1
        for kind in hand:
            score[index] = kind
            index += 1
            print("- left card ", kind, score)

    print("final score: ", score)
    score_str = "".join(score)

    if score_str in rank:
        print("there is already a hand with the same value ", rank[score_str], score_str)
        sys.exit(0)
    rank["".join(score_str)] = this_hand
    print()


total_winnings = 0
index = 1  # starting at one
for value in sorted(rank):
    hand = rank[value]  # get hand to value
    bid = hands[hand]  # get bid from hand
    winning = int(bid) * index  # calculate winning
    print(index, value, hand, bid, winning)
    total_winnings += winning
    index += 1
print(total_winnings)
