with open("knihy.txt", "r") as subor:
    m = subor.readlines()
    for i in range(len(m)):
        riadok = m[i].strip().split()
        if len(riadok)%2 != 0 and i%2 == 1:
            print("Kniha", (i+1)//2, "musi dostat upomienku")
    najpoziciavanejsia = 0
    index = 0
    for i in range(1, len(m), 2):
        if len(m[i].strip().split()) >= najpoziciavanejsia:
            najpoziciavanejsia = len(m[i].strip().split())
            index = i-1
    print(m[index].strip())
    for i in range(1, len(m), 2):
        list = m[i].strip().split()