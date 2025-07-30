import os
import tkinter
import tkinter as t

import CTkMessagebox
import customtkinter as tk

from customtkinter import *
from tkinter import *
from PIL import ImageTk,Image

from CustomTkinterMessagebox import CTkMessagebox
import pymysql
from CTkMessagebox import CTkMessagebox
import random
import pywhatkit





os.environ['TCL_LIBRARY']='C:\\Users\\gokul\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tcl8.6'
os.environ['TK_LIBRARY']='C:\\Users\\gokul\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tk8.6'

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
a=tk.CTk()
a.geometry("1920x1080")


bg_image= Image.open("3391464.jpg")
g_icon=Image.open("google-icon.png")
mail_icon=Image.open("email.png")
phone=Image.open("phone-call.png")
na=Image.open("write.png")
male=Image.open("man.png")
female=Image.open("female-worker.png")
frame2_bg=Image.open("19187761.jpg")
otp_v=Image.open("mobile-banking.png")
lock=Image.open("lock.png")
back_b=Image.open("back (1).png")
p_a=Image.open("otp.png")
bg2=Image.open("3391464.jpg")
bg=Image.open("bg.jpg")



b=CTkImage(dark_image=bg,light_image=bg,size=(1920,1080))
login_bg=CTkImage(dark_image=bg2,light_image=bg2,size=(1920,1080))
p=CTkImage(dark_image=p_a,light_image=p_a,size=(30,30))
ba=CTkImage(dark_image=back_b,light_image=back_b,size=(30,30))
bg=CTkImage(dark_image=bg_image,light_image=bg_image,size=(960,1080))
g=CTkImage(dark_image=g_icon,light_image=g_icon,size=(25,25))
mai=CTkImage(dark_image=mail_icon,light_image=mail_icon,size=(30,30))
pho=CTkImage(dark_image=phone,light_image=phone,size=(30,30))
n=CTkImage(dark_image=na,light_image=na,size=(30,30))
ma=CTkImage(dark_image=male,light_image=male,size=(30,30))
fe=CTkImage(dark_image=female,light_image=female,size=(30,30))
bg_frame2=CTkImage(dark_image=frame2_bg,light_image=frame2_bg,size=(1920,1080))
v_otp=CTkImage(dark_image=otp_v,light_image=otp_v,size=(150,150))
lo=CTkImage(dark_image=lock,light_image=lock,size=(30,30))


def clear():
    for i in frame1.winfo_children():
        i.destroy()



def pass_reset():
    def change_password():
        if mail_id.get()=="" or new_pass.get()=="" or confirm_pass.get()=="":
            CTkMessagebox(title="ERROR", message="All Fields Are Required", icon="multiply.png", option_1="ok",master=frame9)
        elif new_pass.get()!=confirm_pass.get():
            CTkMessagebox(title="ERROR", message="Password and Confirm Password are not matching", icon="multiply.png", option_1="ok",master=frame9)
        else:
            con = pymysql.connect(host="localhost", user="root", password="gokul123", port=3306,database="userdata")
            cu= con.cursor()
            query="select * from data where email=%s"
            cu.execute(query,(mail_id.get()))
            row=cu.fetchone()
            if row==None:
                CTkMessagebox(title="ERROR", message="Incorrect email ID", icon="multiply.png", option_1="ok",master=frame9)
            else:
                query="update data set password=%s where email=%s"
                cu.execute(query,(new_pass.get(),mail_id.get()))
                con.commit()
                con.close()
                CTkMessagebox(title="succes", message="SUCCESSFULLY CHANGED", option_1="ok", icon="check.png",master=frame9)
                clear()
                loginframe()

    frame9= CTkFrame(frame1, fg_color="blue")
    frame9.pack(side=tk.LEFT, fill=tk.BOTH)
    frame9.configure(width=2000)

    d = CTkLabel(frame9, text="", image=b)
    d.place(x=0, y=0)
    headline = CTkLabel(frame9, text="RESET PASSWORD", font=("Arial Bold", 25), fg_color="white", bg_color="magenta2",
                        text_color="magenta2")
    headline.place(x=1255, y=200)
    id = CTkLabel(frame9, text=" Enter Email", font=("Arial Bold", 25), fg_color="white", bg_color="magenta2",
                  text_color="orchid1")
    id.place(x=1100, y=300)

    mail_id = CTkEntry(frame9, width=500, height=30, fg_color="white", bg_color="white", font=("Arial", 22, "bold"),
                       border_width=0, text_color="black")
    mail_id.place(x=1100, y=365)

    CTkFrame(frame9, width=500, height=5, fg_color="orchid1", bg_color="orchid1").place(x=1100, y=393)

    new = CTkLabel(frame9, text="New Password", font=("Arial Bold", 25), fg_color="white", bg_color="magenta2",
                   text_color="orchid1")
    new.place(x=1100, y=450)

    new_pass = CTkEntry(frame9, width=500, height=30, fg_color="white", bg_color="white", font=("Arial", 22, "bold"),
                        border_width=0, text_color="black")
    new_pass.place(x=1100, y=515)

    CTkFrame(frame9, width=500, height=5, fg_color="orchid1", bg_color="orchid1").place(x=1100, y=543)

    cof = CTkLabel(frame9, text="Confirm Password", font=("Arial Bold", 25), fg_color="white", bg_color="magenta2",
                   text_color="orchid1")
    cof.place(x=1100, y=600)

    confirm_pass = CTkEntry(frame9, width=500, height=30, fg_color="white", bg_color="white",
                            font=("Arial", 22, "bold"), border_width=0, text_color="black")
    confirm_pass.place(x=1100, y=665)

    CTkFrame(frame9, width=500, height=5, fg_color="orchid1", bg_color="orchid1").place(x=1100, y=693)

    submit_Button = CTkButton(frame9, width=400, height=50, corner_radius=10, text="SUBMIT", text_color="white",
                              bg_color="white", fg_color="magenta2", font=("Arial Bold", 20),command=lambda :[(change_password())])
    submit_Button.place(x=1150, y=770)




