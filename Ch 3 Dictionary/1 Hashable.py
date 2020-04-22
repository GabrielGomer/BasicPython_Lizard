# Hashable
# Obj is hashable if hash value never changes during its lifetime
# Can be compared to other objects
# Atomic immutable types(str, bytes, numeric types)
# Tuple is hashable iff all items are hashable/flat/immutable
# The hash() method returns the hash value of an object if it has one.
# Hash values are just integers which are used to compare dictionary keys
# during a dictionary lookup quickly.
# Syntax: hash(object)
tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
# print(hash(tl)) # Since list is mutable TypeError
# The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
# Syntax: frozenset([iterable])
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# Order Does Not Matter
# dict()
# zip()
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3,'one': 1,'two': 2})
print(a == b == c == d== e)
