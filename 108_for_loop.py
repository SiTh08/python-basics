# Syntax

# For <placeholder> (items are going to appear like a variable within the loop) in <iteratable>: # don't forget the colon.
#         block of code
#         Indented gets run every iteration

# cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corvette' ]
#
# for car in cars:
#     breakpoint()
#     print('hey : D 2')
#     print(car)
#
# embedded_list = [['Filipe','Francis'], ['Mustafa', 'David', 'Jillian']]
#
# for data in embedded_list:
#     print(data)
#     breakpoint()
#     for name in data:
#         print(name.capitalize())

student1 = {
    'name':'Arya Stark',
    'stream':'Many Face',
    'grade': 10,
    'complete modules': ['sword', 'augmented sense', 'no face', 'no name']
}

# for key in student1:
#     print(key)
#     print(student1[key])

for key in student1:
    print(key.capitalize(),':', student1[key])

# for number, key in enumerate(student1):
#     print(number, key.capitalize(),':', student1[key])
#
count_1 = 1
list_of_skills = []
for key in student1:
    print(f'{count_1} - {key}: {student1[key]}')
    count_1 += 1
    list_of_skills.append(student1['stream'])
    print(list_of_skills)

students = {
    'student1': student1,
    'student2':{
    'name': 'Stirling Archer',
    'stream': 'Chaos',
    'grade': 10,
    'complete modules': ['danger', 'robust liver', 'mummy issues']
    }
}

for key1 in students:
    print(key1)
    print(type(students[key1]))
    for key2 in students[key1]:
        print(key2)
        print(students[key1][key2])
        print(f'{key2}, {students[key1][key2]}')

count_2 = 1
for student_key in students:
    # print(student_key)
    count_2 = 1
    for key in students[student_key]:
        print(count_2, key, ':', students[student_key][key])
        count_2 += 1