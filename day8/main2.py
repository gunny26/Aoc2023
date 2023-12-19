#!/usr/bin/python3
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

    sum_steps = {}
    for start_position, series in intervals.items():
        print(start_position, series)
        step_size = series[-1]
        steps = sum(series)
        print(steps, step_size)
        sum_steps[start_position] = (steps, step_size)

    while True:

        # cehcking if all steps are the same
        all_equal = None
        value = 0
        for position in sum_steps:
            steps = sum_steps[position][0]
            if all_equal is None:  # the first one
                all_equal = True
                value = steps
            else:
                if value != steps:  # they are not the same
                    all_equal = False
                    break

        if all_equal is True:
            print("found the least common multiplier ", sum_steps)
            break

        for position in sum_steps:  # count up
            steps, step_size = sum_steps[position]
            sum_steps[position] = (steps + step_size, step_size)
            print(position, steps)

        print()

