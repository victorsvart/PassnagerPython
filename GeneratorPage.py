import tkinter as tk
from tkinter import *
from tkinter import ttk
from PasswordGenerator import *

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

background_img = PhotoImage(file=f"../assets/backgroundGenerator.png")
background = canvas.create_image(500, 300, image=background_img)

generatedPassword_img = PhotoImage(file=f"../assets/TextBox.png")
generatedPassword_bg = canvas.create_image(180,
                                           380.0,
                                           image=generatedPassword_img)
text = Text(root, bd=0, bg="#FFFFFF", fg="black", highlightthickness=0)
text.place(x=30, y=370, width=300, height=20)


def GeneratePassword():
    password = PasswordGeneration()
    text.delete("1.0", "end")
    for s in password:
        text.insert(tk.END, f"{s}")


btnAdd = PhotoImage(file=f"../assets/buttonGenerator.png")
btn = Button(image=btnAdd,
             bg="#00B5C0",
             borderwidth=0,
             highlightthickness=0,
             command=lambda: GeneratePassword(),
             relief="flat")
btn.place(x=80, y=510, width=192, height=37)
root.resizable(False, False)
root.mainloop()