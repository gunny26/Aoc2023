#!/usr/bin/python3

numbers = [str(number) for number in range(10)]  # sure this gets easier in python
print(numbers)

total_sum = 0
with open("input.txt", "rt") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        found = []  # holding two numbers
        print(line)
        for char in line:
            if char in numbers:
                if not found:
                    found = [int(char) * 10, int(char)]  # first could also be last
                else:
                    found[1] = int(char)  # ok there are more than one number
        print(found)
        line_sum = found[0] + found[1]
        print(line_sum)
        total_sum += line_sum
print(total_sum)
