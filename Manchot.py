from tkinter import *

def loadmap():
    r = 0
    file = open("Maps.txt", "r").read()
    for i in range(216):
            if file[i] != 200000000000000000000000000000000000000:
                print(str(file[i]))
                r += 1
    print("Résultat :", r)
    
    global glace
    for i in range(20):
        for j in range(10):
            elephant.create_image(100+50*i, 100+50*j, image=glace)

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

loadmap()

manchot_a = elephant.create_image(x, y, image=manchot_img[0])

elephant.bind_all("<Key>", deplace)

elephant.pack()
manchot.mainloop()
