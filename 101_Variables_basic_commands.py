# Variables in Python
 # Variable is a box. You can give it a name and put stuff inside.

# Assigning a variable.
 # Giving box a name and putting stuff inside.
box_variable = 'Books and stuff'

# looking inside the box.
print(box_variable)

# Re-assigning a variable.
# Variables are mutable - Hence they can change/be re-assigned.
box_variable = "CD's and other stuff"
print(box_variable)

# Re-assigning with a integer.
# Variable can hold any data type inside.
box_variable = 14
print(box_variable)

# Important python function
# print(arguments) - no space between print and ( and lowercase p.
print('hello') # Printing string
print(box_variable) # Printing variable
print ('hello', box_variable) # Overloading with two argument

# Argument put into method or function vs. variable.

# type(arg)
# Output the data type of an object
print(type('hello'))
print(type(14))
print(type(14.0))
variable_num =  '14'
my_list = [1, 2, 2, 'hey']
print(type(my_list))
# print(type('10'*variable_num)) # This will break.
