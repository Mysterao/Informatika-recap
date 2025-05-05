with open("hlasovanie_1.txt", "r") as subor:
    def krajiny(n):
        m = n.readlines()
        return len(m)
    print(krajiny(subor))

with open("hlasovanie_1.txt", "r") as subor:
    def pocet(n):
        m = n.readlines()
        t = open("5220.txt", "a")
        for i in range(len(m)):
            if m[i] == "5220\n":
                t.write(str(i+1) + "\n")
        t.close()
    pocet(subor)

with open("hlasovanie_1.txt", "r") as subor:
    def pocty(n):
        m = n.readlines()
        for i in range(5221, 5230):
            t = open(str(i)+".txt", "a")
            for j in range(len(m)):
                if m[j] == str(i)+"\n":
                    t.write(str(j+1) + "\n")
            t.close()
    pocty(subor)