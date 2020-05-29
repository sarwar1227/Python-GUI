from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # Save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved !!")
    else:
        #Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo("About Us","This Is A Beautifull Notepad Developed By Sarwar Ali !!")
if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    #Add Text Area
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(fill=BOTH,expand=True)
    #Lets Create a menubar
    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar,tearoff=0)

    #FILE MENU STARTS

    #To Open New File
    FileMenu.add_command(label="New",command=newFile)

     #To Open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    # To Save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)

   #FILE MENU ENDS

   #EDIT MENU STARTS
    EditMenu=Menu(MenuBar,tearoff=0)
   #To Give a feature of cut,copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
   #EDIT MENU ENDS

   #HELP MENU STARTS
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
   #HELP MENU END
    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from tkinter module

    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
