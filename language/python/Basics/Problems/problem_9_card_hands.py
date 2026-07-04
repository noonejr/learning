"""
Deal a hand of 5 cards
"""
import random

suits = ['♠️','♣️','♥️','♦️']
values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

cards = []

for suit in suits:
    for val in values:
        cards.append(f'{suit}{val}')

hand = []

hand_left = 5
while hand_left > 0:
    hand.append(cards.pop(random.randint(0, len(cards))))
    hand_left -= 1

print(hand)