from audioop import mul
from operator import index
from struct import pack
from textwrap import fill
from tkinter import *
import time
from tkinter import ttk,messagebox
from unicodedata import name
from unittest import result
from webbrowser import get
from PIL import Image,ImageTk #pip install pillow 
import cx_Oracle
class BillClass:
   def __init__(self,root):
    self.root=root
    self.root.geometry('1350x700+0+0')
    self.root.title("inventory management system ||  developed By Sumit")
    self.root.config(bg="Cyan")
    self.cart_list=[]

    #======================= Title ======================================
    self.icon_title=PhotoImage(file="images/logo1.png")
    title=Label(self.root,text="Inventory management System",image=self.icon_title,compound=LEFT,font=("times new roman",48,"bold"),bg="Blue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

   #======================btn logout =======================================
    btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="orange").place(x=1300,y=10,height=60,width=160)
    #================== clock ===============================================
    self.lbl_clock=Label(self.root,text="Welcome to Inventory management system\t\t Date=: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",20),bg="#4d636d",fg="white")
    self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

    #============ product frame ==========================
   
    #============ Search Frame ============================
    productFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
    productFrame1.place(x=6,y=110,width=410,height=550)

    pTitle=Label(productFrame1,text="All Product",font=("time new roman",20,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
#================ product search Frame ============================
    self.var_search=StringVar()
    productFrame2=Frame(productFrame1,bd=2,relief=RIDGE,bg="white")
    productFrame2.place(x=2,y=42,width=398,height=90)

    lbl_Search=Label(productFrame2,text="Search Product || By Name",font=("time new roman",15,"bold"),bg="white",fg="red").place(x=2,y=5)

    lbl_name=Label(productFrame2,text="Product Name",font=("time new roman",15,"bold"),bg="white",fg="red").place(x=0,y=45)

    lbl_Search=Label(productFrame2,text="Search Product || By Name",font=("time new roman",15,"bold"),bg="white",fg="red").place(x=2,y=5)
    txt_Search=Entry(productFrame2,textvariable=self.var_search,font=("time new roman",15),bg="lightyellow",fg="red").place(x=140,y=47,width=150,height=22)
    btn_search=Button(productFrame2,text="Search",command=self.search,font=("time new roman",15),bg="blue",fg="white",cursor="hand2").place(x=295,y=45,width=90,height=25)

    btn_show_all=Button(productFrame2,text="Show All",command=self.show,font=("time new roman",15),bg="orange",fg="white",cursor="hand2").place(x=295,y=10,width=90,height=25)
    #=========== Product Detail Frame ==============================================
    ProductFrame3=Frame(productFrame1,bd=3,relief=RIDGE)
    ProductFrame3.place(x=2,y=140,width=398,height=385)

    scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
    scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

    self.product_table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.product_table.xview)
    scrolly.config(command=self.product_table.yview)
    self.product_table.heading("pid",text=" PID")
    self.product_table.heading("name",text="Name")
    self.product_table.heading("price",text="Price")
    self.product_table.heading("qty",text="QTY")
    self.product_table.heading("status",text="Status")
    self.product_table["show"]="headings"

    self.product_table.column("pid",width=90)
    self.product_table.column("name",width=100)
    self.product_table.column("price",width=100)
    self.product_table.column("qty",width=100) 
    self.product_table.column("status",width=100)
    self.product_table.pack(fill=BOTH,expand=1)

    lbl_note=Label(productFrame1,text="Note:Enter 0 quantity to remove product from the cart",font=("time new roman",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

    #=================== Customer Frame ============================================
    self.var_cname=StringVar()
    self.var_contact=StringVar()
    CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
    CustomerFrame.place(x=420,y=110,width=530,height=70)
    ctitle=Label(CustomerFrame,text="Customer Details",font=("time new roman",15),bg="lightgray").pack(side=TOP,fill=X)
    lbl_name=Label(CustomerFrame,text="Name",font=("time new roman",15),bg="white",fg="red").place(x=5,y=35)
    txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("time new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

    lbl_contact=Label(CustomerFrame,text="Conatct No.",font=("time new roman",15),bg="white",fg="red").place(x=270,y=35)
    txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("time new roman",13),bg="lightyellow").place(x=380,y=35,width=140)
#====================Cal Cart button ==============
    Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
#==================== Calculatore Frame ==============
    self.var_cal_input=StringVar()
    Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
    Cal_Frame.place(x=5,y=10,width=268,height=340)
    txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("time new roman",15,"bold"),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
    txt_cal_input.grid(row=0,columnspan=4)
    
    btn_7=Button(Cal_Frame,text='7',font=("times new roman",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
    btn_8=Button(Cal_Frame,text='8',font=("times new roman",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
    btn_9=Button(Cal_Frame,text='9',font=("times new roman",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
    btn_sum=Button(Cal_Frame,text='+',font=("times new roman",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
    
    btn_4=Button(Cal_Frame,text='4',font=("times new roman",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
    btn_5=Button(Cal_Frame,text='5',font=("times new roman",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
    btn_6=Button(Cal_Frame,text='6',font=("times new roman",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
    btn_sub=Button(Cal_Frame,text='-',font=("times new roman",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
    
    btn_1=Button(Cal_Frame,text='1',font=("times new roman",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
    btn_2=Button(Cal_Frame,text='2',font=("times new roman",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
    btn_3=Button(Cal_Frame,text='3',font=("times new roman",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
    btn_mul=Button(Cal_Frame,text='*',font=("times new roman",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
    
    btn_0=Button(Cal_Frame,text='0',font=("times new roman",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
    btn_c=Button(Cal_Frame,text='c',font=("times new roman",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
    btn_eq=Button(Cal_Frame,text='=',font=("times new roman",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
    btn_div=Button(Cal_Frame,text='/',font=("times new roman",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

#==================== Cart Frame ==============
    cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
    cart_Frame.place(x=280,y=8,width=245,height=342)
    self.cartTitle=Label(cart_Frame,text="Cart Totalproduct:[0]",font=("time new roman",15),bg="lightgray")
    self.cartTitle.pack(side=TOP,fill=X)

    scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
    scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

    self.carttable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.carttable.xview)
    scrolly.config(command=self.carttable.yview)
    self.carttable.heading("pid",text=" PID")
    self.carttable.heading("name",text="Name")
    self.carttable.heading("price",text="Price")
    self.carttable.heading("qty",text="QTY")
    self.carttable["show"]="headings"

    self.carttable.column("pid",width=40)
    self.carttable.column("name",width=100)
    self.carttable.column("price",width=90)
    self.carttable.column("qty",width=40) 
    self.carttable.pack(fill=BOTH,expand=1)
    self.carttable.bind("<ButtonRelease-1>",self.get_data_cart)
#==================== ADD Cart Frame============================
    self.var_pid=StringVar()
    self.var_pname=StringVar()
    self.var_price=StringVar()
    self.var_qty=StringVar()
    self.var_stock=StringVar()

    Add_CarrdwidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    Add_CarrdwidgetsFrame.place(x=420,y=550,width=530,height=110)

    lbl_p_name=Label(Add_CarrdwidgetsFrame,text="Product Name",font=("time new roman",15),bg="white").place(x=5,y=5)
    txt_p_name=Entry(Add_CarrdwidgetsFrame,textvariable=self.var_pname,font=("time new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

    lbl_p_price=Label(Add_CarrdwidgetsFrame,text="Price per quanity",font=("time new roman",15),bg="white").place(x=230,y=5)
    txt_p_price=Entry(Add_CarrdwidgetsFrame,textvariable=self.var_price,font=("time new roman",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)

    lbl_p_qty=Label(Add_CarrdwidgetsFrame,text="quanity",font=("time new roman",15),bg="white").place(x=390,y=5)
    txt_p_qty=Entry(Add_CarrdwidgetsFrame,textvariable=self.var_qty,font=("time new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

    self.lbl_instock=Label(Add_CarrdwidgetsFrame,text="In Stock ",font=("time new roman",15),bg="white")
    self.lbl_instock.place(x=5,y=70)

    btn_clear_cart=Button(Add_CarrdwidgetsFrame,text="Clear",font=("time new roman",15),bg="green",cursor="hand2").place(x=180,y=70,width=150,height=30)
    btn_add_cart=Button(Add_CarrdwidgetsFrame,text="Add || Update",command=self.add_uppdate_cart,font=("time new roman",15),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

    #============== billing ================================================
    billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    billFrame.place(x=953,y=110,width=410,height=410)
    BTitle=Label(billFrame,text="Customer Bill Area",font=("time new roman",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
    scrolly=Scrollbar(billFrame,orient=VERTICAL)
    scrolly.pack(side=RIGHT,fill=Y)
    self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
    self.txt_bill_area.pack(fill=BOTH,expand=1)
    scrolly.config(command=self.txt_bill_area.yview)
    #================= billing buttons ==========================
    billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    billMenuFrame.place(x=953,y=520,width=410,height=140)

    self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("time new roman",15,"bold"),bg="#3f51b5",fg="white")
    self.lbl_amnt.place(x=2,y=5,width=120,height=70)
    self.lbl_discount=Label(billMenuFrame,text="Discount\n[5%]",font=("time new roman",15,"bold"),bg="#8bc34a",fg="white")
    self.lbl_discount.place(x=124,y=5,width=120,height=70)
    self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("time new roman",15,"bold"),bg="#607d8b",fg="white")
    self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

    btn_print=Button(billMenuFrame,text="Print",cursor="hand2",font=("time new roman",15,"bold"),bg="lightgreen",fg="white")
    btn_print.place(x=2,y=80,width=120,height=50)
    btn_clear=Button(billMenuFrame,text="Clear All",cursor="hand2",font=("time new roman",15,"bold"),bg="gray",fg="white")
    btn_clear.place(x=124,y=80,width=120,height=50)
    btn_generate=Button(billMenuFrame,text="Generate/save Bill",command=self.generate_bill,cursor="hand2",font=("time new roman",12,"bold"),bg="#009688",fg="white")
    btn_generate.place(x=246,y=80,width=160,height=50)
#=================== footer ===================
    lbl_footer=Label(self.root,text="IMS.Inventory Management System || Developed by Sumit\nfor any technical issue contact: 910XXXXX13 ",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
    #self.show()
    #self.bill_top()
#==================== All Function =======================================
#===================== get function ================================
   def get_input(self,num):
    xnum=self.var_cal_input.get()+str(num)
    self.var_cal_input.set(xnum)
       
   def clear_cal(self):
    self.var_cal_input.set('')
       
   def perform_cal(self):
    result=self.var_cal_input.get()
    self.var_cal_input.set(eval(result))
#===================== Show function ===============================       
   def show(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        cur.execute("select pid,name,price,qty,status from product")
        rows=cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
            self.product_table.insert('',END,values=row)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 #=============search function ================================================       
   def search(self):
    connection=cx_Oracle.connect('sumit/abhinav')
    cur=connection.Cursor()
    try:
        if self.var_search.get()=="":
            messagebox.showerror("error","Search input should be required",parent=self.root)
        else:
            cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:

               self.product_table.delete(*self.product_table.get_children())
               for row in rows:
                  self.product_table.insert('',END,values=row)
            else:
               messagebox.showerror("error","No record found!!!",parent=self.root)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        

   def get_data(self,ev):
    f=self.product_table.focus()
    content=(self.product_table.item(f))
    row=content['values']
    self.var_pid.set(row[0])
    self.var_pname.set(row[1])
    self.var_price.set(row[2])
    self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
    self.var_stock.set(row[3])
    self.var_qty.set('1')
    
    
   def get_data_cart(self,ev):
    f=self.carttable.focus()
    content=(self.carttable.item(f))
    row=content['values']
    self.var_pid.set(row[0])
    self.var_pname.set(row[1])
    self.var_price.set(row[2])
    self.var_qty.set(row[3])
    self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
    self.var_stock.set(row[4])
    
#=======================add and update function =======================
   def add_uppdate_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"please select product from the list",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
        else:
           # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
#===================update cart===========================
            present='no'
            index_=-1
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
                
            if present=='yes':
                op=messagebox.askyesno('confirm',"product already present\n Do you want to update| Remove from the Cart List",parent=self.root)
                if op==True:
                    if self .var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()

            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
#============bill update function =========
   def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
           self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt- self.discount
        self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_amnt.config(text=f'Net pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total product: [{str(len(self.cart_list))}]")

            
   def show_cart(self):
    try:
        self.carttable.delete(*self.carttable.get_children())
        for row in self.cart_list:
            self.carttable.insert('',END,values=row)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
#===== generate bill function =============
   def generate_bill(self):
    if self.var_cname.get()=='' or self.var_contact.get()=='':
        messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
    else:
        #=====Bill Top======
        self.bill_top() 
        #======Bill Middle =======
        self.bill_middle()
        #=====Bill Button =========
        self.bill_bottom()
        #pass

   def bill_top(self):
    invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
    #print(invoice)
    bill_top_temp=f'''
\t\txyz-Inventory
\t Phone No. 912820****,Amritsar-37330
{str("="*47)}
    product Name\t\t\tQTY\tprice
{str("="*47)}
    '''
    self.txt_bill_area.delete('1.0',END)
    self.txt_bill_area.insert('1.0',bill_top_temp)
    
   def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tRs.{self.bill_amnt}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
    '''
        self.txt_bill_area.insert('1.0',bill_bottom_temp)

   def bill_middle(self):
       for row in self.cart_list:
           name=row[1]
           qty=row[3]
           price=float(row[2])*int(row[3])
           price=str(price)
           self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)


           

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()