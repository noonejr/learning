import random

def check_guess_number(guessed_number, user_guess):
    if guessed_number == user_guess:
        print("Correct!")
        return True
    elif guessed_number < user_guess:
        print("Nope, it's lower")
        return False
    else:
        print("Nope, it's higher")
        return False

def run_game():
    max_chances = 3
    chance_took = 0
    guessed_number = random.randint(1,20)
    user_guess_correct = False

    while chance_took < max_chances and (user_guess_correct == False):
        user_guess = int(input("Please guess: "))
        user_guess_correct = check_guess_number(guessed_number, user_guess)
        chance_took = chance_took + 1

    if not user_guess_correct:
        print(f"The number was {guessed_number}")

run_game()