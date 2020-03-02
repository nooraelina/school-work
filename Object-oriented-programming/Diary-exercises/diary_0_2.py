"""diary_0_2.py simple (and clumsy) TKinter GUI added"""

from datetime import date
import tkinter as tk

class Diary(tk.Tk) :
    '''
    Diary class keeps track of observations, is also a TK GUI
    '''
    def __init__(self, name=str(), *args, **kwargs) :
        '''
        Gets a name and sets it to be the value of attribute name. 
        If no name is given the default is 'Diary [month/year]' where year and 
        month are the current year and month e.g. Diary June/2019
        Also adds the GUI elements 
        ver 0.2
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer

        if len(name) <= 0:
            now = date.today()            
            self.__name = f'Diary {now.month}/{now.year}'
        else :
            self.__name = name
        self.observations = dict()
# =============================================================================
#         Simple GUI elements (program window and title)
# =============================================================================
        self.title(self.__name)
        self.geometry('800x500')
        self.resizable(width = False, height = False)

# =============================================================================
#         labels, that do not change (unnamed), 
#         one line Entry fields that are used to read in values for 
#         target, date and notes (implementation specefic attributes), 
#         positioning widgets (labes and entries) using grid() geometry
# =============================================================================
        # Target
        self.__e_target = tk.StringVar()         
        tk.Label( self, text = 'target ').grid(row = 0, column = 0, sticky = tk.W)        
        e_1 = tk.Entry(self, textvariable = self.__e_target, bd = 5, width = 50)               
        e_1.grid(row = 0, column = 1, sticky = tk.W)
        # Date
        self.__e_day = tk.StringVar()         
        tk.Label( self, text = 'date [dd.mm.yyyy] ').grid(row = 1, column = 0, sticky = tk.W)        
        e_2 = tk.Entry(self, textvariable = self.__e_day, bd = 5, width = 20)               
        e_2.grid(row = 1, column = 1, sticky = tk.W)     
        # Notes
        self.__e_notes = tk.StringVar()
        tk.Label( self, text = 'notes ').grid(row = 2, column = 0, sticky = tk.W)        
        e_3 = tk.Entry(self, textvariable = self.__e_notes, bd = 5, width = 90)               
        e_3.grid(row = 2, column = 1, sticky = tk.W)   
# =============================================================================
#         Button 'add' pressing it will read entries, call readvalues and if
#         and call add method can process entries calls add method
# =============================================================================
        b = tk.Button(self, text = 'add', command=self.__readvalues)
        b.grid(row = 3, column = 1, sticky = tk.E + tk.W)
# =============================================================================
#         multiline label to display all observations 
# =============================================================================
        self.__result = tk.StringVar()
        tk.Label(self, textvariable=self.__result, justify = tk.LEFT ).grid(row = 4, column = 1, 
                                                                            sticky = tk.E + tk.W)

    
    def __readvalues(self):
        '''reads entries values and if ok calls add, ver 0.2'''
        #fill in other arguents (key, target, day, *notes) so that 
        #an observation can use all  fields
        try:
            daystr = self.__e_day.get()
            d = daystr.split('.')
            day = date(int(d[2]), int(d[1]), int(d[0]))
        except IndexError:
            day = date.today()
        
        self.add(len(self.observations), self.__e_target.get().strip(), day, self.__e_notes.get().strip())        
        self.__result.set(self) # sets value to be the string given as an arguemnt
        #__str__ is defined so using self calls __str__

    
    @property
    def name(self):
        '''diary name, ver0.1'''
        return self.__name
        
    @property
    def observations(self):
        '''complete dictionary, ver0.1'''
        return self.__observations
    
    @observations.setter
    def observations(self, obs):
        '''
        sets the complete dictionary, ver0.1
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
        ver0.1
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

    
    def __str__(self) :
        '''
        returns the object as an formatted string, ver0.1
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

if __name__ == '__main__' :
    '''
    if the program is started from a script
    ask the diary name first and then open the diary window to feed in observations
    ver 0.2
    '''
    diary = Diary(input('Observation diary includes observations, date of observation and possible notes.\nDiary name:').strip())    
    diary.mainloop()