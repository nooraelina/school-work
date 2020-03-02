# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 02:12:23 2019

@author: noora
"""
import tkinter as tk
import math

# Calculation function
def calculate():
    h = float(height.get())
    degr = float(angle.get())
    rad = math.radians(degr)
    ans = h / math.tan(rad)
    tk.Label(root, text = ans).grid(row = 7, column = 2, padx = 0, pady = 3)
    return
    
root = tk.Tk()
root.title("The projection to x-axis")
root.geometry('400x200')

height = tk.StringVar()
angle = tk.StringVar()
# User inputs
labelHeight = tk.Label(root, 
                       text = 'Height:').grid(row = 1, column = 1, padx = 0, pady = 3)
entHeight = tk.Entry(root, 
                     textvariable = height).grid(row = 1, column = 2)
labelAngle = tk.Label(root, 
                      text = 'Angle (as degrees):').grid(row = 2, column = 1, padx = 0, pady = 3)
entAngle = tk.Entry(root, 
                    textvariable = angle).grid(row = 2, column = 2)
# Button
btn = tk.Button(root, 
                text = 'Calculate', 
                command = calculate).grid(row = 5, column = 2)
# Answer label
labelXaxis = tk.Label(root, 
                      text = 'Answer:').grid(row = 7, column = 1, padx = 0, pady = 3)

tk.mainloop()
