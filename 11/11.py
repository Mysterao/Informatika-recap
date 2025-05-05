import random

with open("obesenec.txt", "r") as subor:
    def vyberslova(n):
        m = n.readlines()
        list = []
        for i in range(len(m)):
            list.append(m[i].strip())
        # print(list)
        nahodneslovo = random.randint(0,len(list)-1)
        # print(list[nahodneslovo])
        slovohviezdy = []
        rozdeleneslovo = []
        for i in range(len(list[nahodneslovo])):
            rozdeleneslovo.append(list[nahodneslovo][i])
        for i in range(len(list[nahodneslovo])):
            slovohviezdy.append("*")
        n = ""
        for letter in slovohviezdy:
            print(f"{letter}", end="")
        print()
        count = 0
        while slovohviezdy != rozdeleneslovo:
            count += 1
            if count == 10:
                print("You lose ! The number o times you´ve guessed is more than 10")
                break
            n = input()
            if n in rozdeleneslovo:
                print(f"This letter is in the word ! ({n})")
                for idx, letter in enumerate(rozdeleneslovo):
                    if letter == n:
                        slovohviezdy[idx] = n
            else:
                print("This letter is not in the word !")
            for letter in slovohviezdy:
                print(f"{letter}", end="")
            print()
            if slovohviezdy == rozdeleneslovo:
                print("You win !")
    vyberslova(subor)