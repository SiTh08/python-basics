# # Numerical Data types
# # - Int, long, float, complex
# # These are numerical data types, which we can use numerical operators.
#
# # Complex and Long we don't use as much
# # Complex brings an imaginary type of number
# # Long - are integers of unlimited size. Prime number
#
#
# # int - Stands for integers
# # Whole numbers
#
# my_int = 10
# print(my_int)
# print(type(my_int))
#
# # Operators - Add, Subtract, divide and multiply
#     # Exponential
#
# print(4 + 3)
# print(4 - 3)
# print(4/2) # Divisions automatically get converted to float
# print(125//3) # Keeps it as a integer / drops the decimal
# print (5/2)
# print (5//2)
# print(4 * 3)
# print(3**2)
#
# # Modulus looks for the remainders number
# # %
#
# print(11%3) ## --> 3*3 = 9, so 2 is the remainder
# print(14%5) ## --> 2*5 = 10, so 4 is the remainder
#
# # Floats = decimals
#
# # Comparison operators # --> (output) boolean value (true or false)
#
# # == - comparison operator
# # < / > - smaller and bigger than
# # <= - smaller than or equal
# # >= - bigger than or equal
# # != - not equal
# # is and is not - equals or not equals
#
# my_variable1 = 10
# my_variable2 = 13
# print(my_variable1 == my_variable2)
# print(my_variable1 > my_variable2)
# print(my_variable1 < my_variable2)
# print(my_variable2 >= 13)
# print(my_variable2 is 13)
# print(my_variable2 is not 13)
#
# # ref to python standard library
#
# # Boolean Values
# # Defined by whether True or False
# print(type(True))
# print(type(False))
# print (0 == False)
# print (1 == True)
#
# ## None
# print(None)
# print(type(None))
# print(bool(None))
# print(0 == None)
# print(False == None)
# print (False == bool(None)) ctrl+/

print ('Logical and & or --------')
# Logical AND & OR
a = True
b = False

# USing *and* both sides have to be true for it to result in true
print(a and True)
print ( (1 == 1) and (True))
print((1 == 1) and False)

# using *or*, OnNLY 1 side needs to be true
print('this will print true')
print (True or False)
print(True or 1 == 2)
print('this will print false')
print(False or 1 == 2)


