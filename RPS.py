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

import random
game_list = [rock,paper,scissors]
user_chc = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors \n"))
if user_chc >= 3 or user_chc < 0:
  print("You've Typed Invalid Number,YOU LOSE!")
else:
  print(game_list[user_chc])
  
  comp_chc = random.randint(0,2)
  print("Computer CHOSE:")
  print(game_list[comp_chc])
  
  
  
  if user_chc == comp_chc:
      print("It's A DRAW!")
  elif user_chc == 0 and comp_chc == 2:
   print("You WON!")
  elif comp_chc == 0 and user_chc == 2:
    print("You LOSE!")
  elif user_chc > comp_chc:
    print("You WON!")
  elif comp_chc > user_chc:
      print("You LOSE!")
