import random

while True:
    choice=input("Enter y/n:").lower()
    if choice=='y':
        dice_roll=random.randint(1,6)
        print(f"{dice_roll}")
    elif choice=='n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n' to.")
    