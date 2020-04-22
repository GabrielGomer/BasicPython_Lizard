# Nested Tuple Unpacking
# Ex: (a, b, (c, d))
# Each tuple holds a tuple of four fields
# Data: (City, abbreviation, population, (latitude, longitude))
metro_areas = [
    ('Detroit', 'DET', 673104, (42.2162, 83.3554)),
    ('New York City', 'NYC', 8.623, (40.7128, 74.0060)),
    ('San Francisco', 'SF', 884363, (37.7749, -122.4194)),
    ('Connecticut', 'CT', 3.573, (41.6032, 73.0877)),
    ('Austin', 'ATX', 931830, (30.2672, 97.7431)),
]
# format()- Link: https://www.programiz.com/python-programming/methods/string/format
#   -Number formatting with alignment
#   -Numbers formatting with format()
# Syntax : {} is used a placeholder for everything in format f() similar to %s
# Ex: {:5d} takes an iteger arg with a width of 5 by default it aligns to right
# {:9.4f} f is stating to round 4 digits for float value
# Type   Meaning
# <      Left aligned to the remaining space
# ^      Center aligned to the remaining space
# >      Right aligned to the remaining space
# =      Forces the signed(+)(-) to the leftmost position
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, abrev, pop, (latitude, longitude) in metro_areas:
    if longitude >= 0:
        print(fmt.format(name, latitude, longitude))
