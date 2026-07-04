"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""
import random

def get_words():
    with open("words.txt", "r") as file:
        return file.readlines()

def get_random_word():
    words = get_words()
    return random.choice(words).strip()

def get_word_to_display(word, guessed_letters):
    display_word_list = [letter if letter in guessed_letters else '_' for letter in word]
    return (" ".join(display_word_list)).strip()

def is_game_won(random_word, guessed_letters):
    for letter in random_word:
        if letter not in guessed_letters:
            return False
    return True


def word_game():
    guess_left = 6
    random_word = get_random_word()
    print(random_word)
    guessed_letters = []

    while guess_left > 0:
        display_word = get_word_to_display(random_word, guessed_letters)
        print(display_word)
        print(f"{guess_left} wrong guesses left.")

        user_letter_guess = input("Guess a letter: ")
        guessed_letters.append(user_letter_guess)
        if user_letter_guess in random_word:
            print("Correct!")

            won = is_game_won(random_word, guessed_letters)
            if won:
                print("You won!🎉👍")
                break
        else:
            print("Nope :(")
            guess_left -= 1

        if guess_left == 0:
            print("Sorry you lost!😢")
            print(f"The word was {random_word}")

word_game()