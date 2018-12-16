import tkinter

def sumuj():
    print(a_entry)
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    wynik.configure(text=a*b*c/100)

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="spalanie paliwa/100 km")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="cena paliwa PLN [l]")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()
c_label = tkinter.Label(master=root, text="odległość [km]")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()
wynik = tkinter.Label(master=root, text=" - ")
wynik.pack()

policz_button = tkinter.Button(
    master=root,
    text="( ͡° ͜ʖ ͡°)",
    command=sumuj
)
policz_button.pack()

root.title("( ͡° ʖ̯ ͡°)")
root.mainloop()
print("( ͡° ͜ʖ ͡°)")