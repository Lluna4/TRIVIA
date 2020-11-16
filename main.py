import random
import tkinter
from tkinter import filedialog, Text  # importa todo lo necesario para gui, ya que todo funciona

preguntas_restantes = [1, 2, 3] #toma la cuenta de las preguntas restantes, si no hay nada se reinicia la cuenta


respuestas_correctas = 0  #toma la cuenta de las preguntas acertadas

archivo_puntuacion = open("puntuacion.txt", "a")     #abre el archivo de la maxima puntuacion


def pregunta_random():                                          #crea la pregunta random y cuando no quedan mas acaba el juego
    global respuestas_correctas
    global preguntas_restantes


    if not preguntas_restantes:          # si no hay cosas en el array de preguntas restantes ejecuta:

        print("has acertado %d preguntas" % respuestas_correctas)     # --Le dice al usuario las preguntas que ha acertado (se reformara con la gui)
        respuestas_correctas_str = str(respuestas_correctas)          # --Pasa a string las preguntas correctas para escribirlas en un archivo
        archivo_puntuacion.write(respuestas_correctas_str)            # --Escribe las preguntas correctas en un archivo
        print("Queres volver a jugar?")                              # --Pregunta al usuario si quiere continuar
        repetimos = input("")
        if repetimos == "si":                                         # --Si la respuesta es si entonces devuelve todas las preguntas al array
            preguntas_restantes = [1, 2, 3]
            pregunta_random()
            respuestas_correctas = 0


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










def pregunta1():                     #ejecuta la primera pregunta (explicacion codigo todas las preguntas)
    global respuestas_correctas                          #--Ya que la variable de las preguntas acertadas se comparte entre todas las funciones, tiene que saber el valor de esa variable la funcion
    print("En que año se fundó Facebook? ")              #--Pregunta la pregunta XD  
    respuesta1 = input()                                 #--Pilla la respuesta del usuario
    if respuesta1 == "2004":                             #--Si el usuario responde correctamente ejecuta:
        respuestas_correctas += 1                        #-- -Suma uno a las respuestas correctas
           

        preguntas_restantes.remove(1)                    #-- -Elimina esta pregunta del array de las preguntas restantes
        pregunta_random()                                #-- -Ejecuta la funcion para elegir otra pregunta (o acabar el juego)
    else:                                                #-- si el usuario no responde correctamente lo ejecuta lo de antes salvo que no suma uno a las preguntas acertadas 
        preguntas_restantes.remove(1)
        pregunta_random()



    return respuestas_correctas                         # Devuelve el valor de la variable para que otras variables lo utilizen







def pregunta_2():                             #ejecuta la segunda pregunta
    global respuestas_correctas
    print("Que beben las vacas?")
    respuesta2 = input()

    if respuesta2 == "Agua":
        respuestas_correctas += 1


        preguntas_restantes.remove(2)

        pregunta_random()
    else:
        preguntas_restantes.remove(2)
        pregunta_random()
    return respuestas_correctas


def pregunta_3():          
    global respuestas_correctas
    print("Cual es la capital de Suiza?")
    respuesta2 = input()

    if respuesta2 == "Berna":
        respuestas_correctas += 1


        preguntas_restantes.remove(3)

        pregunta_random()
    else:
        preguntas_restantes.remove(3)
        pregunta_random()
    return respuestas_correctas

pregunta_random() #ejecuta la funcion de pregunta random

archivo_puntuacion.close() #cierra el archivo de puntuacion


