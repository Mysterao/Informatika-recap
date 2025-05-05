import random

with open("virus.txt", "r") as subor:
    n = subor.readlines()
    for i in range(len(n)):
        print(n[i].strip())
    print()
    list = []
    while len(list) != len(n):
        index = random.randint(0,len(n)-1)
        if index not in list:
            list.append(index)
    for i in range(len(n)):
        slovavriadkoch = random.randint(1,2)
        listslova = []
        if slovavriadkoch == 1:
            index = list[i]
            while len(n[i].strip().split()) != len(listslova):
                indexslova = random.randint(0, len(n[i].strip().split())-1)
                if indexslova not in listslova:
                    listslova.append(indexslova)
            for j in range(len(listslova)):
                indexslova = listslova[j]
                print(n[index].strip().split()[indexslova], end= " ")
        if slovavriadkoch == 2:
            index = list[i]
            print(n[index].strip())
    
    # HOVADINA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!