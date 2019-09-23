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

