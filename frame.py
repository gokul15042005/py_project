import os

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
from mysql.connector.opentelemetry.context_propagation import with_context_propagation

os.environ['TCL_LIBRARY']='C:\\Users\\gokul\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tcl8.6'
os.environ['TK_LIBRARY']='C:\\Users\\gokul\\AppData\\Local\\Programs\\Python\\Python313\\tcl\\tk8.6'

back=Image.open("k.jpg")
mail_icon=Image.open("email.png")
bg=Image.open("bg.jpg")
b=CTkImage(dark_image=bg,light_image=bg,size=(1920,1080))
mai=CTkImage(dark_image=mail_icon,light_image=mail_icon,size=(30,30))
bg_home=CTkImage(dark_image=back,light_image=back,size=(1920,1080))

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
a=tk.CTk()
a.geometry("1920x1080")

homeframe= CTkFrame(a, fg_color="blue")
homeframe.pack(side=tk.LEFT, fill=tk.BOTH)
homeframe.configure(width=2000)

CTkLabel(homeframe,text="",image=bg_home).grid()



a.mainloop()











