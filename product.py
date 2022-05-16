import cx_Oracle
from tkinter import *
from PIL import Image,ImageTk #pip install pillow 
from tkinter import ttk,messagebox
class productClass:
 def __init__(self,root):
    self.root=root
    self.root.geometry('1100x500+200+130')
    self.root.title("inventory management system ||  developed By sumit")
    self.root.config(bg="Cyan")
    self.root.focus_force()
#=================================================
    self.Var_searchby=StringVar()
    self.Var_searchtxt=StringVar()
    self.Var_pid=StringVar()
    self.var_cat=StringVar()
    self.var_sup=StringVar()
    self.cat_list=[]
    self.sup_list=[]
    #self.fetch_cat_sup()
    
    self.var_name=StringVar()
    self.var_price=StringVar()
    self.var_qty=StringVar()
    self.var_status=StringVar()

    product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    product_Frame.place(x=10,y=10,width=450,height=480)
#================title =====================================
    title=Label(product_Frame,text="Manage Product Detail",font=("time new roman",15),bg="#4caf50",fg="white").pack(side=TOP,fill=X)
    #============ column1 =============================================
    lbl_category=Label(product_Frame,text="category",font=("time new roman",15),bg="white").place(x=30,y=60)
    lbl_supplier=Label(product_Frame,text="supplier",font=("time new roman",15),bg="white").place(x=30,y=110)
    lbl_product=Label(product_Frame,text="product",font=("time new roman",15),bg="white").place(x=30,y=160)
    lbl_price=Label(product_Frame,text="price",font=("time new roman",15),bg="white").place(x=30,y=210)
    lbl_quntity=Label(product_Frame,text="Quantity",font=("time new roman",15),bg="white").place(x=30,y=260)
    lbl_status=Label(product_Frame,text="Status",font=("time new roman",15),bg="white").place(x=30,y=310)

   # txt_category=Label(product_Frame,text="category",font=("time new roman",15),bg="white").place(x=30,y=60)
    #============ column2 =============================================
    cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_cat.place(x=150,y=60,width=200)
    #cmb_cat.current(0)
    
    cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_sup.place(x=150,y=110,width=200)
    #cmb_sup.current(0)

    txt_name=Entry(product_Frame,textvariable=self.var_name,font=("time new roman",15),bg="lightyellow").place(x=150,y=160,width=200)
    txt_price=Entry(product_Frame,textvariable=self.var_price,font=("time new roman",15),bg="lightyellow").place(x=150,y=210,width=200)
    txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("time new roman",15),bg="lightyellow").place(x=150,y=260,width=200)

    cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_status.place(x=150,y=310,width=200)
    cmb_status.current(0)

    #================== buttons ===============================
    btn_add=Button(product_Frame,text="Save",command=self.add,font=("time new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=5,y=400,width=100,height=28)

    btn_update=Button(product_Frame,text="Update",font=("time new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=110,y=400,width=100,height=28)

    btn_delete=Button(product_Frame,text="Delete",font=("time new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=224,y=400,width=100,height=28)

    btn_clear=Button(product_Frame,text="Clear",font=("time new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=338,y=400,width=100,height=28)

    #========== search frame =====================================
    SearchFrame=LabelFrame(self.root,text="Search Product",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="white",fg="blue")
    SearchFrame.place(x=520,y=10,width=600,height=80)

    #=================== option =================================
    cmb_search=ttk.Combobox(SearchFrame,textvariable=self.Var_searchby,values=("select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("time new roman",15))
    cmb_search.place(x=10,y=10,width=180)
    cmb_search.current(0)

    text_search=Entry(SearchFrame,textvariable=self.Var_searchtxt,font=("time new roman",15),bg="lightyellow").place(x=200,y=10)
    btn_search=Button(SearchFrame,text="search",font=("time new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=7,width=150,height=30)

    #=========== Product Detail ==============================================
    p_frame=Frame(self.root,bd=3,relief=RIDGE)
    p_frame.place(x=520,y=100,width=600,height=390)

    scrolly=Scrollbar(p_frame,orient=VERTICAL)
    scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

    self.product_table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.product_table.xview)
    scrolly.config(command=self.product_table.yview)
    self.product_table.heading("pid",text="P ID")
    self.product_table.heading("Category",text="Category")
    self.product_table.heading("Supplier",text="Supplier")
    self.product_table.heading("name",text="Name")
    self.product_table.heading("price",text="Price")
    self.product_table.heading("qty",text="Qty")
    self.product_table.heading("status",text="Status")

    self.product_table["show"]="headings"

    self.product_table.column("pid",width=90)
    self.product_table.column("Category",width=100)
    self.product_table.column("Supplier",width=100)
    self.product_table.column("name",width=100)
    self.product_table.column("price",width=100)
    self.product_table.column("qty",width=100)
    self.product_table.column("status",width=100)
    
    self.product_table["show"]="headings"
    self.product_table.pack(fill=BOTH,expand=1)
    
    #self.show()
    
#========================================backend====================================
#====================Added function ====================================================
 def fetch_cat_sup(self):
    self.cat_list.append("Empty")
    self.sup_list.append("Empty")
     
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        cur.execute("select name from category")
        cat=cur.fetchall()
        if len(cat)>0:
            del self.cat_list[:]
            self.cat_list.append("Select")
            for i in cat:
                self.cat_list.append(i[0])
            
        cur.execute("select name from supplier")
        sup=cur.fetchall()
        if len(sup)>0:
            del self.sup_list[:]
            self.sup_list.append("Select")
            for i in sup:
                self.sup_list.append(i[0])
        
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 
 def add(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        if self.var_cat.get()=="select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="select" or self.var_name.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
                
        else:
            cur.execute("select *from product where name=?",(self.var_name.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Product already present,try different",parent=self.root)
            else:
                cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                            self.var_cat.get(),
                                            self.var_sup.get(),
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_qty.get(),
                                             
                                            self.var_status.get(),
                   ))
                connection.Commit()
                messagebox.showinfo("success","Product Added Successfully",parent=self.root)
                self.show()

    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
 def show(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        cur.execute("select *from supplier")
        rows=cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
            self.product_table.insert('',END,values=row)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
 def get_data(self,ev):
    f=self.product_table.focus()
    content=(self.product_table.item(f))
    row=content['values']
    print(row)
    self.Var_pid.set(row[0])
    self.var_sup.set(row[1])
    self.var_cat.set(row[2])
 
    self.var_name.set(row[3])
    self.var_price.set(row[4])
    self.var_qty.set(row[5])
    self.var_status.set(row[6])
    
 def update(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        if self.Var_pid.get()=="":
            messagebox.showerror("Error","please select product from list",parent=self.root)
                
        else:
            cur.execute("select *from product where pid=?",(self.Var_pid.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid product",parent=self.root)
            else:
                cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                            self.var_cat.get(),
                                            self.var_sup.get(),
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_qty.get(),
                                             
                                            self.var_status.get(),
                                            self.Var_pid.get()
                   ))
                connection.Commit()
                messagebox.showinfo("success","Product Updated Successfully",parent=self.root)
                self.show()
                #con.close()

    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
 def delete(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        if self.Var_pid.get()=="":
            messagebox.showerror("Error","Select Product from the list",parent=self.root)
                
        else:
            cur.execute("select *from product where pid=?",(self.Var_pid.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Product",parent=self.root)
            else:
                op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                    cur.execute("delete from product whrere pid=?",(self.Var_pid.get(),))
                    connection.commit()
                    messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                    self.clear()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
 def clear(self):
    self.var_cat.set("")
    self.var_sup.set("")
    self.var_name.set("")
    self.var_price.set("")
    self.var_qty.set("")
                                             
    self.var_status.set("")
    self.Var_pid.set("")
    self.Var_searchtxt.set("")
    self.Var_searchby.set("Select")
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
            cur.execute("select *from product where "+self.Var_searchby.get()+" LIKE '%"+self.Var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:

               self.product_table.delete(*self.product_table.get_children())
               for row in rows:
                  self.product_table.insert('',END,values=row)
            else:
               messagebox.showerror("error","No record found!!!",parent=self.root)
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
     root=Tk()
     obj=productClass(root)
     root.mainloop()