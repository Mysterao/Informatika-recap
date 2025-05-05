import tkinter as tk
import random
canvas = tk.Canvas(width=1000, height=1000)
canvas.pack()

delenec = random.randint(11,20)
delitel = random.randint(2,9)

priklad = f"{delenec} : {delitel} = "

canvas.create_text(500, 200, text = priklad, fill="black", font=('Helvetica 20 bold'))

entry = tk.Entry(canvas)
canvas.create_window(500, 350, window=entry, width=200)

def store_entry_value():
    x = 40
    list = ["blue", "red", "green", "brown", "black", "grey", "white", "navy", "lightgreen","black"]
    entry_value = entry.get()
    if entry_value.isdigit() == False:
        canvas.create_rectangle(400, 220, 600, 300, fill = "white")
        canvas.create_text(500, 250, text = "Invalid value", fill="black", font=('Helvetica 20 bold'))
    # print(f"Stored Entry: {entry_value}")
    number = int(entry_value)
    if number == delenec//delitel:
        canvas.create_rectangle(400, 220, 600, 300, fill = "white")
        canvas.create_text(500, 250, text = "Correct", fill="black", font=('Helvetica 20 bold'))
    if number != delenec//delitel:
        canvas.create_rectangle(400, 220, 600, 300, fill = "white")
        canvas.create_text(500, 250, text = "Wrong", fill="black", font=('Helvetica 20 bold'))
    cycle = 0
    for i in range(1, delenec+1-(delenec%delitel)):
        color = list[cycle]
        if i%delitel == 0:
            cycle += 1
        canvas.create_oval(x - 10, 400, x + 10, 420, fill = color)
        x += 30
    if delenec//delitel != 0:
        zostatok = delenec%delitel
        x = x+60
        for i in range(zostatok):
            canvas.create_oval(x - 10, 400, x + 10, 420, fill = "yellow")
            x += 30

button = tk.Button(canvas, text="Submit", font=("Arial", 12), command= store_entry_value)
canvas.create_window(500, 450, window=button, width=150)

canvas.mainloop()