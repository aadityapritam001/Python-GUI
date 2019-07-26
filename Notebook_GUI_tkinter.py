from tkinter import *
import tkinter.messagebox

def do():
    print("Done")

root=Tk()

#************MAIN MENU **************
m=Menu(root)
root.config(menu=m)

#creating Submenu "File"
submenu=Menu(m)
m.add_cascade(label="file",menu=submenu)
submenu.add_command(label="New",command=do)
submenu.add_command(label="Folder",command=do)
submenu.add_separator()
submenu.add_command(label="Exit",command=do)

                            #creating Submenu "Edit"
Editmenu=Menu(m)

m.add_cascade(label="Edit",menu=Editmenu)
Editmenu.add_command(label="cut",command=do)
Editmenu.add_command(label="copy",command=do)
Editmenu.add_command(label="paste",command=do)

                            #creating submenu "view"
viewMenu=Menu(m)

m.add_cascade(label="View",menu=viewMenu)
viewMenu.add_command(label="ToolBar",command=do)
viewMenu.add_command(label="RecentFile",command=do)

                            #creating toolmenu

ToolMenu=Menu(m)
m.add_cascade(label="Tool",menu=ToolMenu)
ToolMenu.add_command(label="Tasks",command=do)
ToolMenu.add_command(label="Template",command=do)


#**************ToolBar**************

toolbar=Frame(root,  bd=2, relief=SUNKEN, bg="blue")
insertButton=Button(toolbar, text="Insert", command=do)
insertButton.pack(side=LEFT, padx=4 , pady=2)
printbutton=Button(toolbar, text="print", command=do)
printbutton.pack(side=LEFT , padx=4, pady=2)

toolbar.pack(side=TOP , fill=X)


# ----------------STSTUS BAR AT BUTTOM --------------
status=Label(root, text="preparing...", bd=3, relief=SUNKEN,  anchor=W)
status.pack(side=BOTTOM, fill=X)

# --------------showing message or popup--------------
tkinter.messagebox.showinfo("Welcome","welcome to python GUI")

#----------------Asking Question-----------------------
answer=tkinter.messagebox.askquestion("Question 1","Do you like Python")
if answer=="yes":
    print("That,s Great")
if answer=="no":
    print("You should try it once")

#__________Main Loop____________
root.mainloop()
