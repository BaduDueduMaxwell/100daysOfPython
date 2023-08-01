#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(chosen_word)


lives = 6

display = ["_" for _ in chosen_word]

while lives > 0 and "_" in display:
    user_guess = input("Guess the word: ").lower()
    found = False

    for i, letter in enumerate(chosen_word):
        if letter == user_guess:
            display[i] = user_guess
            found = True

    if found:
        print("You won!")

    if not found:
        lives -= 1

    print(stages[lives])
    print(" ".join(display))

if "_" not in display:
    print("You won!")
else:
    print('You lost!')

