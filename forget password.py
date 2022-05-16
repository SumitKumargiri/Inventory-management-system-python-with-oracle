from tkinter import *
from PIL import Image,ImageTk #pip install pillow 
class forgetClass:
  def __init__(self,root):
    self.root=root
    self.root.geometry('1350x700+0+0')
    self.root.title("inventory management system ||  developed By 4s")
    self.root.config(bg="Cyan")
#==============================title============================
    frame=Frame(self.root,bg="lightgreen",bd=10)
    frame.place(x=600,y=60,width=600,height=550)

    title=Label(frame,text="Enter the Detail",font=("time new roman",30,"bold"),bg="lightgreen",fg="blue").place(x=150,y=10)
    uname=Label(frame,text="Username/Email",font=("time new roman",15,"bold"),bg="lightgreen").place(x=50,y=80)
    self.uname=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=uname)
    self.uname.place(x=50,y=120)

    password=Label(frame,text="Password",font=("time new roman",15,"bold"),bg="lightgreen").place(x=50,y=160)
    self.password=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=password)
    self.password.place(x=50,y=200)
    
    c_password=Label(frame,text="conform Password",font=("time new roman",15,"bold"),bg="lightgreen").place(x=50,y=240)
    self.c_password=Entry(frame,font=("time new roman",15),bg="lightyellow",textvariable=c_password)
    self.c_password.place(x=50,y=280)


    
    
if __name__=="__main__":
    root=Tk()
    obj=forgetClass(root)
    root.mainloop()
