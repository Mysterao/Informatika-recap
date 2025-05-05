with open("prevody.txt", "r") as subor:
    def sustavy(n):
        m = n.readlines()
        slovocislo = ""
        spolu = 0
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        # -2, lebo je to sracka, \n
        for i in range(len(m)):
            if m[i][len(m[i])-2] == "2":
                for j in range(len(m[i])):
                    slovocislo += m[i][j]
                slovocislo = str(slovocislo[:len(m[i])-3])
                print(slovocislo)
                nasobok = len(slovocislo)
                for k in range(len(slovocislo)):
                    integer = int(slovocislo[k])
                    spolu += integer*(2**(nasobok-1))
                    nasobok -= 1
                print(f"({spolu}) 2")
                spolu = 0
                slovocislo = ""
            if m[i][len(m[i])-2] == "8":
                for j in range(len(m[i])):
                    slovocislo += m[i][j]
                slovocislo = str(slovocislo[:len(m[i])-3])
                print(slovocislo)
                nasobok = len(slovocislo)
                for k in range(len(slovocislo)):
                    integer = int(slovocislo[k])
                    spolu += integer*(8**(nasobok-1))
                    nasobok -= 1
                print(f"({spolu}) 8")
                spolu = 0
                slovocislo = ""
            if m[i][len(m[i])-2] == "6":
                for j in range(len(m[i])):
                    slovocislo += m[i][j]
                slovocislo = str(slovocislo[:len(m[i])-4])
                print(slovocislo)
                nasobok = len(slovocislo)
                for k in range(len(slovocislo)):
                    if slovocislo[k] in list:
                        integer = list.index(slovocislo[k])
                    spolu += integer*(16**(nasobok-1))
                    nasobok -= 1
                print(f"({spolu}) 16")
                spolu = 0
                slovocislo = ""
    sustavy(subor)