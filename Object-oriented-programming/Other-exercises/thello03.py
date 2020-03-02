'''
Hello World ver0.2
Intruducing message passing
First example, fits for small scripts
'''
#importing tk and ttk keeping them in their own namespaces
import  tkinter  as tk 
from tkinter import ttk
#importing ttk replaces Tk widgets  (better looking ones)

class Logic :
    def __init__(self):
        self.__amount = 0
    def reset(self):
        self.__amount  = 0
        return self.__amount
    def change(self, diff = 1):
        self.__amount += diff
        return self.__amount
    
class HelloView(ttk.Frame):
    ''' uses pack geometry manager http://www.effbot.org/tkinterbook/pack.htm '''
    def __init__(self, parent, *args, **kwargs) :
        super().__init__(parent, *args, **kwargs) 
        self.logic  = Logic() #what if we don't use this ?
        self.v = tk.StringVar() #label text, if changed changes the changes are visible
        self.v.set('Hello World!')
        self.label = ttk.Label(self, textvariable = self.v, width = 100)
        self.button = ttk.Button(self, text = 'PRESS ME', command = self.change) #calls the function when the button is pressed
        self.label.pack(padx=10, pady=10, side = tk.RIGHT) 
        self.button.pack(padx=10, pady=10, side = tk.LEFT)         
    def change(self):                        
        self.v.set(f"You have pressed me {self.logic.change()} times")
#        self.v.set(f"You have pressed me {Logic().change()} times") 
    def reset(self):        
        self.v.set(f"Resetting amounts pressed to {self.logic.reset()}")        
#        self.v.set(f"Resetting amounts pressed to {Logic().reset()}") 
        
    
class Hello(tk.Tk):
    '''uses grid geometry manager '''
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs) 
        self.title('Hello Tkinter Style')
        self.geometry('400x200') #window size in pixels
        self.resizable(width = False, height = False)        
        self.hview = HelloView(self) #place Frame inside the program window (self)
        self.hview.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)
        ttk.Button(self, text = 'ADD', command = self.hview.change).grid(row = 1, column = 0, sticky = tk.N + tk.S + tk.W, padx=10, pady=10)
        ttk.Button(self, text = 'RESET', command = self.reset).grid(row = 2, column = 0, sticky = tk.N + tk.S + tk.W, padx=10, pady=10)             
    def reset(self):
        self.hview.reset()
        
if __name__ == '__main__' :
    app = Hello() #create app object
    app.mainloop() #call app object's mainloop
