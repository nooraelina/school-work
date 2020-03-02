import random as ra

class Dices:
    ''' Dices  ver0.1 (dices_0_1.py) is a double-or-nothing-dice-game where user 
    inputs bet that is between 1 - pot. 
    Pot is 100 in the beginning and after the roll user's bet is first checked, 
    win or lose is calculated and added to the pot. The result, pot, and faces 
    are displayed and if the pot is bigger than 0 the game continues and user 
    can enter new bet. 
    Winnings (updated bet) are added into pot and lost bet is subtracted from the pot. '''
    
    def __init__(self, bet = 1):
        self.__pot = 100
        self.__bet = bet

    @property
    def pot(self):
        return self.__pot
    
    @property
    def bet(self):
        return self.__bet

    def roll(self, bet):
        self.__bet = int(bet)
        sum = 0
        faces = []
        for dice in range(0,2):
            dice = ra.randint(1, 6)
            faces.append(dice)
            sum += dice
        print(f'The faces of dice(s) are: ')
        str_faces = [str(a) for a in faces]
        print(", ".join(str_faces))
        self.check(faces)

    
    def check(self, faces):
        ''' If the two dices faces are:
        - double 1 or 6 user wins the bet  ten fold (multiplied with 10)
        - double 2, 3, 4, or 5 user wins the bet doubled (multiplied with 2)
        - sum equals 6 user loses the bet
        - any other combination (no double, sum not 6) and user loses the doubles bet '''

        wins = self.__bet
        if faces == [1,1] or faces == [6,6]:
            wins *= 10
        elif faces == [2,2] or faces == [3,3] or faces == [4,4] or faces == [5,5]:
            wins *= 2
        elif faces[0] + faces[1] == 6:
            wins = 0
        else:
            wins = -(2*wins)
        print(f'Your wins/losses are {wins}')
        self.__pot += wins

    def __str__(self):
        return f'Your pot is now {self.__pot}. You betted with: {self.__bet}'

def main():
    ''' input -> create game object -> roll -> check the bet 
        -> calc win/lose -> add to the pot -> __str__: The result, pot, faces 
        -> if pot is bigger than bet, continue, enter new bet -> else return '''
    
    userBet = input('Give your bet (1-100) \n')
    if userBet == '':
        game = Dices()
        game.roll(1)
    elif 1 <= int(userBet) <= 100:
        userBetInt = int(userBet)
        game = Dices(userBetInt)
        game.roll(userBet)
    else:
        print('Try again \n')
    print(game)

    while True:
        userBet = input('Give your bet (1-100) \n')
        if userBet == '':
            game.roll(1)
            print(game)
        elif 1 <= int(userBet) <= 100:
            userBetInt = int(userBet)
            game.roll(userBet)
            print(game)
        else:
            print('Try again \n')
        if game.pot > game.bet:
            continue
        else:
            return

if __name__ == '__main__' :
    main()