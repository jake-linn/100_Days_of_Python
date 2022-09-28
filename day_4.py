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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Pulling the game images
game_images = [rock, paper, scissors]

#defining user choice + image 
user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
print(game_images[user_choice])

#defining computer choice 
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

#defining game logic
if user_choice >= 3 or user_choice < 0:
  print("You choice an invalid response, you lose!")
elif user_choice == 0 and computer_choice ==2:
  print("You win!")
elif computer_choice == 0 and user_choice ==2:
  print("You lose.")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw.")