def login_user():
    if mail_entry.get()=="" or pass_entry.get()=="":
        CTkMessagebox(title="ERROR", message="All Fields Are Required", option_1="ok",
                      icon="multiply.png")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="gokul123", port=3306)
            cu = con.cursor()
        except:
            CTkMessagebox(title="ERROR", message="Database connectivity issue,Please Try Again", option_1="ok",icon="lightbulb.png")
            return
        query="use userdata"
        cu.execute(query)
        query="select * from data where email=%s and password=%s"
        cu.execute(query,(mail_entry.get(),pass_entry.get()))
        row=cu.fetchone()
        if row==None:
            CTkMessagebox(title="ERROR", message="Invalid Email and Password", option_1="ok",
                          icon="multiply.png")
        else:
            CTkMessagebox(title="Welcome",message="Login sucessful", option_1="ok",
                          icon="check.png")







def loginframe():
    global mail_entry
    global pass_entry
    frame_3 = CTkFrame(frame1, bg_color="#EEEEEE")
    frame_3.pack(side=tk.LEFT, fill=tk.BOTH)
    frame_3.configure(width=2000)
    z= CTkLabel(frame1, text="", image=login_bg)
    z.place(x=0, y=0)
    frame3=CTkFrame(z,width=680,height=670,corner_radius=15,fg_color="#ffffff",border_color="#ffffff")
    frame3.place(x=620, y=220)
    w=CTkLabel(frame3,text="Welcome Back!",text_color="#601E88",font=("Arial Bold",35))
    w.place(x=80,y=80)
    s=CTkLabel(frame3,text="Sign in to your account", text_color="#7E7E7E",font=("Arial Bold",15))
    s.place(x=80,y=140)
    mail_entry=CTkEntry(frame3,width=480,height=50,corner_radius=10,border_color="#601E88",border_width=5,text_color="#000000",fg_color="#EEEEEE")
    mail_entry.place(x=80,y=250)
    pass_entry = CTkEntry(frame3, width=480, height=50, corner_radius=10, border_color="#601E88", border_width=5,text_color="#000000", fg_color="#EEEEEE")
    pass_entry.place(x=80, y=380)
    b3= tk.CTkButton(frame3, width=425, height=50, text="Login", corner_radius=12, fg_color="#4158D0",hover_color="#C850C0", font=("Arial Bold", 18),command=lambda :[(login_user())])
    b3.place(x=110, y=490)
    b4 = tk.CTkButton(frame3, width=425, height=50, text="Continue With Google", corner_radius=12, fg_color="#EEEEEE",hover_color="#EEEEEE",text_color="#601E88", font=("Arial Bold", 18),image=g,compound="left",border_width=1,border_color="black")
    b4.place(x=110, y=560)
    mail2 = CTkLabel(frame3, text=" Email:", text_color="#601E88", font=("Arial Bold", 22), image=mai, compound="left")
    mail2.place(x=80, y=215)
    password2 = CTkLabel(frame3, text="Enter Password:", text_color="#601E88", font=("Arial Bold",22), image=lo,compound="left")
    password2.place(x=80, y=345)
    login_button=tkinter.Button(frame3,text="Forgot Password?",font=("Arial Bold",13),cursor="hand2",bd=0,bg="white",activebackground="#ffffff",activeforeground="#7E7E7E",fg="#7E7E7E",command=lambda :[(clear(),pass_reset())])
    login_button.place(x=400,y=430)



