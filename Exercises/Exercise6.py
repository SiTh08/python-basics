# 2nd Assignment for post class

# define an empty dictionary # name_dict = {}
# Prompt user for input for a story.
# It should have:
        # hero, beginning, middle, ending
        # 2 other things you define to be part of the story.
        # add each response to the dictonary under an appropriate key

start_dict = input('Please start your story')
hero_dict = input('What is the name of your hero in the story?')
setting_dict = input('Where is the hero from?')
plot_dict = input('What is the plot of the story?')
middle_dict = input('What happens as the story progresses?')
end_dict = input('How does the story end?')

story = {
    'Start': start_dict,
    'Hero': hero_dict,
    'Setting': setting_dict,
    'Plot': plot_dict,
    'Middle': middle_dict,
    'End': end_dict
}

# Print out the dictionary information in a ordered way so we can read the story.

print(f'{start_dict.strip()} {hero_dict.strip()} {setting_dict.strip()} {plot_dict.strip()} {middle_dict.strip()} {end_dict.strip()}')

# Please start your story Once upon a time, there was a kingdom called Hyrule.
# What is the name of your hero in the story? There was a hero called Link.
# Where is the hero from? Link was from Hyrule.
# What is the plot of the story? Link needs to save Zelda.
# What happens as the story progresses? Link faces many puzzles and challenges along the way.
# How does the story end? Link succeeds in saving Zelda and saving Hyrule.


