# 1 Array type
from array import array
from random import random
# 2 Create an array of double-precision floats(typecode 'd')
# from any iterable obj in this case a generator exps
floats = array('d', (random() for i in range(10**7)))
# 3 Inspect the last number in the array
print(floats[-1])
fp = open('floats.bin', 'wb')
# 4 Save the array to a binary file
floats.tofile(fp)
fp.close()
# 5 Create an empty array of doubles
floats2 = array('d')
fp = open('floats.bin', 'rb')
# 6 Read 10 million numbers from the binary file
floats2.fromfile(fp, 10**7)
fp.close()
# 7 Inspect the last number in the array
print(floats2[-1])
# 8 Verify the contents of the array match
print(floats2 == floats)
