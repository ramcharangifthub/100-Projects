from art import logo
import random
print("Welcome to the Number Guessing Game")

easy_level = 10
hard_level = 5

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer is {actual_answer}")

def difficulty():
    set_difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if set_difficulty == "easy":
        return easy_level
    else:
        return hard_level


def play(): 
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1,100)
    turns = difficulty()
    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(user_guess=guess,actual_answer=answer,turns=turns)
        if turns == 0:
            print("you ran out of guesses. You lost")
            return
        elif guess != answer:
            print("guess agian")

            


    
play()