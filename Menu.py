import SnakeTwo as st
import SnakeThree as sth
import tennis as tn
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Label
import  Racer as rc

def tennis():
    theApp = tn.App()
    theApp.on_execute()

def snake_game():
    theApp = st.App()
    theApp.on_execute()

def two_players():
    theApp = sth.App()
    theApp.on_execute()

def wookie_auditor():
    theApp = rc.App()
    theApp.on_execute()

def menu():
    root = Tk()
    root.title("Snake Game - Main Menu")
    #root.geometry("800x400")
    root.attributes('-fullscreen', TRUE)
    root.configure(background='white')

    img = ImageTk.PhotoImage(Image.open('bkg.png'))
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0, activebackground='green')
    filemenu.add_command(label="One Player", command=snake_game)
    filemenu.add_command(label="Two Players", command=two_players)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="Snake", menu=filemenu)
    auditormenu = Menu(menubar, tearoff=0, activebackground='green')
    auditormenu.add_command(label="Wookie Auditor", command=wookie_auditor)
    auditormenu.add_separator()
    auditormenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="Wookie", menu=auditormenu)
    temmismenu = Menu(menubar, tearoff=0, activebackground='green')
    temmismenu.add_command(label="Play Tennis", command=tennis)
    temmismenu.add_separator()
    temmismenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="Tennis Game", menu=temmismenu)
    exitmenu = Menu(menubar, tearoff=0, activebackground='red')
    exitmenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="Quit Gaming :(", menu=exitmenu)
    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    menu()