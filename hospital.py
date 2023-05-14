from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital  Management System")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablet=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpiryDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.BloodPressure=StringVar()
        self.Medicine=StringVar()
        self.PatientID=StringVar()
        self.NHSnumber=StringVar()

        lb1title=Label(self.root,bd=20,relief=RIDGE,text=" + PRESCRIPTION MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lb1title.pack(side=TOP,fill=X)

        #========== UPPER DATA FRAME ===========
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                                    font=("times new roman",12,"bold"),text="Patient and Prescription Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,
                                                    font=("times new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        #========== BUTTONS FRAME ===========
        Buttonsframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonsframe.place(x=0,y=530,width=1530,height=70)

        #========== DETAILS FRAME ===========
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #========== DATA FRAME LEFT ===========
        lblNameTablet = Label(DataFrameLeft,text="Name of tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameOfTablet,state="readonly",font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Nice","Covishield","Acetaminophen","Adderail","Amlodipine","Ativan","Cetrizine","Dolo 650","Paracetamol")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblRef=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblRef.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.Ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNumberOfTablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="Number of Tablets:",padx=2,pady=6)
        lblNumberOfTablets.grid(row=3,column=0,sticky=W)
        txtNTablets=Entry(DataFrameLeft,textvariable=self.NumberOfTablets,font=("arial",12,"bold"),width=35)
        txtNTablets.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.IssueDate,font=("arial",12,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpiryDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExpiryDate.grid(row=6,column=0,sticky=W)
        txtExpiryDate=Entry(DataFrameLeft,textvariable=self.ExpiryDate,font=("arial",12,"bold"),width=35)
        txtExpiryDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.SideEffect,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further information:",padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,textvariable=self.BloodPressure,font=("arial",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,textvariable=self.Medicine,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientID=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataFrameLeft,textvariable=self.PatientID,font=("arial",12,"bold"),width=35)
        txtPatientID.grid(row=4,column=3)

        lblNHSnumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNHSnumber.grid(row=5,column=2,sticky=W)
        txtNHSnumber=Entry(DataFrameLeft,textvariable=self.NHSnumber,font=("arial",12,"bold"),width=35)
        txtNHSnumber.grid(row=5,column=3)

        #========== DATA FRAME RIGHT ===========
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #========== BUTTON FRAME ===========
        btnPrescriptionData=Button(Buttonsframe,command=self.iPrescriptionData,fg="white",bg="green",text="Write Prescription",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=0)

        btnPrescription=Button(Buttonsframe,command=self.show_Prescription,fg="white",bg="green",text="Show Prescription",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=1)

        btnUpdate=Button(Buttonsframe,command=self.update_data,fg="white",bg="green",text="Edit/Update Prescription",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonsframe,command=self.delete_Prescription,fg="white",bg="green",text="Delete Prescription",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonsframe,command=self.clear_Prescription,fg="white",bg="green",text="Clear Screen",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonsframe,command=self.exitPrescription,fg="white",bg="green",text="Exit",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #======= TABLE ======
        #====== SCROLL BAR ======
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","patientid","dose","nooftablets","lot","issuedate",
                                                              "expirydate","dailydose","sideeffect","furtherinfo","bloodpressure","storage",
                                                              "medicine","nhsnumber"),
                                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Ref No")
        self.hospital_table.heading("patientid",text="PatientID")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="Number of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expirydate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily dose")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("furtherinfo",text="Further Info")
        self.hospital_table.heading("bloodpressure",text="BP")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("medicine",text="Medication")
        self.hospital_table.heading("nhsnumber",text="NHS number")
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablet",width=80)
        self.hospital_table.column("ref",width=80)
        self.hospital_table.column("patientid",width=80)
        self.hospital_table.column("dose",width=80)
        self.hospital_table.column("nooftablets",width=80)
        self.hospital_table.column("lot",width=80)
        self.hospital_table.column("issuedate",width=80)
        self.hospital_table.column("expirydate",width=80)
        self.hospital_table.column("dailydose",width=80)
        self.hospital_table.column("sideeffect",width=80)
        self.hospital_table.column("furtherinfo",width=80)
        self.hospital_table.column("bloodpressure",width=80)
        self.hospital_table.column("storage",width=80)
        self.hospital_table.column("medicine",width=80)
        self.hospital_table.column("nhsnumber",width=80)
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        if self.NameOfTablet.get()=="" or self.Ref.get()=="" or self.PatientID.get()=="":
                     messagebox.showerror("Error","All fields are required")
        else:
              conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
              my_cursor=conn.cursor()
              my_cursor.execute("select * from patient where patientid=%s",(self.PatientID.get(),))
              row=my_cursor.fetchone()
              conn.commit()
              conn.close()
              if(row==None):
                     messagebox.showerror("Error","Patient not registered")
              else:
                     conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
                     my_cursor=conn.cursor()
                     my_cursor.execute("insert into prescription values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.NameOfTablet.get(),
                            self.Ref.get(),
                            self.PatientID.get(),
                            self.Dose.get(),
                            self.NumberOfTablets.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpiryDate.get(),
                            self.DailyDose.get(),
                            self.SideEffect.get(),
                            self.FurtherInformation.get(),
                            self.BloodPressure.get(),
                            self.StorageAdvice.get(),
                            self.Medicine.get(),
                            self.NHSnumber.get(),
                     ))
                     conn.commit()
                     self.fetch_data()
                     conn.close()
                     messagebox.showinfo("Success !","Record has been inserted")

    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from prescription")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                       self.hospital_table.delete(*self.hospital_table.get_children())
                       for i in rows:
                              self.hospital_table.insert("",END,values=i)
                conn.commit()
                conn.close()

    def get_cursor(self,event=""):
           self.clear_Prescription()
           cursor_row=self.hospital_table.focus()
           content=self.hospital_table.item(cursor_row)
           row=content["values"]
           self.NameOfTablet.set(row[0])
           self.Ref.set(row[1])
           self.PatientID.set(row[2])
           self.Dose.set(row[3])
           self.NumberOfTablets.set(row[4])
           self.Lot.set(row[5])
           self.IssueDate.set(row[6])
           self.ExpiryDate.set(row[7])
           self.DailyDose.set(row[8])
           self.SideEffect.set(row[9])
           self.FurtherInformation.set(row[10])
           self.BloodPressure.set(row[11])
           self.StorageAdvice.set(row[12])
           self.Medicine.set(row[13])
           self.NHSnumber.set(row[14])

    def update_data(self):
           conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
           my_cursor=conn.cursor()
           my_cursor.execute("update prescription set NameOfTablet=%s,Dose=%s,NumberOfTablets=%s,Lot=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,SideEffect=%s,FurtherInfo=%s,BloodPressure=%s,Storage=%s,Medicine=%s,NHSnumber=%s where Reference_No=%s and PatientID=%s",(
                            self.NameOfTablet.get(),
                            self.Dose.get(),
                            self.NumberOfTablets.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpiryDate.get(),
                            self.DailyDose.get(),
                            self.SideEffect.get(),
                            self.FurtherInformation.get(),
                            self.BloodPressure.get(),
                            self.StorageAdvice.get(),
                            self.Medicine.get(),
                            self.NHSnumber.get(),
                            self.Ref.get(),
                            self.PatientID.get()
           ))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Updated !","Record has been updated")
    
    def show_Prescription(self):
       #     self.txtPrescription.insert(END,"Name of Tablet:\t\t\t"+self.NameOfTablet.get()+"\n")
       #     self.txtPrescription.insert(END,"Reference Number:\t\t\t"+self.Ref.get()+"\n")
       #     self.txtPrescription.insert(END,"Patient ID:\t\t\t"+self.PatientID.get()+"\n")
       #     self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
       #     self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberOfTablets.get()+"\n")
       #     self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
       #     self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
       #     self.txtPrescription.insert(END,"Expiry Date:\t\t\t"+self.ExpiryDate.get()+"\n")
       #     self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
       #     self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")
       #     self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
       #     self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.BloodPressure.get()+"\n")
       #     self.txtPrescription.insert(END,"Storage:\t\t\t"+self.StorageAdvice.get()+"\n")
       #     self.txtPrescription.insert(END,"Medicine:\t\t\t"+self.Medicine.get()+"\n")
       #     self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.NHSnumber.get()+"\n")
               dailyDose=self.DailyDose.get()
       #       self.txtPrescription.insert(END,"Patient ID:\t\tDaily Dosage:\t\n")
       #       self.txtPrescription.insert(END,"\t\tMorn\tAft\tNight\n")
       #       self.txtPrescription.insert(END,self.PatientID.get()+"\t\t"+dailyDose[0]+"\t"+dailyDose[2]+"\t"+dailyDose[4])
               conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
               my_cursor=conn.cursor()
               my_cursor.execute("select * from patient where patientid=%s",(self.PatientID.get(),))
               row=my_cursor.fetchone()
               name=row[1]
               conn.commit()
               conn.close()
               self.txtPrescription.insert(END,"Name: "+name+"\t\tPatient ID: "+self.PatientID.get()+"\t\tRef.No: "+self.Ref.get())
               self.txtPrescription.insert(END,"\n\nS.No\t\tName of Tablet\t\tDosage")
               self.txtPrescription.insert(END,"\n\n\t\t\t\tMorn  Aft  Night")
               self.txtPrescription.insert(END,"\n1\t\t"+self.NameOfTablet.get()+"\t\t"+dailyDose[0]+"          "+dailyDose[2]+"          "+dailyDose[4])

    def delete_Prescription(self):
           conn=mysql.connector.connect(host="localhost",user="root",password="1234dbsPro567",database="mydata", auth_plugin='mysql_native_password')
           my_cursor=conn.cursor()
           query="delete from prescription where Reference_No=%s and PatientID=%s"
           value=(self.Ref.get(),self.PatientID.get(),)
           my_cursor.execute(query,value)
           conn.commit()
           self.fetch_data()
           self.clear_Prescription()
           conn.close()
           messagebox.showinfo("Deleted !","Prescription deleted successfully")
    
    def clear_Prescription(self):
            self.NameOfTablet.set("")
            self.Dose.set("")
            self.NumberOfTablets.set("")
            self.Lot.set("")
            self.IssueDate.set("")
            self.ExpiryDate.set("")
            self.DailyDose.set("")
            self.SideEffect.set("")
            self.FurtherInformation.set("")
            self.BloodPressure.set("")
            self.StorageAdvice.set("")
            self.Medicine.set("")
            self.NHSnumber.set("")
            self.Ref.set("")
            self.PatientID.set("")
            self.txtPrescription.delete("1.0",END)

    def exitPrescription(self):
           exitPrescription=messagebox.askyesno("Prescription Management System","Confirm if you want to exit")
           if exitPrescription>0:
                  root.destroy()
                  return

root=Tk()
ob=Hospital(root)
root.mainloop()