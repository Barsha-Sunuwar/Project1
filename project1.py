from stegano import lsb
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from termcolor import colored
def unreg_user():
    name=input("Enter your name")
    while name.isalpha() == False or len(name) <=5:
        name =input(colored("Alphabet should be more then 5", 'red'))
        name =input(colored("Enter your name", 'blue'))
    age=input("Enter your age")
    while age.isnumeric()==False or int(age)<=18 :
        age=input(colored("Invalid(Age should be above 18)", 'red'))
        age = input(colored("Enter your age", 'blue'))
    password=input("Enter your password")
    while len(password)<7 or len(password)>12:
        password=input(colored("Error(Password length should be between(7-12)", 'red'))
        password = input(colored("Enter your password", 'blue'))
def reg_user():
    u=input(colored("Enter your Username", 'blue'))
    while u!='username':
        u=input(colored("Enter correct Username",'red'))
    a=input(colored("Enter your password", 'blue'))
    while a!='password':
        a=input(colored("Enter the valid password", 'red'))
def valid():
    b=input(colored(" If already registered write Y for yes otherwise write N for no"))
    if b=='Y' or b=='y':
        reg_user()
    elif b=='N' or b=='n':
        unreg_user()
    else:
        valid()
valid()
print("Welcome to the world of secret chat")

def hide_msg(path, message):
    hide = stegano.lsb.hide(path, message)
    hide.sare('spic' + message_time + '.jpg')

def images(path):
    print(path)

def enco(path):
    print(path)
    sms = stegano.lsb.reveal(path)
    print(sms)

#For gui
root=Tk()
def click(a):
  Username.set("")
root.title("Spychat Login")
root.geometry("400x450")
root.resizable(0,0)
root.config(background="pink")
#For menubar
menubar=Menu(root)
encryptmenu=Menu(menubar)
encryptmenu.add_command(label="Encryption", command="Encription")
menubar.add_cascade(label="Encryption", menu="encryptmenu")
decryptmenu=Menu(menubar)
decryptmenu.add_command(label="Decryption", command="Decryption")
menubar.add_cascade(label="Decryption", menu="Decryptmenu")
root.config(menu=menubar)


Username=StringVar()
Password=StringVar()
Username.set('Welcome to the world of Secret chat')
Label(root, text='Login', font=(" ",20)).grid(row=0, column=0,padx=5,pady=10)
Label(root, text='Username', font=(" ",16)).grid(row=3, column=0,padx=5,pady=10)
username=Entry(root,textvariable='Username', font=("",16))
username.grid(row=3, column=2,pady=2)
Label(root,text='Password', font=("",16)).grid(row=5,column=0)
password=Entry(root,textvariable='Password', font=("",16))
password.grid(row=5, column=2,pady=10)
but1=Button(root,text='Login', font=("",16), command=lambda: click(Username))
but1.grid(row=8,column=0,padx=5,pady=25)
root.mainloop()


top=Toplevel(root)
    Label(top, text='Congratulation you have completed the process.', font=("",14), fg="green")
    Label(top, text='Welcome to the world of Secret Chat!!', font=("", 14), fg="green")
    but1 = Button(top, text='ok', font=("", 15), fg="red")
    but1.pack(pady=10