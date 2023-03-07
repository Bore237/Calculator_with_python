##############################################
######### Inport library #####################
from tkinter import *
import math 
import tkinter.messagebox

#--------------------------------------------------------------------#
#------------------------ Main dev ----------------------------------#

#------------------- Design du cardre ------------------------
root = Tk()
root.title("scientific calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("485x568+200+2")

calculator = Frame(root)
calculator.grid()

#------------------------- Command  Bouton ---------------------------
def quitter():
    quitter = tkinter.messagebox.askyesno("scientifique calculator, Ete vous suer de vouloir quitter")
    if quitter > 0:
        root.destroy()
        return
    
#------------------------  Design des menus --------------------
menubar =Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

#------------- Menu Fichier ------------------------------------ 
menubar.add_cascade(label="fichier", menu=filemenu)
filemenu.add_command(label = "standard")
filemenu.add_command(label="scientific")
filemenu.add_separator()
filemenu.add_command(label="Quitter", command = quitter)

#---------------- Menu editer ---------------------------------
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editer", menu=editmenu)
editmenu.add_command(label = "Couper")
editmenu.add_command(label="Copier")
editmenu.add_separator()
editmenu.add_command(label="Coller")

#----------------- Menu help ------------------------------
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=helpmenu)
helpmenu.add_command(label = "Obtenir de l'aide")



root.config(menu = menubar)
root.mainloop()