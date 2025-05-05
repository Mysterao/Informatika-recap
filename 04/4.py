with open("meteo_stanice.txt", "r") as subor:
    def pocet(n):
        m = n.readlines()
        return len(m)
    print(pocet(subor))

with open("meteo_stanice.txt", "r") as subor:
    def teploty(n):
        m = n.readlines()
        teploty = ""
        for i in range(len(m)):
            for j in range(21, 26):
                teploty += str(m[i][j])
            print(teploty)
            teploty = ""
    teploty(subor)

with open("meteo_stanice.txt", "r") as subor:
    def teploty(n):
        m = n.readlines()
        teploty = []
        jedna = ""
        for i in range(len(m)):
            if m[i][21] == "+":
                for j in range(22, 26):
                    if j == 24:
                        jedna += str(m[i][j]).replace(",", ".")
                    else:
                        jedna += str(m[i][j])
                float(jedna)
                teploty.append(jedna)
                jedna = ""
        # print(teploty)
        bruh = max(teploty)
        return bruh
    haha = teploty(subor)
    print("Najvyššia teplota je", haha)

with open("meteo_stanice.txt", "r") as subor:
    def station(n):
        m = n.readlines()
        vsetkyteploty = []
        jedna = ""
        for i in range(len(m)):
            if m[i][21] == "+" or m[i][21] == "-":
                for j in range(22, 26):
                    if j == 24:
                        jedna += str(m[i][j]).replace(",", ".")
                    else:
                        jedna += str(m[i][j])
                float(jedna)
                vsetkyteploty.append(jedna)
                jedna = ""
        b = vsetkyteploty.index(haha)
        print("Teplota bola nameraná okolo stanice", m[b][0] + m[b][1] + m[b][2])
    station(subor)

with open("meteo_stanice.txt", "r") as subor:
    def averageofall(n):
        m = n.readlines()
        total = 0
        for i in range(len(m)):
            jedna = ""
            if m[i][21] == "+" or m[i][21] == "-":
                for j in range(22, 26):
                    if j == 24:
                        jedna += str(m[i][j]).replace(",", ".")
                    else:
                        jedna += str(m[i][j])
            if m[i][21] == "+":
                total += float(jedna)
            else:
                total -= float(jedna)
            jedna = ""
        average = total/len(m)
        print("Priemerná teplota je", average, "°C")
    averageofall(subor)