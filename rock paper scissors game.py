import random

def get_system_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def predict_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    
    while True:
        # User input
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Computer selection
        computer_choice = get_system_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = predict_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display scores
        print(f"Scores -> You: {user_score} | Computer: {computer_score}")
        
        # Play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# Run the game
rock_paper_scissors_game()
