# -*- coding: utf-8 -*-
''' 
ex.1.
'''
import ex_2 

def hello(txt, extension = '!', *notes):
    '''function'''
    print(txt, extension)
    for item in range(len(notes)):        
        print(str(item)) #the length of notes as string
        print(str(notes[item])) #all items separately
        print(str(notes)) #complete notes as one item

def main():
    ''' STARTING FUNCTION - but yet a regular function'''
    print('hello', ' world', sep=',,,,, ')
    print('hello again')
    
    #using hello with different amount of argments
    hello('hello')
    hello('again', ' END ')
    hello('my my', ' !! ', 'these are my notes')
    
    #using hello in another file (imported module ex_2)
    hello(ex_2.hello('try me!'))

if __name__ == '__main__':
    """common pattern to start"""
    main()
