#!/usr/bin/python3

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

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
        matching = [number in winning_numbers for number in my_numbers]
        print(matching)
        result = 0
        for entry in matching:
            if entry is True:
                if not result:
                    result = 1
                else:
                    result *= 2
        print(result)
        total_result += result
        print()
print(f"total result: {total_result}")
