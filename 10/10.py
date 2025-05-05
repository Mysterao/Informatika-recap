import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

with open("anketa.txt", "r") as subor:
    def anketa(n):
        m = n.readlines()
        slovocislo = ""
        canvas.create_text(250,60, text = m[0])
        count = 0
        y = 100
        ysquare = 120
        odpovede = ["", "Áno", "Nie", "Neivem"]
        pocet = []
        for i in range(len(m[1])):
            if m[1][i] != " ":
                slovocislo += m[1][i]
            if m[1][i] == " ":
                count += 1
                textinside = f"{count}) {odpovede[count]} - {slovocislo}"
                canvas.create_text(150, y, text = textinside)
                pocet.append(int(slovocislo))
                y += 20
                slovocislo = ""
        def pridaj():
            canvas.delete(all)
            for i in range(len(pocet)):
                x = pocet[i]
                maximum = max(pocet)
                if i == pocet.index(maximum):
                    canvas.create_rectangle(200, ysquare-25, 200+(x*5), ysquare-15, fill = "Green", width = 0)
                    button = tkinter.Button(canvas, bg = "green", height=0, command = pridaj)
                    canvas.create_window(400, ysquare-25, window=button, width=10)
                else:
                    canvas.create_rectangle(200, ysquare-25, 200+(x*5), ysquare-15, fill = "Red", width = 0)
                    button = tkinter.Button(canvas, bg = "red", height=0)
                    canvas.create_window(400, ysquare-25, window=button, width=10)
                ysquare += 20
            
        for i in range(len(pocet)):
                x = pocet[i]
                maximum = max(pocet)
                if i == pocet.index(maximum):
                    canvas.create_rectangle(200, ysquare-25, 200+(x*5), ysquare-15, fill = "Green", width = 0)
                    button = tkinter.Button(canvas, bg = "green", height=0, command = pridaj)
                    canvas.create_window(400, ysquare-25, window=button, width=10)
                else:
                    canvas.create_rectangle(200, ysquare-25, 200+(x*5), ysquare-15, fill = "Red", width = 0)
                    button = tkinter.Button(canvas, bg = "red", height=0)
                    canvas.create_window(400, ysquare-25, window=button, width=10)
                ysquare += 20
    anketa(subor)

canvas.mainloop()