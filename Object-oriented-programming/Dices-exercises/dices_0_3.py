import tkinter as tk
import random

class Game():
    ''' The logic: calculations happens in here '''
    def __init__(self):
        self.__number = 2
        self.__pot = 100
        self.__bet = 1
        self.__faces = [0] * self.__number

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

    # ============= FUNCTIONS ===========================================
    
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
                self.bet = 0
            else :
                text += f'lost {self.bet} x 2!'
                self.pot -= self.bet * 2
            text += f'\nYour pot is now {self.pot}'
            return text


class Dices(tk.Tk):
    ''' GUI and the reading of values happens in here '''
    def __init__(self, number = 1, pot = 100, bet = 1, *args, **kwargs ) :
        '''
        calls TK initializer
        Takes users bet
        '''
        super().__init__(*args, **kwargs)   #call Tk class initializer

        self.game1 = Game()

        # =============================================================================
        #   GUI
        # =============================================================================
        self.title('Double-or-nothing')
        self.geometry('360x160')
        self.resizable(width = False, height = False)
 
        self.__v_bet = tk.IntVar()
        self.__v_bet.set(1)
        self.__v_roll = tk.StringVar(value='Roll the dices')
        self.__result = tk.StringVar()
        self.__result.set(f'The pot starts from {self.game1.pot}')
         
        self.columnconfigure(0, weight = 1)
        self.__l_bet = tk.Label( self, text = 'Place your bet', justify = tk.CENTER)
        self.__l_bet.grid(sticky = tk.E + tk.W + tk.N + tk.S)
        self.__s_bet = tk.Spinbox( self, from_=1, to = self.game1.pot, increment = 1, 
                                   textvariable = self.__v_bet, justify = tk.CENTER)
        self.__s_bet.grid(sticky = tk.N + tk.S)
 
        self.b = tk.Button(self, textvariable = self.__v_roll, command=self.__rollandcheck)
        self.b.grid(sticky = tk.N + tk.S)
        tk.Label( self, textvariable=self.__result, justify = tk.CENTER ).grid(sticky = tk.E + tk.W + tk.N + tk.S)

        # ==============================================================================

    def __rollandcheck(self):
        '''called when button is pressed, calls roll and then check and shows result'''
        self.game1.bet = self.__v_bet.get()
        self.game1.roll()
        p = self.game1.check()
        self.__result.set(p)
        if self.game1.pot <= 0 : 
            self.title('GAME OVER - pot is gone!')
            self.__l_bet.grid_forget()
            self.__s_bet.grid_forget()
            self.b.grid_forget()

# =================== MAIN LOOP =======================
if __name__ == '__main__' :
    Dices().mainloop()