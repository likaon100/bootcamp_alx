from tkinter import *

import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo('Window Title', 'Wombat')
answer=tkinter.messagebox.askquestion('Question 1', 'Do you are smart?')

if answer =='yes':
    print(':)')
if answer == 'no':
    print(':(')

root.mainloop()