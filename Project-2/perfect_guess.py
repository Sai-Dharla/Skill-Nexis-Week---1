import random

def main():
    print("===== Welcome to The Perfect Guess! =====")
    print("I have generated a random number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")
    # Generate a random number between 1 and 100
    actual_number = random.randint(1, 100)
    guesses = 0
    while True:
        try:
            # Take input from the user
            user_guess = int(input("Enter your guess: "))
            guesses += 1
            if user_guess > actual_number:
                print("Lower number please")
            elif user_guess < actual_number:
                print("Higher number please")
            else:
                # The user guessed correctly
                print(f"Congratulations! You guessed the correct number {actual_number}.")
                print(f"You took {guesses} guesses to arrive at the number.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer number.")
if __name__ == "__main__":
    main()