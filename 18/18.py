import random

kod = random.randint(10000000, 99999999)
stringkod = str(kod)
binary = ""

testcislo = 0
for i in range(4):
    testcislo += int(stringkod[i])
digit1 = str(testcislo%2)
binary += digit1

testcislo = 0
for i in range(2,6):
    testcislo += int(stringkod[i])
digit2 = str(testcislo%2)
binary += digit2

testcislo = 0
for i in range(4,8):
    testcislo += int(stringkod[i])
digit3 = str(testcislo%2)
binary += digit3

x = int(binary, 2)
print(kod, binary, x)

# Druha cast

originalcodes = []
mycodes = []
with open("kod_a.txt", "r") as subor:
    n = subor.readlines()
    for i in range(len(n)):
        originalcodes.append(n[i].strip())
    for i in range(len(n)):
        code = ""
        for j in range(len(n[i])-2):
            code += (n[i][j])
        mycodes.append(code)
        
    testcislo = 0
    for m in range(len(mycodes)):
        binary = ""
        for i in range(4):
            testcislo += int(mycodes[m][i])
        digit1 = str(testcislo%2)
        binary += digit1

        testcislo = 0
        for i in range(2,6):
            testcislo += int(mycodes[m][i])
        digit2 = str(testcislo%2)
        binary += digit2

        testcislo = 0
        for i in range(4,8):
            testcislo += int(mycodes[m][i])
        digit3 = str(testcislo%2)
        binary += digit3
        x = int(binary, 2)
        mycodes[m] += str(x)
        binary = ""
    
    for i in range(len(originalcodes)):
        if originalcodes[i] != mycodes[i]:
            print(originalcodes[i])
    # print("Mozes si pozriet originalne kody :", originalcodes)
    # print("Mozes si pozriet spravne kody :", mycodes)