# Lists
# Lists keep objects in order of index.
# It is defined by []

# Example of a list - index
# list_name      = [     0     ,   1  ,    2    ,   3     ]
crazy_x_partners = ['Carolina', 'JSON', 'Arthur', 'Lana!']

# print and show type (Read ALL)

print(crazy_x_partners)
print(type(crazy_x_partners))

# Get a particular record out (Read one)
# Lists are organised with index
print(crazy_x_partners[0]) # use the index inside square bracket [1]
print(type(crazy_x_partners))

# How do I print the last one?
print(crazy_x_partners[-1])

# Maybe we want to change a record in s specific index?
    # Re-assign an index -edited a record
crazy_x_partners[3] = 'LANAA!! (....) DANGER ZONE!!!'
print(crazy_x_partners[3])

# Add more people to the list (Create one) - append()
print(crazy_x_partners)
crazy_x_partners.append('Cyral Figus')
print(crazy_x_partners)

# insert in index specific location
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)

# Remove someone from the list (Destroy one)
crazy_x_partners.remove('JSON')
print(crazy_x_partners)
crazy_x_partners.remove('Malorie') # removes first one
print(crazy_x_partners)

# Remove using index
crazy_x_partners.pop(1) # Removes based on index
print(crazy_x_partners)

crazy_x_partners.pop() # Removes last entry
print(crazy_x_partners)

# Mixed data and lists
 # Lists can have many data types
hybrid_list = ['this is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]

# What happens when you have lots of records?
# Loops and other data.

# Tuples --> Immutable lists
# They do not change
# syntax
# my_tuple = ()
# tuples are defined by (), not using square brackets - != []
my_tuple = (2, 'hello', 22, 'more value')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
# my_tuple[0] = 30 # this will fail

# Range slicing
print(crazy_x_partners)
print(crazy_x_partners[:1]) # prints 0 to 1, 1 is not inclusive
print(crazy_x_partners [1:2]) # from 1 to 2, not inclusive of 2, not inclusive of number of the right of the range.

# Jumping/slicing
# syntax [N::M]
# N is where it starts.
# M is every record it prints.
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(example_list[1::2])
print(example_list[::3])
print(example_list[::1])

