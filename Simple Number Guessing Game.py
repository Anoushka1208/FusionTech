import random

def number_guessing_game():
    low, high = 1, 100
    target_number = random.randint(low, high)
    attempts = 0

    print(f"Guess the number between {low} and {high}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
