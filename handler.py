from tkinter import *
root = Tk()
root.title("event handler")
label= Label(root,text="press the button" , font=("Arial" , 16))
label.pack(pady=10)
def change_text():
    label.config(text="button clicked")
button = Button(root, text="click me" , command=change_text)
button.pack(pady= 10)
root.mainloop()