def verification():
    if mobile.get()=="":
        CTkMessagebox(title="ERROR", message="Enter mobile number", option_1="ok",
                      icon="multiply.png")
    else:
        global no
        no=str(random.randint(1000,9000))
        p=mobile.get()
        o=otp.get()
        pywhatkit.sendwhatmsg_instantly(p,no)





def submit():
    print(no)

    if no==otp.get():
        CTkMessagebox(title="SUCCESS", message="Verification Completed successfully", option_1="ok",
                      icon="check.png")
        clear()
        loginframe()

    else:
        CTkMessagebox(title="ERROR", message="Invalid OTP", option_1="ok",
                      icon="multiply.png")





def frame2():
    global mobile
    global otp
    frame0=CTkFrame(frame1,bg_color="#601E88")
    frame0.pack(side=tk.LEFT,fill=tk.BOTH)
    frame0.configure(width=2000)

    y= CTkLabel(frame0, text="", image=bg_frame2)
    y.place(x=0, y=0)

    frame2=tk.CTkFrame(frame0,width=780,height=680,corner_radius=25,border_color="#ffffff",fg_color="#ffffff")
    frame2.place(x=550,y=220)

    otp=(CTkEntry(frame2,width=550,height=45,corner_radius=15,border_width=5,border_color="#601E88",fg_color="#ffffff",text_color="#000000"))
    otp.place(x=122,y=500)

    mobile = CTkEntry(frame2, width=550, height=45, corner_radius=15, border_width=5, border_color="#601E88",fg_color="#ffffff", text_color="#000000")
    mobile.place(x=122, y=380)
    lable1= CTkLabel(frame2, text=" Enter phone no:", text_color="#601E88", font=("Arial Bold", 20), image=pho, compound="left")
    lable1.place(x=122, y=340)
    h1= CTkLabel(frame2, text="(Enter with country+)", text_color="#7E7E7E", font=("Arial Bold", 15))
    h1.place(x=313, y=342)

    su=CTkButton(frame2,text="Submit",width=200,height=40,fg_color="#4158D0",hover_color="#C850C0",corner_radius=32,font=("Arial Bold",25),command=lambda :[(submit())])
    su.place(x=460,y=600)
    v=CTkLabel(frame2,text="",image=v_otp)
    v.place(x=325,y=48)
    o=CTkLabel(frame2,text="OTP Verification",text_color="#601E88",font=("Arial Bold",40))
    o.place(x=248,y=225)
    en=CTkLabel(frame2,text=" Enter OTP:",text_color="#601E88",font=("Arial Bold",20),image=n,compound="left")
    en.place(x=122,y=450)
    back=tk.CTkButton(frame2, width=80,height=40, text="", corner_radius=32, fg_color="#EEEEEE",hover_color="#EEEEEE", text_color="#601E88", font=("Arial Bold", 18),image=ba,command=lambda :[(clear(),d_frame1())])
    back.place(x=25,y=25)
    generate=tk.CTkButton(frame2,width=80,height=40,text="Genrate OTP",fg_color="#4158D0",hover_color="#C850C0",corner_radius=32,font=("Arial Bold",25),image=p)
    generate.place(x=122,y=600)





def database():
    if name_entry.get() == '' or phone_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        CTkMessagebox(title="ERROR",message="All Fields Are Required",icon="multiply.png",option_1="ok")

    elif checkbox.get() == 0:
        CTkMessagebox(title="ERROR",message="Please Accpect Tearms & and Condition",option_1="ok",icon="multiply.png")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="gokul123", port=3306)
            cu = con.cursor()
        except:
            CTkMessagebox(title="ERROR", message="Database connectivity issue,Please Try Again", option_1="ok",icon="lightbulb.png")
            return
        try:

            query = "create database userdata"
            cu.execute(query)
            query = "use userdata"
            cu.execute(query)
            query = "create table data(id int auto_increment primary key not null,name varchar(50),phone_no varchar(20),email varchar(50),password varchar(20),gender varchar (10))"
            cu.execute(query)
        except:
            cu.execute("use userdata")
        query="select * from data where email=%s"
        cu.execute(query,(email_entry.get()))
        row=cu.fetchone()
        if row !=None:
            CTkMessagebox(title="ERROR", message="Email ID Already exists", option_1="ok",
                          icon="multiply.png")
        else:
            query = "insert into data(name,phone_no,email,password,gender) values(%s,%s,%s,%s,%s)"
            cu.execute(query,(name_entry.get(), phone_entry.get(), email_entry.get(), password_entry.get(),radio_var.get()))
            con.commit()
            con.close()
            CTkMessagebox(title="succes", message="Registration Succesful", option_1="ok",icon="check.png")
            clear()
            frame2()





