import random 
from art import logo
print(logo)
print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100.")


lives_easy = 10
lives_hard = 5

def guess_number():
    target_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        lives = lives_easy
        print(f"You have {lives} attempts remaining to guess the number.")
        while lives > 0:
            guess = int(input("Make a guess: "))
            if guess > target_number:
                lives -= 1
                print(f"You have {lives} attempts remaining to guess the number.")
                print("Too high.")
                print("Guess again.")

            elif guess < target_number:
                lives -= 1
                print(f"You have {lives} attempts remaining to guess the number.")
                print("Too low")
                print("Guess again.")

            elif guess == target_number:
                print('You guessed right!!!')
                break
            
            if lives == 0:
                print("You lose!!!")
                break
    elif difficulty == 'hard':
        lives = lives_hard 
        print(f"You have {lives} attempts remaining to guess the number.")
        while lives > 0:
            guess = int(input("Make a guess: "))
            if guess > target_number:
                lives -= 1
                print(f"You have {lives } attempts remaining to guess the number.")
                print("Too high.")
                print("Guess again.")

            elif guess < target_number:
                lives -= 1
                print(f"You have {lives } attempts remaining to guess the number.")
                print("Too low")
                print("Guess again.")

            elif guess == target_number:
                print('You guessed right!!!')
                break
            
            if lives == 0:
                print("You lose!!!")
                break

    else:
        print("Input valid difficulty level.")

guess_number()