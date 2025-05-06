import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

with open("krizovka1-2.txt", "r") as subor:
    n = subor.readlines()
    y = 50
    bool = False
    for i in range(len(n)):
        textpismena = n[i].strip().split()[1][int(n[i][0])-1]
        x = 20
        canvas.create_rectangle(200, y, 220, 20+y, fill = "grey")
        canvas.create_text(210, y+10, text = textpismena)
        for j in range(1, len(n[i].strip())-1):
            odpocitaj = abs(int(n[i].strip().split()[0])-j)
            if j < int(n[i].strip().split()[0]):
                canvas.create_rectangle(200-20*odpocitaj, y, 220-20*odpocitaj, 20+y)
                canvas.create_text(210-20*odpocitaj, y+10, text = n[i].strip()[j+1])
            if j > int(n[i].strip().split()[0]):
                canvas.create_rectangle(200+20*odpocitaj, y, 220+20*odpocitaj, 20+y)
                canvas.create_text(210+20*odpocitaj, y+10, text = n[i].strip()[j+1])
            x += 20
        y += 20
canvas.mainloop()