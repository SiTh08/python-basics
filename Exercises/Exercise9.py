## Stupid School Teacher
#Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you respond to your school teacher:
    # Go back to school!
# if you ask a questions
    # HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
    # YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
    # WELLL DONE! YOU can now talk to me
    # Exits

response = input('Hello, I am your teacher. You can ask me anything.').strip()

while response != exit:
    if '?' in response:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif '!' in response:
        print('YES! YES! I WANT YOU TO BE MOTIVATED!! YES!')
    elif response == 'I am a doctor':
        print('WELL DONE! YOU can now talk to me.')
        break
    else:
        print('Go back to school')
    response = input('Hello, I am your teacher. You can ask me anything.').strip()