def d_frame1():
    frame = CTkFrame(a, bg_color="black")
    frame.pack(side=tk.LEFT, fill=tk.BOTH)
    frame.configure(width=2000)

    x = CTkLabel(frame1, text="", image=bg)
    x.place(x=0, y=0)

    c = tk.CTkFrame(frame1, width=960, height=1080, corner_radius=10, border_width=5, fg_color="#ffffff")
    c.place(x=960, y=0)

    d = CTkLabel(c, text="Welcome", text_color="#601E88", font=("Arial Bold", 35))
    d.place(x=425, y=30)
    ac = CTkLabel(c, text="Create a New Account", text_color="#601E88", font=("Arial Bold", 25))
    ac.place(x=365, y=100)

    name_entry = CTkEntry(c, width=600, height=50, corner_radius=15, border_width=5, fg_color="#EEEEEE",
                          border_color="#601E88", text_color="#000000", font=("Arial", 20))
    name_entry.place(x=200, y=275)
    name = CTkLabel(c, text=" Name:", text_color="#601E88", font=("Arial Bold", 25), image=n, compound="left")
    name.place(x=200, y=235)

    phone_entry = CTkEntry(c, width=600, height=50, corner_radius=15, border_width=5, fg_color="#EEEEEE",
                           border_color="#601E88", text_color="#000000", font=("Arial", 20))
    phone_entry.place(x=200, y=425)
    ph = CTkLabel(c, text=" Phone no:", text_color="#601E88", font=("Arial Bold", 25), image=pho, compound="left")
    ph.place(x=200, y=385)

    email_entry = CTkEntry(c, width=600, height=50, corner_radius=15, border_width=5, fg_color="#EEEEEE",
                           border_color="#601E88", text_color="#000000", font=("Arial", 20))
    email_entry.place(x=200, y=572)
    mail = CTkLabel(c, text=" Email:", text_color="#601E88", font=("Arial Bold", 25), image=mai, compound="left")
    mail.place(x=200, y=532)

    password_entry = CTkEntry(c, width=600, height=50, corner_radius=15, border_width=5, fg_color="#EEEEEE",
                              border_color="#601E88", text_color="#000000", font=("Arial", 20))
    password_entry.place(x=200, y=720)
    password = CTkLabel(c, text=" Create Password", text_color="#601E88", font=("Arial Bold", 25), image=lo,
                        compound="left")
    password.place(x=200, y=680)

    login_button = CTkButton(c, text="Login", width=100, height=20, corner_radius=32, fg_color="#4158D0",
                             hover_color="#C850C0", font=("Arial Bold", 15), command=lambda: [(database())])
    login_button.place(x=540, y=175)
    login = CTkLabel(c, text="Already have an account? ", text_color="black", font=("Courier New 12 Bold", 15))
    login.place(x=365, y=175)

    radio_var = tk.StringVar(value="gender")

    radio = CTkRadioButton(c, text="Male", value="male", text_color="#601E88", font=("Arial Bold", 20),
                           variable=radio_var)
    radio.place(x=350, y=795)
    male1 = CTkLabel(c, text="", image=ma)
    male1.place(x=435, y=795)

    radio2 = CTkRadioButton(c, text="Female", value="female", text_color="#601E88", font=("Arial Bold", 20),
                            variable=radio_var)
    radio2.place(x=530, y=795)
    f = CTkLabel(c, text="", image=fe)
    f.place(x=635, y=795)

    registration_button = tk.CTkButton(c, width=500, height=50, text="Create a Account", corner_radius=32,
                                       fg_color="#4158D0", hover_color="#C850C0", font=("Arial Bold", 18),
                                       command=lambda: [(clear(), frame2())])
    registration_button.place(x=250, y=900)

    google_button = tk.CTkButton(c, width=500, height=50, text="Continue With Google", corner_radius=32,
                                 fg_color="#EEEEEE", hover_color="#EEEEEE", text_color="#601E88",
                                 font=("Arial Bold", 18), border_width=1, border_color="black", image=g)
    google_button.place(x=250, y=980)

    checkbox = tk.IntVar()
    team_check = CTkCheckBox(c, checkbox_width=20, fg_color="#EEEEEE", checkmark_color="#601E88",
                             text="  I agree to the Terms & Condition ", variable=checkbox, text_color="#601E88",
                             border_color="black", font=("Microsoft Yahei UI Light", 18, "bold"))
    team_check.place(x=300, y=850)










