# Functions and functional programming
# Functions are like a machine

# They take in arguments (optional)
# They have a block of code to run
# They output (return) something (optional)

#Running and Calling a function
# They need to be called to be executed.

# Good practices:
# good names (names that humans understand and descriptive)
# following convention (lower case and separated with underscore)
# They should be atomic and small - make small test:
    # This makes them testable.
    # Reduces technical debt.
# comments when appropriate
# DO NOT PRINT IN FUNCTION -- return!

# functions allow us to be DRY
# Don't need to repeat yourself.

# Aim for cleaner, dryer and testable.

# def full_name ():
#     print('Hey, Zeus')


def return_hey_to_zeus():
    return ('Hey, Zeus')

print(return_hey_to_zeus())

#              (Argument, argument1)
def full_name (f_name, l_name):
    full = f_name + ' ' + l_name
    return full

print(full_name('Misty', 'Sparks')) # Arguements are not optional (here)

#This is the basis of all test
 # set up (give controlled inputs)
 # Assertion (check for expected outcomes)
 # Feed back output to our users. ,
print(full_name('Frank', 'Henry'))
