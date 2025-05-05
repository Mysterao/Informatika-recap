with open("meteo_stanice.txt", "r") as subor:
    n = subor.readlines()
    print(len(n))
    teploty = []
    for i in range(len(n)):
        print(n[i].strip().split()[3])
        teplotariadok = ""
        for j in range(len(n[i].strip().split()[3])):
            if n[i].strip().split()[3][j] == ",":
                teplotariadok += "."
            else:
                teplotariadok += n[i].strip().split()[3][j]
        teploty.append(float(teplotariadok))
    print()
    print(max(teploty))
    index = teploty.index(max(teploty))
    print(n[index].strip().split()[0])
    print(f"Priemerná teplota je : {sum(teploty)/len(teploty)}°C")