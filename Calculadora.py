from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""
operacion2 = ""
resultado = 0
decimal = ""
#-------pantalla--------

numeroPantalla = StringVar()
signos = StringVar()


pantallaResp = Entry(miFrame, textvariable = signos)
pantallaResp.grid(row = 0, column = 1, padx = 10, columnspan = 4, ipady = 5)
pantallaResp.config(background = "blue", fg = "black", justify = "right")

pantalla = Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 0, columnspan = 4, ipady = 5)
pantalla.config(background = "blue", fg = "black", justify = "right")



#-------pulsaciones teclado------


numeroPantalla.set("0")

def numeroPulsado(num):
    
    global operacion
    global decimal
    global resultado
    
    if (operacion != ""):
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

    otro = numeroPantalla.get()


    if(num == "."):
        decimal = "activo"
    if(otro == "00"):
        numeroPantalla.set("0")
    elif(otro.find("Borrar") != -1):
        otro = otro[:-7]
        numeroPantalla.set(otro)
        if(otro == ""):
            numeroPantalla.set("0")
    elif(num== "CE"):
        numeroPantalla.set("0")
        resultado = 0
        signos.set("")
        decimal = ""
    elif((otro[0] == "0" and num==".")):
        numeroPantalla.set("0.")

    elif(otro[0] == "0" and otro[1] >= "0" ):
            numeroPantalla.set(otro[1])       
    elif(otro.find("..")!= -1):
        numeroPantalla.set(otro[:-1])
    elif(otro.count(".") > 1):
        numeroPantalla.set(otro[:-1])

        


#-------------------- funcion suma------------
def suma(num):
    
    global operacion 
    global resultado
    global decimal
    global operacion2
    
    if(decimal == "activo"):
        resultado +=  float(num)
    else:
        resultado +=  int(num)
    
    signos.set( signos.get() + numeroPantalla.get() + "+" )
        
    operacion = "suma" 
    operacion2 = "suma"
    numeroPantalla.set(resultado)
    
    
#------------------ funcion resta----------------

num1 = 0
contadorResta = 0

def resta(num):

    global operacion 
    global resultado
    global decimal
    global operacion2
    global contadorResta
    
    if(contadorResta == 0 and decimal == ""):
        num1=int(num)
        resultado=num1
    elif(contadorResta == 0 and decimal == "activo"):
        num1=float(num)
        resultado=num1
    else:
        if(decimal == "activo" and contadorResta == 1):
            resultado =  float(num)-float(num1)
        else:
            resultado =  int(num)-int(num1)
    
    signos.set(signos.get() +numeroPantalla.get() + "-" )
        
    operacion = "resta"
    operacion2 = "resta"
    contadorResta=contadorResta+1
    
    numeroPantalla.set(resultado)
    
#------------------ funcion multiplicacion----------------

num1 = 0
contadorMult = 0

def multiplicacion(num):

    global operacion 
    global resultado
    global decimal
    global operacion2
    global contadorMult
    global num1
    
    if(contadorMult == 0 and decimal == ""):
        num1=int(num)
        resultado=num1
    elif(contadorMult == 0 and decimal == "activo"):
        num1=float(num)
        resultado=num1
    else:
        if(decimal == "activo" and contadorMult == 1):
            resultado =  float(num)-float(num1)
        else:
            resultado =  int(num)-int(num1)
    
    signos.set(signos.get() +numeroPantalla.get() + "*" )
        
    operacion = "multiplicacion"
    operacion2 = "multiplicacion"
    contadorMult=contadorMult+1
    
    numeroPantalla.set(resultado)
    
#------------------ funcion division----------------

num1 = 0
contadorDiv = 0

def division(num):

    global operacion 
    global resultado
    global decimal
    global operacion2
    global contadorDiv
    global num1
    
    if(contadorDiv == 0 and decimal == ""):
        num1=int(num)
        resultado=num1
    elif(contadorDiv == 0 and decimal == "activo"):
        num1=float(num)
        resultado=num1
    else:
        if(decimal == "activo" and contadorDiv == 1):
            resultado =  float(num)/float(num1)
        else:
            resultado =  int(num)/int(num1)
    
    signos.set(signos.get() +numeroPantalla.get() + "/" )
        
    operacion = "division"
    operacion2 = "division"
    contadorDiv=contadorDiv+1
    
    numeroPantalla.set(resultado)

    
#------------------ funcion el_resultado-----

