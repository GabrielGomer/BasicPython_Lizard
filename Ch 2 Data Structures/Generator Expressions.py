# Generator Expressions
# The main purpose is to build a list from some data(list or string)
# By doing this method you will also be making your code "more readable"
# We call Genexps
# Genexps saves memory because it yields items one by one
# using the iterator protocol
# Syntax: (sequence(Target list or string) iterable)
# Using () brackets
# tuple() holds data for one field and the position of the item has meaning
# tuple(list or string) == tuple
# the ord(list or string) returns an integer represent the
# Unicode character
# Array Module
# Allows us to store numerical values more efficiently compared to a list
# array does not hold float obj packed bytes representing their
# machine values
# array.array: if list contains only numbers
# array.array: Syntax: ('typecode', [initializer value])
# Array Link: https://docs.python.org/3/library/array.html
# Goal: Take a string of symbol. Apply Genexps as well as the tuple
# ord, array.array f()
import array
symbols = '%$*@!9~' # target string
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))
print(array.array('f', (ord(symbol) for symbol in symbols)))

# Cartesian Product
# Ex: A = (@, #), B = (1, 0)
# A * B == {(@,1), (@,0), (#,1), (#,0)}
# Resulting {set} has a length equal to the length of the input tuples
# multiplied
# GenExps can generate lists from the Cartesian Product of
# two or more iterables
# Goal: Creat a list of dinners avaliable in two cooking preparations
# and three base foods
cook = ['baked', 'fried']
foods = ['potato', 'chicken', 'fish']
for dinner in ('%s %s' % (c, f) for c in cook for f in foods):
    print(dinner)

