import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()
# (a+b)-((a-b)*2)
# (aa))bb(
# (aa)())()(())bb

vyraz = input("Pridajte zatvorkovy vyraz :")
colorslist = ["blue", "red", "green", "yellow", "orange", "purple", "brown"]

x = 0
count = 0
spravne = True
for i in range(len(vyraz)):
    if vyraz[i] == "(":
        color = colorslist[count]
        canvas.create_text(50+x, 80, text = vyraz[i], fill = color, font="Helvetica 20")
        count += 1
    if vyraz[i] == ")":
        count -= 1
        color = colorslist[count]
        canvas.create_text(50+x, 80, text = vyraz[i], fill = color, font="Helvetica 20")
    if count == -1:
        spravne = False
    if vyraz[i] != ")" and vyraz[i] != "(":
        canvas.create_text(50+x, 80, text = vyraz[i], fill = "black", font="Helvetica 20")
    x += 20


if spravne == True:
    canvas.create_text(150, 120, text = "Zátvorkovanie je správne", fill = "black", font="Helvetica 15")
if spravne == False:
    canvas.create_text(150, 120, text = "Zátvorkovanie je nesprávne", fill = "black", font="Helvetica 15")
canvas.mainloop()