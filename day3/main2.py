#!/usr/bin/python3

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# not right: 321498 too low
# not right: 524521 too low

def print_matrix(matrix):
    print(f"matrix dimension {len(matrix)} x {len(matrix[0])}")
    # debug output
    for row in matrix:
        line = " "
        for col in row:
            if col is None:
                line += "  . "
            else:
                line += f"{col:3} "
        print(line)



# first step translate numbers, in every matrix position write the number
i_matrix = []
matrix =[]
rows = None
cols = None
with open("input1.txt", "rt") as infile:
    for row in infile:
        row = row.strip()
        if not row:
            continue
        print(f"analyzing, line legth = {len(row)}")
        print(row)
        i_matrix.append(row)
        number = ""
        if not cols:
            cols = len(row)  # number columns to store
        n_row = [0] * cols
        for index, c in enumerate(row):
            # print(index, c)
            if c.isnumeric():  # could grow up to a number
                number += c
            else:
                if number:  # there exists some number
                    print(f"found {number}")
                    for i in range(len(number)):
                        n_row[index-i-1] = int(number)
                if c != ".":  # a symbol
                    n_row[index] = None
                number = ""

        # SPECIAL case, there could be a number until the last character
        if number:
            print(f"found {number} non end of line")
            for i in range(len(number)):
                n_row[cols-i-1] = int(number)

        print("replacing with")
        print(n_row)
        assert len(n_row) == cols
        matrix.append(n_row)
rows = len(matrix)

print_matrix(matrix)

total_sum = 0
# step 2 counting the sum around every symbol
for rownum in range(1, rows - 1):
    for colnum in range(1, cols -1):
        if matrix[rownum][colnum] is None:  # place of symbol
            numbers = []  # count every part number only once

            numbers.append(matrix[rownum-1][colnum-1])
            numbers.append(matrix[rownum-1][colnum])
            numbers.append(matrix[rownum-1][colnum+1])

            numbers.append(matrix[rownum][colnum-1])
            numbers.append(matrix[rownum][colnum+1])

            numbers.append(matrix[rownum+1][colnum-1])
            numbers.append(matrix[rownum+1][colnum])
            numbers.append(matrix[rownum+1][colnum+1])

            assert None not in numbers  # no other gear nearby

            u_numbers = set((number for number in numbers if number != 0))

            if len(u_numbers) == 2:  # not a valid gear if there are not exactly to numbers
                total_sum += list(u_numbers)[0] * list(u_numbers)[1]  # set could not be indexed
                print("this is a valid gear")

            for number in u_numbers:
                print(f"number {number} appears {numbers.count(number)} times")
                assert numbers.count(number) < 4
            print(f"symbol in [{rownum:3}, {colnum:3}] = {sum(u_numbers):4} = {u_numbers} = {numbers}")
            print(f"original matrix")
            print(f"   {i_matrix[rownum-1][colnum-1]:3} {i_matrix[rownum-1][colnum]:3} {i_matrix[rownum-1][colnum+1]:3}")
            print(f"   {i_matrix[rownum][colnum-1]:3} {i_matrix[rownum][colnum]:3} {i_matrix[rownum][colnum+1]:3}")
            print(f"   {i_matrix[rownum-+1][colnum-1]:3} {i_matrix[rownum+1][colnum]:3} {i_matrix[rownum+1][colnum+1]:3}")
            print(f"translated matrix")
            print(f"   {numbers[0]:3} {numbers[1]:3} {numbers[2]:3}")
            print(f"   {numbers[3]:3}   * {numbers[4]:3}")
            print(f"   {numbers[5]:3} {numbers[6]:3} {numbers[7]:3}")
            assert len(set(numbers[:3])) < 4  # above, including 0
            assert len(set(numbers[3:5])) < 4  # below
            assert len(set(numbers[5:])) < 4  # on the same line
            assert len(set(numbers)) < 7  # all together
            try:
                assert sum(u_numbers) > 0
            except AssertionError as exc:
                print(i_matrix[rownum-1][colnum-1:colnum+2])
                print(matrix[rownum-1][colnum-1:colnum+2])

                print(i_matrix[rownum][colnum-1:colnum+2])
                print(matrix[rownum][colnum-1:colnum+2])

                print(i_matrix[rownum+1][colnum-1:colnum+2])
                print(matrix[rownum+1][colnum-1:colnum+2])
                raise exc


print(f"total_sum : {total_sum}")
