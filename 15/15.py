with open("e.txt", "r") as subor:
    def jedla(n):
        m = n.readlines()
        print(len(m))
    jedla(subor)

with open("e.txt", "r") as subor:
    def jedla(n):
        m = n.readlines()
        zjedlo = []
        hjedlo = []
        mjedlo = []
        cjedlo = []
        countz = 0
        counth = 0
        countm = 0
        countc = 0
        for i in range(len(m)):
            if m[i][-2] == "z":
                countz += 1
            if m[i][-2] == "h":
                counth += 1
            if m[i][-2] == "m":
                countm += 1
            if m[i][-2] == "c":
                countc += 1
        print("Jedlo z", countz)
        print("Jedlo h", counth)
        print("Jedlo m", countm)
        print("Jedlo c", countc)
        
        variable = "fuck"
        if countz < 20:
            print("jedlo z sa neoplati pripravovat")
            variable = "z"
        if counth < 20:
            print("jedlo h sa neoplati pripravovat")
            variable = "h"
        if countm < 20:
            print("jedlo m sa neoplati pripravovat")
            variable = "m"
        if countc < 20:
            print("jedlo m sa neoplati pripravovat")
            variable = "c"
        
        list = []
        if variable != "fuck":
            for i in range(len(m)):
                    if m[i][-2] == variable:
                        person = int(m[i].split()[0])
                        list.append(person)
        print(list)
    jedla(subor)