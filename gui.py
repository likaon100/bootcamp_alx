from tkinter import *

root = Tk()


def printname(event): #akcja - wszystko co może zrobic uzytkownik
    print("Yolo")

button_1=Button(root, text="print my name")
button_1.bind("<Button-1>", printname)
#bind ma dwa parametry.
button_1.pack()

root.mainloop()