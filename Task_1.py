import random

def guess_number(min_val, max_val):
    target_number = random.randint(min_val, max_val)
    attempts = 0

    print(f"Guess the number between {min_val} and {max_val}!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    min_value = 1
    max_value = 100
    guess_number(min_value, max_value)
