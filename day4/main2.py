#!/usr/bin/python3
import json

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# 7256410 is too low

cards = {}
total_result = 0
with open("input1.txt", "rt") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        print(line)
        card_number = int(line.split(":")[0].split(" ")[-1])
        print(f"card number: {card_number}")
        numbers = line.split(":")[1].strip()
        winning_numbers = [int(entry) for entry in numbers.split("|")[0].strip().split(" ") if entry]
        print(winning_numbers)
        my_numbers = [int(entry) for entry in numbers.split("|")[1].strip().split(" ") if entry]
        print(my_numbers)
        cards[card_number] = {
            "winning_numbers": winning_numbers,
            "my_numbers": my_numbers,
            "amount": 1
        }

    max_number = len(cards)
    for card_number in list(cards.keys()):
        winning_numbers = cards[card_number]["winning_numbers"]
        my_numbers = cards[card_number]["my_numbers"]
        matching = [number in winning_numbers for number in my_numbers]
        this_amount = cards[card_number]["amount"]
        print(f"card number {card_number} wins {matching.count(True)} owning {this_amount}")
        cards[card_number]["wins"] = matching.count(True)
        for i in range(matching.count(True)):
            index = card_number + i + 1  # number of card to double
            # if index < max_number:
            cards[index]["amount"] += this_amount
            print(f"  winning copy of {index} now {cards[index]['amount']} added {this_amount}")

total_sum = 0
for card_number in list(cards.keys()):
    print(f"{card_number:3} : {cards[card_number]['wins']:3} : {cards[card_number]['amount']:6}")
    total_sum += cards[card_number]["amount"]
print(f"total_sum: {total_sum}")
