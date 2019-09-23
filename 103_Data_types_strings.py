# Strings
# These are a list of characters put together.
# Defined by '' or " "

# my_string = 'Amazing Grilled Fish'
# print(type(my_string))
#
# # you can print it
# print(my_string)

# Joining of strings - concatenation
first_name = 'Boris'
last_name = 'Becker'
print(first_name[0]) # sting is a list of characters, so behaves like a list

# Concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)
print('string', 14)

# Interpolation
name = 'Rachel'
welcome_message = 'hey there, how you doinn? ;)'
print(f'hey there, {name} how you doinn? ;)')
# place an f on the left/beginning of the string
# then you can use {} to interpolated python variables inside

# Useful Methods for strings
my_string = '  Hello this is an amazing string    '

#.count()
print(my_string.count('i'))
print(my_string.count(' '))

#.strip() - remove trailing white spaces.
print(my_string.strip())

# len() # Not a method - general method built in
print(len(my_string))

#.lower() - lowercase
print(my_string.lower())

#.upper() - uppercase
print(my_string.upper())

#.capitalize() - sentence case
print(my_string.strip().capitalize())

#.replace(arg_int, arg_two)
print(my_string.replace('an', 'the'))

#.split(arg) --> list
print(my_string.split(' '))
print(type(my_string.split('i')))


