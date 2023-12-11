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

def print_matrix(matrix):
    print(f"matrix dimension {len(matrix)} x {len(matrix[0])}")
    # debug output
    for row in matrix:
        line = " "
        for col in row:
            line += f"{col:3} "
        print(line)


def get_matrix(rows, cols, initial=0):
    matrix = []
    for row in range(rows):
        matrix.append([initial] * cols)
    return matrix


def mul_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    assert len(matrix2) == rows
    assert len(matrix2[0]) == cols
    result = get_matrix(rows, cols, 0)
    for col in range(rows):
        for row in range(cols):
            result[row][col] = matrix1[row][col] * matrix2[row][col]
    return result


# first step translate numbers, in every matrix position write the number
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
        number = ""
        if not cols:
            cols = len(row)
        n_row = [0] * len(row)
        for index, c in enumerate(row):
            # print(index, c)
            if c.isnumeric():  # could grow up to a number
                number += c
            else:
                if number:
                    print(f"found {number}")
                    for i in range(len(number)):
                        n_row[index-i-1] = int(number)
                number = ""
                if c != ".":  # a symbol
                    n_row[index] = -1
        print("replacing with")
        print(n_row)
        assert len(n_row) == cols
        matrix.append(n_row)

rows = len(matrix)
print_matrix(matrix)

# step 2 eliminating all numbers not near any symbol
symbol_matrix = get_matrix(rows, cols, 0)  # python mistake !!!
print_matrix(symbol_matrix)
for rownum in range(1, rows - 1):
    for colnum in range(1, cols -1):
        if matrix[rownum][colnum] == -1:  # place of symbol
            print(f"symbol in [{rownum}, {colnum}]")
            # setting corners to 1
            symbol_matrix[rownum-1][colnum-1] = 1 # center
            symbol_matrix[rownum-1][colnum] = 1 # center
            symbol_matrix[rownum-1][colnum+1] = 1 # center
            symbol_matrix[rownum][colnum-1] = 1 # center
            symbol_matrix[rownum][colnum] = 0 # center
            symbol_matrix[rownum][colnum+1] = 1 # center
            symbol_matrix[rownum+1][colnum-1] = 1 # center
            symbol_matrix[rownum+1][colnum] = 1 # center
            symbol_matrix[rownum+1][colnum+1] = 1 # center
            # print_matrix(symbol_matrix)

# step 3 multiplying original matrix with symbol matrix,
# only elemts with part number are left, but there could be double part numbers
print_matrix(matrix)
print_matrix(symbol_matrix)
result = mul_matrix(matrix, symbol_matrix)
print_matrix(result)

# step 4 get rid of double parts
# flatten out matrix
flat = []
unique_numbers = set()
for row in result:
    for number in row:
        unique_numbers.add(number)
        flat.append(number)

for number in unique_numbers:
    print(number, flat.count(number))

print(f"total_sum : {sum(unique_numbers)}")
