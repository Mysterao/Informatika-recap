import tkinter

with open("spokojnost_1.txt", "r") as subor:
    def spokojnosti(n):
        m = n.readlines()
        hodnotenie = ""
        countano = 0
        countnie = 0
        for i in range(len(m)):
            for j in range(6, 9):
                hodnotenie += m[i][j]
            if hodnotenie == "ano":
                countano += 1
                hodnotenie = ""
            if hodnotenie == "nie":
                countnie += 1
                hodnotenie = ""
        print(countnie, "nespokojnych zakaznikov")
        print(countano, "spokojnych zakaznikov")
    spokojnosti(subor)
    
with open("spokojnost_1.txt", "r") as subor:
    def nespokojni(n):
        m = n.readlines()
        hodnotenie = ""
        list = []
        for i in range(len(m)):
            for j in range(6, 9):
                hodnotenie += m[i][j]
            if hodnotenie == "nie":
                a = m[i][0] + m[i][1]
                cislo = int(a)
                list.append(cislo)
            hodnotenie = ""
        hodina  = max(list, key=lambda x: list.count(x))
        pocetnie = list.count(hodina)
        print(list)
        print("Pocas tejto hodiny je najmenej spokojných zákazníkov :", hodina)
        print("Pocet nespokojnych zakaznikov :", pocetnie)
    nespokojni(subor)

with open("spokojnost_1.txt", "r") as subor:
    def nespokojnihodiny(n):
        m = n.readlines()
        listhodin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        hodnotenie = ""
        list = []
        for i in range(len(m)):
            for j in range(6, 9):
                hodnotenie += m[i][j]
            if hodnotenie == "nie":
                a = m[i][0] + m[i][1]
                cislo = int(a)
                list.append(cislo)
            hodnotenie = ""
        print("Pocet nespokojnych zakaznikov na hodiny :")
        for i in range(len(listhodin)):
            if listhodin[i] in list:
                print(f"Hodina dna : {listhodin[i]}, Pocet nespokojnych zakaznikov: {list.count(listhodin[i])}")
    nespokojnihodiny(subor)

with open("spokojnost_1.txt", "r") as subor:
    def nespokojnihodiny(n):
        m = n.readlines()
        canvas = tkinter.Canvas(width=520, height=480)
        canvas.pack()
        listhodin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        hodnotenie = ""
        list = []
        for i in range(len(m)):
            for j in range(6, 9):
                hodnotenie += m[i][j]
            if hodnotenie == "nie":
                a = m[i][0] + m[i][1]
                cislo = int(a)
                list.append(cislo)
            hodnotenie = ""
        sirka2 = 10
        for i in range(0,24):
            canvas.create_text(sirka2, 470, text=i, fill="black", font=('Helvetica 5 bold'))
            sirka2 += 22
        sirka1 = 0
        sirka2 = 22
        for i in range(len(listhodin)):
            amountheight = list.count(listhodin[i])*10
            canvas.create_rectangle(sirka1, 459-amountheight, sirka2, 460, fill = "red", width=2)
            sirka1 += 22
            sirka2 += 22
        canvas.mainloop()
    nespokojnihodiny(subor)