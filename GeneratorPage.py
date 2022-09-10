from multiprocessing.dummy import Manager
import tkinter as tk
from tkinter import *
from PasswordGenerator import *

root = tk.Tk()
root.title("Passnager")
root.geometry("1000x600")
root.configure(bg="#00B5C0")

Generator = tk.Frame(root, width=1000, height=600)
manager = tk.Frame(root, width=1000, height=600)


def showFrame(frame):
    frame.tkraise()


showFrame(Generator)

for frame in (Generator, manager):
    frame.grid(row=0, column=0, sticky="nsew")

################## GENERATOR ####################
canvas = Canvas(Generator,
                bg="#00B5C0",
                height=600,
                width=1000,
                bd=0,
                highlightthickness=0,
                relief="ridge")

canvas.place(x=0, y=0)

global background
background_img = PhotoImage(file=f"../assets/backgroundGenerator.png")
background = canvas.create_image(500, 300, image=background_img)

global generatedPassword_bg
generatedPassword_img = PhotoImage(file=f"../assets/TextBox.png")
generatedPassword_bg = canvas.create_image(180,
                                           380.0,
                                           image=generatedPassword_img)

text = Text(Generator, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
text.place(x=30, y=370, width=300, height=20)

btnAdd = PhotoImage(file=f"../assets/buttonGenerator.png")

btn2 = Button(Generator, text="Frame2", command=lambda: showFrame(manager))
btn2.place(x=0, y=0)

btnAdd = PhotoImage(file=f"../assets/buttonGenerator.png")
btn = Button(Generator,
             image=btnAdd,
             bg="#00B5C0",
             borderwidth=0,
             highlightthickness=0,
             command=lambda: GeneratePassword(),
             relief="flat")
btn.place(x=80, y=510)


def GeneratePassword():
    password = PasswordGeneration()
    text.delete("1.0", "end")
    for s in password:
        text.insert(tk.END, f"{s}")


################## MANAGER ####################

managerCanvas = Canvas(manager,
                       bg="#00B5C0",
                       height=600,
                       width=1000,
                       bd=0,
                       highlightthickness=0,
                       relief="ridge")
managerCanvas.place(x=0, y=0)

global manager_background
managerbackground_img = PhotoImage(
    file=f"../assets/manager/managerbackground.png")
manager_background = managerCanvas.create_image(500,
                                                300,
                                                image=managerbackground_img)

global passwordTextboxes
background_password = PhotoImage(file=f"../assets/manager/Textboxes.png")
passwordTextboxes = managerCanvas.create_image(500,
                                               400,
                                               image=background_password)

password1 = Text(manager, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
password1.place(x=350, y=277, width=300, height=20)

password2 = Text(manager, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
password2.place(x=350, y=333, width=300, height=20)

password3 = Text(manager, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
password3.place(x=350, y=390, width=300, height=20)

password4 = Text(manager, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
password4.place(x=350, y=450, width=300, height=20)

password5 = Text(manager, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
password5.place(x=350, y=505, width=300, height=20)

button = Button(manager, text="Back", command=lambda: showFrame(Generator))
button.place(x=0, y=0)

root.resizable(False, False)
root.mainloop()
