import random
from time import sleep

def dices(x):
    sum = 0
    faces = []
    for dice in range(0,x):
        dice = random.randint(1, 6)
        faces.append(dice)
        sum += dice
    print(f'The faces of dice(s) are: ')
    str_faces = [str(a) for a in faces]
    print(", ".join(str_faces))
    return sum

def main():
    while True:
        how_many = input('How many dices you wish to roll?  \n')
        try:
            if how_many == '':
                how_many = 1
                print('You chose 1 dice to roll.')
            how_many = int(how_many)
        except ValueError:
            print('Please give a integer. Closing in 3 seconds.')
            sleep(3)
            return
        else:
            pass
        sum_of_faces = dices(how_many)
        print(f'The sum of dice(s) is {sum_of_faces}.')
        try_again = input('Press ENTER to try again. Press N to quit. ')
        if try_again.upper() == 'N':
            return
        else:
            pass

if __name__ == '__main__':
    main()