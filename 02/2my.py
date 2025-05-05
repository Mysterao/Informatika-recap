with open("hlasovanie_1.txt", "r") as subor:
    n = subor.readlines()
    print(len(n))

with open("5220.txt", "a") as subor:
    for i in range(len(n)):
        if n[i].strip() == "5220":
            subor.write(str(i+1) + "\n")
            
for i in range(5221, 5230):
    with open(str(i)+".txt", "a") as subor:
        for j in range(len(n)):
            if n[j].strip() == str(i):
                subor.write(str(j+1) + "\n")