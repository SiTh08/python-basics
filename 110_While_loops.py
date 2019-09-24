import time
# While loop!
# Keeps looping and iterating until a condition is met
# or it comes into a break statement.

#Syntax
# While <condition>:
    # Block
    # if <condition>:
        # Break

# counter = 0
# while True:
#     print(counter)
#     print('-PEWWWDIPPPPYYYYY')
#     counter += 1
#     time.sleep(3)

# counter = 0
# while counter < 10:
#     print(counter)
#     print('-PEWWWDIPPPPYYYYY')
#     counter += 1
#     time.sleep(2)

# counter = 0
# while True:
#     print('WAAAAHHHHH')
#     print(counter)
#     if counter > 10:
#         break
#     counter += 1

# while True:
#     print('What up Jigglepuff?')
#     user_input = input().strip().lower()
#     if user_input == 'exit':
#         break
#     elif user_input == 'cute':
#         print('Ahhh Jigglepuff ... <3')
#     else:
#         print('JIGGLIPUFFFF!!!!!')

# user_input2 = ''
# while user_input2 != 'exit':
#     print('What up?')
#     user_input2 = input('new input?')
#     if user_input2 == 'cute':
#         print('ahh Jiggli <3')
#     elif user_input2 == 'cool':
#         print('You must be friends with Snorlax')
#     else:
#         print('Go to the Gym!')

car1 = ['car', 'volvo', 'skoda', 'ferrari', 'Lambo']

# counter = 0
# max_length = len(car1)
# while counter < max_length:
#     print(car1[counter])
#     counter += 1

counter = 0
max_length = len(car1)
while counter < max_length:
    print(counter + 1, '--', car1[counter].capitalize())
    counter += 1


