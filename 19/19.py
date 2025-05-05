with open("pretekari.txt", "r") as subor:
    m = subor.readlines()
    list = []
    with open("stanovistia.txt", "r") as stanovistia:
        n = stanovistia.readlines()
        for i in range(len(n)):
            string = ""
            for j in range(len(n[i])):
                string += n[i][j].strip()
            list.append(string)
    print(list)
    vitaz = []
    popnutivitazi = []
    for i in range(len(m)):
        riadok = m[i].strip().split()
        popnutivitazi.append(riadok[0])
        riadok.pop(0)
        riadok.pop(0)
        # print(riadok)
        bool = False
        for j in range(len(list)):
            if list[j] in riadok :
                bool = True
            if list[j] not in riadok:
                bool = False
                break
        if bool == False:
            print("Sutaziaci", i+1, "Nepresiel vsetky stanovistia")
            vitaz.append(0)
        if bool == True:
            print("Sutaziaci", i+1, "Presiel vsetky stanovistia")
            vitaz.append(1)
    print(vitaz)
    casy = []
    for i in range(len(m)):
        a = m[i][4] + m[i][5] + "." + m[i][7] + m[i][8]
        casy.append(float(a))
    print(casy)
    najrychlejsi = min(casy)
    if vitaz[casy.index(najrychlejsi)] == 1:
        print("Vitaz je", popnutivitazi[casy.index(najrychlejsi)])
    else:
        print("Vitaz bol diskvalifikovany")
    casy.sort()
    print(casy)