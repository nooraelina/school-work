"""
Dices consists of reusable components that are used to build different games using one or several dices. 
Dices class encapsulates attributes commonly used in dice games (pot and bet) and 
functions roll and check. Checking is done according to the rules of each game. 

Dices  ver0.1 (dices_0_1.py) is a double-or-nothing-dice-game where user 
inputs bet that is between 1 - pot. Pot is 100 in the beginning and 
after the roll user's bet is first checked, win or lose is calculated 
and added to the pot. The result, pot, and faces are displayed and if the pot 
is bigger than 0 the game continues and user can enter new bet. 

The game ends when the pot is gone. User can not be in dept (pot is always bigger or equal to 0) 
and if user ends game before the pot is gone the pot is not saved 
to next game (casino can not be in dept).
"""
import random
import tkinter as tk

class Dices(tk.Tk):
    '''
    encapsulates attributes commonly used in dice games (pot and bet) and 
    functions roll and check. Checking is done according to the rules of each game.
    '''
    def __init__(self, number = 1, pot = 100, bet = 1, *args, **kwargs) :
        '''
        Calls TK
        defines and initializes attributes 
        '''
        super().__init__(*args, **kwargs)

        self.pot = pot
        self.bet = bet
        self.number = number
        self.__faces = [0]*number

# =============================================================================
#       GUI elements and attributes         
# =============================================================================

        self.title('Double-or-nothing')
        self.geometry('360x160')
        self.resizable(width = False, height = False)

        self.__v_bet = tk.IntVar()
        self.__v_bet.set(1)
        self.__v_roll = tk.StringVar(value = 'Roll the dices')
        self.__result = tk.StringVar()
        self.__result.set(f'The pot starts from {self.pot}')
        
        self.columnconfigure(0, weight = 1)
        self.__l_bet = tk.Label(self, text = 'Place your bet', justify = tk.CENTER)
        self.__l_bet.grid(sticky = tk.E + tk.W + tk.N + tk.S)
        self.__s_bet = tk.Spinbox(self, from_ = 1, to = self.pot, increment = 1,
                                    textvariable = self.__v_bet, justify = tk.CENTER)
        self.__s_bet.grid(sticky = tk.N + tk.S)

        self.b = tk.Button(self, textvariable = self.__v_roll, command = self.__rollandcheck)
        self.b.grid(sticky = tk.N + tk.S)
        tk.Label(self, textvariable = self.__result, justify = tk.CENTER).grid(sticky = tk.E 
                                                                                + tk.W + tk.N
                                                                                + tk.S)
        
# =============================================================================

    def __rollandcheck(self):
        ''' called when button is pressed, calls roll, checks and shows'''
        self.bet = self.__v_bet.get()
        self.roll()
        p = self.check()
        self.__result.set(p)
        if self.pot <= 0 :
            self.title('GAME OVER!')
            self.__l_bet.grid_forget()
            self.__s_bet.grid_forget()
            self.b.grid_forget()

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
            raise ValueError('bet has to be 1..pot')
   
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
                self.pot -= self.bet
            else :
                text += f'lost {self.bet} x 2!'
                self.pot -= self.bet * 2
            text += f'\nYour pot is now {self.pot}'
            return text
    
if __name__ == '__main__' :
    Dices(2).mainloop()