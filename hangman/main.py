import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # choosing random word from the list of words
    # keep choosinf a random word if the word conatins a space or a hypen
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"Lives left {lives} \tLetters used: {' '.join(used_letters)}")

        # what current word is
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter not in word")

        elif user_letter in used_letters:
            print("Letter already used")

        else:
            print("Invalid character")
    if lives == 0:
        print(f"You died. The word was {word}")
    else:
        print(f"You guessed crrectly: {word}")


hangman()

# TO DO
"""
1. make the game run continuously until the player enters exit
2. Let the user enter their name and play for x attempts and 
3. Initialize and store scores of the words the user guessed correctly
4. Show results when a user wants to see what other players scored
5. Initialize a high score which showing the person with the highest score of words gussed correctly 
"""
