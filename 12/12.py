import tkinter
# (a+b)-((a-b)*2)
# (aa))bb(
# (aa)())()(())bb

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

n = input()
list = []
for i in range(len(n)):
    list.append(n[i])

color = ["red", "blue", "green", "yellow", "brown", "lightblue"]
colorindex = 0
y = 0
zatvorky = []
for i in range(len(list)):
    if list[i] == "(" or list[i] == ")":
        zatvorky.append(list[i])
# print(zatvorky)

count = 0
for i in range(len(zatvorky)):
    if zatvorky[i] == "(":
        count += 1
    if zatvorky[i] == ")":
        count -= 1
    if count == -1:
        break
spravne = True
if count == 0 and zatvorky[len(zatvorky)-1] != "(":
    canvas.create_text(250, 200, text = "Vyraz je zatvorkovany spravne",  fill="Black", font=('Helvetica 20 bold'))
else:
    canvas.create_text(250, 200, text = "Vyraz je zatvorkovany nespravne",  fill="Black", font=('Helvetica 20 bold'))
    spravne = False

for i in range(len(list)):
    if spravne == True:
        if list[i] == "(":
            canvas.create_text(20+y, 150, text = list[i],  fill=color[colorindex], font=('Helvetica 20 bold'))
            colorindex += 1
            y += 20
            continue
        if list[i] == ")":
            colorindex -= 1
            canvas.create_text(20+y, 150, text = list[i],  fill=color[colorindex], font=('Helvetica 20 bold'))
            y += 20
            continue
    canvas.create_text(20+y, 150, text = list[i],  fill="black", font=('Helvetica 20 bold'))
    y += 20

canvas.mainloop()