##########################
# This script defines a list of popular nursery rhyme phrases and uses the random module to select a random number of 
# phrases from the list and join them together to create the lyrics. 
# The generate_lyrics() function returns the generated lyrics which can be printed or used in any other way you wish.
##########################

import random

# List of popular nursery rhyme phrases
phrases = [
    "Mary had a little lamb",
    "Humpty Dumpty sat on a wall",
    "Jack and Jill went up the hill",
    "Rain, rain, go away",
    "Twinkle, twinkle, little star",
    "Itsy bitsy spider climbed up the water spout",
    "Rock-a-bye baby on the treetop",
    "Mary, Mary, quite contrary",
    "Jack be nimble, Jack be quick",
    "Hickory, dickory, dock"
]

# Generate random nursery rhyme lyrics
def generate_lyrics():
    # Select a random number of phrases to use
    num_phrases = random.randint(2, len(phrases))
    
    # Select random phrases from the list
    selected_phrases = random.sample(phrases, num_phrases)
    
    # Join the selected phrases to create the lyrics
    lyrics = " ".join(selected_phrases)
    
    return lyrics

# Generate and print the lyrics
lyrics = generate_lyrics()

print(lyrics)




