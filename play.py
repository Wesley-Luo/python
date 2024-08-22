import tkinter
import random
root=tkinter.Tk() 
root.title("接接樂")
root.geometry("1000x500")
canvas=tkinter.Canvas(width=5000,height=2000,bg="skyblue")
imgcoin=tkinter.PhotoImage(file="coin.png")
imgplane=tkinter.PhotoImage(file="cat.png")
canvas.pack()
x=""
cy=0
locate=0
def mouse_move(e):
    global x,y
    x=e.x
    canvas.delete("plane")
    canvas.create_image(x,550,image=imgplane,tag="plane")
canvas.bind("<Motion>",mouse_move)


name=0
def main():
    global name,cy,x,locate
    name=name+1
    def coin():
        global name,cy
        cy=cy+5
        canvas.delete("coin")
        canvas.create_image(locate,cy,image=imgcoin,tag="coin")
        if not cy>=900 :
            root.after(10,coin)
        else:
            fall()

    def fall():
        global name,locate,cy
        cy=0
        locate=random.randint(0,1500)
        coin()
    fall()
main()
print(name)
root.mainloop()
