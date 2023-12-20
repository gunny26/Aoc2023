#!/usr/bin/python3

with open("input1.txt", "rt") as infile:
    indata = [line.strip() for line in infile.read().split("\n") if line]


total_value = 0
for line in indata:
    # print(line)
    rows = []
    numbers = [int(number) for number in line.split(" ")]
    rows.append(numbers)
    this_row = list(numbers)

    # calculating diff diff rows
    while True:
        print(this_row)
        diff = []
        for index in range(len(this_row)-1):
            diff.append(this_row[index+1] - this_row[index])
        print(diff)
        rows.append(diff)

        if all((col == 0 for col in diff if col)):
            break

        this_row = list(diff)

    print()

    # just for debug
    for row in rows:
        print(row)

    print()

    # adding 0 on latest row
    rows[-1].append(0)  # add zero to the last row

    # adding missing colums in very row
    for row_id in range(len(rows) - 2, -1, -1):
        print(row_id, rows[row_id])
        rows[row_id].append( rows[row_id][-1] + rows[row_id+1][-1])

    print()

    # just for debug
    for row in rows:
        print(row)

    total_value += rows[0][-1]

print("total value ", total_value)

