# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:52:34 2019

@author: noora
"""
# Tehtävä 1
import tkinter as tk

root = tk.Tk()
w = tk.Label(root, 
             text = 'Python',
             bg = 'blue',
             width = 5).pack()
w2 = tk.Label(root,
              text = 'Perl',
              bg = 'light green',
              width = 5).pack()
w3 = tk.Label(root,
              text = 'C++',
              bg = 'pink',
              width = 5).pack()
w4 = tk.Label(root,
              text = 'Java',
              bg = 'light yellow',
              width = 5).pack()
w5 = tk.Label(root,
              text = 'Tcl/Tk',
              bg = 'grey',
              width = 5).pack()
root.mainloop()

