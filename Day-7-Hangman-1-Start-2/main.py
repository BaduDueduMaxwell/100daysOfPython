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

    if not found:
        lives -= 1

    print(stages[lives])
    print(" ".join(display))

# check if it has empty spaces
if "_" not in display:
    print("Congratulations! You won!")
else:
    print('You lose!')


