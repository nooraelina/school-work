import tkinter as tk

def show_entry_fields():
   # e1.get() is the contents of the first Entry widget
   print('First Name: {0}\nLast Name: {1}'.format(e1.get(), e2.get()))

root = tk.Tk()

lab1 = tk.Label(root, text = "First Name")
# Grid layout, row = 0, column = 0
lab1.grid(row = 0)
lab2 = tk.Label(root, text = "Last Name")
# Grid layout, row = 1, column = 0
lab2.grid(row = 1)

# With Entry widget the user can input a text
e1 = tk.Entry(root)
e1.grid(row = 0, column = 1)
e2 = tk.Entry(root)
e2.grid(row = 1, column = 1)

# calling root.quit() quits the mainloop, but not the root window
b1 = tk.Button(root, text = 'Quit', command = root.quit)
b1.grid(row = 3, column = 0, sticky = tk.W, pady = 4)
# calling our function show_entry_fields
b2 = tk.Button(root, text = 'Show', command = show_entry_fields)
b2.grid(row = 3, column = 1, pady = 4)

tk.mainloop( )
