with open("stanovistia.txt", "r") as subor:
    n = subor.read().strip().split()

with open("pretekari.txt", "r") as subor:
    m = subor.readlines()
    casy = []
    for i in range(len(m)):
        cas = 0
        bool = True
        for j in range(len(n)):
            if n[j] not in m[i].strip().split()[2:]:
                bool = False
        if bool == True:
            print(f"Pretekar {m[i].strip().split()[0]} presiel vsetky stanovistia")
            cas += int(m[i].strip().split()[1].split(":")[0])
            cas += int(m[i].strip().split()[1].split(":")[1])/60
            casy.append(cas)
        if bool == False:
            print(f"Pretekar {m[i].strip().split()[0]} NEpresiel vsetky stanovistia")
            casy.append(1000)
    print()
    print(f"Vitaz je {m[casy.index(min(casy))].strip().split()[0]} s casom {min(casy)} min" + "\n")

    for i in range(len(n)):
        if casy[i] != 1000:
            print(f"Sutaziaci {m[i].strip().split()[0]} s casom {casy[i]} min")
        if casy[i] == 1000:
            print(f"Sutaziaci {m[i].strip().split()[0]} bol DISKVALIFIKOVANY ZA NEDOKONCENIE TRASY")