import tkinter.messagebox
import tkinter
import math
root = tkinter.Tk()
img = ""
root.title("move")
root.geometry("2000x900")
canvas = tkinter.Canvas(root, width=2000, height=900, bg="skyblue")
canvas.pack()
img=tkinter.PhotoImage(file="istockphoto-1097490360-60x60.png")

#def circle():
    #if scan <= r1 + r2:
    #    return True
    #return False

mx=150

# def move():
#     global img
#     global mx, my
#     if key == "Up":
#        my = my-10
#     if key == "Down":
#         my = my+10
#     if key == "Right": 
#         img=tkinter.PhotoImage(file="istockphoto-1097490360-60x60.png")
#         mx = mx+10
#     if key == "Left":
#         img=tkinter.PhotoImage(file="istockphoto-1097490360-60x60.left.png")
#         mx = mx-10
#     canvas.delete("cc")
#     canvas.create_image(mx,my,image=img,tag="cc")
#     #canvas.create_image(mx,my,image=coin,tag="coin")
#     root.after(50, move)
# root.bind("<KeyPress>", key_down)
# root.bind("<KeyRelease>", key_up)


def mouse_move(e):
    global x1, y1
    x1 = e.x
    y1 = e.y
canvas.bind("<Motion>", mouse_move)

#move()
root.mainloop()
