import random
import tkinter
import pygame
from tkinter import *
from tkinter import filedialog, Text  # importa todo lo necesario para gui, ya que todo funciona
from tkinter import Image
preguntas_restantes = [1, 2, 3, 4, 5, 6] #toma la cuenta de las preguntas restantes, si no hay nada se reinicia la cuenta
root = tkinter.Tk()  #incia la interfaz grafica
root.title("TEST")   #le pone un titulo a la ventana



#Le pone el tamaño a la ventana, como esto es un juego de movil es mas largo que ancho
canvas = tkinter.Canvas(root, height=1280, width=720)
canvas.pack()



#Inicia el lugar donde se va a poner la pregunta, esta pintada de azul para verla mejor
preguntas = tkinter.Frame(root, bg="blue")
preguntas.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Inicia el texto de la pregunta
texto_pregunta = tkinter.StringVar()
texto_pregunta.set("")

#Inicia el texto del boton 1
texto_boton_1 = tkinter.StringVar()
texto_boton_1.set("")

#Inicia el texto del boton 2
texto_boton_2 = tkinter.StringVar()
texto_boton_2.set("")

#Inicia el texto del boton 3
texto_boton_3 = tkinter.StringVar()
texto_boton_3.set("")

#inicia el lugar donde se ponen los botones
botonera = tkinter.Frame(root, bg="red")
botonera.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)
lugar_imagenes = tkinter.Label(botonera)

#Inicia el lugar donde van escritas las preguntas
lugar_de_las_preguntas = tkinter.Label(preguntas, textvariable=texto_pregunta , bg="white", fg="black")
lugar_de_las_preguntas.pack(side="top")

#inicia el boton 1
boton1 = tkinter.Button(botonera, textvariable=texto_boton_1, bg="white", fg="black")
boton1.pack(side="top")

#inicia el boton 2
boton2 = tkinter.Button(botonera, textvariable=texto_boton_2, bg="white", fg="black")
boton2.place(x=160, y=180)

#inicia el boton 3
boton3 = tkinter.Button(botonera, textvariable=texto_boton_3, bg="white", fg="black")
boton3.pack(side="bottom")



respuestas_correctas = 0  #toma la cuenta de las preguntas acertadas


def personalizacion1():
    preguntas.config(bg="deeppink")
    botonera.config(bg="purple")
    lugar_de_las_preguntas.config(bg="white", fg="black")
    boton1.config(bg="white", fg="black")
    boton2.config(bg="white", fg="black")
    boton3.config(bg="white", fg="black")
    inicio()



def personalizacion2():
    preguntas.config(bg="yellow")
    botonera.config(bg="orange")
    lugar_de_las_preguntas.config(bg="white", fg="black")
    boton1.config(bg="white", fg="black")
    boton2.config(bg="white", fg="black")
    boton3.config(bg="white", fg="black")
    inicio()


def personalizacion3():
    preguntas.config(bg="black")
    botonera.config(bg="dimgray")
    lugar_de_las_preguntas.config(bg="black", fg="white")
    boton1.config(bg="dimgray", fg="white")
    boton2.config(bg="dimgray", fg="white")
    boton3.config(bg="dimgray", fg="white")
    inicio()

def personalizacion():
    boton2.place(x=90, y=180)
    boton3.pack(side="bottom")
    texto_pregunta.set("Este es el lugar de personalizacion, aqui podras elegir el fondo (test)") #no definitivo solo es para probar
    texto_boton_1.set("fondo1 morado/ fondo2 fondo2 rosa")
    boton1.config(command=personalizacion1)
    texto_boton_2.set("fondo1 amarillo/ fondo2 naranja")
    boton2.config(command=personalizacion2)
    texto_boton_3.set("negro programador")
    boton3.config(command=personalizacion3)






