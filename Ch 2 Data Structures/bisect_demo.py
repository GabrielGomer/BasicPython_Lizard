# Searching with bisect
# The bisect module is the standard library for the binary search algorithms
import bisect
import sys

hay_stack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# 'd' Decimal iteger. Outputs the number in base 10.
row_fmt = '{0:2d} @ {1:2d}  {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(needles):
        # Use the chosen bisect f() to get the insertion point
        position = bisect_fn(hay_stack, needle)
        # Build a pattern of vertical bars proportional to the offset
        offset = position * '  |'
        # Print formatted row showing needle and insertion point
        print(row_fmt.format(needle, position, offset))


if __name__ == '__main__':
    # Choose the bisect f() to use according to the last cmd line arg
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    # Print header with name of f() selected
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in hay_stack))
    demo(bisect_fn)

# # Application of biscect: Do this in console
# # Given a test score, grade return the corresponding letter grade
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.biscect(breakpoints, score)
#     return grades[i]
#
#
# print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
#
