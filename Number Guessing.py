import random
from newart import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
win_number=random.randrange(1,101)
print(win_number)
def easy():
    attempts=10
    print(f"You have {attempts} attempts remaining to guess the number.")
    while True:
        guess=int(input("Make a Guess: "))
        if guess < win_number:
            print("Too Low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("Guess Again.")
        elif guess > win_number:
            print("Too High")
            print("Guess Again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess == win_number:
            print(f"You Got it Answer was {win_number}")
            print(f"Run Again for further Playing")
            break
        elif attempts == 0:
            print("You Lost the Game.")
            break

def hard():
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    while True:
        guess = int(input("Make a Guess: "))
        if guess < win_number:
            print("Too Low")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("Guess Again.")
        elif guess > win_number:
            print("Too High")
            print("Guess Again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess == win_number:
            print(f"You Got it Answer was {win_number}")
            print(f"Run Again for further Playing")
            break
        if attempts == 0:
            print("You Lost the Game.")
            print(f"The Number was {win_number}.")
            break
# Choose Difficulty
while True:
    choose_difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_difficulty == 'easy':
        easy()
        break
    elif choose_difficulty == 'hard':
        hard()
        break
    else:
        print("Get Out")
        break

