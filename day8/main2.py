#!/usr/bin/python3
import sys
import time

from lcm import lcm_with_offset


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
        step_size = series[-1]  # steps in interval
        steps = series[0]  # initial
        print(steps, step_size)
        sum_steps[start_position] = [steps, step_size]

    # brute force until all paths are at the same step - like lcm but
    # steps to first found target is the problem

    values = list(sum_steps.values())  # list of [start, step]
    print(values)

    print("calculating LCM with offset")
    print(lcm_with_offset(*values))


"""
paths look like that

**********************+---+---+---+---+---+---+---+---+---+
*******+----+----+----+----+----+----+----+----+----+----+-
*************************+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
************+-----+-----+----+-----+----+-----+-----+-----+

"""

