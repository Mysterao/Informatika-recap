import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

def store_entry_value():
    canvas.delete("all")
    with open("anketa.txt", "r") as subor:
        n = subor.readlines()
        canvas.create_text(150, 100, text = n[0].strip(), font = "Helvetica 10")
        list = ["ano", "nie", "nvm"]

        maximalnecislo = 0
        for i in range(len(n[1].strip().split())):
            if int(n[1].strip().split()[i]) >= maximalnecislo:
                maximalnecislo = int(n[1].strip().split()[i])
        y = 0
        for i in range(len(n)+1):
            textanonie = f"{i+1}){list[i]} - {n[1].strip().split()[i]}"
            canvas.create_text(50, 140+y, text = textanonie)

            if int(n[1].strip().split()[i]) == maximalnecislo:
                color = "green"
            else:
                color = "red"
            canvas.create_rectangle(100, 130+y, 100+int(n[1].strip().split()[i])*4, 150+y, fill = color)
            y += 40
        button = tkinter.Button(canvas, text="Initiate", font=("Arial", 12), command= store_entry_value)
        canvas.create_window(100, 300, window=button, width=50)

button = tkinter.Button(canvas, text="Initiate", font=("Arial", 12), command= store_entry_value)
canvas.create_window(100, 300, window=button, width=50)

canvas.mainloop()