with open("skok_do_dialky.txt", "r") as subor:
    n = subor.readlines()
    zoznamkrajin = []
    for i in range(len(n)):
        riadok = n[i].strip().split()
        if riadok[1] not in zoznamkrajin:
            zoznamkrajin.append(riadok[1])
    print(f"Krajiny, zastúpené v skokoch : {zoznamkrajin}")
    for i in range(len(zoznamkrajin)):
        count = 0
        for j in range(len(n)):
            if zoznamkrajin[i] in n[j]:
                count += 1
        print(zoznamkrajin[i], "-", count)
    
    celkovebody = []
    for i in range(len(n)):
        jeden = []
        riadok = n[i].strip().split()
        jeden.append(riadok[0])
        jeden.append(int(riadok[2])+int(riadok[3])+int(riadok[4])+int(riadok[5])+int(riadok[6]))
        celkovebody.append(jeden)
    print(*celkovebody)

    vitaz = 0
    indexvitaza = []
    index = 0
    for i in range(len(celkovebody)):
        if vitaz < celkovebody[i][1]:
            vitaz = celkovebody[i][1]
            indexvitaza = celkovebody[i]
            index = i
    print(*indexvitaza)
    celkovebody.pop(index)
    for i in range(len(celkovebody)):
        if celkovebody[i][1] == indexvitaza[1]:
            print(*celkovebody[i])