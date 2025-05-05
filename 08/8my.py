def prevod(original):
    rozdelene = original.split()
    cislo = rozdelene[0][::-1]

    allvalues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    count = 0
    for i in range(len(cislo)):
        count += allvalues.index(cislo[i])*(int(rozdelene[1])**i)
    print(f"({rozdelene[0]}){rozdelene[1]} = {count}")
with open("prevody.txt", "r") as subor:
    n = subor.readlines()
    for i in range(len(n)):
        prevod(n[i].strip())

# original = input("Input any number and its base : ")
# rozdelene = original.split()
# cislo = rozdelene[0][::-1]

# allvalues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# count = 0
# for i in range(len(cislo)):
#     count += allvalues.index(cislo[i])*(int(rozdelene[1])**i)
# print(f"({rozdelene[0]}){rozdelene[1]} = {count}")