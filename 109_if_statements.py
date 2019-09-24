# Control flow - if statements
# Controls where the code is going to go.
# Depending on the results of the evaluations that return True or False, it runs a block of code or not.


# syntax
# if <condition>:
    # block
# elif <condition>:
    # block
    # block does stuff
# else:
    # block

weather = 'snowy and rainy and stormy'

if ('rainy' in weather) and ('stormy' in weather):
    print('stay home')
elif weather == 'rainy':
    print('take an umbrella')
elif weather == 'snowy':
    print('wear boots and scarf')
else:
    print('take shades')

# - you can vote and drive
# - you can vote
# - you can drive
# - you cannot legally drink but your mates/uncle might have your back.
# - You are too young, go back to school.

age = 19
driver_licence = True

if (age >= 16) and driver_licence == False:
    print('You can vote.')
elif (age > 17) and driver_licence == True:
    print('You can vote and drive.')
elif (age > 17) and driver_licence == False:
    print('You can vote.')
else:
    print('You are too young, go back to school.')

