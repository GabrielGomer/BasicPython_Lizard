# Augmented Assignment
# The id() function returns a unique id for the specified object.
# All objects in Python has its own unique id.
# The id is assigned to the object when it is created.
# The id is the object's memory address,'
# and will be different for each time you run the program.
# (except for some object that has a constant unique id, like integers from -5 to 256)
l = [1, 2, 3]
# ID of th initial list
print(id(l))
l *= 2
# Multiples the list is the same object with new items appended
print(l)
print(id(l))
t = (1, 2, 3)
# ID of the initial tuple
print(id(t))
t *= 2
# After * a new tuple is created
print(id(t))
# A += Assignment Puzzle
# What does constole return
t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)
# We get a Type Error
# DEBUG -tuples are immutable must convert to list before augmented assignment +=