#inicia la pestaña de configuracion (esto sirve para cambiar el color de la interfaz y el idioma (no estoy seguro))
def configuaracion():
    boton2.place(x=130, y=180)
    boton3.pack(side="bottom")
    texto_pregunta.set("Esta es la configuracion, donde puedes personalizar el juego y el idioma (no funcional)")
    texto_boton_1.set("Personalizacion")
    boton1.config(command=personalizacion) #de normal es personalizacion, none para no causar bugs hasta que se acabe personalizacion, funciona como pregunta_random()
    texto_boton_2.set("Idioma (no funcional)")
    boton2.config(command=None) #de normal es idioma, none porque a quien le apetece traducir un juego sin acabar?, funciona como configuracion()
    texto_boton_3.set("Volver")
    boton3.config(command=inicio)




#inicia lo primer que sale en pantalla al ejecutar el programa (da la opcion de continuar, Ejecuta pregunta_random o de la configuracion)
def inicio():
    boton2.place(x=140, y=180)
    
    
    boton3.pack_forget()
    texto_pregunta.set("Hola! Bienvenido al trivia, puedes darle a continuar o si quieres puedes configurar la interfaz y el idioma (beta)")
    texto_boton_1.set("continuar")
    boton1.config(command=pregunta_random)
    texto_boton_2.set("configuracion")
    boton2.config(command=configuaracion)


#cuando acaban de verse todas las preguntas se viene aqui para preguntar al jugador si quiere volver a jugar si dice que si reestablece todo sino cierra la app
def volver_a_jugar():
    global preguntas_restantes
    global respuestas_correctas
    preguntas_restantes = [1, 2, 3, 4, 5, 6]
    respuestas_correctas = 0
    pregunta_random()
    return respuestas_correctas
    return preguntas_restantes

#si el usuario no deasea volver a jugar directamente cierra la app
def no_volver_a_jugar():
    quit()



#cuando acaban de verse todas las preguntas se viene aqui para preguntar al jugador si quiere volver a jugar si dice que si reestablece(funcion volver a jugar) todo sino cierra la app (funcion no volver a jugar)
def pregunta_random():                                         
    global respuestas_correctas
    global preguntas_restantes
    
    boton3.pack(side="bottom")

     # si no hay preguntas en la lista de preguntas restantes pregunta al jugador si quiere volver (o no) a jugar
    if not preguntas_restantes: 
        boton3.pack_forget()
        texto_pregunta.set("Has acertado %d preguntas quieres volver a jugar?" %respuestas_correctas)
        texto_boton_1.set("si")
        boton1.config(command=volver_a_jugar)         
        texto_boton_2.set("no")
        boton2.config(command=no_volver_a_jugar)
        

        


    else:                            #si hay cosas en el array elige aleatoriamente otra pregunta
        pregunta = random.choice(preguntas_restantes)
        if pregunta == 1:
            pregunta1()

        if pregunta == 2:
            pregunta_2()

        if pregunta == 3:
            pregunta_3()
        
        if pregunta == 4:
            pregunta_4()

        if pregunta == 5:
            pregunta_5()
        
        if pregunta == 6:
            pregunta_6()
    
    return respuestas_correctas
    return preguntas_restantes  #pone que el codigo no sirve, no lo borrare por si acaso ya que el codigo funciona




#si acierta la pregunta 1 le suma uno a la cuenta de las respuestas correcta, elimina la pregunta 1 de la lista de preguntas y escoge una pregunta aleatoria, lo mismo que las de las otras preguntas
def pregunta1_acertado():
    
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(1)
    pregunta_random()
    

#si falla la pregunta, la elimina de la cuenta de preguntas y escoge una pregunta random, lo mismo que las de las otras preguntas
def pregunta1_fallado():
    preguntas_restantes.remove(1)
    pregunta_random()



def pregunta2_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(2)
    pregunta_random()
    


def pregunta2_fallado():
    preguntas_restantes.remove(2)
    pregunta_random()



def pregunta3_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(3)
    pregunta_random()
    


def pregunta3_fallado():
    preguntas_restantes.remove(3)
    pregunta_random()


