import random
import tkinter
from tkinter import filedialog, Text  # importa todo lo necesario para gui, ya que todo funciona

preguntas_restantes = [1, 2, 3] #toma la cuenta de las preguntas restantes, si no hay nada se reinicia la cuenta
root = tkinter.Tk()
root.title("TEST")

canvas = tkinter.Canvas(root, height=1280, width=720)
canvas.pack()

preguntas = tkinter.Frame(root, bg="blue")
preguntas.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

texto_pregunta = tkinter.StringVar()
texto_pregunta.set("")

texto_boton_1 = tkinter.StringVar()
texto_boton_1.set("")

texto_boton_2 = tkinter.StringVar()
texto_boton_2.set("")

texto_boton_3 = tkinter.StringVar()
texto_boton_3.set("")


botonera = tkinter.Frame(root, bg="red")
botonera.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)

lugar_de_las_preguntas = tkinter.Label(preguntas, textvariable=texto_pregunta , bg="white", fg="black")
lugar_de_las_preguntas.pack(side="top")

boton1 = tkinter.Button(botonera, textvariable=texto_boton_1, bg="white", fg="black")
boton1.pack(side="top")

boton2 = tkinter.Button(botonera, textvariable=texto_boton_2, bg="white", fg="black")
boton2.pack(anchor=tkinter.CENTER)

boton3 = tkinter.Button(botonera, textvariable=texto_boton_3, bg="white", fg="black")
boton3.pack(side="bottom")



respuestas_correctas = 0  #toma la cuenta de las preguntas acertadas

    #abre el archivo de la maxima puntuacion



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




def pregunta_random():                                          #crea la pregunta random y cuando no quedan mas acaba el juego
    global respuestas_correctas
    global preguntas_restantes


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





def pregunta1_acertado():
    global respuestas_correctas
    respuestas_correctas += 1
    preguntas_restantes.remove(1)
    pregunta_random()
    


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

pregunta_random() #ejecuta la funcion de pregunta random




root.mainloop()