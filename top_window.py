from tkinter import *
root = Tk()
root.title("hfifo;qwth4")
root.geometry("400x300")
def open_window():
    top = Toplevel()
    top.title("second window")
    top.geometry("300x200")
    label = Label(top , text= "you have read the world mst funniest joke" , font=("Arial" , 14))
    label.pack(pady= 40)
button = Button(root , text= "open new window" , command= open_window)
button.pack(pady=100)
root.mainloop()

