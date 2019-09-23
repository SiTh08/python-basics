# 1st Assignment for post class
# # Use Variables, print and different data types
# # ask and store the following variables:
#  # First_Name, last_name, age, age_of_mother, 3 skills

first_name = input('What is your first name?').strip().capitalize()
print('Your name is', first_name)

last_name = input('What is your last name?').strip().capitalize()
print('Your last name is', last_name)

age = int(input('What is your age?').strip())
print('You are', age)

age_of_mother = int(input("What is your mother's age?").strip())
print('Your mother is', age_of_mother)

first_skill = input('What is your first skill?').strip().lower()
print('Your first skill is', first_skill)

second_skill = input('What is your second skill?').strip().lower()
print('Your second skill is', second_skill)

third_skill = input('What is your third skill?').strip().lower()
print('Your third skill is', third_skill)

#  # Print out the information in a formatted manner.
print(f'Hello {first_name} {last_name}, you are {age} years old, your mother is {age_of_mother} and your three skills are that you are a {first_skill.lower()}, {second_skill.lower()} and {third_skill.lower()}.')

#  # Calculate age difference between responder and mother
age_difference = age_of_mother - age
print(age_difference)

#  # store skills in a list
skill_set = [first_skill, second_skill, third_skill]
print(skill_set)

#  # print each skill in a formatted way.
print('Your three skills are that you are a', (first_skill.strip().lower()) + ', ' + (second_skill.strip().lower()) + ' and ' + (third_skill.strip().lower()) + '.')

#Skills = Good Problem Solver, Good team player, Good researcher
# # Definition of formatted
#  # a little context text
#  # appropriate string formatting like lower case or upper case, or other formats.