import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

with open("vystavba_na_ulici.txt", "r") as subor:
    n = subor.readlines()
    x = 5
    for i in range(len(n)):
        if int(n[i].strip().split()[1]) == 0:
            canvas.create_rectangle(x, 200, x+int(n[i].strip().split()[0]), 200-int(n[i].strip().split()[1]), fill = "green", outline="green", width = "2")
        if int(n[i].strip().split()[1]) != 0:
            canvas.create_rectangle(x, 200, x+int(n[i].strip().split()[0]), 200-int(n[i].strip().split()[1]), fill = "grey")
        x += int(n[i].strip().split()[0])
    
    def button_on_click():
        entry_value = int(entry.get())
        x = 5
        for i in range(1, len(n)):
            list = []
            if abs(int(n[i-1].strip().split()[1]) - int(n[i].strip().split()[1])) >= entry_value and int(n[i-1].strip().split()[1]) != 0 and int(n[i].strip().split()[1]) != 0:
                list.append(int(n[i-1].strip().split()[1]))
                list.append(int(n[i].strip().split()[1]))
                high = max(list)
                low = min(list)
                canvas.create_line(x+int(n[i-1].strip().split()[0]), 200-high, x+int(n[i-1].strip().split()[0]), 200-low, fill = "red", width="2")
            x += int(n[i-1].strip().split()[0])

    entry = tkinter.Entry(canvas)
    canvas.create_window(250, 220, window=entry, width=50)

    button = tkinter.Button(canvas, text="Submit", font=("Arial", 12), command= button_on_click)
    canvas.create_window(250, 250, window=button, width=50)
    

canvas.mainloop()