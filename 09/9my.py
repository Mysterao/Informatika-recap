import random
import tkinter

canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

delenec = random.randint(11, 20)
delitel = random.randint(2, 9)
priklad = f"{delenec} : {delitel} ="

entry = tkinter.Entry(canvas)
canvas.create_window(100, 200, window=entry, width=50)
farby = ["blue", "black", "green", "red", "yellow", "purple", "pink", "orange", "navy", "grey"]

def store_entry_value():
    entry_value = int(entry.get())
    if entry_value == delenec//delitel:
        canvas.create_text(300, 100, text = "Správne !", font = "Helvetica 20")
    else:
        canvas.create_text(300, 100, text = "Nesprávne !", font = "Helvetica 20")
    canvas.create_text(200, 100, text = delenec//delitel, font = "Helvetica 30")

    color = 0
    x = 10
    pocetrealnychguliciek = delenec-(delenec%delitel)
    for i in range(pocetrealnychguliciek):
        if i%delitel == 0:
            color += 1
        canvas.create_oval(x, 150, x+10, 160, fill = farby[color])
        x += 20

    x += 20
    for i in range(delenec%delitel):
        canvas.create_oval(x, 150, x+10, 160, fill = "yellow")
        x += 20

button = tkinter.Button(canvas, text="Submit", font=("Arial", 12), command= store_entry_value)
canvas.create_window(100, 240, window=button, width=50)
canvas.create_text(100, 100, text = priklad, font = "Helvetica 30")
canvas.mainloop()