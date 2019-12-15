from stegano import lsb
from  tkinter import *
from tkinter import messagebox
from tkinter import filedialog

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




    lab1=Label(dec,text="welcome!!!",bg='maroon',fg='white').place(relx=0.4,rely=0.05)

    lab2=Label(dec,text='VIEW THE SECRETE MESSAGE!!!!!',bg="maroon",fg="white").place(relx=0.3,rely=0.2)

    lab3=Label(dec,text=yam,bg='maroon',fg='white',bd=5).place(relx=0.2,rely=0.4)


    lab4=Label(dec,text="visit 2020 NEPAL" ,bg="maroon",fg="white").place(relx=0.3,rely=0.6)







#gui program start from here

root=Tk()
root.geometry("400x200")
root.resizable(0,0)
root.config(bg="skyblue")


choose=Button(root,text='choose image',command=browse,bg="maroon",bd=4,fg="white").place(relx=0.4,rely=0.2)


encrp=Button(root,text="encrypt",command=lambda:enc(filename),bd=4,bg="maroon",fg="white" ).place(relx=0.4,rely=0.4)


decrypt=Button(root,text='decrypt',bg="maroon",fg="white",bd=4,command=lambda :dec(filename)).place(relx=0.4,rely=0.6)






root.mainloop()