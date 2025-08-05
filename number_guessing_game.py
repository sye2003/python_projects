import random
# Number Guessing Game
print("Welcome to the Number Guessing Game!")
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("guess a number between 1 and 100:"))
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Kindly enter a valid integer:")
