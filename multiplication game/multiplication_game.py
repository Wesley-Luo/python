#這是一個乘法遊戲
import tkinter
import pygame
import tkinter.messagebox
import random
import time
import os
pygame.mixer.init()
pygame.display.init()
tk = tkinter.Tk()
tk.title("乘法遊戲")
tk.geometry("1000x600")
tk.iconphoto(False,tkinter.PhotoImage(file=os.path.join("multiplication game","multiplication.png")))
tk.resizable(False,False)
cvs = tkinter.Canvas(tk,width=1000,height=600)
correct_sd = pygame.mixer.Sound(os.path.join("multiplication game","correct.wav"))
wrong_sd = pygame.mixer.Sound(os.path.join("multiplication game","wrong.wav"))
win_sd = pygame.mixer.Sound(os.path.join("multiplication game","Triumph.wav"))
lose_sd = pygame.mixer.Sound(os.path.join("multiplication game","Big_Boing.wav"))

win_img = tkinter.PhotoImage(file=os.path.join("multiplication game","math_win.png"))
lose_img = tkinter.PhotoImage(file=os.path.join("multiplication game","math_lose.png"))

score = 1
chance = 3
wait = True
pygame.mixer.music.load(os.path.join("multiplication game","multiplication_game_sd.wav"))

def draw_sc():
    global score,score_text,chance_text
    score_text = tkinter.Label(tk,text=str(score)+"/50",font=("Helvetica",(35)),fg="black")
    score_text.pack()
    chance_text = tkinter.Label(tk,text="chance: "+str(chance),font=("Helvetica",(35)))
    chance_text.pack()

def new_quest():
    global a,b,button,entry,text,entry_var
    a = random.randint(1,10)
    b = random.randint(1,10)

    text = tkinter.Label(tk,text=str(a)+"x"+str(b)+"=?",font=("Helvetica",(150)),bg=random.choice(["light blue","yellow","brown"]))
    text.pack()

    entry_var = tkinter.StringVar()
    entry = tkinter.Entry(textvariable=entry_var,font=("Helvetica",(50)),fg="black",bg=random.choice(["light green","pink","grey"]))
    entry.pack()
    entry.focus()
    entry.get()

    button = tkinter.Button(font=("Helvetica",(50)),command=update,text="submit",bg=random.choice(["red","orange","purple"]))
    button.pack()

def alldestroy():
    global text,entry,button,score_text,chance_text
    text.destroy()
    entry.destroy()
    button.destroy()
    score_text.destroy()
    chance_text.destroy()

def update():
    global score,chance_text,chance,entry_var
    value = entry.get()
    if value != "" and ("1" in value or "2" in value or "3" in value or "4" in value or "5" in value or "6" in value or "7" in value or "8" in value or "9" in value or "0" in value):
        if str(value) == str(a*b):
            correct_sd.play()
            score += 1
            tkinter.messagebox.showinfo(title='"Correct" answer:',message=f'✅Your answer is "right" ,{str(a)} x {str(b)} = {str(a*b)}.')
            time.sleep(0.5)
        else:
            wrong_sd.play()
            chance -= 1
            tkinter.messagebox.showinfo(title='"Wrong" answer:',message=f'❎Your answer is "wrong" ,{str(a)} x {str(b)} = {str(a*b)}.')
            time.sleep(0.5)
        alldestroy()
        
        if chance < 0 or score > 50:
            if score > 50:
                alldestroy()
                cvs.create_image(500,300,image=win_img)
                cvs.pack()
                cvs.update()
                win_sd.play()
            else:
                alldestroy()
                cvs.create_image(500,300,image=lose_img)
                cvs.pack()
                cvs.update()
                lose_sd.play()
            time.sleep(3)
            tk.destroy()
            exit()

        new_quest()
        draw_sc()
    else:
        tkinter.messagebox.showerror(title="Please enter numbers",message="Please enter numbers.")
        entry_var.set("")

pygame.mixer.music.play(-1)

tk.bind("<Return>",update)
new_quest()
draw_sc()
tk.mainloop()