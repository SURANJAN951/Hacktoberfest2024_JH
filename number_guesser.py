import random

def number_guesser():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        try:
            # Take input from the user
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function to run the game
if __name__ == "__main__":
    number_guesser()
