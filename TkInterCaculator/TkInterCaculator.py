import Tkinter
import tkMessageBox

window = Tkinter.Tk()
greeting = Tkinter.Label(window, text="Calculator")
greeting.pack()

x = Tkinter.Entry(window)
x.pack()
y = Tkinter.Entry(window)
y.pack()
operacija = Tkinter.Entry(window)
operacija.pack()

def check_guess():
    if operacija.get() == "+":
        rezultat = int(x.get())+int(y.get())
    if operacija.get() == "-":
        rezultat = int(x.get())-int(y.get())
    if operacija.get() == "*":
        rezultat = int(x.get())*int(y.get())
    if operacija.get() == "/":
        rezultat = int(x.get())/int(y.get())

    tkMessageBox.showinfo("Result", rezultat)


submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()


window.mainloop()