frame1=CTkFrame(a,bg_color="black")
frame1.pack(side=tk.LEFT,fill=tk.BOTH)
frame1.configure(width=2000)

x=CTkLabel(frame1,text="",image=bg)
x.place(x=0,y=0)


c=tk.CTkFrame(frame1,width=960,height=1080,corner_radius=10,border_width=5,fg_color="#ffffff")
c.place(x=960,y=0)


d=CTkLabel(c,text="Welcome",text_color="#601E88",font=("Arial Bold", 35))
d.place(x=425,y=30)
ac=CTkLabel(c,text="Create a New Account",text_color="#601E88",font=("Arial Bold",25))
ac.place(x=365,y=100)

name_entry=CTkEntry(c,width=600,height=50,corner_radius=15,border_width=5,fg_color="#EEEEEE",border_color="#601E88",text_color="#000000",font=("Arial",20))
name_entry.place(x=200,y=275)
name=CTkLabel(c,text=" Name:",text_color="#601E88",font=("Arial Bold",25),image=n,compound="left")
name.place(x=200,y=235)


phone_entry=CTkEntry(c,width=600,height=50,corner_radius=15,border_width=5,fg_color="#EEEEEE",border_color="#601E88",text_color="#000000",font=("Arial",20))
phone_entry.place(x=200,y=425)
ph=CTkLabel(c,text=" Phone no:",text_color="#601E88",font=("Arial Bold",25),image=pho,compound="left")
ph.place(x=200,y=385)



email_entry=CTkEntry(c,width=600,height=50,corner_radius=15,border_width=5,fg_color="#EEEEEE",border_color="#601E88",text_color="#000000",font=("Arial",20))
email_entry.place(x=200,y=572)
mail=CTkLabel(c,text=" Email:",text_color="#601E88",font=("Arial Bold",25),image=mai,compound="left")
mail.place(x=200,y=532)



password_entry=CTkEntry(c,width=600,height=50,corner_radius=15,border_width=5,fg_color="#EEEEEE",border_color="#601E88",text_color="#000000",font=("Arial",20))
password_entry.place(x=200,y=720)
password=CTkLabel(c,text=" Create Password",text_color="#601E88",font=("Arial Bold",25),image=lo,compound="left")
password.place(x=200,y=680)

login_button=CTkButton(c,text="Login",width=100,height=20,corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",font=("Arial Bold",15),command=lambda :[(clear(),loginframe())])
login_button.place(x=540,y=175)
login=CTkLabel(c,text="Already have an account? ",text_color="black",font=("Courier New 12 Bold",15))
login.place(x=365,y=175)



radio_var=tk.StringVar(value="gender")

radio=CTkRadioButton(c,text="Male",value="male",text_color="#601E88",font=("Arial Bold",20),variable=radio_var)
radio.place(x=350,y=795)
male1=CTkLabel(c,text="",image=ma)
male1.place(x=435,y=795)


radio2=CTkRadioButton(c,text="Female",value="female",text_color="#601E88",font=("Arial Bold",20),variable=radio_var)
radio2.place(x=530,y=795)
f=CTkLabel(c,text="",image=fe)
f.place(x=635,y=795)


registration_button=tk.CTkButton(c,width=500,height=50,text="Create a Account",corner_radius=32,fg_color="#4158D0",hover_color="#C850C0",font=("Arial Bold",18),command=lambda:[(database())])
registration_button.place(x=250,y=900)

google_button=tk.CTkButton(c,width=500,height=50,text="Continue With Google",corner_radius=32,fg_color="#EEEEEE",hover_color="#EEEEEE",text_color="#601E88",font=("Arial Bold",18),border_width=1,border_color="black",image=g)
google_button.place(x=250,y=980)


checkbox=tk.IntVar()
team_check=CTkCheckBox(c,checkbox_width=20,fg_color="#EEEEEE",checkmark_color="#601E88",text="  I agree to the Terms & Condition ",variable=checkbox,text_color="#601E88",border_color="black",font=("Microsoft Yahei UI Light",18,"bold"))
team_check.place(x=300,y=850)








a.mainloop()