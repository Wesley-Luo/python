import tkinter
root=tkinter.Tk()
root.title("maze")
root.geometry("612x612")
canvas=tkinter.Canvas(root,width=612,height=612,bg="red")
img=tkinter.PhotoImage(file="istockphoto-1097490360-612x612.png")
canvas.pack()
canvas.create_image  (306,306,image=img)
root.mainloop()