#!/usr/bin/python3

numbers = [str(number) for number in range(10)]  # sure this gets easier in python
print(numbers)

translate = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

"""
what is right??

--- hhlqztk22qczrcqnxrtfourtwo3oneightsck
**- hhlqztk22qczrcqnxrt4   two3on8    sck
=== 28

--- hhlqztk22qczrcqnxrtfourtwo3oneightsck
--- hhlqztk22qczrcqnxrt4   2  31  ightsck
=== 21


line zfxbzhczcx9eightwockk
alternate 982

direct method eliminated two, by replacing eigth with 8 (so only wo is left of two)
diret = 98

the alternate method is the questioned !!
"""



total_sum = 0
alternate_sum = 0
with open("input2.txt", "rt") as infile:
    for line in infile:
        line = line.strip().lower()
        if not line:
            continue
        print(f"--- {line}")

        print("alternate method")
        numbers = []
        part = ""
        for c in line:
            part += c
            if c.isnumeric():
                numbers.append(c)
            for key in translate:
                if part.endswith(key):
                    numbers.append(translate[key])
        alternate = int(str(numbers[0] + numbers[-1]))
        print(f"alternate result: {alternate}")

        # translate spelled out number strings with 1 char digits
        # the appearance in the string does matter
        # more left will be replaced first
        # more right will be replaced at last
        positions = {}
        # step 1 find position of possible strings
        for key, value in translate.items():  # translate spelled number to 1 char digits
            min_index = line.find(key)  # where is this string placed, lowest index
            if min_index == -1:  # not found in this string
                continue
            print(f"*-- {key} {min_index}")
            positions[min_index] = key

            max_index = line.rfind(key)  # where is this string placed, highest index
            if max_index == min_index:  # thats the same position
                continue
            print(f"*-- {key} {max_index}")
            positions[max_index] = key

        # print(positions)
        # step 2 replace min and max position
        # other position do not matter
        if positions:

            for index in sorted(positions.keys()):
                number_str = positions[index]
                print(f"*** replacing first {number_str} on {index}")
                line = line.replace(number_str, translate[number_str], 1)

            # min_number_str = positions[min(positions.keys())]
            # print(f"*** replacing first {min_number_str}")
            # line = line.replace(min_number_str, translate[min_number_str], 1)  # only the left one

            # max_number_str = positions[max(positions.keys())]
            # print(f"*** replacing all {max_number_str}")
            # line = line.replace(max_number_str, translate[max_number_str]) # replace all

        print(f"**- {line}")
        found = []  # holding two numbers
        for char in line:
            if char in numbers:
                if not found:
                    found = [int(char) * 10, int(char)]  # first could also be last
                else:
                    found[1] = int(char)  # ok there are more than one number
        # print(found)
        line_sum = found[0] + found[1]
        print(f"=== {line_sum}")
        total_sum += line_sum
        alternate_sum += alternate
print("sum by replacing strings")
print(total_sum)
print("sum by matching string as they go")
print(alternate_sum)
