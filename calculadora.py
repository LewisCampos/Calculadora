from tkinter import *
from math import *


#Raiz
root=Tk()
root.title('Calculadora LE-1409')
root.iconbitmap('calculadora.ico')
root.geometry('510x480')
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

#Botones
button_color="gray99"
width_button=10
height_button=3

#Fila 1
Button_Pi=Button(root, text="π", bg=button_color, width=width_button, height=height_button,
command=lambda:click("pi"))
Button_Pi.grid(row=1, column=0, padx=10, pady=10)
Button_Left=Button(root, text="(", bg=button_color, width=width_button, height=height_button,
command=lambda:click("("))
Button_Left.grid(row=1, column=1, padx=10, pady=10)
Button_Right=Button(root, text=")", bg=button_color, width=width_button, height=height_button,
command=lambda:click(")"))
Button_Right.grid(row=1, column=2, padx=10, pady=10)
Button_AC=Button(root, text="AC", bg=button_color, width=width_button, height=height_button,
command=lambda:borrar())
Button_AC.grid(row=1, column=3, padx=10, pady=10)
Button_Div=Button(root, text="÷", bg=button_color, width=width_button, height=height_button,
command=lambda:click("/"))
Button_Div.grid(row=1, column=4, padx=10, pady=10)

#Fila 2
Button_Exp=Button(root, text="EXP", bg=button_color, width=width_button, height=height_button,
command=lambda:click("exp"))
Button_Exp.grid(row=2, column=0, padx=10, pady=10)
Button_7=Button(root, text="7", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(7))
Button_7.grid(row=2, column=1, padx=10, pady=10)
Button_8=Button(root, text="8", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(8))
Button_8.grid(row=2, column=2, padx=10, pady=10)
Button_9=Button(root, text="9", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(9))
Button_9.grid(row=2, column=3, padx=10, pady=10)
Button_Multi=Button(root, text="x", bg=button_color, width=width_button, height=height_button,
command=lambda:click("*"))
Button_Multi.grid(row=2, column=4, padx=10, pady=10)

#Fila 3
Button_Raiz=Button(root, text="√", bg=button_color, width=width_button, height=height_button,
command=lambda:click("sqrt"))
Button_Raiz.grid(row=3, column=0, padx=10, pady=10)
Button_4=Button(root, text="4", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(4))
Button_4.grid(row=3, column=1, padx=10, pady=10)
Button_5=Button(root, text="5", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(5))
Button_5.grid(row=3, column=2, padx=10, pady=10)
Button_6=Button(root, text="6", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(6))
Button_6.grid(row=3, column=3, padx=10, pady=10)
Button_Menos=Button(root, text="-", bg=button_color, width=width_button, height=height_button,
command=lambda:click("-"))
Button_Menos.grid(row=3, column=4, padx=10, pady=10)

#Fila 4
Button_LN=Button(root, text="LN", bg=button_color, width=width_button, height=height_button,
command=lambda:click("log"))
Button_LN.grid(row=4, column=0, padx=10, pady=10)
Button_1=Button(root, text="1", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(1))
Button_1.grid(row=4, column=1, padx=10, pady=10)
Button_2=Button(root, text="2", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(2))
Button_2.grid(row=4, column=2, padx=10, pady=10)
Button_3=Button(root, text="3", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(3))
Button_3.grid(row=4, column=3, padx=10, pady=10)
Button_Mas=Button(root, text="+", bg=button_color, width=width_button, height=height_button,
command=lambda:click("+"))
Button_Mas.grid(row=4, column=4, padx=10, pady=10)

#Fila 5
Button_Point=Button(root, text=".", bg=button_color, width=width_button, height=height_button,
command=lambda:click("."))
Button_Point.grid(row=5, column=0, padx=10, pady=10)
Button_0=Button(root, text="0", bg="CadetBlue1", width=width_button, height=height_button,
command=lambda:click(0))
Button_0.grid(row=5, column=1, padx=10, pady=10)
Button_Igual=Button(root, text="=", bg=button_color, width="40", height=height_button, 
command=lambda: hacer_operacion())
Button_Igual.grid(row=5, column=2, columnspan=3, padx=10, pady=10)


root.mainloop()