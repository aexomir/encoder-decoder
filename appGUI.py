# this was one of the learning projects
# i've found useful for starting Tkinter
# and for understanding concept of message encryption in a very very simple version..
# NB-NOTE: THE ORIGINAL PROJECT
# CAN BE FOUND IN THE FOLLOWING ADDRESS:
# https://www.geeksforgeeks.org/python-message-encode-decode-using-tkinter/


# This Project is redesigned and updated in a more understandable way
# by me! (/https://github.com/AmirHosseinRnj1)
# If you have any problem running or understanding this project,
# feel free to make contact with me...


#TKINTER MODULE SETUP

#import tkinter module
from tkinter import *
import random
import time
import datetime
from EnDeCoder import encode,decode


###################
###CREATING GUI####
###################

#creating root object
from tkinter import Label

root = Tk()
#defining size of window
root.geometry("1200x6000")
#defining title
root.title("Message Encryption And Decryption")
#creating frames
Tops = Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

######################
####TIME AND LABELS####
######################
localtime = time.asctime(time.localtime(time.time()))

#initialize_Parameters
rand = StringVar()
Msg = StringVar()
Key = StringVar()
Mode = StringVar()
Result = StringVar()

#making labels for created frames
lblinfo = Label(Tops,font=('helvetica',50,'bold'),
                text="SECRET MESSAGING \n Vigenère cipher",
                fg="Black",bd=10,anchor="w")
lblinfo.grid(row=0,column=0)

lblinfo = Label(Tops,font=('Arial',25,'bold'),
                text=localtime,
                fg="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=1,column=0)

lblReference = Label(f1,font=('arial',16,'bold'),
                    text="Name",bd=16,anchor='w')
lblReference.grid(row=0,column=0)

txtReference = Entry(f1,font=('arial',16,'bold'),
                     textvariable=rand,bd=10,insertwidth=4,
                     bg='Powder Blue',justify="center")
txtReference.grid(row=0,column=1)

lblMsg = Label(f1,font=('arial',16,'bold'),
               text="Message",bd=16,anchor='w')
lblMsg.grid(row=1,column=0)

txtMsg = Entry(f1,font=('arial',16,'bold'),
               textvariable=Msg,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtMsg.grid(row=1,column=1)

lblKey = Label(f1,font=('arial',16,'bold'),
               text="Key",bd=16,anchor='w')
lblKey.grid(row=2,column=0)

txtKey = Entry(f1,font=('arial',16,'bold'),
               textvariable=Key,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtKey.grid(row=2,column=1)

lblMode = Label(f1,font=('arial',16,'bold'),
               text="Choose Mode : (E) for Encryption or (D) for Decryption",bd=16,anchor='w')
lblMode.grid(row=3,column=0)

txtMode = Entry(f1,font=('arial',16,'bold'),
               textvariable=Mode,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtMode.grid(row=3,column=1)

lblService = Label(f1,font=('arial',16,'bold'),
               text="The Result",bd=16,anchor='w')
lblService.grid(row=2,column=2)

txtService = Entry(f1,font=('arial',16,'bold'),
               textvariable=Result,bd=10,insertwidth=4,
               bg="Powder Blue",justify="center")
txtService.grid(row=2,column=3)

########################
####INITIALIZED FUN####
########################

def exit():
    root.destroy()

def reset():
    rand.set("")
    Msg.set("")
    Key.set("")
    Mode.set("")
    Result.set("")

def Ref():

    clear = txtMsg.get()
    key = txtKey.get()
    mode = txtMode.get()
    try:
        if mode == "e":
            Result.set(encode(key,clear))
        elif mode == "d":
            Result.set(decode(key,clear))
    except:
        print("Bad Input, Plz Give e for Encode and d for Decode")
        reset()

btnShow = Button(f1,padx=16,pady=8,bd=16,fg="black",
                 font=('Arial',16,'bold'),width=10,
                 text="Show Result",bg="powder blue",
                 command=Ref).grid(row=7,column=1)

btnReset = Button(f1,padx=16,pady=8,bd=16,fg="black",
                 font=('Arial',16,'bold'),width=10,
                 text="Reset",bg="green",
                 command=reset).grid(row=7,column=2)

btnExit = Button(f1,padx=16,pady=8,bd=16,fg="black",
                 font=('Arial',16,'bold'),width=10,
                 text="Exit",bg="Red",
                 command=exit).grid(row=7,column=3)

root.mainloop()