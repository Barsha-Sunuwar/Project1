from tkinter import *
from stegano import lsb
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msBox
import datetime
import re
#Process to do (Encrypt or Decrypt)
def click():
    root = Tk()
    root.title("Spychat")
    root.geometry("700x300")
    root.resizable(0, 0)
    tab = ttk.Notebook(root)
    tab1 = ttk.Frame(tab)
    tab2 = ttk.Frame(tab)
    tab.add(tab1, text="Encryption")
    tab.add(tab2, text="Decryption")
    tab.pack(expand=1, fill="both")

    # encoding
    def browse(path):
        filename = filedialog.askopenfilename()
        if re.search('\.jpg$', filename) or re.search('\.png$', filename):
            # path_entry.config(text="path to the file")
            # path_entry.insert(0,filename)
            path.set(filename)

        else:
            msBox.showinfo("You have choosen a wrong file, it is neither jpg nor png")

    path = " "

    def image(path):
        print(path)

    def hide_msg(path, message):
        hide = lsb.hide(path.get(), message.get())
        message_time = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        hide.save('secrt_pic' + message_time + '.jpg')
        msBox.showinfo("Saved", "image has been saved with name secrt_pic" + message_time + '.jpg')

    path = StringVar()
    but1 = Button(tab1, text="Search Image", fg='black', bg='red', width=20, command=lambda: browse(path))
    but1.place(relx=0.25, rely=0.02)

    path_entry = Entry(tab1, width=30, borderwidth=2, textvariable=path)
    path_entry.place(relx=0.25, rely=0.15)
    sms = StringVar()
    message = Label(tab1, text="Message", fg='black', bg='red', font=(" ", 15))
    message.place(relx=0.25, rely=0.30)
    msg = StringVar()
    msg_entry = Entry(tab1, width=30, borderwidth=2, textvariable=msg)

    msg_entry.place(relx=0.25, rely=0.43)
    enc = Button(tab1, text="Encode", fg='black', bg='yellow', command=lambda: hide_msg(path, msg))
    enc.place(relx=0.4, rely=0.85)
    upload_butn = Button(tab1, text="save", fg='black', bg='yellow')
    upload_butn.place(relx=0.8, rely=0.85)
    # for decoding
    path2 = " "

    def browser(path):
        filename = filedialog.askopenfilename()
        if re.search('\.png$', filename) or re.search('\.jpg$', filename):
            path_entry1.config(text="path to the file")
            path_entry1.insert(0, filename)


        else:
            msBox.showinfo("you have choosen a wrong file, it is neither jpg nor png")

    def images(path):
        print(path)

    def enc(path):
        print(path)
        sms = lsb.reveal(path)
        print(sms)

    but2 = Button(tab2, text="Search Image", fg="black", bg='yellow', width=10, command=lambda: browser(path))
    but2.place(relx=0.25, rely=0.02)
    path_entry1 = Entry(tab2, width=30, borderwidth=2)
    path_entry1.place(relx=0.25, rely=0.15)
    sms1 = StringVar()
    but3 = Button(tab2, text=" View message", fg="black", bg='green', font=(" ", 15))
    but3.place(relx=0.25, rely=0.30)
    dec = Button(tab2, text="Decode", fg="black", bg="red", command=lambda: images(path))
    dec.place(relx=0.4, rely=0)

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

    label_5=Label(sign, text='Password', font=("", 12))
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
