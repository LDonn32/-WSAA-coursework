# Assignment 2: Card Draw
# Author: Laura Donnelly

# https://deckofcardsapi.com/api/deck/new/draw/?count=2


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



