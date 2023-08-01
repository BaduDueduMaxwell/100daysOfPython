rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# get computer to randomly select a number between 1 -3
# get user to select a num btw 1 -3
# if user == 1 or 2 or 3 and computer == 1 or 2 or 3; Draw
# if user == 1 and computer == 2; you lost ; vice versa for computer
# if user == 2 and computer == 3; you lost; vice versa for computer
# if user == 1 and computer == 3; you win; vice versa for computer

import random


user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. \n"))

computer_choice = random.randint(1,3)

if user_choice == computer_choice and computer_choice == user_choice:
    if user_choice == 1 and computer_choice == 1:
        print(rock)
        print(f"Computer chose: \n {rock}")
    elif user_choice == 2 and computer_choice == 2:
        print(paper)
        print(f"Computer chose: \n {paper}")
    elif user_choice == 3 and computer_choice == 3:
        print(scissors)
        print(f"Computer chose: {scissors}")
    print("Draw! Play again")
elif user_choice == 1 and computer_choice == 2:
    print(rock)
    print(f"Computer chose: \n {paper}")
    print("You lost!")
elif computer_choice == 1 and user_choice == 2:
    print(paper)
    print(f"Computer chose: \n {rock}")
    print("You won!")
elif user_choice == 2 and computer_choice == 3:
    print(paper)
    print(f"Computer chose: \n {scissors}")
    print("You lost!")
elif computer_choice == 2 and user_choice == 3:
    print(scissors)
    print(f'Computer chose: \n {paper}')
    print("You won!")
elif user_choice == 3 and computer_choice == 1:
    print(scissors)
    print(f'Computer chose: \n {rock}')
    print("You lost!")
elif computer_choice == 3 and user_choice == 1:
    print(rock)
    print(f'Computer chose: \n {scissors}')
    print('You won!')
elif user_choice > 3:
    print("Invalid choice. Run the program again")
    exit(0)
