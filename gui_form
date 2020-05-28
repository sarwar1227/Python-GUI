from tkinter import *
root=Tk()
root.geometry("664x444")
root.title("Sarwar Travels Portal")
def sarwar(event):
    if foodservicevalue.get() == 1:
        food = "Yes"
    else:
        food = "No"
    with open("record.txt","a") as f:
        f.write(f"{namevalue.get()} {phonevalue.get()} {gendervalue.get()} {emergencyvalue.get()} {paymentmodevalue.get()} {food}\n")
    namevalue.set("")
    phonevalue.set("")
    gendervalue.set("")
    emergencyvalue.set("")
    paymentmodevalue.set("")
    foodservicevalue.set(0)
    Label(root,text="You Ticket is Booked !!").grid(row=8,column=3)
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
