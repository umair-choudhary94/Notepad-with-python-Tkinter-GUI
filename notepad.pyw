# from tkinter import *
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
root.title('Untitled-Notepad')
root.geometry('644x788')
#OUR FUNCTION
def newfile():
    global file
    root.title('Untitled-Notepad')
    file = None
    Textarea.delete(1.0,END)
def openfile():
    global file
    file = askopenfilename(defaultextension='.txt',
    filetypes=[('All Files','*.*'),('Text Documest','*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file)+'-Notepad')
        Textarea.delete(1.0,END)
        f = open(file,'r')
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',
    filetypes=[('All Files','*.*'),('Text Documest','*.txt')])
        if file=='':
            file = None
        else:
            #save as new file
            f = open(file,'w')
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'-Notepad')
            print('saved')
    else:
        #save the file
            f = open(file,'w')
            f.write(Textarea.get(1.0,END))
            f.close()

def quitapp():
    root.destroy()
def cut():
    Textarea.event_generate(('<<Cut>>'))
def copy():
    Textarea.event_generate(('<<Copy>>'))
def paste():
    Textarea.event_generate(('<<Paste>>'))
def about():
    messagebox.showinfo('Notepad','Notepad by codevision')

#textarea
Textarea = Text(root)
Textarea.pack(fill=BOTH,expand=TRUE)
file = None
#ADDING MENU
menu_bar = Menu()
filemenu = Menu(menu_bar,tearoff=0)
#to open new file
filemenu.add_command(label='New',command=newfile)
#to open already existing file
filemenu.add_command(label='Open',command=openfile)
#to save curent file
filemenu.add_command(label='Save',command=savefile)
# to exit
filemenu.add_command(label='Exit',command=quitapp)
menu_bar.add_cascade(label='File',menu=filemenu)

#Edit Menu
editmenu = Menu(menu_bar,tearoff=0)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
menu_bar.add_cascade(label='Edit',menu=editmenu)
#HELP Menu
helpmenu = Menu(menu_bar,tearoff=0)
helpmenu.add_command(label='About Notepad',command=about)
menu_bar.add_cascade(label='Help',menu=helpmenu)


root.config(menu=menu_bar)
#ADDING SCROLLBAR
Scroll = Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=Scroll.set)
root.mainloop()