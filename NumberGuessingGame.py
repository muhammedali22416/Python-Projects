import random

def number_guessing():
    number = random.randint(1,20)
    tries = 0
    guess = 0 

    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 20.")

    while guess != number:
        guess = int(input("Enter Your Guess: "))
        tries += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
             print(f"Congratulations! You guessed the number {number} in {tries} tries.")
             
number_guessing()