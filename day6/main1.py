#!/usr/bin/python4

"""
Time:      7  15   30
Distance:  9  40  200
"""

with open("input1.txt", "rt") as infile:
    lines = [line.strip() for line in infile.read().split("\n")]
    times = [int(entry) for entry in lines[0].split()[1:]]
    print(times)
    distances = [int(entry) for entry in lines[1].split()[1:]]
    print(distances)

    points = []

    for index, distance in enumerate(distances):
        print(f"race {index} - record is {distance}")
        wins = 0
        for presstime in range(times[index] + 1):
            time_left = times[index] - presstime
            this_distance = presstime * time_left
            print(f"presstime {presstime} - distance {this_distance} - record {distance}")
            if this_distance > distance:
                print(f"new record")
                wins += 1
        points.append(wins)
    print(f"found {points} ways to break the record")
    result = 1
    for entry in points:
        result = result * entry
    print(f"result {result}")

