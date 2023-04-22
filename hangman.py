# This is hangman, although without the actual picture of the man hanging. 
# As with the pictorial version, in this game you will also lose after 6 wrong guesses.

# The computer will select a word at random from a list, and then present to you the
# number of letters contained in that word. If you guess a letter correctly, the computer
# will fill out the slots where that letter goes and then present it to you for your benefit.

import random

with open('2hangman_words.txt','r') as words_file:
    wordlist = words_file.read().split()

random_word = random.choice(wordlist)

#x = len(random_word)

underscores = []

for letter in random_word:
    underscores.append('_')

joined_underscores = (' '.join(underscores))

print("Here is the representation of your word...")
print()

print(joined_underscores)
print()

i=0

while True:
    
    if i==6:
        print(f"Sorry, that's all 6 of your strikes! You have lost the game, your word was {random_word}. Please try again.\n")
        break

    elif '_' not in underscores:
        print(f"Congratulations, you have won the game! Your word is {random_word}!\n")
        break

    print("Please enter your guess now, it should be a single letter...")
    guess = input()
    print()
    
    if guess in random_word:
        indexes = []
        for n in range(len(random_word)):
            if random_word[n] == guess:
                indexes.append(n)
        for index in indexes:
            underscores[index] = guess            
#        guess_index = random_word.index(guess)
#        underscores[guess_index] = guess
        string_underscores = (' '.join(underscores))
        print(f"Good guess! Here is the updated representation of your word:\n{string_underscores}\n")

    elif guess not in random_word:
        i+=1
        string_underscores = (' '.join(underscores))
        print(f"Sorry, that is incorrect! That is strike {i} of 6.\n")
        print(f"Here is what you have so far:\n{string_underscores}\n")

# 4/22/23 -- almost done here, just need to debug. The only bug still left that I can see is that guessing a letter correctly
# does not fill in ALL instances of the word in the underscores, only the FIRST one. Not sure how to fix this yet...