def pregunta1():                     #ejecuta la primera pregunta (explicacion codigo todas las preguntas)
    global respuestas_correctas                          #--Ya que la variable de las preguntas acertadas se comparte entre todas las funciones, tiene que saber el valor de esa variable la funcion
    
    lugar_imagenes.place(relwidth=1, relheight=1)
    boton2.place(x=160, y=180)
    texto_pregunta.set("En que año se fundó Facebook?")  #--Pone la pregunta en pantalla
    texto_boton_1.set("2014")                            #--Pone el texto del boton en pantalla
    boton1.config(command=pregunta1_fallado)             #--Le dice al boton que tiene que hacer al pulsarse, lo mismo con los demas
    texto_boton_2.set("2004")
    boton2.config(command=pregunta1_acertado)
    texto_boton_3.set("2008")
    boton3.config(command=pregunta1_fallado)
    
    
    return respuestas_correctas                         # Devuelve el valor de la variable para que otras variables lo utilizen






# Ejecuta la segunda pregunta, su estructura es igual a la primera
def pregunta_2():                             
    global respuestas_correctas
    boton2.place(x=160, y=180)
    texto_pregunta.set("Que beben las vacas?")
    texto_boton_1.set("Agua")
    boton1.config(command=pregunta2_acertado)
    texto_boton_2.set("Leche")
    boton2.config(command=pregunta2_fallado)
    texto_boton_3.set("Nada")
    boton3.config(command=pregunta2_fallado)
    
    
    return respuestas_correctas

# Ejecuta la tercera (espera eso existe?) pregunta, su estructura es igual a la primera
def pregunta_3():          
    global respuestas_correctas
    boton2.place(x=160, y=180)
    texto_pregunta.set("Cual es la capital de Suiza")
    texto_boton_1.set("Zurich")
    boton1.config(command=pregunta3_fallado)
    texto_boton_2.set("Ginibra")
    boton2.config(command=pregunta3_fallado)
    texto_boton_3.set("Berna")
    boton3.config(command=pregunta3_acertado)
    return respuestas_correctas



def pregunta4_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(4)
    pregunta_random()

def pregunta4_fallado():
    preguntas_restantes.remove(4)
    pregunta_random()

# Ejecuta la cuarta (quarta siempre en mi corazon) pregunta, su estructura es igual a la primera
def pregunta_4():          
    global respuestas_correctas
    boton2.place(x=160, y=180)
    texto_pregunta.set("Cual es el lugar mas frio del mundo?")
    texto_boton_1.set("Antartida")
    boton1.config(command=pregunta4_acertado)
    texto_boton_2.set("Siberia")
    boton2.config(command=pregunta4_fallado)
    texto_boton_3.set("Suecia")
    boton3.config(command=pregunta4_fallado)
    return respuestas_correctas




def pregunta5_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(5)
    pregunta_random()

def pregunta5_fallado():
    preguntas_restantes.remove(5)
    pregunta_random()

# Ejecuta la quinta (ojooo cinco preguntas) pregunta, su estructura es igual a la primera
def pregunta_5():          
    global respuestas_correctas
    boton2.place(x=120, y=180)
    texto_pregunta.set("De que estado es la isla de la ibertadad (dificil)") # es un tema bastante discutido ya que el estado de Nueva York y el de Nueva Jersey la reclaman
    texto_boton_1.set("Nueva Yersey")
    boton1.config(command=pregunta5_fallado)
    texto_boton_2.set("No es de ningun estado")
    boton2.config(command=pregunta5_fallado)
    texto_boton_3.set("Nueva York")
    boton3.config(command=pregunta5_acertado)
    return respuestas_correctas


def pregunta6_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(6)
    pregunta_random()

def pregunta6_fallado():
    preguntas_restantes.remove(6)
    pregunta_random()



def pregunta_6():          
    global respuestas_correctas
    boton2.place(x=135, y=180)
    texto_pregunta.set("Cual fue la segunda persona en pisar la luna? (pregunta troll)") # es un tema bastante discutido ya que el estado de Nueva York y el de Nueva Jersey la reclaman
    texto_boton_1.set("Buzz Aldrin")
    boton1.config(command=pregunta6_acertado)
    texto_boton_2.set("Neil Amstrong")
    boton2.config(command=pregunta6_fallado)
    texto_boton_3.set("Houston")
    boton3.config(command=pregunta6_fallado)
    return respuestas_correctas

inicio()




root.mainloop()