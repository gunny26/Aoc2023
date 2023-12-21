#!/usr/bin/python3
from math import lcm

def mylcm_wrong(*values):
    """ thats wrong """
    print(values)
    steps = list(values)
    while not all((value == values[0] for value in values[1:])):  # comparing all items to first one
        values = [value + step for (value, step) in zip(values, steps)]  # adding up one
        print(values)
        input()
    return values[0]

def mylcm1(*values):
    # print(values)
    value = step = min(values)
    other_values = list(values)
    other_values.remove(value)
    while not all((value % other_value == 0 for other_value in other_values)):  # comparing all items to first one
        value = value + step
        # print(value)
        # input()
    return value

def lcm_with_offset(*offset_and_step):
    min_value = None  # finding min values, by offset
    for entry in offset_and_step:
        if min_value is None:
            min_value = list(entry)
        else:
            if entry[0] < min_value[0]:
                min_value = list(entry)
    print("chosen min value: ", min_value)

    other_values = list(offset_and_step)
    other_values.remove(tuple(min_value))

    print("other values to compare: ", other_values)

    while True:

        ret = []
        for entry in other_values:
            diff = min_value[0] - entry[0]
            print(entry, diff, max(diff, 0) % entry[1])
            ret.append(max(diff, 0) % entry[1] == 0)
        if all(ret):  # check if all other series without remainder
            break  # thats it

        min_value[0] += min_value[1]
        print(min_value)

    return min_value[0]


print(lcm(3, 4, 5))
print(mylcm1(3, 4, 5))
print(lcm_with_offset((100, 3), (110, 4), (120, 5)))
print(lcm_with_offset((123234, 3), (23452345, 4), (12312312, 5)))

