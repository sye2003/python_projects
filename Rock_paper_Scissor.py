import random

print("Welcome to Rock, Paper, Scissors!")

ROCK ='r'
PAPER ='p'
SCISSORS ='s'
emojis={ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
choices=tuple(emojis.keys())


def get_user_choice():
    while True:
        user=input("Enter your choice (r/p/s): ").lower()

        if user  in choices:
            return  user
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")


def display_choices(user, computer_choice):
   
    print(f"You chose: {emojis[user]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def winner(user, computer_choice):
        if user == computer_choice:
            print("Tie!")
        elif( (user == ROCK and computer_choice == SCISSORS) or
            (user == PAPER and computer_choice == ROCK) or
            (user == SCISSORS and computer_choice == PAPER)):
            print("You win!")
        else:
            print("Computer wins!")
def play_game():
    while True:

        user = get_user_choice()
        computer_choice=random.choice(choices)

        display_choices(user, computer_choice)

        winner(user, computer_choice)
            
    
        print("Play again? (y/n)")
        play_again = input().lower()
        if play_again != "y":
            break


play_game()