def el_resultado():
    
    global resultado
    global decimal
    global operacion2
    global contadorResta
    global contadorMult
    global contadorDiv
    
    if(operacion2 == "suma"):  
        if(decimal == "activo"):
            otro = round(resultado,1) + float(numeroPantalla.get())
            numeroPantalla.set(otro)
        
        else:
            otro = resultado + int(numeroPantalla.get())
            numeroPantalla.set(otro)
            decimal = ""
        print(otro)
        restultado = 0

    elif(operacion2 == "resta"):
        if(decimal == "activo"):
            otro = round(resultado,1) - float(numeroPantalla.get())
            numeroPantalla.set(otro)
            contadorResta=0
        
        else:
            otro = resultado - int(numeroPantalla.get())
            numeroPantalla.set(otro)
            decimal = ""
        print(otro)
        contadorResta=0
        restultado = 0
        
    elif(operacion2 == "multiplicacion"):
        if(decimal == "activo"):
            otro = round(resultado,1) * float(numeroPantalla.get())
            numeroPantalla.set(otro)
            contadorResta=0
        
        else:
            otro = resultado * int(numeroPantalla.get())
            numeroPantalla.set(otro)
            decimal = ""
        print(otro)
        contadorMult=0
        restultado = 0
    elif(operacion2 == "division"):
        if(decimal == "activo"):
            otro = round(resultado,1) / float(numeroPantalla.get())
            numeroPantalla.set(otro)
            contadorResta=0
        
        else:
            otro = resultado / int(numeroPantalla.get())
            numeroPantalla.set(otro)
            decimal = ""
        print(otro)
        contadorDiv=0
        restultado = 0
    
    #print(otro)
    #restultado = 0

## nueva funcion columnespan sirve para que la pantalla se adapte al tamaño de las columnas y va en el grid
#---- fila 1-------------------

boton7= Button(miFrame, text = "7", width = 3,command =lambda:numeroPulsado("7"))
boton7.grid(row = 2, column = 1)
boton8= Button(miFrame, text = "8", width = 3,command =lambda:numeroPulsado("8"))
boton8.grid(row = 2, column = 2)
boton9= Button(miFrame, text = "9", width = 3,command =lambda:numeroPulsado("9"))
boton9.grid(row = 2, column = 3)
botonDiv= Button(miFrame, text = "/", width = 3, command =lambda:division(numeroPantalla.get()))
botonDiv.grid(row = 2, column = 4)

#---- fila 2-------------------

boton4= Button(miFrame, text = "4", width = 3, command =lambda:numeroPulsado("4"))
boton4.grid(row = 3, column = 1)
boton5= Button(miFrame, text = "5", width = 3,command =lambda:numeroPulsado("5"))
boton5.grid(row = 3, column = 2)
boton6= Button(miFrame, text = "6", width = 3,command =lambda:numeroPulsado("6"))
boton6.grid(row = 3, column = 3)
botonMul= Button(miFrame, text = "X", width = 3,command =lambda:multiplicacion(numeroPantalla.get()))
botonMul.grid(row = 3, column = 4)


#---- fila 3-------------------

boton1= Button(miFrame, text = "1", width = 3,command =lambda:numeroPulsado("1"))
boton1.grid(row = 4, column = 1)
boton2= Button(miFrame, text = "2", width = 3,command =lambda:numeroPulsado("2"))
boton2.grid(row = 4, column = 2)
boton3= Button(miFrame, text = "3", width = 3,command =lambda:numeroPulsado("3"))
boton3.grid(row = 4, column = 3)
botonRest= Button(miFrame, text = "-", width = 3,command =lambda:resta(numeroPantalla.get()))
botonRest.grid(row = 4, column = 4)

#---- fila 4-------------------

boton0= Button(miFrame, text = "0", width = 3,command =lambda:numeroPulsado("0"))
boton0.grid(row = 5, column = 1)
botonComa= Button(miFrame, text = ",", width = 3,command =lambda:numeroPulsado("."))
botonComa.grid(row = 5, column = 2)
botonIgual= Button(miFrame, text = "=", width = 3,command =lambda:el_resultado())
botonIgual.grid(row = 5, column = 3)
botonSuma= Button(miFrame, text = "+", width = 3,command =lambda:suma(numeroPantalla.get()))
botonSuma.grid(row = 5, column = 4)

#---- fila 5-------------------

botonBorrar= Button(miFrame, text = "Borrar", width =  9,command =lambda:numeroPulsado("Borrar"))
botonBorrar.grid(row = 6, column = 1, columnspan = 2)
botonBorrar= Button(miFrame, text = "CE", width =  9,command =lambda:numeroPulsado("CE"))
botonBorrar.grid(row = 6, column = 3, columnspan = 2)

raiz.mainloop()