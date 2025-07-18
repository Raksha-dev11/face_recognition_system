from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition_app import Face_Recognition
import os
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

        # First image
        img = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\university.webp")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\face_recognition.webp")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=520, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\uni.webp")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=1040, y=0, width=500, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\bg.webp")
        img3 = img3.resize((1530, 700), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=700)

        # Title label
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details ,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face detector button
        img5 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\face_detector.webp")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance
        img6 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\attendance.webp")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help desk
        img7 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\help.webp")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\train.webp")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=380, width=220, height=220)
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # Photos
        img9 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\photos.webp")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)
        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer
        img10 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\dev.webp")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b7.place(x=800, y=380, width=220, height=220)
        b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit
        img11 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\exit.webp")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.exit_page)
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.exit_page,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)


    def open_img(self):
        os.startfile("data")



        #Function buttons

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Attendance(self.new_window)

    def developer_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Developer(self.new_window)
    
    def help_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Help(self.new_window)

    def exit_page(self):
          exit_confirm=messagebox.askyesno("Face Recognition","Are you sure you want to exit this window")
          if exit_confirm>0:
                self.root.destroy()
          else:
                return



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
