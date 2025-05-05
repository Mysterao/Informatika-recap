import tkinter as tk
# canvas = tk.Canvas(height = 500, width = 500)
# canvas.pack()

with open("ciarovy_kod_3.txt", "r") as subor:
    n = subor.read().strip().split()
    x = 0
    count = 0
    for i in range(len(n)//4):
        canvas = tk.Canvas(height = 500, width = 500)
        canvas.pack()
        for k in range(4):
            count += 1
            for j in range(len(n[i])):
                canvas.create_rectangle(20+x, 20, 20+int(n[count][j])+x, 100, fill = "black")
                x += 12
            canvas.create_text(x-30, 110, text = n[count])
            x += 20
        x = 0
        canvas.mainloop()
    canvas = tk.Canvas(height = 500, width = 500)
    canvas.pack()
    for i in range(len(n)%4):
        count += 1
        for j in range(len(n[i])):
            canvas.create_rectangle(20+x, 20, 20+int(n[count-1][j])+x, 100, fill = "black")
            x += 12
        x += 20
        canvas.create_text(x-50, 110, text = n[count-1])
    canvas.mainloop()