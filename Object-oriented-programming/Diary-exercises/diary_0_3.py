"""
diary_0_3.py simple (and clumsy) TKinter GUI added
"""

from datetime import date
import tkinter as tk

class DiaryDict:
    '''ver0.3 Diary's user interfacce independet part'''
    def __init__(self):
        self.__name = ''
        self.observations = dict()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name != '':
            self.__name = name
        else:
            self.__name = f'Diary {date.today()}'
    
    def add(self, key, target, day,*notes):
        observation = []
        if target and day <= date.today() :
            observation = [target, day]
            if notes :
                note = str()
                for item in notes : 
                    note += item
                observation.append(note)
            self.observations[key] = observation

    def __str__(self):
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
        
class Diary(tk.Tk) :
    '''
    Diary class keeps track of observations, is also a TK GUI
    '''
    def __init__(self, name=str(), *args, **kwargs) :
        '''
        that passes the diary name to DiaryDict type object who checks the validity and 
        sets the title to be diarydict objects name attribute
        Created GUI
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer
         #ver 0.3 create DiaryDict object, pass name to it to check the validity for the name
        self.__diary = DiaryDict()      # Creating DiaryDict object
        self.__diary.name = name        # Setting the name, if no input, default name

# =============================================================================
#         Add simple GUI elements (labels, entries, and button)
# =============================================================================
         #ver0.3 set the title to be the DiaryDict object's validated name 
        self.title(self.__diary.name)
        self.geometry('900x400')
        self.resizable(width = False, height = False)
# =============================================================================
#         labels, that do not change, 
#         one line Entry fields that are used to read in values for 
#         target, date and notes 
#         position widgets (labes and entries) using grid() geometry
# =============================================================================
        self.__e_target, self.__e_day, self.__e_notes = tk.StringVar(), tk.StringVar(), tk.StringVar()
        tk.Label( self, text = 'target ').grid(row = 0, column = 0, sticky = tk.W)
        tk.Label( self, text = 'date [dd.mm.yyyy] ').grid(row = 1, column = 0, sticky = tk.W)
        tk.Label( self, text = 'notes ') .grid(row = 2, column = 0, sticky = tk.W)
        e_1 = tk.Entry(self, textvariable = self.__e_target, bd = 5, width = 50)
        e_2 = tk.Entry(self, textvariable = self.__e_day, bd = 5, width = 10)
        e_3 = tk.Entry(self, textvariable = self.__e_notes, bd = 5, width = 100)        
        e_1.grid(row = 0, column = 1, sticky = tk.W)
        e_2.grid(row = 1, column = 1, sticky = tk.W)
        e_3.grid(row = 2, column = 1, sticky = tk.W)
# =============================================================================
#         Add button and pressing it will read entries, call readvalues and if
#         and call add method can process entries calls add method
# =============================================================================
        b = tk.Button(self, text = 'add', command=self.__readvalues)
        b.grid(row = 3, column = 1, sticky = tk.E + tk.W)
# =============================================================================
#         multiline label to display all observations 
# =============================================================================
        self.__result = tk.StringVar()
        tk.Label( self, textvariable=self.__result, justify = tk.LEFT ).grid(row = 4, column = 1, sticky = tk.E + tk.W)

    
    def __readvalues(self):
        '''reads entries values and if ok calls add, calls DiaryDict object's services'''
        d = str(self.__e_day.get().strip()).split('.')
        if len(d) == 3 : 
            day = date(int(d[2]), int(d[1]), int(d[0])) 
        else :
            day = date.today() 
        
        #ver0.3 call DiaryDict object's add
        self.__diary.add(len(self.__diary.observations), self.__e_target.get().strip(), day, self.__e_notes.get().strip())
        #ver0.3 set __result value to DiaryDict object's string representation  
        self.__result.set(self.__diary)

if __name__ == '__main__' :
    '''
    if the program is started from a script
    ask the diary name first and then open the diary window to feed in observations
    '''
    diary = Diary(input('Observation diary includes observations, date of observation and possible notes.\nDiary name: ').strip())    
    diary.mainloop()