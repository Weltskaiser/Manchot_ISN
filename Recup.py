from tkinter import *

def loadmap(x, y):
    file = open("Maps.txt", "r").read()

    global glace, manchot_img

    '''for i in range(20):
        for j in range(10):
            elephant.create_image(200+50*i, 200+50*j, image=glace)'''

    i = 0
    j = 0
    q = 0

    for p in range(235):
            if file[p] == " ":
                elephant.create_image(100+50*i, 100+50*j, image=glace)
                #print("rr", 100+50*i, 100+50*j, "rr")

            if file[p] == "|":
                q = 20
                #print("|", i, j)
            if q != 0:
                q -= 1
                i += 1
            if i == 20:
                i = 0
                j += 1

    #manchot_a = elephant.create_image(x, y, image=manchot_img[0])

def deplace(even):
    global x, y, i, manchot_img, manchot_a
    if even.keysym=="Right":
        x+=50
        i = 0
    elif even.keysym=="Left":
        x-=50
        i = 1
    elif even.keysym=="Up":
        y-=50
        i = 2
    elif even.keysym=="Down":
        y+=50
        i = 3
    elephant.delete(manchot_a)
    manchot_a = elephant.create_image(x, y, image=manchot_img[i])

x = 200
y = 200

manchot = Tk()
manchot.geometry("1200x700+0+0")
manchot.resizable(width=True, height=True)
manchot.title("Manchot")

elephant = Canvas(manchot, bg="cyan", width=1200, height=700)

manchot_img = [PhotoImage(file="Sans titre.png"), PhotoImage(file="Sans titre2.gif"),
                  PhotoImage(file="Sans titre3.gif"), PhotoImage(file="Sans titre4.gif")]
glace = PhotoImage(file="Glace.png")

loadmap(x, y)

elephant.bind_all("<Key>", deplace)

elephant.pack()
manchot.mainloop()
