class Lottery:
    def __init__(self, numbers, pool):

        self.lotto = set()
        if numbers < pool :
            self.__numbers = numbers
            self.__pool = pool
        else :
            self.__numbers = 7
            self.__pool = 37

    def generate(self):

        while len(self.lotto) < self.__numbers : 
            self.lotto.add(random.randint(self.__numbers, self.__pool)) 
        print(f'lotttery numbers are {self.lotto}')