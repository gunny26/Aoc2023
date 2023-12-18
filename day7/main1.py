#!/usr/bin/python3

# 12808797 is too low
# 251591612 is too high

# possible card types
cards       = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]  # 1 only for lowest value
# values from 1 ... 13 are possible index, 0 will never be used
cards.reverse()  # so highest value is highest index
# maximum high_card value is
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 91
print(cards)

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

# basic testing
assert five_of_a_kind("AAAAA"), five_of_a_kind("AAAAA")
assert not five_of_a_kind("AAAAB"), five_of_a_kind("AAAAB")
assert four_of_a_kind("AA8AA"), four_of_a_kind("AA8AA")
assert not four_of_a_kind("AA88A"), four_of_a_kind("AA88A")
assert three_of_a_kind("TTT98"), three_of_a_kind("TTT98")
assert not three_of_a_kind("TT998"), three_of_a_kind("TT998")
assert two_of_a_kind("TT889"), two_of_a_kind("TT889")
assert not two_of_a_kind("TTT98"), two_of_a_kind("TTT98")
assert two_pairs("TT988"), two_pairs("TT988")
assert not two_pairs("TT999"), two_pairs("TT999")
assert high_card("23456"), high_card("23456")
assert not high_card("23455"), high_card("23455")
assert full_house("23332"), full_house("23332")
assert not full_house("23333"), full_house("23333")

# algorithm
# five of a kinds   13 ^ 6 + card_index
# four of a kinds   13 ^ 5 + card_index
# full house        13 ^ 4 + card[0] index * 13 + card[1] index
# three of a kinds  13 ^ 3 + card index
# two pairs         13 ^ 2 + card[0] index * 13 + card[1] index
# one pairs         13 ^ 1 + card[0] index * 13 + card[1] index
# all cards left    13 ^ 0 + card index


hands = {}  # hand to bid mapping
rank = {}  # rank to hand mapping

for this_hand, bid in [line.split() for line in indata]:

    print(this_hand, bid)
    hands[this_hand] = bid  # storing hand to bid map
    hand = str(this_hand)  # will be modified
    value = 0

    if five_of_a_kind(hand):  # one kind
        kind = five_of_a_kind(hand)[0]  # A .. 2
        value = 1 << 19 | cards.index(kind)
        print("- five of a kind ", kind, value)
        hand = hand.replace(kind, "")

    elif four_of_a_kind(hand):  # one kind
        kind = four_of_a_kind(hand)[0]
        value = 1 << 18 | 1 << cards.index(kind)
        print("- four of a kind ", kind, value)
        hand = hand.replace(kind, "")

    elif full_house(hand):  # two kinds
        kinds = full_house(hand)
        kinds.reverse()
        value = 1 << 17 | 1 << (cards.index(kinds[0]) + 1) | cards.index(kinds[1])
        print("- full house ", kinds, value)
        hand = hand.replace(kinds[0], "")
        hand = hand.replace(kinds[1], "")

    elif three_of_a_kind(hand):  # one kind
        kind = three_of_a_kind(hand)[0]
        value = 1 << 16 | cards.index(kind)
        print("- three of a kind ", kind, value)
        hand = hand.replace(kind, "")

    elif two_pairs(hand):  # two kinds
        kinds = two_pairs(hand)
        kinds.reverse()
        value = (cards.index(kinds[0]) * 13 + cards.index(kinds[1])) << 15
        print("- two pairs ", kinds, value)
        hand = hand.replace(kinds[0], "")
        hand = hand.replace(kinds[1], "")

    elif one_pair(hand):  # one kind
        kind = one_pair(hand)[0]
        value = 1 << 14 |  cards.index(kind)
        print("- one pair ", kind, value)
        hand = hand.replace(kind, "")

    if hand:
        for kind in hand:
            this_value = 1 << cards.index(kind)
            print("- left card ", kind, this_value)
            value = value | this_value

    print("total value of this hand ", value)

    if value in rank:
        print("there is already a hand with the same value ", rank[value], value)
        sys.exit(0)
    rank[value] = this_hand
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
