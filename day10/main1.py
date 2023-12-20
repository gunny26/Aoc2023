#!/usr/bin/python3

with open("example1a.txt", "rt") as infile:
    indata = [line.strip() for line in infile.read().split("\n") if line]

print(indata)
for row in indata:
    print(row)

# find start
for row_id, row in enumerate(indata):
    line = indata[row_id]
    try:
        col_id = line.index("S")
        print(row_id, col_id)
        start_pos = (row_id, col_id)
    except ValueError:
        pass  # not in this row
print("found start position at ", start_pos)
