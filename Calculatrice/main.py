##############################################
######### Inport library #####################
from tkinter import *
import math 
import tkinter.messagebox

##############################################
######### Main dev #####################
root = Tk()
root.title("scientific calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("485x568+0+0")

calculator = Frame(root)
calculator.grid()

menubar =Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="fichier", menu=filemenu)
filemenu.add_command(label = "standard")
filemenu.add_command(label="scientific")
filemenu.add_separator()
filemenu.add_command(label="Quitter")

root.config(menu = menubar)
root.mainloop()