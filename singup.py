# from email.errors import MessageParseError
# from inspect import getargvalues
# from textwrap import fill
from cProfile import label
from email.mime import image
from json import load
from msilib import text
from tkinter import *
from tkinter import messagebox
from turtle import left, title
from PIL import Image,ImageTk #pip install pillow 
import cx_Oracle

#def getvals():
       # print("Accepted")
class singupClass:
    def __init__(self,root):
        self.roots=root
        self.roots.geometry('1350x700+0+0')
        self.roots.title("singup")
        self.roots.config(bg="Cyan")
#========= singup frame ===============
        frame=Frame(self.roots,bg="orange",bd=10)
        frame.place(x=600,y=60,width=600,height=550)
    
        self.MenuLogo=Image.open("images/img7.png")
        self.MenuLogo=self.MenuLogo.resize((560,550),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        lbl_menuLogo=Label(self.roots,image=self.MenuLogo)
        lbl_menuLogo.place(x=4,y=60)

    
        fname=StringVar()
        title=Label(frame,text="SINGUP HERE",font=("time new roman",30,"bold"),bg="orange",fg="blue").place(x=150,y=10)
        f_name=Label(frame,text="First Name",font=("time new roman",15,"bold"),bg="orange").place(x=50,y=80)
        self.f_name=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=fname)
        self.f_name.place(x=20,y=120)
    
        lname=StringVar()
        last_name=Label(frame,text="Last Name",font=("time new roman",15,"bold"),bg="orange").place(x=420,y=80)
        self.last_name=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=lname)
        self.last_name.place(x=350,y=120)
    
        contact1=StringVar()
        contact=Label(frame,text="Contact",font=("time new roman",15,"bold"),bg="orange").place(x=50,y=200)
        self.contact=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=contact1)
        self.contact.place(x=20,y=240)
    
        email1=StringVar()
        email=Label(frame,text="Email",font=("time new roman",15,"bold"),bg="orange").place(x=430,y=200)
        self.email=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=email1)
        self.email.place(x=350,y=240)
    
        password1=StringVar()
        password=Label(frame,text="Password",font=("time new roman",15,"bold"),bg="orange").place(x=50,y=320)
        self.password=Entry(frame,show="*",font=("time new roman",15),bg="lightyellow",textvariable=password1)
        self.password.place(x=20,y=360)
    
        password2=StringVar()
        c_password=Label(frame,text="Conform Password",font=("time new roman",15,"bold"),bg="orange").place(x=360,y=320)
        self.c_password=Entry(frame,show="*",font=("time new roman",15),bg="lightyellow",textvariable=password2)
        self.c_password.place(x=350,y=360)
        
       
   #============== submit ============================
        btn_submit=Button(frame,text="submit",command=self.sign,font=("times new roman",20),bg="green",fg="red",bd=5).place(x=230,y=430,height=50,width=120)
    
    
    #=====================backend=============================
    def sign(self):
        
        connection = cx_Oracle.connect('sumit/abhinav')
        cur = connection.cursor()
        
          
        f=self.f_name.get()
        l=self.last_name.get()
        c=self.contact.get()
        e=self.email.get()                                     
        p=self.password.get()
        c=self.c_password.get()
        cur.execute("insert into singup values(:fn,:ln,:us,:em,:pa,:c_pa)",{":fn":f,":ln":l,":us":c,":em":e,":pa":p,":c_pa":c})
        cur.close()
        connection.commit()
        connection.close()
        messagebox.showinfo("Register Successful",parent=self.roots)
        
       
if __name__=="__main__":
    root=Tk()
    obj=singupClass(root)
    root.mainloop()
