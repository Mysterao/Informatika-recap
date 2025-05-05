import random
tipy = input("Zdajte svoj tip, cisla oddelene ciarkou :")
list = tipy.split(" ")
print(list)

with open("loteria_1.txt", "r") as subor:
    n = subor.read().strip().split()
    vyzrebovanecisla = []
    for i in range(6):
        cislo = random.randint(0, 90)
        vyzrebovanecisla.append(n[cislo])
    print(f"Vyzrebovane boli cisla : {vyzrebovanecisla}")
    count = 0
    for i in range(len(list)):
        if list[i] in vyzrebovanecisla:
            count += 1
            print(list[i])

# NEDOKONČENÉ !!!