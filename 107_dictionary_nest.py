# # Nested list and dictionaries.
# #
# #
# # nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice'], {'name':'Buttercup'}]
# #
# # variable_bread = nested_list [0]
# # variable_nested = nested_list[2]
# #
# # print(type(variable_bread))
# # print(variable_nested[4])
# #
# # print(nested_list[0])
# # print(nested_list[2][4])
# #
# # print(nested_list[2][5]['name'])

student1 = {
    'name':'Arya Stark',
    'stream':'Many Face',
    'grade': 10,
    'complete modules': ['sword', 'augmented sense', 'no face']
}

students = {
    'student1': student1,
    'student2':{
    'name': 'Stirling Archer',
    'stream': 'Chaos',
    'grade': 10,
    'complete modules': ['danger', 'robust liver', 'mummy issues']
    }
}

breakpoint() # to complete breakpoint type

print(students['student1'])
print(students['student1']['name'])
print(students['student2']['name'])