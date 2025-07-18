from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")


        #variables
        self.var_attenID=StringVar()
        self.var_attenRoll=StringVar()
        self.var_attenName=StringVar()
        self.var_attenDep=StringVar()
        self.var_attenTime=StringVar()
        self.var_attenDate=StringVar()
        self.var_attenAttendance=StringVar()


         # First image
        img = Image.open(r"images\student2.webp")
        img = img.resize((800, 200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=800, height=200)

        # Second image
        img1 = Image.open(r"images\student4.webp")
        img1 = img1.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=800, y=0, width=800, height=200)

        # Background image
        img3 = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\bg.webp")
        img3 = img3.resize((1530, 700), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=700)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",
                        font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1490,height=600)

         # left label frame 
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width="750",height="580")

        img_left = Image.open(r"C:\Users\RakshaShandilya\OneDrive\Desktop\face_recognition_system\images\student4.webp")
        img_left = img_left.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=740, height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=740,height=370)

        #labels and entry
        #attendance id 
        AttendanceId_label=Label(left_inside_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attenID,width=20,font=("times new roman",13,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        Roll_label=Label(left_inside_frame,text="Roll:",font=("comicsansns",11,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=4,pady=8)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attenRoll,width=22,font=("comicsansns",11,"bold"))
        roll_entry.grid(row=0,column=3,pady=8)

        #Name
        Name_label=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg="white")
        Name_label.grid(row=1,column=0)

        Name_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_attenName,font=("comicsansns",11,"bold"))
        Name_entry.grid(row=1,column=1,pady=8)

        #department
        dep_label=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attenDep,width=20,font=("comicsansns",11,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        #time
        Time_label=Label(left_inside_frame,text="Time:",font=("comicsansns",11,"bold"),bg="white")
        Time_label.grid(row=2,column=0)

        Time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attenTime,width=20,font=("comicsansns",11,"bold"))
        Time_entry.grid(row=2,column=1,pady=8)

        #date
        Date_label=Label(left_inside_frame,text="Date:",font=("comicsansns",11,"bold"),bg="white")
        Date_label.grid(row=2,column=2)

        Date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attenDate,width=20,font=("comicsansns",11,"bold"))
        Date_entry.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        Atten_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attenAttendance,font=("comicsansns",11,"bold"),state="readonly")
        Atten_combo["values"]=("Status","Absent","Present")
        Atten_combo.grid(row=3,column=1,pady=8)
        Atten_combo.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=730,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.import_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.export_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=770,y=10,width="700",height="580")

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=690,height=455)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"
        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#fetch data
    def fetch_data(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)
#import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
    initialdir=os.getcwd(),
    title="Open CSV",
    filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
    parent=self.root
)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data!","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
    initialdir=os.getcwd(),
    title="Open CSV",
    filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
    parent=self.root
)
            with open(fln,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export!","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        if rows and len(rows)==7:
            self.var_attenID.set(rows[0])
            self.var_attenRoll.set(rows[1])
            self.var_attenName.set(rows[2])
            self.var_attenDep.set(rows[3])
            self.var_attenTime.set(rows[4])
            self.var_attenDate.set(rows[5])
            self.var_attenAttendance.set(rows[6])

    def reset(self):
        self.var_attenID.set("")
        self.var_attenRoll.set("")
        self.var_attenName.set("")
        self.var_attenDep.set("")
        self.var_attenTime.set("")
        self.var_attenDate.set("")
        self.var_attenAttendance.set("")



      







if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()