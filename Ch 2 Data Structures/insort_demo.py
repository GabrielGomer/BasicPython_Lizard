import bisect
import random
# bisect: find within a sorted sequence
# insort: insert items within a sorted sequence
# - insort(seq, item) inserts into seq so
# as to keep seq in ascending order.
# Insort keeps a sorted seq always sorted
# Insort takes optional
# lo, hi args to limit the search to a sub-seq
size = 7

random.seed(1729)

my_list = []
for i in range(size):
    new_item = random.randrange(size*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
