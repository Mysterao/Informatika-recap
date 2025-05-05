import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

with open("trasa_linky_metra.txt", "r") as subor:
    n = subor.readlines()
    xline = 30
    for i in range(1, len(n)):
        textvnutri = n[i].strip()
        canvas.create_text(xline+20, 220, text=textvnutri, fill="black", font=('Helvetica 6'), angle = 45)
        if i != len(n)-1:
            canvas.create_rectangle(xline, 250, xline+20, 255, fill = "red", width = 0)
        if i == 1:
            canvas.create_rectangle(xline-2, 248, xline+7, 257, fill = "red", width = 1)
        if i == len(n)-1:
            canvas.create_rectangle(xline-2, 248, xline+7, 257, fill = "red", width = 1)
        if i != 1 and i != len(n)-1 and n[i][0] != "*":
            canvas.create_oval(xline-2, 248, xline+7, 257, fill = "red", width = 2, outline = "red")
        if n[i][0] == "*":
            canvas.create_oval(xline-2, 248, xline+7, 257, fill = "white", width = 2, outline = "red")
        xline += 20
    canvas.mainloop()