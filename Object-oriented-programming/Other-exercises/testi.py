class Dices :

    '''
    encapsulates attributes commonly used in dice games (pot and bet) and 
    functions roll and check. Checking is done according to the rules of each game.
    '''
    def __init__(self, number = 1, pot = 100, bet = 1 ) :

        '''
        defines and initializes attributes 
        '''
        self.pot = pot
        self.bet = bet
        self.number = number
        self.__faces = [0]*number
    
    def __str__(self) :

        return f'pot is {self.pot}, the bet is set to {self.bet} and number of dices is {self.number}'


print(Dices(2, 200, 2))