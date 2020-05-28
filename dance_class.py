from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("Sarwar Dance Classes")

def store_into_file():
    f=open("dance.txt","a")
    f.write(f"Name : {user_name.get()} Phone Number : {user_phone.get()} Address : {user_address.get()}\n")
    Label(text="Registered Successfully !!").pack()
    f.close()
    Button(text="Tap to close",command=exit).pack()
Label(text="Welcome to Sarwar Dance Classes",font="comicsansms 19 bold",bg="red",fg="white").pack()
Label(text="Kindly Fill this form to get Registered !!",borderwidth=9,font="arial 10",fg="red",bg="white").pack()

user_name=StringVar()
user_phone=StringVar()
user_address=StringVar()

Label(text="Full Name ",font="arial 9").pack()
Entry(textvariable=user_name).pack()
Label(text="Phone No ",font="arial 9").pack()
Entry(textvariable=user_phone,).pack()
Label(text="Address ",font="arial 9").pack()
Entry(textvariable=user_address).pack()

Button(text="Register",command=store_into_file).pack()

root.mainloop()
