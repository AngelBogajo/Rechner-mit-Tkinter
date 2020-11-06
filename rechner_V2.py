"""
RECHNER

- 2 Textfelder
- 4 Buttons für mathematische Operationen
- Zeigen das Ergebnis in einem Alert an.
"""

from tkinter import *
from tkinter import messagebox


class Rechner():
    def __init__(self, achtung):

        self.nummer1 = StringVar()
        self.nummer2 = StringVar()
        self.result = StringVar()
        self.achtung = achtung


    def addieren(self):
        try:
            self.result.set(float(self.nummer1.get()) + float(self.nummer2.get()))
            self.mostrar_result()
        except:
            messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")

    def subtrahieren(self):
        try:
            self.result.set(float(self.nummer1.get()) - float(self.nummer2.get()))
            self.mostrar_result()
        except:
            messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")

    def multiplizieren(self):
        try:
            self.result.set(float(self.nummer1.get()) * float(self.nummer2.get()))
            self.mostrar_result()
        except:
            messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")

    def dividieren(self):
        try:
            self.result.set(float(self.nummer1.get()) / float(self.nummer2.get()))
            self.mostrar_result()
        except:
            messagebox.showinfo("Error", "Die Nummern sind nicht korrekt")

    def mostrar_result(self):
        self.achtung.showinfo("Ergebnis", f"Die Ergebnis ist: {self.result.get()}")
        self.nummer1.set("")
        self.nummer2.set("")

window = Tk()
window.title("RECHNER")
window.geometry("400x300")
window.config(bd=25)

# Objekt
rechner = Rechner(messagebox)

frame = Frame(window, width=340, height=250)
frame.config(bd=5, relief=SOLID, padx=15, pady=15)
frame.pack(side=TOP, anchor=CENTER)
frame.pack_propagate(False)

Label(frame, text="Geben Sie eine Nummer ein:").pack()
Entry(frame, textvariable=rechner.nummer1, justify="center").pack()

Label(frame, text="Geben Sie andere Nummer ein:").pack()
Entry(frame, textvariable=rechner.nummer2, justify="center").pack()

Label(frame, text="").pack()

Button(frame, text="Addieren", command=rechner.addieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Subtrahieren", command=rechner.subtrahieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Multiplizieren", command=rechner.multiplizieren).pack(side=LEFT, expand=YES, fill=X)
Button(frame, text="Dividieren", command=rechner.dividieren).pack(side=LEFT, expand=YES, fill=X)


window.mainloop()
