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

root.mainloop()