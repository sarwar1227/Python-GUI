from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("420x400")
root.maxsize(420,400)
root.minsize(420,400)
root.title("Sarwar Travels Portal")
israr=StringVar()
slider = Scale(root, from_=1, to=5, orient=HORIZONTAL, tickinterval=1)
def rate():
    tmsg.showinfo("Rating Popup",f"Thanks For Giving Us {slider.get()} star rating")
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
    if ans=="yes":
        with open("record.txt","a") as f:
            f.write(f"{namevalue.get()} {phonevalue.get()} {gendervalue.get()} {emergencyvalue.get()} {paymentmodevalue.get()} {food}\n")
            ans2=tmsg.showinfo("Confirmation Popup", "Booking Successfull !!")
            if ans2=="ok":
                israr.set("Your Ticket is Booked !!")
                Label(root, textvariable=israr).grid(row=8, column=3)
                button=Button(root,text="Book Again")
                button.grid(row=9,column=3)
                button.bind('<Button-1>',reset_values)
                Label(root, text="Please Rate Our App").grid(row=13,column=3)
                slider.grid(row=12,column=3)
                Button(root, text="Rate",command=rate).grid(row=14,column=3)
Label(root,text="Welcome to sarwar travels",bg="pink",fg="black",font="comicsansms 15 bold",).grid(row=0,column=3)
name=Label(root,text="Name",fg="black",bg="white")
phone=Label(root,text="Phone",fg="black",bg="white")
gender=Label(root,text="Gender",fg="black",bg="white")
emergency=Label(root,text="Emergency",fg="black",bg="white")
paymentmode=Label(root,text="Payment Mode",fg="black",bg="white")

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
check=Checkbutton(root,text="Want to prebook your meal ?",variable=foodservicevalue,font="arial 10 bold")
check.grid(row=6,column=3)
button=Button(root,text="Book")
button.grid(row=7,column=3)
button.bind('<Button-1>',sarwar)
check.bind('<Return>',sarwar)
entry.bind('<Return>',sarwar)
root.mainloop()
