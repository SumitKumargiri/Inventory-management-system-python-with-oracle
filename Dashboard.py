import bdb
from ctypes import resize
from tkinter import *
from turtle import width
from PIL import Image,ImageTk #pip install pillow 
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
  def __init__(self,root):
    self.root=root
    self.root.geometry('1350x700+0+0')
    self.root.title("inventory management system ||  developed By 4S")
    self.root.config(bg="Cyan")
    
#     self.bg=ImageTk.PhotoImage(file="images/10158.jpg")
#     lbl_bg=Label(self.root,image=self.bg,padx=100,pady=200)
#     lbl_bg.place(x=190,y=100,width=1360,height=650)

    self.im1=Image.open("images/img1.png")
    self.im1=self.im1.resize((1500,710),Image.ANTIALIAS)
    self.im1=ImageTk.PhotoImage(self.im1)

    self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
    self.lbl_im1.place(x=50,y=20)

    #======================= Title ======================================
    self.icon_title=PhotoImage(file="images/logo1.png")
    title=Label(self.root,text="Inventory management System",image=self.icon_title,compound=LEFT,font=("times new roman",44,"bold"),bg="Blue",fg="white",anchor="w",padx=100).place(x=0,y=0,relwidth=1,height=70)

   #======================btn logout =======================================
    btn_logout=Button(self.root,text="Logout",font=("times new roman",11,"bold"),bg="orange",bd=5).place(x=1300,y=10,height=60,width=160)
    #================== clock ===============================================
    self.lbl_clock=Label(self.root,text="Welcome to Inventory management system\t\t Date=: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",20),bg="orangered",fg="white",bd=5)
    self.lbl_clock.place(x=0,y=70,relwidth=1,height=32)

    #================ Left menu ===================================================
    self.MenuLogo=Image.open("images/menu_im.png")
    self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
    self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

    Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="Silver")
    Leftmenu.place(x=0,y=102,width=200,height=660)
    
    lbl_menuLogo=Label(Leftmenu,image=self.MenuLogo)
    lbl_menuLogo.pack(side=TOP,fill=X)

    lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="crimson").pack(side=TOP,fill=X)
    btn_Employee=Button(Leftmenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)
    btn_supplier=Button(Leftmenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)
    btn_category=Button(Leftmenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)
    btn_product=Button(Leftmenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)
    btn_sales=Button(Leftmenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)
    btn_exit=Button(Leftmenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=5,cursor="hand2").pack(side=TOP,fill=X)

    #================== content ================================================
    self.lbl_employee=Label(self.root,text="Total Employee \n[ 0 ]",bd=5,relief=RIDGE,bg="olive",fg="white",font=("time new roman",11,"bold"))
    self.lbl_employee.place(x=300,y=120,height=150,width=300)

    self.lbl_supplier=Label(self.root,text="Total Supplier \n[ 0 ]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("time new roman",11,"bold"))
    self.lbl_supplier.place(x=650,y=120,height=150,width=300)

    self.lbl_category=Label(self.root,text="Total Category \n[ 0 ]",bd=5,relief=RIDGE,bg="lightgreen",fg="white",font=("time new roman",11,"bold"))
    self.lbl_category.place(x=1000,y=120,height=150,width=300)

    self.lbl_product=Label(self.root,text="Total Product \n[ 0 ]",bd=5,relief=RIDGE,bg="green",fg="white",font=("time new roman",11,"bold"))
    self.lbl_product.place(x=460,y=300,height=150,width=300)

    self.lbl_sales=Label(self.root,text="Total Sales \n[ 0 ]",bd=5,relief=RIDGE,bg="brown",fg="white",font=("time new roman",11,"bold"))
    self.lbl_sales.place(x=850,y=300,height=150,width=300)
    #================== footer ===============================================
    lbl_footer=Label(self.root,text="IMS.Inventory Management System || Developed by 4S\nfor any technical issue contact: 910XXXXX13 ",font=("times new roman",12),bg="deepskyblue",fg="white",bd=10).pack(side=BOTTOM,fill=X)
    #============================================================================
    
  def employee(self):
    self.new_win=Toplevel(self.root)
    self.new_win=employeeClass(self.new_win)

  def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

  def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

        
  def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

        
  def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
