import random

# Define the game logic
def play_game(uc, rc):
    if uc == rc:
        print(f"Put in a number between 1-3 {uc}. Your wrong!")
    elif (uc == "1" and rc == "2") or \
         (uc == "3" and rc == "1") or \
         (uc == "1" and rc == "3"):
        print(f"You chose {uc} and the computer chose {rc}. Your wrong!")
    else:
        print(f"You chose {uc} and the computer chose {rc}. You win!")

# Main game loop
def game():
    print("Welcome Calculator game!")
    
    while True:
        user_choice = input("Enter your choice (1, 2, 3): ").lower()
        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice! Please try again.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(["1", "2", "3"])

        # Play the round
        play_game(user_choice, computer_choice)

        # Ask to continue or exit
        option = input("Do you want to play again? (yes/no): ").lower()
        if option != "yes":
            print("Thank you for playing!")
            break

# Start the game
if __name__ == "__main__":
    game()