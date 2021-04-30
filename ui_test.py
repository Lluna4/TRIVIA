import tkinter as tk

root = tk.Tk()
root.title("test")

canvas = tk.Canvas(root, height=1280, width=720)
canvas.pack()

frame = tk.Frame(root, bg="pink")
frame.place(relwidth=1, relheight=0.2)

t = tk.StringVar()
t.set("adgajdhahdjavyegfu")

p = tk.Label(frame, textvariable=t, bg="pink")
p.config(font=("arial", 30))
p.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

tb1 = tk.StringVar()
tb1.set("test1")

def cerrar():
    quit()

b1 = tk.Button(canvas, textvariable=tb1, command=cerrar)
b1.config(font=("arial", 14))
b1.place(relx=0.5, rely=0.3, anchor=tk.CENTER, relwidth=0.1, relheight=0.05)





tk.mainloop()