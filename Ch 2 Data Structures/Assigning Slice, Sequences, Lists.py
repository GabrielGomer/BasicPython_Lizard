# Assigning to slices
# Add comment
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
l[2:5] = 100 #
# l[2:5] = 100
l[2:5] = [100]
print(l)

# Working with + and * with Sequences
# Concatenate multiple copies of the same seq, multiply it by an itenger.
# Both + and * create a new object
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

# Building Lists of Lists
# A list with three lists of length 3
# Create a tic tac toe board
# Create a list of three list of three items each. Inspect the structure
board = [['_'] * 3 for i in range(3)]
print(board)
# Place a mark (0) in row1, column 2
board[1][2] = '0'
# Result
print(board)

# List with 3 references to the same list is useless
# Outer list is made of 3 references to the same inner list
useless_board = [['_'] * 3] * 3
print(useless_board)
# Placing a mark (X) in row1, column2
# Notice that all rows refer to same object
useless_board[1][2] = 'X'
print(useless_board)

# The list comprehension method that we used above is equivalent:
board = []
# Each iteration builds a new row and appends it to board
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
# Placing a mark in row2, column 0
board[2][0] = 'X'
# Result
print(board)
