import random
import tkinter
from tkinter import filedialog, Text  # importa todo lo necesario para gui, ya que todo funciona

preguntas_restantes = [1, 2, 3] #toma la cuenta de las preguntas restantes, si no hay nada se reinicia la cuenta
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

#inicia la pestaña de configuracion (esto sirve para cambiar el color de la interfaz y el idioma (no estoy seguro))
def configuaracion():
    texto_pregunta.set("Esta es la configuracion, donde puedes personalizar el juego y el idioma (no funcional)")
    texto_boton_1.set("Personalizacion")
    boton1.config(command=None) #de normal es personalizacion, none para no causar bugs hasta que se acabe personalizacion, funciona como pregunta_random()
    texto_boton_2.set("Idioma (no funcional)")
    boton2.config(command=None) #de normal es idioma, none porque a quien le apetece traducir un juego sin acabar?, funciona como configuracion()
    
#inicia lo primer que sale en pantalla al ejecutar el programa (da la opcion de continuar, Ejecuta pregunta_random o de la configuracion)
def inicio():
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
    preguntas_restantes = [1, 2, 3]
    respuestas_correctas = 0
    pregunta_random()
    return respuestas_correctas
    return preguntas_restantes

def no_volver_a_jugar():
    quit()



#cuando acaban de verse todas las preguntas se viene aqui para preguntar al jugador si quiere volver a jugar si dice que si reestablece(funcion volver a jugar) todo sino cierra la app (funcion no volver a jugar)
def pregunta_random():                                         
    global respuestas_correctas
    global preguntas_restantes
    boton3.pack(side="bottom")


    if not preguntas_restantes: 
        texto_pregunta.set("Has acertado %d preguntas quieres volver a jugar?" %respuestas_correctas)
        texto_boton_1.set("si")
        boton1.config(command=volver_a_jugar)         
        texto_boton_2.set("no")
        boton2.config(command=no_volver_a_jugar)
        texto_boton_3.set("")
        boton3.config(command=None)

        


    else:                            #si hay cosas en el array elige aleatoriamente otra pregunta
        pregunta = random.choice(preguntas_restantes)
        if pregunta == 1:
            pregunta1()

        if pregunta == 2:
            pregunta_2()

        if pregunta == 3:
            pregunta_3()
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
    
    texto_pregunta.set("En que año se fundó Facebook?")
    texto_boton_1.set("2014")
    boton1.config(command=pregunta1_fallado)
    texto_boton_2.set("2004")
    boton2.config(command=pregunta1_acertado)
    texto_boton_3.set("2008")
    boton3.config(command=pregunta1_fallado)
    
    
    return respuestas_correctas                         # Devuelve el valor de la variable para que otras variables lo utilizen







def pregunta_2():                             #ejecuta la segunda pregunta
    global respuestas_correctas
    texto_pregunta.set("Que beben las vacas?")
    texto_boton_1.set("Agua")
    boton1.config(command=pregunta2_acertado)
    texto_boton_2.set("Leche")
    boton2.config(command=pregunta2_fallado)
    texto_boton_3.set("Nada")
    boton3.config(command=pregunta2_fallado)
    
    
    return respuestas_correctas


def pregunta_3():          
    global respuestas_correctas
    
    texto_pregunta.set("Cual es la capital de Suiza")
    texto_boton_1.set("Zurich")
    boton1.config(command=pregunta3_fallado)
    texto_boton_2.set("Ginibra")
    boton2.config(command=pregunta3_fallado)
    texto_boton_3.set("Berna")
    boton3.config(command=pregunta3_acertado)
    return respuestas_correctas

inicio()




root.mainloop()