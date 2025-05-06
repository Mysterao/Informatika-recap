with open("knihy.txt", "r") as subor:
    n = subor.readlines()
    najpoziciavanejsia = ""
    akocasto = 0
    for i in range(1, len(n), 2):
        if len(n[i].strip().split())%2 == 1:
            print(n[i-1].strip())
        if len(n[i].strip().split()) >= akocasto:
            akocasto = len(n[i].strip().split())
            najpoziciavanejsia = n[i].strip()
    print("Najpoziciavanejsie knihy su : ", end = "")
    for i in range(1, len(n), 2):
        if len(n[i].strip().split()) == akocasto:
            print(n[i-1].strip(), end = ", ")
    print("\n")

    count = 1
    for i in range(1, len(n), 2):
        print(f"Kniha : {n[i-1]}", end="")
        list = []
        if len(n[i].strip().split())%2 == 0:
            for j in range(0, len(n[i].strip().split()), 2):
                jednakniha = []
                cislo2 = ""
                cislo1 = ""

                cislo2 += n[i].strip().split()[j+1][0]
                cislo2 += n[i].strip().split()[j+1][1]

                cislo1 += n[i].strip().split()[j][0]
                cislo1 += n[i].strip().split()[j][1]

                vypozicanie = int(cislo2) - int(cislo1)
                jednakniha.append(vypozicanie)
                jednakniha.append(f"Kniha {count}")
                list.append(jednakniha)
                count += 1
        if len(n[i].strip().split())%2 == 1:
            for j in range(0, len(n[i].strip().split())-1, 2):
                jednakniha = []
                cislo2 = ""
                cislo1 = ""

                cislo2 += n[i].strip().split()[j+1][0]
                cislo2 += n[i].strip().split()[j+1][1]

                cislo1 += n[i].strip().split()[j][0]
                cislo1 += n[i].strip().split()[j][1]

                vypozicanie = int(cislo2) - int(cislo1)
                jednakniha.append(vypozicanie)
                jednakniha.append(f"Kniha {count}")
                list.append(jednakniha)
            # list.append("Pocet nevratenych knih = 1")
                count += 1
        count = 1
        list.sort()
        print(*list)