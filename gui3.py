from tkinter import *


def doNothing():
    print("bla bla bla")


root = Tk()
# Main Menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now project...", command=doNothing)
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=subMenu.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)
editMenu.add_command(label="Exit", command=subMenu.quit)

# Creating toolbar

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#status bar

status=Label(root, text="Preparing to do nothing", bd=5, relief=SUNKEN, anchor=W) #w - form left site
status.pack(side=BOTTOM, fill=X)
root.mainloop()
