import random

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
0
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get input from user and their choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
user_choice = int(user_choice)

computer_choice = random.randint(0, 2)

# assign art to list
game_choices = [rock, paper, scissors]

# print graphic of choices on screen
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"You chose - {game_choices[user_choice]}\nComputer chose - {game_choices[computer_choice]}")

# game logic

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        ("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw. Try again!")

print("\n")