import tkinter
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

with open("vystavba_na_ulici.txt", "r") as subor:
    def vyberslova(n):
        m = n.readlines()
        x = [0]
        y = [0]
        for i in range(len(m)):
            hodnota = ""
            for j in range(len(m[i])):
                if m[i][j] != " ":
                    hodnota += m[i][j]
                else:
                    cislo = int(hodnota)
                    x.append(cislo)
                    index = j
                    hodnota = ""
                    break
            for j in range(j+1, len(m[i])):
                if m[i][j].isdigit() == True:
                    hodnota += m[i][j]
                else:
                    cislo = int(hodnota)
                    y.append(cislo)
                    hodnota = ""
                    break
        sirka = 10
        for i in range(len(y)-1):
            if y[i+1] == 0:
                canvas.create_rectangle(sirka, 500, sirka+x[i+1], 500-2, fill = "green", outline="lightgreen")
            else:
                canvas.create_rectangle(sirka, 500, sirka+x[i+1], 500-y[i+1], fill = "grey", outline="black")
            sirka += x[i+1]
            
        def store_entry_value():
            value = entry.get()
            convertedvalue = int(value)
            sirka = 10
            for i in range(len(y)-1):
                if abs(y[i] - y[i+1]) >= convertedvalue and y[i] != 0 and y[i+1] != 0:
                    canvas.create_line(sirka+x[i], 500-y[i], sirka+x[i], 500-y[i+1], fill = "red")
                sirka += x[i]
        
        entry = tkinter.Entry(canvas)
        canvas.create_window(700, 350, window=entry, width=200)
        
        button = tkinter.Button(canvas, text="Submit", font=("Arial", 12), command= store_entry_value)
        canvas.create_window(700, 450, window=button, width=150)
        
    vyberslova(subor)
canvas.mainloop()