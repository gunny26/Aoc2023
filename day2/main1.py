#!/usr/bin/python3

possibles = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


possible_sum = 0
with open("input1.txt", "rt") as infile:
    for line in infile.read().split("\n"):
        if not line:
            continue
        print(line)
        game_id = int(line.split(":")[0].strip().split(" ")[-1])
        # print(game_id)
        # thats left :6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        possible = True
        for sub_result in line.split(":")[1].strip().split(";"):
            # something like that 3 blue, 4 red
            # print(sub_result)
            for result in [part.strip() for part in sub_result.split(",")]:
                amount = int(result.split(" ")[0])
                # print(amount)
                for color, max_amount in possibles.items():
                    if color in result:
                        if amount > max_amount:
                            possible = False
                            print(f"ERROR: {color} = {amount} <=  {max_amount}")
                        else:
                            print(f"OK   : {color} = {amount} <= {max_amount}")
        if not possible:
            print(f"{game_id} is impossible")
        else:
            possible_sum += game_id
print(f"result {possible_sum}")
