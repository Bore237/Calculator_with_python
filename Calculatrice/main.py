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
root.geometry("485x568+0+0")

calculator = Frame(root)
calculator.grid()

#------------------------- Command  Bouton ---------------------------
def quitter():
    quitter = tkinter.messagebox.askyesno("scientifique calculator, Ete vous suer de vouloir quitter")
    if quitter > 0:
        root.destroy()
        return

def scientifique():
    root.resizable(width=False, height=False)
    root.geometry("944x572+0+0")
    
def standard():
    root.resizable(width=False, height=False)
    root.geometry("924x572+0+0")
    
#------------------------  Design des menus --------------------
menubar =Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

#------------------------ Calculator Logical -------------------

#------------------------ Entry information --------------------

txtDisplay = Entry(calculator, font=('arail', 20, 'bold'), 
                   bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


#------------- Innsert standard keyboad ---------------------
numberstd = "789456123"
btn = []
i=0
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calculator, width=5, height=2, font=('arail', 20, 'bold'),
                          bd =4, text=numberstd[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i+=1
        
btnClear = Button(calculator,text=chr(67),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=0, pady=1)
btnAllClear = Button(calculator,text=chr(67)+chr(69),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=1, pady=1)
btnsq = Button(calculator,text=chr(8730)+chr(69),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=2, pady=1)
btnAdd = Button(calculator,text="+",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=3, pady=1)
btnASub = Button(calculator,text="-",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=2, column=3, pady=1)
btnMul = Button(calculator,text="*",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=3, column=3, pady=1)
btnDiv = Button(calculator,text=chr(247),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=4, column=3, pady=1)

btnZero = Button(calculator,text="0",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=0, pady=1)
btnPoint = Button(calculator,text=".",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=1, pady=1)
btnPM = Button(calculator,text=chr(177),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=2, pady=1)
btnPM = Button(calculator,text="=",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=3, pady=1)

#------------- Innsert scintifique keyboad ---------------------
btnpi = Button(calculator,text="π",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=4, pady=1)
btnCos = Button(calculator,text="cos",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=5, pady=1)
btnTan = Button(calculator,text="tan",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=6, pady=1)
btnSin = Button(calculator,text="sin",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=1, column=7, pady=1)

#----nextrow
btn2pi = Button(calculator,text="2π",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=2, column=4, pady=1)
btnCoh = Button(calculator,text="coh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=2, column=5, pady=1)
btnTanh = Button(calculator,text="tanh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=2, column=6, pady=1)
btnSinh = Button(calculator,text="sinh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=2, column=7, pady=1)

#---- nextrow
btnLog = Button(calculator,text="log",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=3, column=4, pady=1)
btnExp = Button(calculator,text="Exp",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=3, column=5, pady=1)
btnPtg = Button(calculator,text="%",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=3, column=6, pady=1)
btnEuler = Button(calculator,text="e",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=3, column=7, pady=1)

#---- nextrow
btnLog2 = Button(calculator,text="log2",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=4, column=4, pady=1)
btnDeg = Button(calculator,text="deg",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=4, column=5, pady=1)
btnAcoh = Button(calculator,text="acoh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=4, column=6, pady=1)
btnAsinh = Button(calculator,text="asinh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=4, column=7, pady=1)

#---- nextrow
btnLog10 = Button(calculator,text="log10",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=4, pady=1)
btnLog1p = Button(calculator,text="log1p",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=5, pady=1)
btExpm1 = Button(calculator,text="expm1",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=6, pady=1)
btnLgamma = Button(calculator,text="lgamma",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue").grid(row=5, column=7, pady=1)

TextDisplay = Label(calculator,text="Scientific Calculator", font=('arail', 30, 'bold'), justify=CENTER)
TextDisplay.grid(row=0, column=4, columnspan=4)
#------------- Menu Fichier ------------------------------------ 
menubar.add_cascade(label="fichier", menu=filemenu)
filemenu.add_command(label = "standard", command = standard)
filemenu.add_command(label="scientific", command = scientifique)
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