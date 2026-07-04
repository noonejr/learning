"""
Guess the number between 1 and 10
"""

import  random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

if answer == guess:
    print("You guessed it correct.")
elif answer < guess:
    print("The number is lower.")
else:
    print("The number is higher")

print(f"The number was {answer}")