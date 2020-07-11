import os
import random

os.system("clear")
# Guess a random number between 0 and 20.
# You only have 3 chances and the number changes everytime the game is run
# If you guess it right, you get guess prize money
# It will reveal the secret number in the end if you fail
# Have FUN!!

secret_number = random.randint(0, 20)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter guess: "))
    guess_count += 1
    if guess == secret_number:
        guess_prize = guess * secret_number * 10
        print(f"The secret number was indeed {secret_number}!")
        print("You have won $%0.2f!!!" % (guess_prize))
        break
    else:
        if guess_count == 3:
            print(f"The secret number was actually {secret_number}")
            print("Sorry you lost!")
        else:
            print("Sorry, try again champ!")
