from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(self.root, text="DEVELOPER",font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top= Image.open(r"images\developer.webp")
        img_top= img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(first_label,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_side= Image.open(r"images/deve.webp")
        img_side= img_side.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_side)

        first_label = Label(main_frame, image=self.photoimg_top1)
        first_label.place(x=300, y=0, width=200, height=200)
        # developer info
        dev_label=Label(main_frame,text="Hello I am Adam",font=("comicsansns",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        deve_label=Label(main_frame,text="I am FullStack Developer",font=("comicsansns",20,"bold"),bg="white")
        deve_label.place(x=0,y=40)

        img1 = Image.open(r"images\group.webp")
        img1 = img1.resize((500,400), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(main_frame, image=self.photoimg1)
        first_label.place(x=0, y=210, width=500, height=400)






if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()