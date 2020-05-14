# Partially written by Greg Jewell...9-3-19
# Updated by Greg Jewell...1-17-2020

import random

"""
Function: test_word
Description: takes a word and a list of letters and sees whether the word can be 
made from the list of letters, e.g. "apple" can be made from ['p', 'a', 'p', 'e', 'l'] but not from ['p', 'l', 'e', 'a'] 
because in the latter case there is only one "p".

Parameters: word is a string containing the word to be checked, letters is a list 
of letters available to try making the word

Returns: boolean -- True if word can be made from letters, False otherwise
"""

def test_word(word, letters):
# make a deep copy of the list of letters, so I can overwrite parts of the copy
    letter_list = letters[:]
# loop through each letter in the word
    for letter in word:
        i = 0
# find first instance of that letter in the list of letters
        while i < len(letter_list):
# if letter is found, overwrite it with asterisk so it cannot be reused
            if letter_list[i] == letter:
                letter_list[i] = '*'
                break
            i += 1
# if letter wasn't found, not possible to make word from list of letters
        if i == len(letter_list):
            return False
# if successfully found all letters in word, return True
    return True
################################################################################
###                       Given Sample Code Above                            ###
################################################################################

# used to jumble the selected word; do not confuse with shuffle
def jumble(word):
    random_word = random.sample(word, len(word))

    jumbled = ''.join(random_word)
    return jumbled

# Run code here :)
def main():

    sixLetter = open("sixLetters.txt", "r")
    if sixLetter.mode == "r":
        sixLetterList = sixLetter.readlines()

    d = open("dictionary.txt", "r")
    if d.mode == "r":
        dictionary = d.readlines()

    sixLetter.close()
    d.close()

# Empty List to append obtainable words to
    l = []

# Remember to strip the word you select, and later words or strings WILL NOT MATCH
    selected = random.choice(sixLetterList)
    selected = selected.strip('\n')

# Loading message
    print("Generating Word Bank, please wait!\n")

# Iterate through dictionary.txt to find obtainable words
    for x in range(len(dictionary)):
        check = dictionary[x].strip('\n')
        if test_word(check, list(selected)):
            l.append(check)

# Output the information needed to play
    print("What words can you spell with the jumbled word: " + jumble(selected))
    print("There are currently ", len(l), " words from the list that can be made")
    print("Type 'qqq' to quit at any time!\n")

# Game loop
    correct_guess = [] #stores correct guesses
    while len(l) > 0:
        x = 0; x += 1
        correct = False; guessed = False
        answer = input("\nWhat word would you like to guess?")

        for y in range(len(correct_guess)):
            if answer == correct_guess[y]:
                print("\nYou have already guessed that word!")
                print(correct_guess)
                guessed = True

        for y in range(len(l)):
            if answer == l[y]:
                correct = True
                correct_guess.append(answer)
                l.remove(l[y])
                break
            elif answer != l[y]:
                correct = False

        if answer == "qqq":
            print("Quitting Is Not Winning!")
            break
        elif correct:
            print(answer.strip('\n') + " is one of the words!")
            print("There are currently ", len(l), " words from the list that can be made")
        else:
            if guessed:
                continue
            else:
                print(answer + " is not a choice")

# I guess they won, if they get here!
    if len(l) == 0:
        print("You Win!!!")


main()