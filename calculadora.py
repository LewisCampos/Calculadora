from tkinter import *
from math import *


#Raiz
root=Tk()
root.title('Calculadora LE-1409')
root.iconbitmap('calculadora.ico')
root.geometry('500x480')
root.config(bg='gray42')
root.resizable(False, False)

#Pantalla
screen=Entry(root, font=("arial",20, "bold"), width=22, borderwidth=10, background="CadetBlue1", justify="right")
screen.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

#Logica
i = 0
def click(valor):
    global i 
    screen.insert(i, valor)
    i += 1

def borrar():
    screen.delete(0, END)
    i = 0

def hacer_operacion():
    ecuacion=screen.get()
    try:
        result=eval(ecuacion)
        screen.delete(0, END)
        screen.insert(0, result)
        i = 0
    except:
        screen.delete(0, END)
        r=screen.insert(0, "ERROR")
        print(r)

root.mainloop()