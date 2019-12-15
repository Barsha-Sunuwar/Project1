from tkinter import *
from stegano import lsb
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import datetime
import re
def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir="/root/Desktop/images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
    path = filename

def encrpt_ok(path,message):
    hide=lsb.hide(path,message)
    hide.save('C:/Users/admin/Desktop/images/secret_message.png')
    messagebox.showinfo("saved","the image is saved with....")

def enc(filename):
    encrpt=Toplevel(root)
    encrpt.geometry("400x200")
    encrpt.config(bg='maroon')
    encrpt.resizable(0,0)
    encrpt.title("encrypt")

    message=StringVar()
    path=StringVar
    path=filename

    lb1=Label(encrpt,text='WELCOME!!!!',bg='maroon',fg="white").place(relx=0.4,rely=0.1)

    lb2=Label(encrpt,text='ENTER THE MESSAGE IN YOUR IMAGE',bg='maroon',fg="white").place(relx=0.3,rely=0.3)

    lb4=Entry(encrpt,textvariable=message,bd=4).place(rely=0.5,relheight=0.1,relwidth=1)


    but0=Button(encrpt,text='encrypt',bd=2,command=lambda:encrpt_ok(filename,message.get())).place(rely=0.7,relx=0.4,relheight=0.2,relwidth=0.2)

def dec(filename):
    decrypt_message=lsb.reveal(filename)
    decryptmess=decrypt_message

    dec=Toplevel(root)
    dec.geometry("400x200")
    dec.config(bg="maroon")
    dec.title("decode")

    path = StringVar()
    yam=StringVar()
    yam=decryptmess
    path=filename


    lab1=Label(dec,text="welcome!!!",bg='maroon',fg='white').place(relx=0.4,rely=0.05)

    lab2=Label(dec,text='VIEW THE SECRETE MESSAGE!!!!!',bg="maroon",fg="white").place(relx=0.3,rely=0.2)

    lab3=Label(dec,text=yam,bg='maroon',fg='white',bd=5).place(relx=0.2,rely=0.4)


    lab4=Label(dec,text="visit 2020 NEPAL" ,bg="maroon",fg="white").place(relx=0.3,rely=0.6)


#gui for encrypt & decrypt
def click():

    root=Toplevel()
    root.geometry("400x200")
    root.resizable(0,0)
    root.config(bg="skyblue")


    choose=Button(root,text='choose image',command=browse,bg="maroon",bd=4,fg="white").place(relx=0.4,rely=0.2)
    encrp=Button(root,text="Encrypt",command=lambda:enc(filename),bd=4,bg="maroon",fg="white" ).place(relx=0.4,rely=0.4)
    decrypt=Button(root,text='Decrypt',bg="maroon",fg="white",bd=4,command=lambda :dec(filename)).place(relx=0.4,rely=0.6)
    root.mainloop()

#For diplaying that the sign up process is completed / account is registered
def submit():
    top = Toplevel(root)
    top.geometry('500x150')
    Label(top, text='Congratulation you have completed the process.', font=("", 14), fg="green").place(relx=0.02,rely=0.1)
    Label(top, text='Welcome to the world of Secret Chat!!', font=("", 14), fg="green").place(relx=0.02,rely=0.3)
    but1 = Button(top, text='OK', font=("", 14), fg="red", command=lambda: top.destroy())
    but1.place(relx=0.4,rely=0.5)

