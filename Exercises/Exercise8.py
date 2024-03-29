# The game POP and TOC!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiple of 3 and 5 are POPTOC

# As a user, I should be asked for a number,
# so that I can play the game with my input.

# As a player, I should see the game counting up to my number and
 # substituting the multiples of 3 and 5 with the appropriate values,
 # so that I can see if it is working.

# As a player, I should be able to exit the game using a key word,
 # so that I can stop playing.

play_game = input('Would you like to PICTOC?').strip()
while True:
    if play_game == 'yes':
        number = int(input('What is your number?').strip())
        counter = 0
        while counter < number:
            counter += 1
            if (counter%3 == 0) and (counter%5 == 0):
                print('POPTOC')
            elif counter%5 == 0:
                print('TOC')
            elif counter%3 == 0:
                print('POP')
            else:
                print(counter)
        else:
            play_again = input('Would you like to play again?').strip()
            if play_again == 'yes':
                play_game
            elif play_again == 'no':
                break
            else:
                print('Please answer with yes or no.')
                play_again
    elif play_game == 'no':
        break
    else:
        print('Please answer with yes or no.')
        play_game = input('Would you like to PICTOC?').strip()
