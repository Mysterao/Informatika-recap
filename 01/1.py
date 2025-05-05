menosuboru = input()

with open(menosuboru, "r") as subor:
    def krajiny(n):
        list1 = []
        m = n.readlines()
        string = ""
        for i in range(len(m)):
            count = 0
            for j in range(len(m[i])):
                if m[i][j] == " ":
                    count += 1
                if count == 1:
                    string += m[i][j+1]
                if count == 2:
                    list1.append(string)
                    string = ""
                    break
        return list1
    newcountries = krajiny(subor)
    print(newcountries)

with open(menosuboru, "r") as subor:
    def score(n):
        m = n.readlines()
        list = []
        for i in range(len(m)):
            total = 0
            nasobok = 100
            for j in range(len(m[i])):
                if nasobok == 0.1:
                    nasobok = 100
                if m[i][j].isdigit() == True:
                    total += int(m[i][j])*nasobok
                    nasobok /= 10
            list.append(total)
        return list
    newlist = score(subor)
    print(newlist)

fck = max(newlist)
a = newlist.index(fck)
print(newcountries[a])

# skok_do_dialky.txt

numberofcountries = []
for i in range(len(newcountries)):
    if newcountries[i] not in numberofcountries:
        numberofcountries.append(newcountries[i])
print(numberofcountries)
        
for i in range(len(numberofcountries)):
    a = newcountries.count(numberofcountries[i])
    print(numberofcountries[i], a)