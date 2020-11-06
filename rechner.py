"""
RECHNER

- 2 Textfelder
- 4 Buttons für mathematische Operationen
- Zeigen das Ergebnis in einem Alert an.
"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("RECHNER")
window.geometry("400x300")
window.config(bd=25)


def addieren():
    try:
        result.set(float(nummer1.get()) + float(nummer2.get()))
        mostrar_result()
    except:
        messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")


def subtrahieren():
    try:
        result.set(float(nummer1.get()) - float(nummer2.get()))
        mostrar_result()
    except:
        messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")


def multiplizieren():
    try:
        result.set(float(nummer1.get()) * float(nummer2.get()))
        mostrar_result()
    except:
        messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")


def dividieren():
    try:
        result.set(float(nummer1.get()) / float(nummer2.get()))
        mostrar_result()
    except:
        messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")


def mostrar_result():
    messagebox.showinfo("Ergebnis", f"Die Ergebnis ist: {result.get()}")
    nummer1.set("")
    nummer2.set("")


nummer1 = StringVar()
nummer2 = StringVar()
result = StringVar()

frame = Frame(window, width=340, height=250)
frame.config(bd=5, relief=SOLID, padx=15, pady=15)
frame.pack(side=TOP, anchor=CENTER)
frame.pack_propagate(False)

Label(frame, text="Geben Sie eine Nummer ein:").pack()
Entry(frame, textvariable=nummer1, justify="center").pack()

Label(frame, text="Geben Sie andere Nummer ein:").pack()
Entry(frame, textvariable=nummer2, justify="center").pack()

Label(frame, text="").pack()

Button(frame, text="Addieren", command=addieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Subtrahieren", command=subtrahieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Multiplizieren", command=multiplizieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Dividieren", command=dividieren).pack(side=LEFT, expand=YES, fill=X)


window.mainloop()
