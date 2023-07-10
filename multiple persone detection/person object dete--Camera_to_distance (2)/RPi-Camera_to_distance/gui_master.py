
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk
import tkinter as tk
from PIL import Image, ImageTk

# main Class


root = tk.Tk()

#root.configure(background="grey")
#root.geometry("500x400")
#root.title("Login")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Multiple person detection ")

image2 = Image.open('face.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
label_l1 = tk.Label(root, text="Multiple person detection",font=("Times New Roman", 30, 'bold'),
                    background="#152238", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)


def log():
    from subprocess import call
    call(["python","cam.py"])

    
def window():
  root.destroy()

button1 = tk.Button(root, text=" Person Detection", command=log, width=18, height=1,font=('times', 25, ' bold '), bg="hot pink", fg="white")
button1.place(x=0, y=160)


button2 = tk.Button(root, text="Exit",command=window,width=18, height=1,font=('times', 25, ' bold '), bg="hot pink", fg="white")
button2.place(x=0, y=250)

root.mainloop()
