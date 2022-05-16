from ast import Delete
from importlib.resources import contents
from multiprocessing import connection
from multiprocessing.sharedctypes import Value
from optparse import Values
from select import select
from webbrowser import get
import cx_Oracle
from tkinter import *
from PIL import Image,ImageTk #pip install pillow 
from tkinter import ttk,messagebox
class employeeClass:
 def __init__(self,root):
    self.root=root
    self.root.geometry('1100x500+200+130')
    self.root.title("inventory management system ||  developed By 4S")
    self.root.config(bg="Cyan")
    self.root.focus_force()
    #============== all variable ================================
    self.Var_searchby=StringVar()
    self.Var_searchtxt=StringVar()
    
    self.Var_emp_id=StringVar()
    self.Var_gender=StringVar()
    self.Var_contact=StringVar()
    self.Var_name=StringVar()
    self.Var_dob=StringVar()
    self.Var_doj=StringVar()
    self.Var_email=StringVar()
    self.Var_pass=StringVar()
    self.Var_utype=StringVar()
    self.Var_address=StringVar()
    self.Var_salary=StringVar()
    
    
    #========== search frame =====================================
    SearchFrame=LabelFrame(self.root,text="Search Employee",font=("time new roman",12,"bold"),bd=5,relief=RIDGE,bg="white",fg="blue")
    SearchFrame.place(x=250,y=20,width=600,height=70)

    #=================== option =================================
    cmb_search=ttk.Combobox(SearchFrame,textvariable=self.Var_searchby,values=("select","Email","Name","contact"),state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_search.place(x=10,y=10,width=180)
    cmb_search.current(0)

    text_search=Entry(SearchFrame,textvariable=self.Var_searchtxt,font=("time new roman",15),bg="lightyellow").place(x=200,y=10)
    btn_search=Button(SearchFrame,text="search",command=self.search,font=("time new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=7,width=150,height=30)
    
    #============= title ================================================
    title=Label(self.root,text="Employee Detail",font=("time new roman",15),bg="green",fg="white",bd=5,cursor="hand2").place(x=50,y=100,width=1000)

    #============ content =================================================
    #============= row1 =====================================================
    lbl_emp_id=Label(self.root,text="Emp ID",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=150)
    lbl_gender=Label(self.root,text="Gender",font=("time new roman",15,"bold"),bg="cyan").place(x=400,y=150)
    lbl_contact=Label(self.root,text="Contact",font=("time new roman",15,"bold"),bg="cyan").place(x=750,y=150)

    self.emp_id=Entry(self.root,textvariable=self.Var_emp_id,font=("time new roman",15),bg="lightyellow")
    self.emp_id.place(x=150,y=150)
    #txt_gender=Entry(self.root,textvariable=self.Var_gender,font=("time new roman",15),bg="lightyellow").place(x=500,y=150)
    cmb_gender=ttk.Combobox(self.root,textvariable=self.Var_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_gender.place(x=500,y=150,width=220)
    cmb_gender.current(0)
    self.contact=Entry(self.root,textvariable=self.Var_contact,font=("time new roman",15),bg="lightyellow")
    self.contact.place(x=900,y=150)
    #====================== row2 =====================================================
    lbl_name=Label(self.root,text="Name",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=190)
    lbl_dob=Label(self.root,text="D.O.B",font=("time new roman",15,"bold"),bg="cyan").place(x=400,y=190)
    lbl_doj=Label(self.root,text="D.O.J",font=("time new roman",15,"bold"),bg="cyan").place(x=750,y=190)

    self.name=Entry(self.root,textvariable=self.Var_name,font=("time new roman",15),bg="lightyellow")
    self.name.place(x=150,y=190)
    self.dob=Entry(self.root,textvariable=self.Var_dob,font=("time new roman",15),bg="lightyellow")
    self.dob.place(x=500,y=190)
    self.doj=Entry(self.root,textvariable=self.Var_doj,font=("time new roman",15),bg="lightyellow")
    self.doj.place(x=900,y=190)

     #====================== row3 =====================================================
    lbl_email=Label(self.root,text="Email",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=230)
    lbl_pass=Label(self.root,text="Password",font=("time new roman",15,"bold"),bg="cyan").place(x=400,y=230)
    lbl_utype=Label(self.root,text="User Type",font=("time new roman",15,"bold"),bg="cyan").place(x=750,y=230)

    self.email=Entry(self.root,textvariable=self.Var_email,font=("time new roman",15),bg="lightyellow")
    self.email.place(x=150,y=230,width=220)
    self.password=Entry(self.root,textvariable=self.Var_pass,font=("time new roman",15),bg="lightyellow")
    self.password.place(x=500,y=230,width=220)
    #txt_utype=Entry(self.root,textvariable=self.Var_utype,font=("time new roman",15),bg="lightyellow").place(x=900,y=230,width=220)
    cmb_utype=ttk.Combobox(self.root,textvariable=self.Var_utype,values=("select","Admin","Employee"),state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_utype.place(x=900,y=230,width=220)
    cmb_utype.current(0)

    #=================== row4 =============================================================
    lbl_address=Label(self.root,text="Address",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=270)
    lbl_salary=Label(self.root,text="Salary",font=("time new roman",15,"bold"),bg="cyan").place(x=750,y=270)
    
    self.address=Entry(self.root,font=("time new roman",15),bg="lightyellow")
    self.address.place(x=150,y=270,width=320,height=70)
    
    self.salary=Entry(self.root,textvariable=self.Var_salary,font=("time new roman",15),bg="lightyellow")
    self.salary.place(x=900,y=270,width=220)
    #================== buttons ===============================
    btn_add=Button(self.root,text="Save",command=self.add,font=("time new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)

    btn_update=Button(self.root,text="Update",command=self.update,font=("time new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)

    btn_delete=Button(self.root,text="Delete",command=self.delete,font=("time new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)

    btn_clear=Button(self.root,text="Clear",command=self.clear,font=("time new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

    #=========== Employee Detail ==============================================
    emp_frame=Frame(self.root,bd=3,relief=RIDGE)
    emp_frame.place(x=0,y=350,relwidth=1,height=150)

    scrolly=Scrollbar(emp_frame,orient=VERTICAL)
    scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

    self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.EmployeeTable.xview)
    scrolly.config(command=self.EmployeeTable.yview)
    #===========heading========================================
    self.EmployeeTable.heading("eid",text="EMP ID")
    self.EmployeeTable.heading("name",text="Name")
    self.EmployeeTable.heading("email",text="Email")
    self.EmployeeTable.heading("gender",text="Gender")
    self.EmployeeTable.heading("contact",text="Contact")
    self.EmployeeTable.heading("dob",text="D.O.B")
    self.EmployeeTable.heading("doj",text="D.O.J")
    self.EmployeeTable.heading("pass",text="Password")
    self.EmployeeTable.heading("utype",text="User Type")
    self.EmployeeTable.heading("address",text="Address")
    self.EmployeeTable.heading("salary",text="Salary")
    self.EmployeeTable["show"]="headings"
#==============column =============================================
    self.EmployeeTable.column("eid",width=90)
    self.EmployeeTable.column("name",width=100)
    self.EmployeeTable.column("email",width=100)
    self.EmployeeTable.column("gender",width=100)
    self.EmployeeTable.column("contact",width=100)
    self.EmployeeTable.column("dob",width=100)
    self.EmployeeTable.column("doj",width=100)
    self.EmployeeTable.column("pass",width=100)
    self.EmployeeTable.column("utype",width=100)
    self.EmployeeTable.column("address",width=100)
    self.EmployeeTable.column("salary",width=100)
    self.EmployeeTable["show"]="headings"
    self.EmployeeTable.pack(fill=BOTH,expand=1)
    #self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
    #self.show()

#========================================backend====================================
#====================Added function ====================================================
 def add(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.Var_emp_id.get()=="":
               messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
                
         else:
               cur.execute("select *from employee where eid=?",(self.Var_emp_id.get(),))
               row=cur.fetchone()
               if row!=None:
                     messagebox.showerror("Error","This Employee ID already assigned,try different",parent=self.root)
               else:
                  cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                             self.Var_emp_id.get(),
                                             self.Var_name.get(),
                                             self.Var_email.get(),
                                             self.Var_gender.get(),
                                             self.Var_contact.get(),
                                             
                                             self.Var_dob.get(),
                                             self.Var_doj.get(),
                                             
                                             self.Var_pass.get(),
                                             self.Var_utype.get(),
                                             self.Var_address.get('1.0',END),
                                             self.Var_salary.get(),
                   ))
                  connection.Commit()
                  messagebox.showinfo("success","Employee Added Successfully",parent=self.root)
                  self.show()

      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
 def show(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         cur.execute("select *from employee")
         rows=cur.fetchall()
         self.EmployeeTable.delete(*self.EmployeeTable.get_children())
         for row in rows:
               self.EmployeeTable.insert('',END,values=row)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
 def get_data(self,ev):
      f=self.EmployeeTable.focus()
      content=(self.EmployeeTable.item(f))
      row=content['values']
      print(row)
      
      self.Var_emp_id.set(row[0])
      self.Var_name.set(row[1])
      self.Var_email.set(row[2])
      self.Var_gender.set(row[3])
      self.Var_contact.set(row[4])
      self.Var_dob.set(row[5])
      self.Var_doj.set(row[6])
      self.Var_pass.set(row[7])
      self.Var_utype.set(row[8])
      self.Var_address.delete('1.0',END)
      self.Var_address.insert(END,row[9])
      self.Var_salary.set(row[10])
#=========== Update function ==============================================
 def update(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.Var_emp_id.get()=="":
               messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
                
         else:
               cur.execute("select *from employee where eid=?",(self.Var_emp_id.get(),))
               row=cur.fetchone()
               if row==None:
                     messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
               else:
                  cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(

                                             self.Var_name.get(),
                                             self.Var_email.get(),
                                             self.Var_gender.get(),
                                             self.Var_contact.get(),
                                             
                                             self.Var_dob.get(),
                                             self.Var_doj.get(),
                                             
                                             self.Var_pass.get(),
                                             self.Var_utype.get(),
                                             self.Var_address.get('1.0',END),
                                             self.Var_salary.get(),
                                             self.Var_emp_id.get(),
                   ))
                  connection.Commit()
                  messagebox.showinfo("success","Employee Updated Successfully",parent=self.root)
                  self.show()
                  #con.close()

      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#================ Delete function =================================================
 def delete(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.Var_emp_id.get()=="":
               messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
                
         else:
               cur.execute("select *from employee where eid=?",(self.Var_emp_id.get(),))
               row=cur.fetchone()
               if row==None:
                     messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
               else:
                  op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                  if op==True:
                     cur.execute("delete from employee whrere eid=?",(self.Var_emp_id.get(),))
                     connection.commit()
                     messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                     self.clear()
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
#=============Clear function ======================================
 def clear(self):
      self.Var_emp_id.set("")
      self.Var_name.set("")
      self.Var_email.set("")
      self.Var_gender.set("Select")
      self.Var_contact.set("")
      self.Var_dob.set("")
      self.Var_doj.set("")
      self.Var_pass.set("")
      self.Var_utype.set("Admin")
      self.Var_address.delete('1.0',END)
      self.Var_salary.set("")
      self.Var_searchtxt.get("")
      self.Var_searchby.get("Select")
      self.show()
      
 def search(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.Var_searchby.get()=="select":
                messagebox.showerror("error","select Search By option",parent=self.root)
         elif self.Var_searchtxt.get()=="":
                messagebox.showerror("error","Search input should be required",parent=self.root)
         else:
            cur.execute("select *from employee where "+self.Var_searchby.get()+" LIKE '%"+self.Var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:

               self.EmployeeTable.delete(*self.EmployeeTable.get_children())
               for row in rows:
                  self.EmployeeTable.insert('',END,values=row)
            else:
               messagebox.showerror("error","No record found!!!",parent=self.root)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
   root=Tk()
   obj=employeeClass(root)
   root.mainloop()
