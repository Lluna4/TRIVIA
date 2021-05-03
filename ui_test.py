import tkinter as tk
import os

root = tk.Tk()
root.geometry("720x1024")
root.title("test")


canvas = tk.Canvas(root, height=1024, width=720)
canvas.pack()

frame = tk.Frame(root, bg="pink")
frame.place(relwidth=1, relheight=0.2)

t = tk.StringVar()
t.set("adgajdhahdjavyegfu")

p = tk.Label(frame, textvariable=t, bg="pink")
p.config(font=("arial", 30))
p.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

v = tk.Label(canvas, text="hp=100")
v.config(font=("arial", 14))
v.place(relx=0.05, rely=0.18, relwidth=0.1, relheight=0.1)

texto_boton_1 = tk.StringVar()
texto_boton_1.set("dolor")

texto_boton_2 = tk.StringVar()
texto_boton_2.set("test2")

texto_boton_3= tk.StringVar()
texto_boton_3.set("test3")


def cerrar():
    ltroll = tk.Label(canvas, text="Has desbloqueado la puta")
    ltroll.pack(side=tk.TOP)
    os.startfile("C:/Riot Games/League of Legends/LeagueClient.exe")
    #quit()

boton1 = tk.Button(canvas, textvariable=texto_boton_1, command=cerrar)
boton1.config(font=("arial", 14))
boton1.place(relx=0.5, rely=0.325, anchor=tk.CENTER, relwidth=0.2, relheight=0.05)

boton2 = tk.Button(canvas, textvariable=texto_boton_2, command=cerrar)
boton2.config(font=("arial", 14))
boton2.place(relx=0.5, rely=0.525, anchor=tk.CENTER, relwidth=0.2, relheight=0.05)

boton3 = tk.Button(canvas, textvariable=texto_boton_3, command=cerrar)
boton3.config(font=("arial", 14))
boton3.place(relx=0.5, rely=0.725, anchor=tk.CENTER, relwidth=0.2, relheight=0.05)






tk.mainloop()