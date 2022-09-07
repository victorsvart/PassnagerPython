import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from subprocess import call


def showInfo():
    root.destroy()
    call(["python", "GeneratorPage.py"])


root = tk.Tk()
root.title("Passnager")
root.geometry("1000x600")

root.configure(bg="#00B5C0")
canvas = Canvas(root,
                bg="#00B5C0",
                height=600,
                width=1000,
                bd=0,
                highlightthickness=0,
                relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"../assets/background.png")
background = canvas.create_image(500, 300, image=background_img)

entryPasskey_img = PhotoImage(file=f"../assets/TextBox.png")
entryPasskey_bg = canvas.create_image(501.0, 380.0, image=entryPasskey_img)

entryPasskey = Entry(bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
entryPasskey.place(x=350, y=370, width=300, height=20)

btnAdd = PhotoImage(file=f"../assets/button.png")
btn = Button(image=btnAdd,
             borderwidth=0,
             highlightthickness=0,
             command=showInfo,
             relief="flat")
btn.place(x=400, y=526, width=193, height=37)
root.resizable(False, False)
root.mainloop()
