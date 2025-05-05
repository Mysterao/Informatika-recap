with open("jedla.txt", "r") as subor:
    n = subor.readlines()

print("Celkovy pocet jedal je :", len(n))
jedla = ["z", "c", "m", "h"]
pocetjedal = [0, 0, 0, 0]
for i in range(len(n)):
    riadok = n[i].strip().split()
    if riadok[1] in jedla:
        x = jedla.index(riadok[1])
        pocetjedal[x] += 1
print(*jedla)
print(*pocetjedal)

maloludi = []
for i in range(len(pocetjedal)):
    if pocetjedal[i] < 20:
        maloludi.append(jedla[i])
        print(f"Jedlo {jedla[i]} bolo objednané menej, ako 20 ludmi - {pocetjedal[i]}-krát")
for i in range(len(n)):
    if n[i].strip().split()[1] in maloludi:
        print(f"Musi byt upozorneny clovek : {n[i].strip().split()[0]}")