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

    position = "AAA"  # initial start positions

    starttime = time.time()
    steps = 0

    while True:
        direction = directions[steps % len_directions]
        if direction == "L":
            position = positions[position][0]
        else:
            position = positions[position][1]

        if position == "ZZZ":
            break

        steps += 1
        if steps % 1000000 == 0:
            print(position, steps, time.time()-starttime)
            starttime = time.time()

    print(position)
    print("position ZZZ found in ", steps, " steps")
