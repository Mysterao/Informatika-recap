import random

ciarovykod = str(random.randint(10000000, 99999999))
bity = ""
bity += str(int((ciarovykod[0]+ciarovykod[1]+ciarovykod[2]+ciarovykod[3]))%2)
bity += str(int((ciarovykod[2]+ciarovykod[3]+ciarovykod[4]+ciarovykod[5]))%2)
bity += str(int((ciarovykod[4]+ciarovykod[5]+ciarovykod[6]+ciarovykod[7]))%2)
kod = str(int(bity, 2))
ciarovykod += kod
print(ciarovykod + "\n")

with open("kod_a.txt", "r") as subor:
    n = subor.read().strip().split()
    for i in range(len(n)):
        bity = ""
        bity += str(int((n[i][0]+n[i][1]+n[i][2]+n[i][3]))%2)
        bity += str(int((n[i][2]+n[i][3]+n[i][4]+n[i][5]))%2)
        bity += str(int((n[i][4]+n[i][5]+n[i][6]+n[i][7]))%2)
        kod = int(bity, 2)
        if int(n[i][8]) != kod:
            print(n[i])