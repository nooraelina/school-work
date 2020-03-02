from datetime import date

class Diary :
    '''
    Diary class keeps track of observations
    '''
    def __init__(self, name=str()) :
        '''
        Gets a name and sets it to be the value of attribute name. 
        If no name is given the default is 'Diary [month/year]' where year and 
        month are the current year and month e.g. Diary June/2019
        '''
        self.__observations = dict()
        if name == str():
            today = date.today()
            self.__name = today.strftime('Diary %B/%Y')
        else:
            self.__name = name
    
    @property
    def name(self):
        print('name')
        return self.__name
    
    @name.setter
    def name(self, name):
        '''
        setting is not factually possible, but does not generate error
        '''
        try:
            self.__name = name
        except AttributeError:
            '''Notice that the class attribute can be accessed 
            as a class property and as an instance property, however, 
            accessing an instance attribute as a class property raises an AttributeError.'''
            pass
    
    @property
    def observations(self):
       return self.__observations

    
    @observations.setter
    def observations(self, obs):
        '''
        sets the complete dictionary
        '''
        self.__observations[obs]
    
    def obsSetter(self,obs):
        self.__observations.update(obs)
        
        
    def add(self, key, target, day = date.today(), *notes ) :
        '''
        parameters:
            * 'key' 
            * 'target' (actual observation e.g.king fisher, blue tit, Perseides)
            * default parameter 'day', that is the current date or a given date
            * an optional parameter '*notes'. 
        The function checks that 'target' is not an empty string and, if day is given, 
        the date is not after current date, adds the observation, date, and 
        possible notes to a list which is  added into dictionary observations with given key as key.
        If addition was successful, target and day were valid not None, True is retuned.  
        '''
        observation = []
        obs = dict()
        
        if target and day <= date.today():
            observation.append(day.strftime('%d - %b - %Y'))
            observation.append(target)
            if notes :
                note = str()
                for item in notes : 
                    note += item
                observation.append(note)
                obs[key] = observation
                self.obsSetter(obs)
        else:
            print('Invalid input.')
        
        return len(observation) #False = 0, True != 0

    
    def __str__(self) :
        '''
        returns the object as an formatted string
        '''
        result = f'Diary name: {self.__name} \n'
        
        for key,value in self.__observations.items():
            result += f'# {key} |'
            for a in value:
                result += f' {a}'
            result += '\n'
        
        return result
    

def main() :
    '''
    Creates a diary object.
    Main loop that reads user input, calls diary's method add, 
    and if the returned value is True 
    upates the loop counter, 
    prints the diary, and asks if user wants to add another value or 
    closes the program
    '''
    newName = input('Give a name of your diary. If no input, the name will be formatted as Diary MM/YYYY. \n')
    if newName == '':
        diary = Diary()
    else:
        diary = Diary(newName)
    counter = 0
    
    while True :
        try :
            newObs = input('Give the observation, then press ENTER.\n')
            newDate = input('Date as DD.MM.YYYY: \n')
            if newDate != '':
                d = newDate.split('.')
                newDate = date(int(d[2]), int(d[1]), int(d[0]))
            else:
                newDate = date.today()
            notes = input('Add notes ( additional ) \n')
            if diary.add(counter, newObs, newDate, notes) != 0:
                counter += 1
                print(diary)
            add_more = input('Add another observation? (Program closes if no) Y/N \n')
            if add_more.upper() == 'N':
                return
            else:
                pass
            
        except ValueError : print('check your input')


if __name__ == '__main__' :
    '''
    if the program is started from a script
    '''
    main()