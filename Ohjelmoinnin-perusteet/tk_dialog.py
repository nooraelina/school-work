import tkinter as tk
import tkinter.messagebox as msg

# Answer button pressed
def answer():
    # Error message box with OK button
    # 1st param is a title, 2nd param is a text
    msg.showerror("Answer", "Sorry, no answer available")

def callback():
    # Yes No box
    # If the user clicks Yes, askyesno returns True
    if msg.askyesno('Verify', 'Really quit?'):
        # Warning message
        msg.showwarning('Yes', 'Not yet implemented')
    else:
        # Info message
        msg.showinfo('No', 'Quit has been cancelled')

root = tk.Tk()
# Main window with two buttons
# Pressing this button calls the function callback()
b1 = tk.Button(text = 'Quit', command = callback)
# fill means that b1 fills the entire space horizontally
# Y would be vertically
b1.pack(fill = tk.X)
# Pressing this button calls the function answer()
b2 = tk.Button(text = 'Answer', command = answer)
# fill means that b2 fills the entire space horizontally
b2.pack(fill = tk.X)
root.mainloop()
