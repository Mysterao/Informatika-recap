import tkinter
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

with open("krizovka1-1.txt", "r") as subor:
    n = subor.readlines()
    zoznam = []
    for i in range(len(n)):
        zoznam.append(n[i].split())
    print(zoznam)
    y = 0
    for i in range(len(zoznam)):
        canvas.create_rectangle(475, 200+y, 525, 250+y, width= 2, fill = "grey")
        canvas.create_text(500, 225+y, text = zoznam[i][1][int(zoznam[i][0])-1])
        y += 50
    y = 0
    for i in range(len(zoznam)):
        x = 0
        for j in range(1, len(zoznam[i][1])):
            if j < int(zoznam[i][0]):
                x += 50
                canvas.create_rectangle(475-x, 200+y, 525-x, 250+y, width=2, fill = "White")
                canvas.create_text(500-x, 225+y, text = zoznam[i][1][int(zoznam[i][0])-j-1], font=('Helvetica 10 bold'))
            if j == int(zoznam[i][0]):
                x = 50
                canvas.create_rectangle(475+x, 200+y, 525+x, 250+y, width=2, fill = "White")
                canvas.create_text(500+x, 225+y, text = zoznam[i][1][int(zoznam[i][0])+(j-int(zoznam[i][0]))], font=('Helvetica 10 bold'))
            if j > int(zoznam[i][0]):
                x += 50
                canvas.create_rectangle(475+x, 200+y, 525+x, 250+y, width=2, fill = "White")
                canvas.create_text(500+x, 225+y, text = zoznam[i][1][int(zoznam[i][0])+(j-int(zoznam[i][0]))], font=('Helvetica 10 bold'))
        y += 50
canvas.mainloop()