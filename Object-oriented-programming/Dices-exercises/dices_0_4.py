''' 
Dices consists of reusable components that are used to build different games using one or several dices. 
Dices class encapsulates attributes commonly used in dice games (pot and bet) and 
functions roll and check. Checking is done according to the rules of each game. 

Dices ver0.4 adds a new functionality 'tenner' to Double-or-Nothing game.
If user selects to play 'tenner' the bet is multiplied with 10 prior checking the result of roll.
If 'tenner' is selected and the sum of the two dices is 10 user wins the already tenned bet tenfold.
    
    e.g.
    if user bet 1 and 'tenner' is selected the bet value in chcecking is 10.
    If the sum of dices is 10 user wins 1*10*10 = 100 which is then added to the pot.

User must be able to select and deselect the tenner option for each roll. 
It is a property linked with individual roll not to complete game.
'''

import random
import tkinter as tk

class Game:
    def __init__(self, number = 1, pot = 100, bet = 1) :       
        self.pot = pot 
        self.bet = bet
        self.number = number
        self.__faces = [0]*number    

    @property
    def pot(self):
        return self.__pot
    
    @pot.setter
    def pot(self, pot):
        '''
        forces pot to be >= 0
        '''
        self.__pot = pot
        if self.__pot < 0 : self.__pot = 0
    
    @property
    def bet(self):
        return self.__bet
    
    @bet.setter
    def bet(self, bet):
        '''
        sets bet if in [1, pot]
        '''
        if bet >= 1 and bet <= self.pot :
            self.__bet = bet
        else :
            raise ValueError(f'bet has to be 1..pot')
   
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        '''
        sets number of dices if bigger than 0
        '''
        if number > 0:
            self.__number = number
            self.__faces = [0]*number
    
    def roll(self) : 
        '''
        fills faces list with new random numbers [1,6]
        '''
        for i in range(self.number) :
            self.__faces[i] = random.randint(1, 6)

    def tenner(self):
        '''
        If user selects to play 'tenner' the bet is multiplied with 10 prior checking the result of roll.
        If 'tenner' is selected and the sum of the two dices is 10 user wins the already tenned bet tenfold.
        
        Checks if the sum is 10. 
        If it is the pot is updated and check method is not called.
        if the sum is not 10, check method is called and pot is updated.
        '''
        self.bet *= 10
        text = f'{self.__faces[0]} and {self.__faces[1]} - You '
        if self.number != 2 :
            raise ValueError('Wrong game, double-or-nothing is two dice game')
        else :
            if sum(self.__faces) == 10:
                self.pot += self.bet * 10
                text += f'won {self.bet} tenfold !'
                text += f'\nYour pot is now {self.pot}'
                return text
            else:
                text = self.check()
                return text
    
    def check(self):
        '''
        double-or-nothing - if the two dices faces are:
            * double 1 or 6 user wins the bet  ten fold (multiplied with 10)
            * double 2, 3, 4, or 5 user wins the bet doubled (multiplied with 2)
            * no double and sum equals 6 user loses the bet
            * any other combination (no double, sum not 6) and user loses the doubled bet  
        Winnings (updated bet) are added into pot and lost bet is subtracted from the pot. 
        '''
        text = f'{self.__faces[0]} and {self.__faces[1]} - You '
        if self.number != 2 :
            raise ValueError('Wrong game, double-or-nothing is two dice game')
        else :
            if self.__faces[0] == self.__faces[1] :
                if self.__faces[0] == 1 or self.__faces[0] == 6 :
                    text += f'won {self.bet} x 10!'
                    self.pot += self.bet * 10
                else :
                    text += f'won {self.bet} x 2!'
                    self.pot += self.bet * 2
            elif sum(self.__faces) == 6 :
                text += f'lost your bet!'
                self.bet = 0
            else :
                text += f'lost {self.bet} x 2!'
                self.pot -= self.bet * 2
            text += f'\nYour pot is now {self.pot}'
            return text
    
class Dices(tk.Tk) :
    '''
    encapsulates a dice game and provides user interface to call
    functions roll and check. Checking is done according to the rules of each game.
    '''
    def __init__(self, *args, **kwargs ) :
        '''
        calls TK initializer
        defines and initializes attributes 
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer
        self.__game = Game(2)
       
# =============================================================================
#       GUI elements and attributes         
# =============================================================================
        self.title('Double-or-nothing')
        self.geometry('360x160')
        self.resizable(width = False, height = False)
 
        self.__v_bet = tk.IntVar()
        self.__v_bet.set(1)
        self.__v_roll = tk.StringVar(value='Roll the dices')
        self.__result = tk.StringVar()
        self.__result.set(f'The pot starts from {self.__game.pot}')
         
        self.columnconfigure(0, weight = 1)
        self.__l_bet = tk.Label( self, text = 'Place your bet', justify = tk.CENTER)
        self.__l_bet.grid(sticky = tk.E + tk.W + tk.N + tk.S)
        self.__s_bet = tk.Spinbox( self, from_=1, to = self.__game.pot, increment = 1, 
                                   textvariable = self.__v_bet, justify = tk.CENTER)
        self.__s_bet.grid(sticky = tk.N + tk.S)

        # Checkbutton for tenner mode
        self.__v_checkbtn = tk.IntVar()
        tk.Checkbutton(self, text="Tenner mode on/off", variable=self.__v_checkbtn).grid(row=2, sticky=tk.E + tk.W) 

        self.b = tk.Button(self, textvariable = self.__v_roll, command=self.__rollandcheck)
        self.b.grid(sticky = tk.N + tk.S)

        tk.Label( self, textvariable=self.__result, justify = tk.CENTER ).grid(sticky = tk.E + tk.W + tk.N + tk.S)
# =============================================================================        

    def __rollandcheck(self):
        '''
        called when button is pressed, calls roll(), checks if the tenner mode is on,
        calls tenner() if it is, calls check() if not. Shows result last.
        '''
        self.__game.bet = self.__v_bet.get()
        self.__game.roll()
        
        if self.__v_checkbtn.get() == 1:
            a = self.__game.tenner()
            self.__result.set(a)

        else:
            p = self.__game.check()
            self.__result.set(p)

        if self.__game.pot <= 0 : 
            self.title('GAME OVER - pot is gone!')
            self.__l_bet.grid_forget()
            self.__s_bet.grid_forget()
            self.b.grid_forget()
            
if __name__ == '__main__' :
    Dices().mainloop()