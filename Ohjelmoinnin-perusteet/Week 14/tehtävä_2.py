# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:15:24 2019

@author: noora
"""

import tkinter as tk
root = tk.Tk()
root.title('Off')
root.geometry('250x70')
value = 'Off'

def callback():
    global value
    if value == 'Off':
        root.title('On')
        value = 'On'
    else:
        root.title('Off')
        value = 'Off'

b = tk.Button(root, text='On/Off', command=callback)
b.pack()

tk.mainloop()