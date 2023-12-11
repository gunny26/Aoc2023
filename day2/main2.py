#!/usr/bin/python3

colors = [
    "red",
    "green",
    "blue",
]


total_sum = 0
with open("input2.txt", "rt") as infile:
    for line in infile.read().split("\n"):
        if not line:
            continue
        print(line)
        game_id = int(line.split(":")[0].strip().split(" ")[-1])
        # print(game_id)
        # thats left :6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        max_amounts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for sub_result in line.split(":")[1].strip().split(";"):
            # something like that 3 blue, 4 red
            # print(sub_result)
            for result in [part.strip() for part in sub_result.split(",")]:
                amount = int(result.split(" ")[0])
                # print(amount)
                for color in colors:
                    if color in result:
                        max_amounts[color] = max(max_amounts[color], amount)
        print(f"{game_id} is possible with {max_amounts}")
        line_result = 1
        for value in max_amounts.values():
            line_result = line_result * value
        print(line_result)
        total_sum += line_result
print(f"result {total_sum}")
