# Write a method to shuffle a deck of cards
# It must be a perfect shuffle - in other words, each 52! permutations
# of the deck has to be equally likely
# Assume that you are given a random number generator which is perfect

import random

cards = []
for i in range(1,53):
    cards.append(i)

print('Before Shuffle:')
print(cards)

def shuffle_cards(cards):
    for position in cards:
        pick = random.randint(position,52)
        swap_index = cards.index(pick)
        current_index = cards.index(position)
        # swap the picked card with the first element so that same card doesn't get picked up again
        cards[current_index] , cards[swap_index] = cards[swap_index] , cards[current_index]
    return cards

shuffle_cards(cards)
print('After Shuffle:')
print(cards)
