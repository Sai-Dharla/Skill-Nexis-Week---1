import random

def get_computer_choice():
    """Randomly selects Snake, Water, or Gun for the computer."""
    choices = ['s', 'w', 'g']
    return random.choice(choices)
def determine_winner(player, computer):
    """
    Determines the winner based on the rules:
    - Snake (s) drinks Water (w) -> Snake wins
    - Water (w) ruins Gun (g) -> Water wins
    - Gun (g) shoots Snake (s) -> Gun wins
    """
    if player == computer:
        return "Tie"
    if player == 's':
        if computer == 'w':
            return "Player"
        else: # computer == 'g'
            return "Computer"
    elif player == 'w':
        if computer == 'g':
            return "Player"
        else: # computer == 's'
            return "Computer"
    elif player == 'g':
        if computer == 's':
            return "Player"
        else: # computer == 'w'
            return "Computer"
def main():
    print("===== Welcome to Snake, Water, Gun Game =====")
    print("Options:")
    print(" 's' for Snake")
    print(" 'w' for Water")
    print(" 'g' for Gun")
    # Dictionary mapping for full names when printing
    names = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    while True:
        player_choice = input("\nEnter your choice (s/w/g) or 'q' to quit: ").lower()
        if player_choice == 'q':
            print("Thanks for playing! Goodbye.")
            break
        if player_choice not in ['s', 'w', 'g']:
            print("Invalid input! Please choose 's', 'w', or 'g'.")
            continue
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {names[player_choice]}")
        print(f"Computer chose: {names[computer_choice]}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "Tie":
            print("Result: It's a Tie!")
        elif winner == "Player":
            print("Result: You Win!")
        else:
            print("Result: Computer Wins!")
if __name__ == "__main__":
    main()

