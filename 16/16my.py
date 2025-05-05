with open("frekv.txt", "r") as subor:
    n = subor.readlines()

frekvencia = []
for i in range(len(n)):
    riadok = []
    if i == 0:
        riadok.append(" ")
        riadok.append(int(n[i].strip().split()[0]))
    else:
        riadok.append(n[i].strip()[0])
        riadok.append(int(n[i].strip().split()[1]))
    frekvencia.append(riadok)
print(*frekvencia)

with open("sifro.txt", "r") as subor:
    m = subor.read().strip()

povodneznaky = []
sifra = []
for i in range(len(m)):
    for j in range(len(frekvencia)):
        if m[i] == "\n":
            continue
        if m.count(m[i]) == frekvencia[j][1]:
            print(frekvencia[j][0], end="")
            if m[i] == "\n":
                continue
            if m[i] not in povodneznaky:
                povodneznaky.append(m[i])
            if frekvencia[j][0] not in sifra:
                sifra.append(frekvencia[j][0])
print()
print(povodneznaky)
print(sifra)

with open("kluc.txt", "a") as subor:
    for i in range(len(povodneznaky)):
        riadok = f"{povodneznaky[i]} = {sifra[i]}"
        subor.write(riadok + "\n")