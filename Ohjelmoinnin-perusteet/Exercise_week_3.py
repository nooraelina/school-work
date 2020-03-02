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
