from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x250")
root.maxsize(400,250)
root.minsize(400,250)
root.title("Sarwar Travels Portal")
israr=StringVar()
def reset_values(event):
    namevalue.set("")
    phonevalue.set("")
    gendervalue.set("")
    emergencyvalue.set("")
    paymentmodevalue.set("")
    foodservicevalue.set(0)
    israr.set("")
def sarwar(event):
    if foodservicevalue.get() == 1:
        food = "Yes"
    else:
        food = "No"
    ans=tmsg.askquestion("Confirm Booking","Do You Really Want to Book Your Ticket?")
    israr.set("Your Ticket is Booked !!")
    if ans=="yes":
        with open("record.txt","a") as f:
            f.write(f"{namevalue.get()} {phonevalue.get()} {gendervalue.get()} {emergencyvalue.get()} {paymentmodevalue.get()} {food}\n")
            Label(root, textvariable=israr).grid(row=8, column=3)
            button=Button(root,text="Book Again")
            button.grid(row=8, column=4)
            button.bind('<Button-1>',reset_values)
Label(root,text="Welcome to sarwar travels",font="comicsansms 13 bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

Entry(root,textvariable=namevalue).grid(row=1,column=3)
Entry(root,textvariable=phonevalue).grid(row=2,column=3)
Entry(root,textvariable=gendervalue).grid(row=3,column=3)
Entry(root,textvariable=emergencyvalue).grid(row=4,column=3)
entry=Entry(root,textvariable=paymentmodevalue)
entry.grid(row=5,column=3)
check=Checkbutton(root,text="Want to prebook your meal ?",variable=foodservicevalue)
check.grid(row=6,column=3)
button=Button(root,text="Book")
button.grid(row=7,column=3)
button.bind('<Button-1>',sarwar)
check.bind('<Return>',sarwar)
entry.bind('<Return>',sarwar)
root.mainloop()
