# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:36:55 2019

@author: noora

4. Use the file dialog to show the contents of the selected 
file in the Text widget. Use also a scrollbar.
"""

import tkinter as tk

# Function as user presses Read-button
def read():
    T = tk.Text(root, height=5, width=100)
    S = tk.Scrollbar(root)
    S.pack(side= tk.RIGHT, fill=tk.Y)
    T.pack(side= tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """HAMLET:
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
    T.insert(tk.END, quote)
    return

# Main window
root = tk.Tk()
root.title("Quote")
root.geometry('450x200')

lbl1 = tk.Label(root, text = 'Do you want to read the quote?').pack()
btn1 = tk.Button(root, text = 'Read', command = read).pack()
btn2 = tk.Button(root, text = 'Quit',command = root.destroy).pack()

root.mainloop()