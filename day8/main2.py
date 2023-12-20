#!/usr/bin/python3
import sys
from math import lcm
import time


with open("input1.txt", "rt") as infile:
    lines = [line.strip() for line in infile.read().split("\n") if line]
    directions = lines[0]
    len_directions = len(directions)  # calculate only once
    print(directions)
    positions = {}
    for line in lines[1:]:
        position = line[0:3]
        left = line[7:10]
        right = line[12:15]
        print(position, left, right)
        positions[position] = (left, right)
    print()

    start_positions = [entry for entry in positions if entry[2] == "A"]  # initial start positions
    print(start_positions)

    starttime = time.time()
    steps = 0

    intervals = {}

    for position in start_positions:

        start_position = str(position)
        intervals[start_position] = []
        last_interval = 0

        while True:
            direction = directions[steps % len_directions]
            if direction == "L":
                position = positions[position][0]
            else:
                position = positions[position][1]

            if position[2] == "Z":
                print("* ", steps)
                intervals[start_position].append(steps)
                if last_interval == 0:
                    last_interval = steps
                else:
                    if last_interval == steps:  # loop detected
                        print("   found repeating cycle")
                        break
                    else:
                        last_interval = 0  # forget that
                steps = 0

            steps += 1
            if steps % 1000000 == 0:
                print(position, steps, time.time()-starttime)
                starttime = time.time()

        print(position)
        print("position ending on Z found in ", steps, " steps")
        print(intervals[start_position])


    # add up all paths to number of steps so far and interval of
    # repeating steps to get to the same entry
    sum_steps = {}
    for start_position, series in intervals.items():
        print(start_position, series)
        step_size = series[-1]
        steps = sum(series)
        print(steps, step_size)
        sum_steps[start_position] = [steps, step_size]

    # brute force until all paths are at the same step - like lcm but
    # steps to first found target is the problem

    values = list(sum_steps.values())  # list of [start, step]
    print(values)

    # get the value with highest step_size
    # add up to entry with highest step count
    # from there on ad
    # searching entry with highest steps
    test_entry = values[0]
    for value in values[1:]:
        if value[0] > test_entry[0]:
            test_entry = value
    print(f"using this value to test lcm {test_entry}")

    values.remove(test_entry)

    starttime = time.time()
    index = 0

    while True:

        result = [(test_entry[0] - step) % step_size for (step, step_size) in values[1:]]  # test all other value if they could get to this step without reminder

        if result.count(0) > 1:
            print("remainders ", result)
            # print(values)

        if not any(result):
            print("remainders ", result)
            print("result ", test_entry)
            break

        test_entry[0] = test_entry[0] + test_entry[1]

        index += 1
        if index % 10**6 == 0:
            print(f"duration for 10**6 iterations {(time.time()-starttime):0.2f}, steps {test_entry}")
            starttime = time.time()

"""

**********************+---+---+---+---+---+---+---+---+---+
*******+----+----+----+----+----+----+----+----+----+----+-
*************************+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
************+-----+-----+----+-----+----+-----+-----+-----+

"""

