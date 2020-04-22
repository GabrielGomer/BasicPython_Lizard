# Handling Missing Keys w/ setdefault
# dict access w/ d[k] KeyError when k is not an existing key
# d.get(k, default) == d[k]
# sys modules allows user to enter input dynamic data into console
# For this example a text file  containing zen_of_python.txt
# re module provides regular expression matching operations
# re Link: https://docs.python.org/3/library/re.html
# for testing re: https://pythex.org/
#       compile() -Compile a regular expression pattern into a regular expression object
#       Syntax: re.compile(pattern)
#       finditer() -Return an iterator yielding MatchObject instances over all
#       non-overlapping matches for the RE pattern in string.
#       The string is scanned left-to-right, and matches are returned in the order found.
#       Empty matches are included in the result.
#       Syntax: re.finditer(pattern, string, flags=0)
# enumerate()-The enumerate() method adds counter to an iterable and returns it (the enumerate object).
#     Syntax: enumerate(iterable, start=0(optional))
#     The result will be the (counter depending on start value, item)
# group()
# append()
""" Build an index mapping word -> list of occurrences"""
import sys
import re

word_re = re.compile(r'\w+')
index = {}

# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in word_re.finditer(line):
#             word = match.group()
#             column_no = match.start()+1
#             location = (line_no, column_no)
#             # this is ugly; coded like this to make a point
#             # Get the list of occurrences for word, or [] if not found.
#             occurrences = index.get(word, [])
#             # Append new location to occurrences
#             occurrences.append(location)
#             # Put changed occurrences into index dict; this entails a second search through the index
#             index[word] = occurrences
#
#
# # print in alphabetical order
# # Output = word [(line,number) , ...]; Number of occurrences
# for word in sorted(index, key=str.upper):
#     print(word, index[word])

with  open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])