from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")


        title_lbl = Label(self.root, text="Help Desk",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top= Image.open(r"images\helpdesk.webp")
        img_top= img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=720)

        dev_label=Label(first_label,text="Email:raksha@drupaltechie.com",font=("comicsansns",20,"bold"),bg="blue")
        dev_label.place(x=600,y=150)




if __name__ == "__main__":
    root = Tk()
    obj =Help(root)
    root.mainloop()