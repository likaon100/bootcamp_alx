import tkinter

def jakas_funkcja():
    wartosc=entry.get()
    label.configure(text="( ͡° ͜ʖ ͡°)")

root = tkinter.Tk()
root.columnconfigure(1)

entry = tkinter.Entry(master=root)
entry.grid(row=0, column=0)
label=tkinter.Label(master=root, text ="ukulele")
label.grid(row=1, column=3, sticky=tkinter.E)
button= tkinter.Button(master=root, text ="łeło")
button.grid(row=0, column=1)
root.mainloop()


