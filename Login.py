#importing modules

import tkinter as tk

from functools import partial

def validateLogin(username,password):
    print('usename entered: ',username.get())
    print("password entered: ",password.get())

#creating an exit function

#creating a confirmation window before quiting
from tkinter import messagebox
def cancelconfirm():
    response=messagebox.askokcancel('Login',message="Are YOU SURE?")

    if response==1:
        window.quit()


#initializing the window
window=tk.Tk()

window.title('Mkenzo') #the tittle of the window
window['bg']='#1C2029'
window.geometry('400x200')

frame=tk.Frame(window,bg='#1987B8')
frame.place(x=0,y=0,relwidth=1,relheight=1)

usernameLabel=tk.Label(frame,text='username',bg='#1987B8',fg='white')
usernameLabel.grid(row=0,column=0)
username=tk.StringVar()
usernameEntry=tk.Entry(frame,textvariable=username).grid(row=0,column=1)

passwordLabel=tk.Label(frame,text='password',bg='#1987B8',fg='white',bd=7).grid(row=1,column=0,padx=10,pady=20)

password=tk.StringVar()
passwordEntry=tk.Entry(frame,textvariable=password).grid(row=1,column=1)

validateLogin=partial(validateLogin,username,password)

#login button
lb=tk.Button(frame,text='LogIn',bg='#1987B8',font=('impact',15),fg='white',bd=8,command=validateLogin).grid(row=10,column=2)
cancel=tk.Button(frame,text='Cancel',bg='#1987B8',bd=8,fg='white',font=('impact',15),command=cancelconfirm).grid(row=10,column=0)

#icon picture
# photo=tk.PhotoImage(file="C:\\Users\\user\\Desktop\\Sketchg.png")
# window.iconphoto(False,pho

tk.mainloop()

