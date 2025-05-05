import random

n = input()
list = []
slovo = ""

for i in range(len(n)):
    if n[i].isnumeric() == True:
        slovo += n[i]
    if n[i] == " " or n[i] == "":
        number = int(slovo)
        list.append(number)
        slovo = ""
print(list)

vyzrebovancisla = []
while len(vyzrebovancisla) != 6:
    a = random.randint(1, 50)
    if a not in vyzrebovancisla:
        vyzrebovancisla.append(a)
print("Vyzrebovane cisla su :", vyzrebovancisla)
print("")

count = 0
uhadnutecisla = []
for i in range(len(list)):
    if list[i] in vyzrebovancisla:
        uhadnutecisla.append(list[i])
        count += 1
print(f"Uhadnute cisla su :", uhadnutecisla)
print("Celkovo uhadnutych cisel", count)

with open("loteria_1.txt", "r") as subor:
    def pocet(n):
        m = n.readlines()
        count0 = 0
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        for i in range(len(m)):
            otherlist = []
            slovo = ""
            count = 0
            uhadnutecisla = []
            for j in range(len(m[i])):
                    if m[i][j].isnumeric() == True:
                        slovo += m[i][j]
                    if m[i][j] == " " or m[i][j] == "":
                        number = int(slovo)
                        otherlist.append(number)
                        slovo = ""
            for i in range(len(otherlist)):
                    if otherlist[i] in vyzrebovancisla:
                        uhadnutecisla.append(otherlist[i])
                        count += 1
            print(f"Uhadnute cisla su :", uhadnutecisla)
            print("Celkovo uhadnutych cisel", count)
            if count == 0:
                count0 += 1
            if count == 1:
                count1 += 1
            if count == 2:
                count2 += 1
            if count == 3:
                count3 += 1
            if count == 4:
                count4 += 1
            if count == 5:
                count5 += 1
            if count == 6:
                count6 += 1
        print("")
        print("Počet účastníkov s dobrými 0 číslom :", count0)
        print("Počet účastníkov s dobrými 1 číslom :", count1)
        print("Počet účastníkov s dobrými 2 číslami :", count2)
        print("Počet účastníkov s dobrými 3 číslami :", count3)
        print("Počet účastníkov s dobrými 4 číslami :", count4)
        print("Počet účastníkov s dobrými 5 číslami :", count5)
        print("Počet účastníkov s dobrými 6 číslami :", count6)
    print(pocet(subor))