import random

with open("virus.txt", "r") as subor:
    def virus(n):
        m = n.readlines()
        print(len(m))
        print()
        t = open("virus_vystup.txt", "a")
        randomcislo = random.randint(1,2)
        if randomcislo == 1:
            list = []
            while len(list) != len(m):
                cislo = random.randint(0,len(m)-1)
                if cislo not in list:
                    list.append(cislo)
            for i in range(len(list)):  
                print(m[list[i]].strip())
                t.write(m[list[i]].strip() + "\n")
        else:
            for i in range(len(m)):
                print(m[i].strip())
                t.write(m[i].strip() + "\n")
        t.close()
        print()
    virus(subor)
    
with open("virus.txt", "r") as subor:
    def prehadzovanie(n):
        m = n.readlines()
        print()
        t = open("virus_vystup.txt", "a")
        for i in range(len(m)):
            slova = []
            slovo = ""
            for j in range(len(m[i])):
                if m[i][j] != " ":
                    slovo += m[i][j]
                if m[i][j] == " ":
                    otocslovo = random.randint(1,2)
                    if otocslovo == 2:
                        slova.append(slovo[::-1])
                    else:
                        slova.append(slovo)
                    slovo = ""
            list = []
            while len(list) != len(slova):
                cislo = random.randint(0,len(slova)-1)
                if cislo not in list:
                    list.append(cislo)
            randomcislo = random.randint(1,2)
            if randomcislo == 1:
                for j in range(len(slova)):
                    print(slova[list[j]].strip(), end = " ")
                    t.write(slova[list[j]].strip() + " ")
                t.write("\n")
            else:
                for j in range(len(slova)):
                    print(slova[list[j]].strip(), end = " ")
                    t.write(slova[list[j]].strip() + " ")
                t.write("\n")
            print()
        t.close()
        print()
    prehadzovanie(subor)