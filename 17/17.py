import random
import tkinter

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

# list = []
# for i in range(8):
#     if i == 0:
#         kod = random.randint(1,9)
#     else:
#         kod = random.randint(0,9)
#     list.append(kod)
    
# x = 200
# for i in range(len(list)):
#     if i == 0 or i == len(list)-1:
#         canvas.create_line(x, 200, x, 320, width=list[i],)
#     else:
#         canvas.create_line(x, 200, x, 280, width=list[i],)
#     x += 10

# string = ""
# for i in range(len(list)):
#     string += str(list[i])

# canvas.create_text(235, 300, text= string, font="Helvetica 11 bold")
# canvas.mainloop()

with open("ciarovy_kod_1.txt", "r") as subor:
    n = subor.readlines()
    list = []
    for i in range(len(n)):
        list.append(n[i].strip())
    print(list)
    
    x = 10
    for i in range(len(list)):
        for j in range(len(list[i])):
            if j == 0 or j == len(list[i])-1:
                canvas.create_line(x, 200, x, 320, width=int(list[i][j]))
            else:
                canvas.create_line(x, 200, x, 280, width=int(list[i][j]))
            x += 10
        canvas.create_text(x-45, 300, text= list[i], font="Helvetica 10 bold")
        if i%4 == 3:
            medzera = input("Hit space for new codes")
            if i%4 == 3 and medzera == " ":
                canvas.delete("all")
                x = -10
        x += 20
canvas.mainloop()