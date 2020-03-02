# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:48:28 2019

@author: noora
"""

# Tehtävä 1
f = open('somefile.txt')
for line in f:
    for word in line.split():
        print(word)

# Tehtävä 2


# Tehtävä 3
import random
import ast

def dashToChar(li, w, c):
    """Changes the character list li, if character c is in w"""
    for i in range(len(w)):
        if w[i] == c:
            li[i] = c
    return li

def hangmanGame(times):
    """Hangman game. times is the number of wrong guesses"""
    with open('animals.txt', 'r') as a:
        cats = ast.literal_eval(a.read())
    ranCat = random.choice(cats)
    dashed = len(ranCat) * ['-']
    while times:
        print('You have {0} guesses'.format(times))
        print(''.join(dashed))
        guessed = input('What character? ')
        if guessed not in ranCat:
            times -= 1
            continue
        dashed = dashToChar(dashed, ranCat, guessed)
        if '-' not in dashed:
            return ''.join(dashed)
    return 'Sorry, you are hanging'

print(hangmanGame(2))

# animals.txt sisältää seuraavan:
# ['lion', 'tiger', 'puma', 'cheetah', 'leopard', 'lynx']

# Tehtävä 4
import random as ra

print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if ra.randrange(0, 2) == 1:
        heads = heads + 1
    flips = flips + 1
    if flips % 100 == 0:
        print('+100 flips, press enter to keep going')
        input()
    if flips == 900:
        print('900 flips and there have been ' + str(heads) + ' heads.')
    if flips == 100:
        print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
    if flips == 500:
        print('Half way done, and heads has come up ' + str(heads) + ' times.')

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
print('Were you close?')
 
# Tehtävä 5
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def morse(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher
def main():
    message = "Programming"
    output = morse(message.upper())
    print(output)
    
main()