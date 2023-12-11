#!/usr/bin/python3

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


seeds = []  # holding seeds on first line
nexts = []
mapnames = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

maps = {}
mapname = None
previous_map = None
with open("input1.txt", "rt") as infile:
    for line in infile:
        line = line.strip()

        if not line:  # blank lines
            continue

        if line.startswith("seeds:"):  # first line
            seeds = [int(number) for number in line.split(":")[1].strip().split(" ")]
            print("seeds found: ", seeds)
        elif "map" in line:  # headline of next map
            mapname = line.split(" ")[0]  # get actual mapname, this will change
            source_map, _, destination_map = mapname.split("-")
            if mapname not in maps:
                maps[mapname] = {}
            if source_map not in maps:
                maps[source_map] = {}
            if destination_map not in maps:
                maps[destination_map] = {}
            print("next mapname found:", mapname)
            # switching
            if not previous_map:  # thats the first map
                numbers = list(seeds)  # get from seeds
            else:
                numbers = list(maps[previous_map].values())  # get interesting numbers from last map
            print("interesting number: ", numbers)
        else:  # some numbers
            destination_start, source_start, range_length = [int(number) for number in line.split(" ")]
            print(destination_start, source_start, range_length)
            for number in numbers:
                source_end = source_start + range_length
                if source_start <= number <= source_end:  # this number is in range
                    index = number-source_start  # calculate index
                    source_index = number  # thats the only interesting
                    destination_index = destination_start + index
                    maps[mapname][source_index] = destination_index  # relationship
                else:
                    print(f"  skipping, {number} is not in range [{source_start} : {source_end}]")
            previous_map = mapname  # remember mapname

            # at least all interesting number must be added, if they had
            # no entry
            for number in numbers:
                if not number in maps[mapname]:
                    maps[mapname][number] = number

def get_next(index, key):
    mapname = mapnames[index]  # get actual mapname
    if index == 6: # we are at location level
        if key in maps[mapname]:
            print(" " * index, mapname, key, maps[mapname][key])
            return maps[mapname][key]  # the second in the tuple
        else:
            print(" " * index, mapname, key, key)
            return key
    else:
        if key in maps[mapname]:
            print(" " * index, mapname, key, maps[mapname][key])
            return get_next(index+1, maps[mapname][key])
        else:
            print(" " * index, mapname, key, key)
            return get_next(index+1, key)

print()
print("searching for lowest location")
# now get seed to location relationship
lowest_location = -1
for seed in seeds:
    location = get_next(0, seed)
    print(f"seed {seed} is on location {location}")
    if lowest_location == -1:
        lowest_location = location
    else:
        lowest_location = min(location, lowest_location)
print(f"lowest_location found {lowest_location}")
