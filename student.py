
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_divison=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()


         # First image
        img = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student1.webp")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student2.webp")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=520, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student3.webp")
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
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                        font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1490,height=600)

        # left label frame 
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width="750",height="580")

        img_left = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student4.webp")
        img_left = img_left.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=740, height=130)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,bg="white",text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width="740",height="150")
   

         # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)  # ✅ column changed to 4



        #Year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)

        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        Year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 
        
        #Semester
        Sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Sem_label.grid(row=1,column=2,padx=10,sticky=W)

        Sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        Sem_combo["values"]=("Select Semester","Sem1","Sem2")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student info 
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,bg="white",text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width="740",height="300")
 
        #studentid
        StudentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        StudentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class division
        class_div_label=Label(class_student_frame,text="Class Divison:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        classDiv_combo=ttk.Combobox(class_student_frame,textvariable=self.var_divison,font=("times new roman",13,"bold"),state="readonly",width=18)
        classDiv_combo["values"]=("Select Division","A","B","C")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        Gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        Gender_combo["values"]=("Select gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        Dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_no_label=Label(class_student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_name_label=Label(class_student_frame,text="Teacher name:",font=("times new roman",12,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=730,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=730,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        # right label frame 
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=770,y=10,width="700",height="580")

        img_right = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student5.webp")
        img_right = img_right.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_label = Label(right_frame, image=self.photoimg_right)
        first_label.place(x=5, y=0, width=740, height=130)

        #Search system
        Search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white",text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=140,width=690,height=70)

        Search_label=Label(Search_frame,text="Search bar",font=("times new roman",12,"bold"),bg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        search_combo["values"]=("Select","Roll no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        Table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        Table_frame.place(x=5,y=210,width=690,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame,
                                  columns=("department", "course", "year", "sem", "id", "name", "divison", "roll", "gender", "dob", "phone", "email", "address", "teacher", "photo"),
                                  xscrollcommand=scroll_x.set,
                                  yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("divison", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        
        self.student_table["show"] = "headings"
        
        self.student_table.column("department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("divison", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()==" ":
            messagebox.showerror("Error","All fields are required!",parent=self.root)

        else:
            try:

            
                conn=mysql.connector.connect(host="localhost",username="root",password="Raksha431@",database="facerecogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                               
                                                                               self.var_dep.get(),
                                                                               self.var_course.get(),
                                                                               self.var_year.get(),
                                                                               self.var_semester.get(),
                                                                               self.var_id.get(),
                                                                               self.var_name.get(),
                                                                               self.var_divison.get(),
                                                                               self.var_roll.get(),
                                                                               self.var_gender.get(),
                                                                               self.var_dob.get(),
                                                                               self.var_phone.get(),
                                                                               self.var_email.get(),
                                                                               self.var_address.get(),
                                                                               self.var_teacher.get(),
                                                                               self.var_radio1.get()
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
          
        


     #Fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Raksha431@",database="facerecogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        if data and len(data) >= 15:  # Make sure it has all expected columns
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_id.set(data[4])
            self.var_name.set(data[5])
            self.var_divison.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_phone.set(data[10])
            self.var_email.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        else:
            messagebox.showerror("Error", "Selected row is empty or corrupted.")

    #update function
    
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Raksha431@",database="facerecogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s ,Course=%s, Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                       self.var_dep.get(),
                                                                                                                       self.var_course.get(),
                                                                                                                       self.var_year.get(),
                                                                                                                       self.var_semester.get(),
                                                                                                                       self.var_name.get(),
                                                                                                                       self.var_divison.get(),
                                                                                                                       self.var_roll.get(),
                                                                                                                       self.var_gender.get(),
                                                                                                                       self.var_dob.get(),
                                                                                                                       self.var_phone.get(),
                                                                                                                       self.var_email.get(),
                                                                                                                       self.var_address.get(),
                                                                                                                       self.var_teacher.get(),
                                                                                                                       self.var_radio1.get(),
                                                                                                                       self.var_id.get()
                                                                                                                     ))
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if  not Update:
                        return 
                # messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                # conn.commit()
                # self.fetch_data()
                # conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_id.get=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Raksha431@",database="facerecogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")           
        self.var_divison.set("Select Division")  
        self.var_roll.set("")
        self.var_gender.set("Select gender")  
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")   



#generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Raksha431@",database="facerecogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s ,Course=%s, Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                       self.var_dep.get(),
                                                                                                                       self.var_course.get(),
                                                                                                                       self.var_year.get(),
                                                                                                                       self.var_semester.get(),
                                                                                                                       self.var_name.get(),
                                                                                                                       self.var_divison.get(),
                                                                                                                       self.var_roll.get(),
                                                                                                                       self.var_gender.get(),
                                                                                                                       self.var_dob.get(),
                                                                                                                       self.var_phone.get(),
                                                                                                                       self.var_email.get(),
                                                                                                                       self.var_address.get(),
                                                                                                                       self.var_teacher.get(),
                                                                                                                       self.var_radio1.get(),
                                                                                                                       self.var_id.get()==id+1 
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from open cv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data set completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

                    



        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()