#For Registration/Sign up Page
def signup():
    global sign
    sign = Toplevel(root)
    sign.title("Register form of Secret Chat")
    sign.geometry('500x600')
    sign.resizable(0,0)
    gender=StringVar()
    global username
    global first
    global last
    global password
    global email
    global username_entry
    global first_entry
    global last_entry
    global password_entry
    global email_entry
    username = StringVar()
    first = StringVar
    last = StringVar
    password = StringVar
    email = StringVar()

    label_1=Label(sign, text='Secret Chat', font=("Script MT Bold ", 20),fg="red", bg="skyblue")
    label_1.place(relx=0.3, rely=0.01)

    label_2=Label(sign, text='Username', font=(" ", 12))
    label_2.place(relx=0.03,rely=0.1)
    username_entry = Entry(sign, textvariable='Username', font=("", 12))
    username_entry.place(relx=0.3,rely=0.1)

    label_3=Label(sign, text='First Name', font=("", 12))
    label_3.place(relx=0.03, rely=0.2)
    first_entry= Entry(sign, textvariable='First Name', font=("", 12))
    first_entry.place(relx=0.3, rely=0.2)

    label_4=Label(sign, text='Last Name', font=(" ", 12))
    label_4.place(relx=0.03, rely=0.3)
    last_entry= Entry(sign, textvariable='Last Name', font=("", 12))
    last_entry.place(relx=0.3, rely=0.3)

    label_5 = Label(sign, text='Password', font=("", 12))
    label_5.place(relx=0.03, rely=0.4)
    password_entry = Entry(sign, textvariable='Password', font=("", 12))
    password_entry.place(relx=0.3, rely=0.4)

    label_6=Label(sign, text='E-mail', font=("", 12))
    label_6.place(relx=0.03, rely=0.5)
    email_entry = Entry(sign, textvariable='E-mail', font=("", 12))
    email_entry.place(relx=0.3, rely=0.5)

    label_7=Label(sign, text='Address', font=(" ", 12))
    label_7.place(relx=0.03, rely=0.6)
    address = Entry(sign, textvariable='Address', font=("", 12))
    address.place(relx=0.3, rely=0.6)

    label_8=Label(sign, text='Country', font=(" ", 12))
    label_8.place(relx=0.03, rely=0.7)

    list1 = ['Nepal', 'India', 'UK', 'Canada', 'Australia', 'South Africa', 'China', 'Japan'];
    c = StringVar()
    droplist = OptionMenu(sign, c, *list1)
    droplist.config(font=("",12))
    c.set('Select your country')
    droplist.place(relx=0.3, rely=0.7)

    label_9= Label(sign, text='Gender', font=("",12))
    label_9.place(relx=0.03,rely=0.8)
    male=Radiobutton(sign, text='Male', variable=gender, value='Male', font=("",12), fg="blue")
    male.place(relx=0.3,rely=0.8)
    female=Radiobutton(sign, text='Female', variable=gender, value='Female', font=("",12), fg="blue")
    female.place(relx=0.5,rely=0.8)

    buts = Button(sign, text='Submit', font=("", 13),bg='brown',fg='white', command=lambda: submit())
    buts.place(relx=0.4, rely=0.9)
    sign.mainloop()


#For Secret Chat login page
root=Tk()
root.title("Spychat Login")
root.geometry("400x450")
root.resizable(0,0)
root.config(background="skyblue")
Username=StringVar()
Password=StringVar()
Username.set('Welcome to the world of Secret chat')
Label(root, text='Secret Chat', font=(" ",20)).place(relx=0.3,rely=0.03)
Label(root, text='Username', font=(" ",16)).place(relx=0.03,rely=0.2)
username=Entry(root, textvariable='Username', font=("",16))
username.place(relx=0.3,rely=0.2)
Label(root, text='Password', font=("",16)).place(relx=0.03,rely=0.3)
password=Entry(root, textvariable='Password', font=("",16))
password.place(relx=0.3,rely=0.3)
but1=Button(root, text='Login', font=("",16), command=lambda: click())
but1.place(relx=0.4,rely=0.4)
Label(root, text="Don't have an account", font=("",14)).place(relx=0.03,rely=0.6)
Label(text = "").pack()
but2=Button(root, text='Sign Up', font=("",15), fg="red",bg="grey", command=lambda: signup())
but2.place(relx=0.6,rely=0.6)

root.mainloop()