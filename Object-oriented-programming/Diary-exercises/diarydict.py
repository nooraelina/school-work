from datetime import date

class DiaryDict:
    def __init__(self, name=str(), *args, **kwargs) :
        '''
        Gets a name and sets it to be the value of attribute name. 
        If no name is given the default is 'Diary [month/year]' where year and 
        month are the current year and month e.g. Diary June/2019
        '''

        if len(name) <= 0:
            now = date.today()            
            self.__name = f'Diary {now.month}/{now.year}'
        else :
            self.__name = name
        self.observations = dict()

    @property
    def name(self):
        '''diary name'''
        return self.__name
        
    @property
    def observations(self):
        '''complete dictionary'''
        return self.__observations
    
    @observations.setter
    def observations(self, obs):
        '''
        sets the complete dictionary
        '''
        self.__observations = obs
        
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
        if target and day <= date.today() :
            observation = [target, day]
            if notes :
                note = str()
                for item in notes : 
                    note += item
                observation.append(note)
            self.observations[key] = observation
            
        return len(observation) #False = 0, True != 0

    def modify(self, key, target, day, *notes):
        ''' 
        retrieves key value pair from observations dictionary 
        and resets (modify(self, key, target, day, *notes)) 
        '''
        change = {key: f"{key, target, day, notes}"}
        self.observations.update(change)

    def remove(self, key):
        '''
        removes a key value pair from observations dictionary 
        and returns the removed value (remove(self, key) 
        '''
        if key in self.observations:
            del self.observations[key]
        return list(self.observations)
    
    def __str__(self) :
        '''
        returns the object as an formatted string
        '''
        result = '\n\n'+ self.name.capitalize() +'\n\n'
        for key in self.observations :
            result += str(key) + ': '
            for i in range(len(self.observations[key])) :
                if i < len(self.observations[key]) - 1 :
                    result += str(self.observations[key][i]) + ', '
                else :
                     result += str(self.observations[key][i]) + '\n'
        return result         
