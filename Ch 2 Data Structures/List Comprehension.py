# List Comprehension
# The main purpose is to build a list from some data(list or string)
# By doing this method you will also be making your code "more readable"
# We call them List Comps
# Use [] brackets
# Syntax: [sequence(Target list or string) iterable]
# Goal: Build a List of Unicode codepoints from a list of symbols
# Unicode codepoint is a character encoding and is represented
# in numerical values
# The ord() function return an integer represents the Unicode
# character

symbols = '%$*@' # target string
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

symbols = '%$*@' # target list
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC' # The value of x target is constant
ord_char = [ord(x) for x in x]
print(x)
print(ord_char)

symbols = '%$*@' # target string
beyond_ascii = [ord(s) for s in symbols if ord(s) > 40]
print(beyond_ascii)

# Cartesian Product
# Ex: A = (@, #), B = (1, 0)
# A * B == {(@,1), (@,0), (#,1), (#,0)}
# Resulting {set} has a length equal to the length of the input tuples
# multiplied
# ListComps can generates lists from the Cartesian Product of
# two or more iterables
# Goal: Create a list of cars available in two energy sources
# and three car companys
energys = ['electric', 'fuel']
car_manufacturers = ['Ford', 'GM', 'Chrysler']
# ListComps generates a list of tuples arranged by (energy, car man)
cars = [(energy, car_manufacturer) for energy in energys
        for car_manufacturer in car_manufacturers]
print(cars)
# Nested for Loop
for energy in energys:
    for car_manufacturer in car_manufacturers:
        print((energy, car_manufacturer))
cars = [(energy, car_manufacturer) for car_manufacturer in car_manufacturers
        for energy in energys]
print(cars)




