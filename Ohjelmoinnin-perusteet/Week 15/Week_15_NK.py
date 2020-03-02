# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:25:45 2019

@author: noora

"""
import random

class Card:
    suite = ['♣','♦','♥','♠']    # 1. attribuutti
    value = ['2','3','4','5','6','7','8','9',
             '10','J','Q','K','A']    # 2. attribuutti

class Deck(Card):
    card = []
    def __init__(self):
        for i in self.suite:
            for j in self.value:
                self.card.append(i + j)
    def show_all(self):
        print(self.card)
            

def main():
    card1 = random.choice(Card.suite) + random.choice(Card.value)
    print('{} is first card.'.format(card1))
    card2 = random.choice(Card.suite) + random.choice(Card.value)
    print('{} is second card.'.format(card2))
    deck1 = Deck()
    deck1.show_all()
    print('Random card: ', random.choice(deck1.card))    # Tehtävä 3
    random.shuffle(deck1.card)          # Tehtävä 4
    deck1.show_all()
    deal1 = deck1.card[0:12]
    deal2 = deck1.card[13:25]
    deal3 = deck1.card[26:39]
    deal4 = deck1.card[40:52]
    print('''Player 1 cards: {0}. \n
Player 2 cards: {1}. \n
Player 3 cards: {2}. \n
Player 4 cards: {3}. '''
          .format(deal1,deal2,deal3,deal4))
    
main()
