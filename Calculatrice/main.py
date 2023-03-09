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

#------------------------ Entry information --------------------

txtDisplay = Entry(calculator, font=('arail', 20, 'bold'), 
                   bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


#------------------------ Calculator Logical -------------------
class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value =True
        self.check_sum = False
        self.oper = ''
        self.result = False
        
    def numberEnter(self, num):
        self.resultat = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
        
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
            
    def valid_function(self):
        if self.oper == 'add':
            self.total += self.current 
        if self.oper == 'sub':
            self.total -= self.current 
        if self.oper == 'mul':
            self.total *= self.current 
        if self.oper == 'div':
            self.total /= self.current            
        if self.oper == 'mod':
            self.total %= self.current 
            
        self.input_value =  True
        self.check_sum = False
        self.display(self.total)
        
    def operator(self, oper):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.oper = oper
        self.result = False
        
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    
    def clear(self):
        self.resultat = False
        if len(self.current) > 0:
            if len(self.current) == 1:
                self.display(0)
                self.input_value = True
            else:
                self.current = self.current[0:len(self.current)-1]
                self.display(self.current)
        else:
           self.display(0)
           self.input_value = True
            
    def clearAll(self):
        self.display(0)
        self.input_value = True
        
    def pm(self):
        self.result = False
        self.current = -float(txtDisplay.get())
        self.display(self.current)
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def twopi(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
        
    def log(self):
        self.result = False
        a = (float(txtDisplay.get()))
        
        if a <= 0:
            txtDisplay.display("can't log negatif number or null number")
        else:
            self.current = math.log(a)
            self.display(self.current)

    def log10(self):
        self.result = False
        a = (float(txtDisplay.get()))
        
        if a <= 0:
            txtDisplay.display("can't log negatif number or null number")
        else:
            self.current = math.log10(a)
            self.display(self.current)

    def log2(self):
        self.result = False
        a = (float(txtDisplay.get()))
        
        if a <= 0:
            txtDisplay.display("can't log negatif number or null number")
        else:
            self.current = math.log2(a)
            self.display(self.current)
            
    def log1p(self):
        self.result = False
        a = (float(txtDisplay.get()))
        
        if a <= 0:
            txtDisplay.display("can't log negatif number or null number")
        else:
            self.current = math.log1p(a)
            self.display(self.current)
            
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current) 
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current) 

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current) 
    
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current) 
        
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current) 

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)     
        
    def acosh(self):
        self.result = False
        a = txtDisplay.get()
        if a >= 1:
            self.current = math.acosh(float(a))
            self.display(self.current) 
        else:
            self.display("Error") 
        
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current) 

    def atanh(self):
        self.result = False
        self.current = math.atanh(float(txtDisplay.get()))
        self.display(self.current) 

    def exp(self):
        self.result = False
        self.current = math.exp (float(txtDisplay.get()))
        self.display(self.current)
        
    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
        
    def sqrt(self): 
        self.result = False
        a = txtDisplay.get()
        if a > 0:
            self.current = math.sqrt(float(a))
            self.display(self.current)
        else:
            self.display("Put the positif number")
            
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)
        
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
        
    def tanh(self):
        self.result = False
        self.current = math.p (math.radians(float(txtDisplay.get())))
        self.display(self.current)  
        
    def percen(self):
        self.result = False
        self.current = float(txtDisplay.get()) * 100
        self.display(self.current)
        
#--------- Create the calculate objet---------
added_value = Calculator()    
        
#------------- Innsert standard keyboad ---------------------
numberstd = "789456123"
btn = []
i=0
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calculator, width=5, height=2, font=('arail', 20, 'bold'),
                          bd =4, text=numberstd[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberstd[i]: added_value.numberEnter(x)
        i+=1
        
btnClear = Button(calculator,text=chr(67),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.clear ).grid(row=1, column=0, pady=1)
btnAllClear = Button(calculator,text=chr(67)+chr(69),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.clearAll).grid(row=1, column=1, pady=1)
btnsq = Button(calculator,text=chr(8730)+chr(69),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.sqrt).grid(row=1, column=2, pady=1)
btnAdd = Button(calculator,text="+",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.operator("add")).grid(row=1, column=3, pady=1)
btnASub = Button(calculator,text="-",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.operator("sub")).grid(row=2, column=3, pady=1)
btnMul = Button(calculator,text="*",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.operator("mul")).grid(row=3, column=3, pady=1)
btnDiv = Button(calculator,text=chr(247),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.operator("div")).grid(row=4, column=3, pady=1)

btnZero = Button(calculator,text="0",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.numberEnter("0")).grid(row=5, column=0, pady=1)
btnPoint = Button(calculator,text=".",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = lambda : added_value.numberEnter('.')).grid(row=5, column=1, pady=1)
btnPM = Button(calculator,text=chr(177),  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.pm).grid(row=5, column=2, pady=1)
btnPM = Button(calculator,text="=",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.sum_of_total).grid(row=5, column=3, pady=1)

#------------- Innsert scintifique keyboad ---------------------
btnpi = Button(calculator,text="π",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.pi).grid(row=1, column=4, pady=1)
btnCos = Button(calculator,text="cos",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.cos).grid(row=1, column=5, pady=1)
btnTan = Button(calculator,text="tan",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.tan).grid(row=1, column=6, pady=1)
btnSin = Button(calculator,text="sin",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.sin).grid(row=1, column=7, pady=1)

#----nextrow
btn2pi = Button(calculator,text="2π",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.twopi).grid(row=2, column=4, pady=1)
btnCoh = Button(calculator,text="cosh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.cosh).grid(row=2, column=5, pady=1)
btnTanh = Button(calculator,text="tanh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.tanh).grid(row=2, column=6, pady=1)
btnSinh = Button(calculator,text="sinh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.sinh).grid(row=2, column=7, pady=1)

#---- nextrow
btnLog = Button(calculator,text="log",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.log).grid(row=3, column=4, pady=1)
btnExp = Button(calculator,text="exp",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.exp).grid(row=3, column=5, pady=1)
btnPtg = Button(calculator,text="%",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.percen).grid(row=3, column=6, pady=1)
btnEuler = Button(calculator,text="e",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.e).grid(row=3, column=7, pady=1)

#---- nextrow
btnLog2 = Button(calculator,text="log2",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.log2).grid(row=4, column=4, pady=1)
btnDeg = Button(calculator,text="deg",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.deg).grid(row=4, column=5, pady=1)
btnAcoh = Button(calculator,text="acosh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue",command = added_value.acosh).grid(row=4, column=6, pady=1)
btnAsinh = Button(calculator,text="asinh",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.asinh).grid(row=4, column=7, pady=1)

#---- nextrow
btnLog10 = Button(calculator,text="log10",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue" , command = added_value.log10).grid(row=5, column=4, pady=1)
btnLog1p = Button(calculator,text="log1p",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.log1p).grid(row=5, column=5, pady=1)
btExpm1 = Button(calculator,text="expm1",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.expm1).grid(row=5, column=6, pady=1)
btnLgamma = Button(calculator,text="lgamma",  width=5, height=2, font=('arail', 20, 'bold'),
                bd =4, bg="powder blue", command = added_value.lgamma).grid(row=5, column=7, pady=1)

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