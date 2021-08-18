from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import asksaveasfilename,askopenfilename,askopenfile
import os
import win32api
from tkinter.messagebox import showinfo
import pyautogui
import win32print
from datetime import datetime
root=Tk()
root.geometry("1200x720")
root.title("Notepad by Saurav")
root.minsize(1200,720)
root.wm_iconbitmap("notepad_icon.ico")
file=None
font_size=('normal',16)
def newfile():
    root.title("Untitled.txt")
    file=None
    window.delete(1.0,END)
def saveas():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(window.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(window.get(1.0, END))
        f.close()
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        window.delete(1.0, END)
        f = open(file, "r")
        window.insert(1.0, f.read())
        f.close()
def print_file():
    # a printer should be attached in order to  print something
    printer_name=win32print.GetDefaultPrinter()

    showinfo("Printer Info", printer_name)
    global file
    file_to_print = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)
def func():
    pass

def show_datetime():
    today=datetime.now()
    showinfo("Date and Time",f" Current date and time are {today}")
def about():
    showinfo("Notepad", "Notepad by Saurav")
window=scrolledtext.ScrolledText(root,height=700,width=1200, font = font_size)
window.pack(fill=BOTH)
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="New File",command=newfile)
m1.add_command(label="Open file",command=openFile)
m1.add_separator()
m1.add_command(label="Save as",command=saveas)
m1.add_command(label="Save",command=saveas)
m1.add_command(label="Print",command=print_file)
m1.add_separator()
m1.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File",menu=m1)
root.config(menu=menubar)
#Edit button
m2=Menu(menubar,tearoff=0)
m2.add_command(label="Cut",accelerator="Ctrl+X", command=lambda: window.focus_get().event_generate('<<Cut>>'))
m2.add_command(label="Copy",accelerator="Ctrl+C", command=lambda: window.focus_get().event_generate('<<Copy>>'))
m2.add_command(label="Paste",accelerator="Ctrl+V", command=lambda: window.focus_get().event_generate('<<Paste>>'))
m2.add_separator()
m2.add_command(label="Select All",accelerator="Ctrl+A",command=lambda *awargs:pyautogui.hotkey("ctrl","a"))
m2.add_command(label="Time Date",command=show_datetime)
menubar.add_cascade(label="Edit",menu=m2)
root.config(menu=menubar)
# #Help button
m5=Menu(menubar,tearoff=0)
m5.add_command(label="About Notepad",command=about)
menubar.add_cascade(label="About",menu=m5)
root.config(menu=menubar)

root.mainloop()
