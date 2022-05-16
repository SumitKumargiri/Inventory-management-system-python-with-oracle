from multiprocessing import connection
import cx_Oracle
from tkinter import *
from PIL import Image,ImageTk #pip install pillow 
from tkinter import ttk,messagebox
class supplierClass:
 def __init__(self,root):
    self.root=root
    self.root.geometry('1100x500+200+130')
    self.root.title("inventory management system ||  developed By Sumit")
    self.root.config(bg="Cyan")
    self.root.focus_force()
    #============== all variable ================================
    self.Var_searchby=StringVar()
    self.Var_searchtxt=StringVar()
    
    self.var_sup_invoice=StringVar()
    self.Var_name=StringVar()
    self.Var_contact=StringVar()

    #========== search frame =====================================
    SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="white",fg="blue")
    SearchFrame.place(x=250,y=20,width=600,height=70)

    #=================== option =================================
    lbl_search=Label(SearchFrame,text="Search By Invoice No.",bg="white",font=("time new roman",12,"bold"))
    lbl_search.place(x=10,y=10)

    text_search=Entry(SearchFrame,textvariable=self.Var_searchtxt,font=("time new roman",15),bg="lightyellow").place(x=200,y=10)
    btn_search=Button(SearchFrame,text="search",command=self.search,font=("time new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=7,width=150,height=30)
    
    #============= title ================================================
    title=Label(self.root,text="Supplier Detail",font=("time new roman",15,"bold"),bg="green",fg="white",bd=5,cursor="hand2").place(x=50,y=100,width=1000)

    #============ content =================================================
    #============= row1 =====================================================
    lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=150)

    txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("time new roman",15),bg="lightyellow").place(x=170,y=150)
    #====================== row2 =====================================================
    lbl_name=Label(self.root,text="Name",font=("time new roman",15,"bold"),bg="cyan").place(x=460,y=150)
    txt_name=Entry(self.root,textvariable=self.Var_name,font=("time new roman",15),bg="lightyellow").place(x=550,y=150)

     #====================== row3 =====================================================
    lbl_contact=Label(self.root,text="Contact",font=("time new roman",15,"bold"),bg="cyan").place(x=50,y=200)

    txt_contact=Entry(self.root,textvariable=self.Var_contact,font=("time new roman",15),bg="lightyellow").place(x=170,y=200,width=220)
    #=================== row4 =============================================================
    lbl_desc=Label(self.root,text="Description",font=("time new roman",15,"bold"),bg="cyan").place(x=440,y=200)    
    self.txt_desc=Text(self.root,font=("time new roman",15),bg="lightyellow")
    self.txt_desc.place(x=570,y=200,width=350,height=70)
    #================== buttons ===============================
    btn_add=Button(self.root,text="Save",command=self.add,font=("time new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)

    btn_update=Button(self.root,text="Update",command=self.update,font=("time new roman",15),bg="orange",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)

    btn_delete=Button(self.root,text="Delete",command=self.delete,font=("time new roman",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)

    btn_clear=Button(self.root,text="Clear",command=self.clear,font=("time new roman",15),bg="gray",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

    #=========== supplier Detail ==============================================
    sup_frame=Frame(self.root,bd=3,relief=RIDGE)
    sup_frame.place(x=0,y=350,relwidth=1,height=150)

    scrolly=Scrollbar(sup_frame,orient=VERTICAL)
    scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

    self.supplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.supplierTable.xview)
    scrolly.config(command=self.supplierTable.yview)
    self.supplierTable.heading("invoice",text="Invoice No.")
    self.supplierTable.heading("name",text="Name")
    self.supplierTable.heading("contact",text="Contact")
    self.supplierTable.heading("desc",text="Description")
    self.supplierTable["show"]="headings"

    self.supplierTable.column("invoice",width=90)
    self.supplierTable.column("name",width=100)
    self.supplierTable.column("contact",width=100)
    self.supplierTable.column("desc",width=100)
    self.supplierTable.pack(fill=BOTH,expand=1)
 #   self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

   #  self.show()

#========================================backend====================================
#====================Added function ====================================================
 def add(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Invoice Must be required",parent=self.root)
                
         else:
               cur.execute("select *from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row!=None:
                     messagebox.showerror("Error","INvoice no. already assigned,try different",parent=self.root)
               else:
                  cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                             self.var_sup_invoice.get(),
                                             self.Var_name.get(),
                                             self.Var_contact.get(),
                                             
                                             self.txt_desc.get('1.0',END),
                   ))
                  connection.Commit()
                  messagebox.showinfo("success","Supplier Added Successfully",parent=self.root)
                  self.show()

      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
 def show(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         cur.execute("select *from supplier")
         rows=cur.fetchall()
         self.supplierTable.delete(*self.supplierTable.get_children())
         for row in rows:
               self.supplierTable.insert('',END,values=row)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
 def get_data(self,ev):
      f=self.supplierTable.focus()
      content=(self.supplierTable.item(f))
      row=content['values']
      print(row)
      
      self.var_sup_invoice.set(row[0])
      self.Var_name.set(row[1])
 
      self.Var_contact.set(row[2])
 
      self.txt_desc.delete('1.0',END)
      self.txt_desc.insert(END,row[3])
#=========== Update function ==============================================
 def update(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
                
         else:
               cur.execute("select *from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row==None:
                     messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
               else:
                  cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(

                                             self.Var_name.get(),
                                             
                                             self.Var_contact.get(),
                                             self.txt_desc.get('1.0',END),
                                             self.var_sup_invoice.get(),
                   ))
                  connection.Commit()
                  messagebox.showinfo("success","Supplier Updated Successfully",parent=self.root)
                  self.show()
                  #con.close()

      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#================ Delete function =================================================
 def delete(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
                
         else:
               cur.execute("select *from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row==None:
                     messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
               else:
                  op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                  if op==True:
                     cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                     connection.commit()
                     messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                     self.clear()
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
#=============Clear function ======================================
 def clear(self):
      self.var_sup_invoice.set("")
      self.Var_name.set("")
      self.Var_contact.set("")
    
      self.txt_desc.delete('1.0',END)
      self.Var_searchtxt.get("")
      self.show()
      
 def search(self):
      connection=cx_Oracle.connect('sumit/abhinav')
      cur=connection.Cursor()
      try:
         if self.Var_searchtxt.get()=="":
                messagebox.showerror("error","Invoice No. should be required",parent=self.root)
         else:
            cur.execute("select *from supplier where invoice=?",(self.Var_searchtxt.get(),))
            row=cur.fetchone()
            if row!=None:

               self.supplierTable.delete(*self.supplierTable.get_children())
               self.supplierTable.insert('',END,values=row)
            else:
               messagebox.showerror("error","No record found!!!",parent=self.root)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

      
if __name__=="__main__":
     root=Tk()
     obj=supplierClass(root)
     root.mainloop()
