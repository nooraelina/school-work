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
import celsfahr2 as cf

Cels_Fahr = {
        '20':68.0,
        '21':69.8,
        '22':71.6,
        '23':73.4,
        '24':75.2,
        '25':77.0,
        '26':78.8,
        '27':80.6,
        '28':82.4,
        '29':84.2
        }

f2 = open("newfile.txt","w+")
for key , value in Cels_Fahr.items():
    tiedot = "Celcius: {}  Fahrenheit: {} \n".format(key,value)
    f2.write(tiedot)
f2.close()

# Tehtävä 3
import hangman as hm
print(hm.hangmanGame(3))

# Tehtävä 4
import debugger2 as de
print(de)
 
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