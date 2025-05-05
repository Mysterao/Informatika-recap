with open("hada.txt", "r") as subor:
    n = subor.readlines()
    print(len(n))
    najdlhsia = 0
    for i in range(len(n)):
        if len(n[i].strip()) >= najdlhsia:
            najdlhsia = len(n[i].strip())
    print(najdlhsia)

with open("kopia_hada.txt", "a") as subor:
    for i in range(len(n)):
        subor.write(n[i].strip()+"\n")

with open("komprimovana_kopia_hada.txt", "a") as subor:
    for i in range(len(n)):
        count = 0
        for j in range(1, len(n[i].strip())):
            count += 1
            if n[i][j] != n[i][j-1]:
                subor.write(n[i][j-1] + str(count))
                count = 0
        subor.write("\n")