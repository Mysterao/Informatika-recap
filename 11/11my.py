import random

with open("obesenec.txt", "r") as subor:
    n = subor.read().strip().split()
    index = random.randint(0, len(n)-1)
    uhadni = list(n[index])
    print(*uhadni, sep="")
    hviezdy = []
    for i in range(len(uhadni)):
        hviezdy.append("*")
    count = 0
    while hviezdy != uhadni:
        print(*hviezdy, sep="")
        n = input("Input your guess :")
        if n in uhadni:
            print("This letter is in the word")
            for i in range(len(uhadni)):
                    if uhadni[i] == n:
                        hviezdy[i] = n
        else:
             print("This letter is not in the word")
             count += 1
        if hviezdy == uhadni:
             print(*uhadni, sep="")
             print("Vyhral si !")
        if count == 10:
             print("You lose !")
             break