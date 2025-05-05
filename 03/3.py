with open("hada.txt", "r") as subor:
    def krajiny(n):
        m = n.readlines()
        return len(m)
    print(krajiny(subor))
    
with open("hada.txt", "r") as subor:
    def kroky(n):
        max = 0
        m = n.readlines()
        for i in range(len(m)):
            c = len(m[i])
            if max <= c:
                max = c
        return max
    print(kroky(subor))

with open("hada.txt", "r") as subor:
    def kopia(n):
        m = n.readlines()
        t = open("kopia.txt", "a")
        for i in range(len(m)):
            t.write(m[i])
        t.close()
    kopia(subor)

with open("hada.txt", "r") as subor:
    def kopiakomprimovana(n):
        m = n.readlines()
        t = open("kopiakomprimovana.txt", "w")
        for i in range(len(m)):
            count = 0
            for j in range(len(m[i])-1):
                if m[i][j] != m[i][j+1]:
                    t.write(str(m[i][j]) + str(count))
                    count = 0
                count += 1
            t.write("\n")
        t.close()
    kopiakomprimovana(subor)