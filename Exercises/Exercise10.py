# Story book!
# Create a dictionary with 3 stories inside! like a book :)
# each story should be it's own dictionary with:
    # beggining, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:
 # you already built a dictionary with a story
 # You already have something to prompt user for input & build dictionaries
 # Now what we want is to create a book that hold 3 stories

# extra:
 # stick it in a while loop so we continue to listen to stories :)
 # It would be nice to be able to read only one story


story_book = {
    'story1' : {
        'Hero': 'There were three little pigs.',
        'Start': 'The pigs lived in houses.',
        'Middle': 'A wolf tried to blow their brick house down.',
        'End': 'The wolf could not blow the pigs house down and died.'
    },
    'story2': {
        'Hero': 'There was a hero called Link.',
        'Start': 'Link lived in Hyrule.',
        'Middle': 'The princess of Hyrule, Zelda, was in danger.',
        'End': 'Link saved the princess and lived happily ever after.'
    },
    'story3': {
        'Hero': 'There was a boy called Ash.',
        'Start': 'Ash set out to be a pokemon master.',
        'Middle': 'To be a pokemon master, a trainer needed to win battles and win the league.',
        'End': 'Ash won the battles and the league and became a pokemon master.'
    }
}


for key in story_book:
    print(key)
    for key2 in story_book[key]:
        print(story_book[key][key2])
