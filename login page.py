from contextlib import redirect_stderr
from itertools import product
from multiprocessing import connection
from tkinter import*
from tkinter import font
from tkinter import messagebox
import cx_Oracle
import os
from PIL import ImageTk
from singup import singupClass
from Dashboard import IMS
class Login_System:
    def __init__(self,root):
        self.roots=root
        self.roots.title("Login_System || Developed By Sumit")
        self.roots.geometry("1350x700+0+0")
        self.roots.config(bg="Cyan")
        #========== images =================
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.roots,image=self.phone_image,bd=0).place(x=200,y=50)
        self.roots.config(bg="white")
        #=========Login frame ======================
        self.employee_id=StringVar()
        self.password=StringVar()
        login_Frame=Frame(self.roots,bd=2,relief=RIDGE,bg="white")
        login_Frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_Frame,text="Login System",font=("time new roman",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        #=========employee_id ====================
        lbl_user=Label(login_Frame,text="User Name/Email",font=("time new roman",15,"bold"),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        self.username=Entry(login_Frame,textvariable=self.username,font=("times new roman",15),bg="lightyellow")
        self.username.place(x=50,y=140)

        lbl_pass=Label(login_Frame,text="Password",font=("time new",15,"bold"),bg="white",fg="#767171").place(x=50,y=200)
        self.password=Entry(login_Frame,textvariable=self.password,show="*",font=("times new roman",15),bg="lightyellow")
        self.password.place(x=50,y=240)

        btn_login=Button(login_Frame,text="Log in",command=self.login,font=("time new roman",15),bg="blue",activebackground="blue",fg="white",bd=0,activeforeground="white",cursor="hand2").place(x=50,y=300,width=210,height=35)
        hr=Label(login_Frame,bg="green").place(x=50,y=370,width=250,height=2)
        or_=Label(login_Frame,text="OR",bg="white",fg="green",font=("time new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_Frame,text="Forget Password",font=("time new roman",13),bg="white",fg="black",bd=0,activebackground="white",activeforeground="black").place(x=100,y=390)

        register_Frame=Frame(self.roots,bd=2,relief=RIDGE,bg="red")
        register_Frame.place(x=650,y=570,width=350,height=60)
        btn_singnup=Button(register_Frame,text="Sign Up",command=self.singup,font=("time new roman",15,"bold"),bg="red",activebackground="red",fg="white",activeforeground="white",cursor="hand2").place(x=2,y=0,width=350,height=60)

        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.roots,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
#================ animation ===========================================
        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im 
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def singup(self):
        self.new_win=Toplevel(self.roots)
        self.new_win=singupClass(self.new_win)
        
    def login(self):
        flag=0
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error!","All Field are required",parent=self.root)
        elif self.username.get()!='' and self.password.get()!='':
            connection=cx_Oracle.connect('sumit/abhinav')
            cur=connection.cursor()
            cur.execute("select * from singup")
            row=cur.fetchall()
            for i in row:
                if(self.username.get()==i[3]) and (self.password.get()==i[4]):
                    print('user has accessed the system')
                    flag=1
                    break
            if(flag==1):
                print('user has accessed the system')
                self.redirect_windows()
            else:
                messagebox.showerror("Error")
            
    def redirect_windows(self):
        self.roots.destroy()
        root=Tk()
        obj=IMS(root)
        root.mainloop()
        
        


    
#=============== forget password ============================================
#def forget_window(self):

if __name__=="__main__":
    root=Tk()
    obj=Login_System(root)
    root.mainloop()