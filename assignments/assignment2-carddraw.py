# Assignment 2: Card Draw
# Author: Laura Donnelly

# https://deckofcardsapi.com/api/deck/new/draw/?count=2

'''
import requests

# shufftle the deck and draw 5 cards

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
data = response.json()
deck_id = data['deck_id']
response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
data = response.json()
for card in data['cards']:
    print(f"{card['value']} of {card['suit']}")
# Example output of 5 cards:
# 3 of DIAMONDS
# KING of CLUBS
# 10 of HEARTS
# ACE of SPADES
# 7 of CLUBS
'''

# base 
'''
response = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
data = response.json()
for card in data['cards']:
    print(f"{card['value']} of {card['suit']}")

# Example output of 2 cards:
# 7 of HEARTS
# ACE of SPADES
'''



# look next  at congratulating user if they pull a pair, triple, straight or all same suit.

import requests

# Shuffle the deck
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
data = response.json()
deck_id = data['deck_id']

# draw 5 cards
response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
data = response.json()

cards = data['cards']

# Print the cards
print("Your hand:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")



# Convert face cards to numbers for straight checking
value_map = {
    "ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11,
    "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
    "5": 5, "4": 4, "3": 3, "2": 2
}

values = [value_map[c['value']] for c in cards]
suits = [c['suit'] for c in cards]

# Count occurrences
from collections import Counter
value_counts = Counter(values)
suit_counts = Counter(suits)

# Check for pair and triple
has_pair = any(count == 2 for count in value_counts.values())
has_triple = any(count == 3 for count in value_counts.values())

# Check for straight
sorted_vals = sorted(values)
is_straight = all(sorted_vals[i] + 1 == sorted_vals[i+1] for i in range(4))

# Check for flush
is_flush = any(count == 5 for count in suit_counts.values())

# Congratulatory Messages for user
print("\n--- Results ---")

if has_triple:
    print(" Congratulations! You got a THREE-OF-A-KIND!")
elif has_pair:
    print(" Nice! You pulled a PAIR!")
if is_straight:
    print("Wow! You got a STRAIGHT!")
if is_flush:
    print(" Incredible! You got a FLUSH — all cards are the same suit!")

# If nothing pulled
if not (has_pair or has_triple or is_straight or is_flush):
    print("Hard Luck! No special hand this time — try again!")


