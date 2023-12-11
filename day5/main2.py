#!/usr/bin/python3
import sys
"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""



seed_ranges = None
seeds = []  # holding seeds on first line
nexts = []
maps = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {},
}


def get_next(index, key):
    mapname = list(maps.keys())[index]  # get actual mapname
    if index == 6: # we are at location level
        if key in maps[mapname]:
            #print(" " * index, mapname, key, maps[mapname][key])
            return maps[mapname][key]  # the second in the tuple
        else:
            #print(" " * index, mapname, key, key)
            return key
    else:
        if key in maps[mapname]:
            #print(" " * index, mapname, key, maps[mapname][key])
            return get_next(index+1, maps[mapname][key])
        else:
            #print(" " * index, mapname, key, key)
            return get_next(index+1, key)


def analyze_seed(seed):
    """ get one seed and find every route to location """

    #print(f"searching for seeds {seeds}")
    previous_map = None
    numbers = None
    mapname = None

    for line in indata:

        if not line:  # blank lines
            continue

        if line.startswith("seeds:"):  # first line
            pass

        elif "map" in line:  # headline of next map
            mapname = line.split(" ")[0]  # get actual mapname, this will change
            # print("next mapname found:", mapname)

            # switching interestin index numbers
            if not previous_map:  # thats the first map
                number = seed  # get from seeds
            else:
                # at least all interesting numbers must be added, if
                # they got no entry
                if number not in maps[previous_map]:
                    # print(f"- adding index for interesting number {number} for previous {previous_map}")
                    maps[previous_map][number] = number

                number = maps[previous_map][number]  # get interesting numbers from last map
            # print("switching interesting number: ", numbers)

        else:  # some numbers
            destination_start, source_start, range_length = [int(number) for number in line.split(" ")]
            # print(destination_start, source_start, range_length)
            source_end = source_start + range_length - 1  # PROBLEM !!! - counting at 1 not zero, cost me an hour
            if source_start <= number <= source_end:  # this number is in range
                source_index = number  # thats the only interesting for this number
                index = number - source_start  # calculate index
                destination_index = destination_start + index  # thats the destination for this number
                maps[mapname][source_index] = destination_index  # relationship
                # print(f"-- adding relationship  {number} : {destination_index}")
            else:
                # print(f"-- skipping, {number} is not in range [{source_start} : {source_end}]")
                pass
            previous_map = mapname  # remember mapname
    return number


with open("input1.txt", "rt") as infile:
    indata = [line.strip() for line in infile.read().split("\n")]

    lowest_location = sys.maxsize   # starting point

    for line in indata:

        if not line:  # blank lines
            continue

        if line.startswith("seeds:"):  # first line
            print("found seed ranges")
            seed_ranges = [int(number) for number in line.split(":")[1].strip().split(" ")]
            print(seed_ranges)
            for index in range(0, len(seed_ranges), 2):
                start = seed_ranges[index]
                stop = start + seed_ranges[index+1]
                print(start, stop)
                for seed in range(start, stop):
                    lowest_location = min(lowest_location, analyze_seed(seed))
                print(lowest_location)

    print(f"lowest_location found {lowest_location}")
