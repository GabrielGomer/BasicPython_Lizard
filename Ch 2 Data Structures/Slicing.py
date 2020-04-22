# Slicing
# Must use []
# Compute the length of slice or range when start and stop are given: stop - start
# Syntax s[a:b]
# Extracts a slice from the s list that is from element a to element b,
# meaning it does not include b.
# Similar to how range(a, b) works.

l = [10, 20, 30, 40, 50, 60]
print(l[:2])    # split at 2 includes index 0, 1
print(l[2:])    # split at 2 includes index 2-5
print(l[:3])    # split at 3 includes index 0-2
print(l[3:])    # split at 3 includes index 3-5

# Slice Objects
# Syntax s[a:b:c] , s[include: include before: increment]
# seq[start:stop:step]
# Recount when traversing string, list, or tuple
s = 'skateboard'
print(s[::3])   # increments index 3
print(s[::-1])  # increment index -1 reversed string; moving backwards
print(s[::-2])  # increment index -2
print(s[2:9:2]) # split 2 every other 2 string values within 2-8

# Line items from a flat-file invoice
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
stock_keeping_unit = slice(0, 6)
description = slice(6, 40)
unit_price = slice(40, 52)
quantity = slice(52, 55)
item_total = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[unit_price], item[description])