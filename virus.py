from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("virus scanner")
label = Label(root , text="scan for viruses or spam")
label.pack(pady= 10)

def scan():
    messagebox.showwarning("a virus has been detected!")
    label.config(text="install updates and scan is complete")
button = Button(root, text= "scan" , command= scan)
button.pack(pady= 10)
root.mainloop()