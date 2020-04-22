# List.sort method
# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax: list.sort(reverse=True or False, key=myFunc)
# Sorted():
#   -Accepts any iterable object as an arg
#     -Including immutable sequences and generators
#     -Any type of iterable will output a list
# list.sort and sorted(): 2 keyword args
#     -reversed: items are returned in decending
#     -key: one-arg f() that will be applied to each item produce its sorting list
#           Ex: Sorting a list of strings, key=str.lower (case insensitive sort)
#               key=len(sort by string length)
fruits = ['grape', 'raspberry', 'apple', 'orange']
# Results in a new list of strings sorted alphabetically
sorted(fruits)
# Inspecting the orignal list, we see it is unchanged
print(fruits)
# This is simply reverse alphabetical ordering.
sorted(fruits, reverse=True)
# New list of strings, sorted by length.
# Sorting algorithm is stable, grape and apple both have the same length in original order
sorted(fruits, key=len)
# String sorted in descending order of length. It is not the reverse of the previous result
sorted(fruits, key=len, reverse=True)
print(fruits)
# fruits is sorted
fruits.sort()
print(fruits)
# Sorting your list can allow you to efficiently search through them.