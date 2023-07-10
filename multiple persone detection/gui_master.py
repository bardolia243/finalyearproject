
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk
import tkinter as tk
from PIL import Image, ImageTk
from tkvideo import tkvideo
# main Class


root = tk.Tk()

#root.configure(background="grey")
#root.geometry("500x400")
#root.title("Login")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Multiple person detection ")

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("mp4.mp4", video_label,loop = 1, size = (w, h))
player.play()


label_l1 = tk.Label(root, text="Welcome to Multiple People Detection System",font=("Times New Roman", 30, 'bold'),
                    background="black", fg="white", width=60, height=1)
label_l1.place(x=0, y=0)


def log():
    from subprocess import call
    call(["python","cam.py"])

    
def window():
  root.destroy()

button1 = tk.Button(root, text=" Identify Person", command=log, width=16, height=1,font=('times', 25, ' bold '), bg="#152238", fg="white")
button1.place(x=350, y=150)


button2 = tk.Button(root, text="Exit",command=window,width=16, height=1,font=('times', 25, ' bold '), bg="red", fg="white")
button2.place(x=750, y=150)

label_l1 = tk.Label(root, text="** Multiple People Target Detection @2023 By Trinity College Of Engineering **",font=("Times New Roman", 15, 'bold'),
                    background="black", fg="white", width=60, height=1)
label_l1.place(x=350, y=600)

root.mainloop()
