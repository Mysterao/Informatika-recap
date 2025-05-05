import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

with open("spokojnost_1.txt", "r") as subor:
    n = subor.readlines()
    countnie = 0
    matrix = []
    for i in range(len(n)):
        listvsetkych = []
        if n[i].strip().split()[1] == "nie":
            countnie += 1
        listvsetkych.append(int(n[i].strip().split()[0][0:2]))
        listvsetkych.append(n[i].strip().split()[1])
        matrix.append(listvsetkych)
    print(f"Pocet nespokojnych zakaznikov : {countnie}")
    matrix.sort()
    matrix.append([0,0])

    hodina = 6
    hodinynie = []
    count = 0
    jedencas = []
    for i in range(1, len(matrix)):
        if matrix[i][1] == "nie":
            count += 1
        if matrix[i][0] != hodina:
            hodina = matrix[i-1][0]
            if count != 0:
                jedencas.append(matrix[i-1][0])
                jedencas.append(count)
                hodinynie.append(jedencas)
                jedencas = []
                count = 0
    print(hodinynie)
    matrix.pop(len(matrix)-1)

    najcastejsienie = 0
    index = 0
    for i in range(len(hodinynie)):
        if hodinynie[i][1] > najcastejsienie:
            najcastejsienie = hodinynie[i][1]
            index = i
    print(f"Hodina, pocas ktorej je najviac nespokojnych zakaznikov: {hodinynie[index][0]}, pocet zakaznikov: {hodinynie[index][1]}")

    x = 10
    for i in range(0, 24):
        if i == hodinynie[0][0]:
            canvas.create_rectangle(x, 450, x+20, 448-hodinynie[2][1]*10, fill = "red", width = 1)
            canvas.create_text(x+10, 460, text = i)
        else:
            canvas.create_rectangle(x, 450, x+20, 448, fill = "black")
            canvas.create_text(x+10, 460, text = i)
        x += 20
    canvas.mainloop()

    # NEFUNGUJE !!!!