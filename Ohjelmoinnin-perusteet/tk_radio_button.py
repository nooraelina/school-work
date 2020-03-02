import tkinter as tk

root = tk.Tk()

# Tkinter integer variable
v = tk.IntVar()
# Set the value of the variable to 0
v.set(0)  # initializing the choice, i.e. Python

languages = ['Python', 'Perl', 'Java', 'C++', 'C']

def ShowChoice():
    # Get the value of the variable v
    print(v.get())

# It is possible to combine pack() with tk.Label()
tk.Label(root, 
         text = """Choose your favourite 
programming language:""",
         # Start the text from the left
         justify = tk.LEFT,
         # Leave space 20 pixels
         padx = 20).pack()

# enumerate gives the counter val and the element language
for val, language in enumerate(languages):
    rb = tk.Radiobutton(root, 
                  text = language,
                  padx = 20,
        # Tkinter variable defined earlier
                  variable = v, 
                  command = ShowChoice,
        # value is the value of variable v
                  value = val)
    # Anchors are used to define where text is positioned
    # relative to a reference point. W = West
    rb.pack(anchor = tk.W)

root.mainloop()
