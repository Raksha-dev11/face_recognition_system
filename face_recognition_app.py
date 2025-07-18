from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

        # Title
        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # 1st image
        img_top = Image.open(r"images\face_detector.webp")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"images\detection.webp")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        second_label = Label(self.root, image=self.photoimg_bottom)
        second_label.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(second_label, text="Face Recognition", command=self.recognition, cursor="hand2",
                      font=("times new roman", 20, "bold"), bg="red", fg="white")
        b1_1.place(x=280, y=620, width=400, height=60)

    #attendance
    def mark_atttendance(self,i,s,r,n):
        with open("Raksha.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_List.append(entry[0])
            if((i not in name_List) and (s not in name_List) and (r not in name_List) and (n not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{s},{i},{r},{dtString},{d1},Present")





    # face recognition logic
    def recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    
            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
    
                conn = mysql.connector.connect(host="localhost", username="root", password="Raksha431@", database="facerecogniser")
                my_cursor = conn.cursor()
    
                my_cursor.execute("select Name from student where Student_id=%s", (str(id),))
                name = "+".join(my_cursor.fetchone() or ["Unknown"])
    
                my_cursor.execute("select Roll from student where Student_id=%s", (str(id),))
                roll = "+".join(my_cursor.fetchone() or ["Unknown"])
    
                my_cursor.execute("select Dep from student where Student_id=%s", (str(id),))
                dep = "+".join(my_cursor.fetchone() or ["Unknown"])
    
                my_cursor.execute("select Student_id from student where Student_id=%s", (str(id),))
                student_id = "+".join(my_cursor.fetchone() or ["Unknown"])
    
                conn.close()
    
                if confidence > 77:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(img, f"ID:{student_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dep:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
    
                    if student_id not in self.recognized_ids:
                        self.mark_atttendance(name, roll, student_id, dep)
                        self.recognized_ids.add(student_id)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
    
        def recognise(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), clf)
            return img
    
        self.recognized_ids = set()
    
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
        video_cam = cv2.VideoCapture(0)
    
        while True:
            ret, img = video_cam.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)
    
            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cam.release()
        cv2.destroyAllWindows()


    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
