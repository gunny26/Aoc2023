#!/usr/bin/python4

"""
Time:      7  15   30
Distance:  9  40  200
"""

with open("input1.txt", "rt") as infile:
    lines = [line.strip() for line in infile.read().split("\n")]
    times = [entry for entry in lines[0].split()[1:]]
    time = int("".join(times))
    print(time)
    distances = [entry for entry in lines[1].split()[1:]]
    distance = int("".join(distances))
    print(distance)

    print(f"record is {distance}")
    wins = 0
    for presstime in range(time + 1):
        this_distance = presstime * (time - presstime)
        # print(f"presstime {presstime} - distance {this_distance} - record {distance}")
        if this_distance > distance:
            # print(f"new record")
            wins += 1
    print(f"result {wins}")

