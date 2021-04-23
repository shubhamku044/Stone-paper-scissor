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
user = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp = random.randint(0, 2)

names = ["Rock", "Paper", "Scissor"]

comp_option = names[comp]
user_option = names[user]



if comp_option == user_option:
    print("game draw\n")
    print(f"You both Choosen {comp_option}\n")
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    elif user == 2:
        print(scissors)

elif user_option == "Rock" and comp_option == "Paper":
    print(f"Computer win's the game.\nComputer choosen Paper\n{paper}\nYou choosen Rock\n{rock}")
elif comp_option == "Rock" and user_option == "Paper":
    print(f"You win's the game.\nYou choosen Paper\n{paper}\nComputer choosen Rock\n{rock}")


elif user_option == "Scissor" and comp_option == "Rock":
    print(f"Computer win's the game.\nComputer choosen Rock\n{rock}\nYou choosen Scissor\n{scissors}")
elif comp_option == "Scissor" and user_option == "Rock":
    print(f"You win's the game.\nYou choosen Rock\n{rock}\nComputer choosen Scissor\n{scissors}")



elif user_option == "Paper" and comp_option == "Scissor":
    print(f"Computer win's the game.\nComputer choosen Scissor\n{scissors}\nYou choosen Paper\n{paper}")
elif comp_option == "Paper" and user_option == "Scissor":
    print(f"You win's the game.\nYou choosen Scissor\n{scissors}\nComputer choosen Paper\n{paper}")