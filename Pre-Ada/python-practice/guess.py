import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)


def get_guess():
    user_guess = input("Guess the number (it is between 0 and 100): ")
    while not is_valid_guess(user_guess):
        if not user_guess.isnumeric():
            user_guess = input(
                "Oops! Please input a number using numeric characters: ")
        else:
            print("Aww your guess is out of bounds!")
            user_guess = input(
                f"It must be a number between {RANGE_LOW} and {RANGE_HIGH}!. Try again: ")
    return int(user_guess)


def is_valid_guess(user_guess):
    if not user_guess.isnumeric() or \
    (int(user_guess) < 0 or int(user_guess) > 100):
        return False
    else:
        return True


def run_guess_game():
    user_guess = get_guess()
    while True:
        if user_guess == random_number:
            print("You guessed the number! Good job!")
            break
        elif user_guess > random_number:
            print("Your guess is too high.")
            user_guess = get_guess()
        else:
            print("Your guess is too low.")
            user_guess = get_guess()


if __name__ == "__main__":
    run_guess_game()
