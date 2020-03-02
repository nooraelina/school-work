"""diary_0_4.py simple (and clumsy) TKinter GUI added"""

#from datetime import date
from diarydict import DiaryDict, date
import tkinter as tk
from tkinter import ttk

class ButtonView(ttk.Frame):
    ''' places buttons inside a Frame that is then placed inside window as one element '''
    def __init__(self, parent, *args, **kwargs) :
        super().__init__(parent, *args, **kwargs) 
        tk.Button(self, text = 'add', command = parent.readvalues, width = 10).grid(row = 0, column = 0,  pady = 10, )        
        tk.Button(self, text = 'update', command = parent.updatevalues, width = 10).grid(row = 0, column = 1,  pady = 10, )        
        tk.Button(self, text = 'delete', command = parent.deletevalues, width = 10).grid(row = 0, column = 2,  pady = 10, )
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        
class Diary(tk.Tk) :
    '''
    Diary class keeps track of observations in DiaryDict object, is also a TK GUI
    '''
    def __init__(self, name=str(), *args, **kwargs) :
        '''
        Gets a name and sets it to be the value of attribute name. 
        If no name is given the default is 'Diary [month/year]' where year and 
        month are the current year and month e.g. Diary June/2019
        Also adds the GUI elements 
        '''
        super().__init__(*args, **kwargs) #call Tk class initializer
        self.__diary = DiaryDict(name) #__diary checks the validity for the name
        self.__selected_key = -1 #valid values 0...
        self.__max = len(self.__diary.observations) # if observations are deleted from middle this is the next to be added

# =============================================================================
#         Add simple GUI elements (labels, entries, and button)
# =============================================================================
        self.title(self.__diary.name)  #title is the validated attribute name
        self.geometry('900x600')
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
#        Add button and pressing it will read entries, call readvalues and if
#       and call add method can process entries calls add method
#       Modify and Delete buttons call respective methods in DiaryDict
#       Buttons are inside a Frame that is placed inside the program window (self)        
# =============================================================================
        #TODO ver0.4 add ButtonView object containing buttonsa add, modify and delete
        ButtonView(self).grid(row = 3, column = 1, sticky = tk.E + tk.W)

# =============================================================================
#         Treeview to show all observations, select one for modifying and removing
# =============================================================================
  
        self.__tv = ttk.Treeview(self, columns=['target', 'date', 'notes'], selectmode = 'browse')
        self.__tv.heading('#0', text = 'ID')
        self.__tv.heading('target', text = 'Target' )
        self.__tv.heading('date', text = 'Date' )
        self.__tv.heading('notes', text = 'Notes' )
        self.__tv.column('#0', width = 50)
        self.__tv.column('target', width = 250 )
        self.__tv.column('date', width = 100 )
        self.__tv.column('notes', stretch = True )        
        self.__tv.grid(row = 4, column = 1, pady = 10, sticky = tk.W + tk.E)
        self.__scrollbar = ttk.Scrollbar(self, orient = tk.VERTICAL, command = self.__tv.yview)
        self.__tv.configure(yscrollcommand = self.__scrollbar.set)
        self.__scrollbar.grid(row = 4, column = 1, sticky = 'NSE')
        self.__tv.bind('<<TreeviewOpen>>', self.__open_observation) #bind to doubleclick
        
        tk.Label( self, text = 'Use double click to select a row for modifying or deleting ').grid(row = 5, column = 1, sticky = tk.W + tk.E)
    
    def readvalues(self):
        '''reads entries values and if ok calls add, calls __diary's services'''
        d = str(self.__e_day.get().strip()).split('.')
        if len(d) == 3 : 
            day = date(int(d[2]), int(d[1]), int(d[0])) 
        else :
            day = date.today() 
# =============================================================================
#         add to datamodel (DiaryDict object)
# =============================================================================    
        #ensure that you added key does not exist (add to the end)
        key = self.__max
        if len(self.__diary.observations) > self.__max : 
            key = len(self.__diary.observations)
        if self.__diary.add(key, self.__e_target.get().strip(), day, self.__e_notes.get().strip()) :
# =============================================================================
#         add to treeview if adding was successful, add to the end and update max
#         The ttk.Treeview widget displays a hierarchical collection of items. 
#         Each item has a textual label, an optional image, and an optional list of data values. 
#         The data values are displayed in successive columns after the tree label.
# =============================================================================              
             self.__tv.insert('','end', iid=str(key), text = str(key), 
                          values = [self.__e_target.get().strip(), day, self.__e_notes.get().strip()])
             self.__max += 1

    def updatevalues(self):
        '''updates selected item in diarydict and treeview'''
        if self.__selected_key >= 0:
            #re-read values target, date and notes
            d = str(self.__e_day.get().strip()).split('.')
            if len(d) == 3 : 
                day = date(int(d[2]), int(d[1]), int(d[0])) 
            else :
                day = date.today() 
            #TODO ver0.4 call diarydict modify method  
            self.__diary.modify(self.__selected_key, self.__e_target.get().strip(), day, self.__e_notes.get().strip())

            #update treeview
            item = self.__tv.selection()
            self.__tv.item(item, text = str(self.__selected_key), 
                          values = [self.__e_target.get().strip(), day, self.__e_notes.get().strip()])

    def deletevalues(self):
        '''removes item with selected key from diarydict and treeview'''
        if self.__selected_key >= 0:
            #TODO ver0.4 call diarydict remove
            self.__diary.remove(self.__selected_key)
          
            #update treeview
            item = self.__tv.selection()
            self.__tv.delete(item)

    def __open_observation(self, *args):
        '''reponds to double click'''
        self.__selected_key = int(self.__tv.selection()[0])
        self.__e_target.set( self.__diary.observations[self.__selected_key][0])
        self.__e_day.set(self.__diary.observations[self.__selected_key][1])
        self.__e_notes.set(self.__diary.observations[self.__selected_key][2])

if __name__ == '__main__' :
    '''
    if the program is started from a script
    ask the diary name first and then open the diary window to feed in observations
    '''
    diary = Diary(input('Observation diary includes observations, date of observation and possible notes.\nDiary name:').strip())    
    diary.mainloop()