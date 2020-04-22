# MemoryView
# Changing the value of an array item by poking one of its bytes
# Syntax: array.array('typecode', initializer(must be a list))
import array
# 'h' signed short int
numbers = array.array('h', [-2, -1, 0, 1, 2])
# Build memoryview from array of 5 short signed integers (typecode 'h')
memv = memoryview(numbers)
print(len(memv))
# memv sees the same 5 items in the array
print(memv[0])
# Create memv_oct by casting the elements of memv to typecode 'B' (unsigned char)
memv_oct = memv.cast('B')
# Export elements of memv_oct as a list, for inspection
print(memv_oct.tolist())
# Assign value 4 to byte offset 5
memv_oct[5] = 4
print(memv_oct.tolist())
# Note change to numbers: a 4 in the most significant byte of a 2 byte unsigned integer is 1024
print(numbers)