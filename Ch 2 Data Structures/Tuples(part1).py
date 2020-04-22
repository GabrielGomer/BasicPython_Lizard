# # Tuples
# # holds data for one field and the position of the item has meaning
# # Both immutabl and mutable
# # Sorting the tuple would destroy the data
# # because the meaning of each data item is given by its position
# # # Latitude and Longitude of DTW Airport
# dtw_coordinates = (42.2162, 83.3554)
# # Data about Detroit: Name, year, population(milions), population change(%)
# # area(km^2)
# city, year, pop, chg, area = ('Detroit', 2018, 4.3, 0.66, 370.1)
# # A list of tuples of the form (country_code, passport_number)
# traveler_ids = [('USA', '3119123321'), ('BRA', 'CE343'),
#                 ('ESP', '231asdas')]
# # Iterate through traveler_ids list passport is bound to each tuple
# # sorted() sort list from the items in an iterable
# # Syntax: sorted(iterable, key=None, reverse=False)
# for passport in sorted(traveler_ids):
#     # % formatting operator %s(string values) treats each field in tuple
#     # as separte values
#     print('%s/%s' % passport)
# # Unpacking for loop know how to retrieve items from a tuple separately
# # The _ is used as a placeholder for a value in tuple
# for country, __ in traveler_ids:
#     print(country)
#
# # Tuple Unpacking
# # Parallel Assignment
# # Syntax: *variable/arg: Grab excess items
# #   known as prefixing an argument
# #   when calling varable with *prefix_arg exclude *
# #    Can appear in any position of unpacking
# #   Can only be applied to exactly one variable
# dtw_coordinates = (42.2162, 83.3554)
# latitude, longitude = dtw_coordinates # tuple unpacking
# print(f'Latitude: {latitude} Longitude: {longitude}')
#
# # The divmod() returns a tuple containing the quotient
# # and the remainder when arg1( divident numerator)
# # arg2(divisor denominator)
# # Syntax:(divident numerator, divisor denominator) = (quotient, remainder)
# print(divmod(20, 8))
# t = (20, 8)
# # unpacking the args from the tuple t
# print(divmod(*t))
# quotient, remainder = divmod(*t)
# print(f'Quotient: {quotient} Remainder: {remainder}')

# os module uses operating system f()
import os
# BasicPython_Lizard/Ch 2 Data Structures/Tuples(part1).py
# Filepath consists of a head and tail
#   head = must have a /at its last index of string
#   tail = does not include / at its last index of string
_, filename = os.path.split('BasicPython_Lizard/Ch 2 Data Structures/Tuples(part1).py')
print(f'Filename: {filename}')
# Star * to grab excess items
# Parallel Assignment
# range() start from 0
# the 8rest is taking the remaing values and assigning
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)








