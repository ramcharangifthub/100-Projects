import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [rock,paper,scissors]
computer_number = random.randint(0,2)
computer_choice = game[computer_number]
print("Welcome to rock paper scissors game")
user_number = int(input("what do you choose?(0 for rock,1 for paper and 2 for scissors): "))
if user_number<=2 and user_number>=0:
    print("user choice:")
    print(game[user_number])
print("computer choice: ")
print(computer_choice)
if user_number > 2 or user_number < 0:
    print("you have entered a invalid choice")
elif user_number == 0 and computer_number == 2:
    print("You won, Computer lost")
elif computer_number == 0 and user_number == 2:
    print("You lost, Computer won")
elif computer_number>user_number:
    print("You lost, Computer won")
elif user_number>computer_number:
    print("You won , Computer lost")
elif user_number == computer_number:
    print("It's a tie") 