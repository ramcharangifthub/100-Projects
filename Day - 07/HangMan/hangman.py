import random

from hangmanart import logo,stages
from hangmanwords import word_list

print("Welcome to Hangman Project")

print(logo)
lives = 6

choosen_word = random.choice(word_list)
guess_word = ""
for letter in choosen_word:
    guess_word += "_"
print(f"word to guess : {guess_word}")
game_over = False
correct_letters = []
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")      
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print(f"you have already guessed {guess}")
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in display:
        lives -= 1
        print(f"you guessed {guess} that's not in the word. You lose a life.") 
        if lives == 0:
            game_over == True
            print(f"***********************It was chosen word {choosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("You win")
    
    print(stages[lives])