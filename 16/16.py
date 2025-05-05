with open("frekv.txt", "r") as subor:
    m = subor.readlines()
    listznakov = []
    pocetznakov = []
    for i in range(len(m)):
        if m[i][0] == " ":
            znak = " "
        else:
            znak = str(m[i].split()[0])
        listznakov.append(znak)
        
    for i in range(len(m)):
        if m[i][0] == " ":
            pocet = int(m[i].split()[0])
        else:
            pocet = int(m[i].split()[1])
        pocetznakov.append(pocet)
    print(listznakov)
    print(pocetznakov)
    
with open("sifro.txt", "r") as subor:
    m = subor.readlines()
    text = ""
    for i in range(len(m)):
        for j in range(len(m[i])):
                text += m[i][j].strip()
    print(text)
    result = ""

    for i in text:
        pismeno = text.count(i)
        if pismeno in pocetznakov:
            result += listznakov[pocetznakov.index(pismeno)]
    print(result)