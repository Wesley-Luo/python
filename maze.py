import tkinter.messagebox
import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

mx = 1
my = 1

def move():
    global mx, my
    if key == "Up" and maze[my-1][mx] == 0:
       my = my-1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my+1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx+1
    if key == "Left" and maze[my+1][mx-1] == 0:
        mx = mx-1
    create()
    root.after(200, move)

root = tkinter.Tk()
img = ""
root.title("maze")
root.geometry("2000x5000")
canvas = tkinter.Canvas(root, width=2000, height=5000, bg="white")
a = 100
canvas.pack()
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]   
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*a, y*a, x*a+a, y*a+a, fill="blue")


def create():
    global img
    global mx, my
    canvas.delete("PH")
    canvas.create_image(mx*80, my*80, image=img, tag='PH')


root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
move()

img = tkinter.PhotoImage(file="coin.png")
canvas.create_image(mx*100, my*100, image=img, tag='PH')
root.mainloop()
