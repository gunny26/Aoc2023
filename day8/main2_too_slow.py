#!/usr/bin/python3

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

    # get initial start positions
    start_positions = [key for key in positions.keys() if key[2] == "A"][:1]
    print(start_positions)
    len_start_positions = list(range(len(start_positions)))  # calculate only once

    # dones = {}  # loophole detection

    starttime = time.time()
    steps = 0

    while not all((position[2] == "Z" for position in start_positions)):
        direction = directions[steps % len_directions]

        for position_id in len_start_positions:
            # print(position, direction)
            position = start_positions[position_id]
            if direction == "L":
                start_positions[position_id] = positions[position][0]
            else:
                start_positions[position_id] = positions[position][1]
        # print(start_positions)

        # loophole detection
        # key = "".join(start_positions)
        # if key in dones:
        #     break
        # dones[key] = direction

        # if all((position[2] == "Z" for position in start_positions)):
        #     break

        steps += 1
        if steps % 1000000 == 0:
            print(start_positions, steps, time.time()-starttime)
            starttime = time.time()

    print(start_positions)
    print("all positions ending with Z found in ", steps, " steps")
