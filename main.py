from tkinter import messagebox
import customtkinter
import customtkinter as ctk
import tkinter as tk
import pyshorteners

w=customtkinter.CTk()
w.title('URL Shorten')
w.geometry('500x350+650+150')


def shorten():
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(txt1.get())
    print=(txt2.insert(0,short_url))
def reset():
    txt1.delete(0,'end')
    txt1.focus()
def refresh():
    txt1.delete(0,'end')
    txt2.delete(0,'end')
    txt1.focus()
def copy():
    text=txt2.get()
    w.clipboard_clear()
    w.clipboard_append(text)
    b2.configure(text="copied",state="disabled")

label=customtkinter.CTkLabel(master=w,text='URL Shortener',font=('Ubuntu', 30,'bold'))
label.place(x=150,y=30)

txt1=customtkinter.CTkEntry(w,width=200,height=20,placeholder_text="enter long url",font=('Trebuchet MS', 22,'bold'))
txt1.place(x=150,y=100)

label2=customtkinter.CTkLabel(master=w,text='short URL',font=('Trebuchet MS', 24,'bold'))
label2.place(x=190, y=160)

txt2=customtkinter.CTkEntry(master=w,width=200,font=('Trebuchet MS', 22,'bold'))
txt2.place(x=150, y=200)

b=customtkinter.CTkButton(master=w, text='Short',width=150,height=40,font=('Trebuchet MS', 18,'bold'),command=shorten)
b.place(x=110,y=265)
b1=customtkinter.CTkButton(master=w, text='X',width=40,height=35,font=('Trebuchet MS', 18,'bold'),fg_color="red",command=reset)
b1.place(x=360,y=100)
b2=customtkinter.CTkButton(master=w, text='copy',width=80,height=35,font=('Trebuchet MS', 18,'bold'),command=copy)
b2.place(x=360,y=200)
b3=customtkinter.CTkButton(master=w, text='reset',width=150,height=40,font=('Trebuchet MS', 18,'bold'),command=refresh)
b3.place(x=270,y=265)

w.mainloop()
