# Define the following variables
# first_name, last_name, age, eye_colour, hair_colour
first_name = 'Francis'
last_name = 'Thevipagan'
age = 25
eye_colour = 'Brown'
hair_colour = 'Black'

# Prompt user for input and Re-assign these
first_name = input('What is your first name?').capitalize().strip()
print(first_name)

last_name = input('What is your last name?').capitalize().strip()
print(last_name)

age = input('What is your age?').strip()
print(age)

eye_colour = input('What is your eye colour?').lower().strip()
print(eye_colour)

hair_colour = input('What is your hair colour?').lower().strip()
print(hair_colour)

# Print them back to the user as a conversation - interpolation or concatenation. Interpolation used here.

print(f'Hello {first_name} {last_name}, you are {age} years old, you have {eye_colour} eyes and {hair_colour} hair.')

# Section 2 - Calculate in what year was the person born?

Date_of_birth = (2019 - int(age))
Date_of_birth = 2019 - age
print(Date_of_birth)
print(f'You said you were {age}, hence you were born in {Date_of_birth}')
print(f'You said you were {age}, hence you were born in {2019 - int(age)}')
print(f'You said you were {age}, hence you were born in {2019 - age}')

