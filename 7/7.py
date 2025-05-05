import tkinter
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

with open("trasa_linky_metra.txt", "r") as subor:
    def metro(n):
        m = n.readlines()
        farba = ""
        width1 = 40
        width2 = 80
        text = 60
        for i in range(len(m[0])-1):
            farba += m[0][i]
        for i in range(len(m)-1):
            canvas.create_rectangle(width1, 500, width2, 505, fill = farba, width=0)
            if i == 0 or i == len(m)-2:
                canvas.create_rectangle(width1-5, 480, width2+5, 525, fill = farba)
            canvas.create_oval(text-2, 498, text+5, 507, fill = "red", width = 0)
            width1 += 40
            width2 += 40
            text += 40
        text = 100
        for i in range(1, len(m)):
            veta = ""
            for j in range(len(m[i])):
                if m[i][j] != "*":
                    veta += m[i][j]
            canvas.create_text(text, 470, text=veta, fill="black", font=('Helvetica 8'), angle = 45)
            if m[i][0] == "*":
                canvas.create_oval(text-40-2, 498, text-40+5, 507, fill = "white", width = 1)
            text += 40
            veta = ""
        canvas.mainloop()
    metro(subor)