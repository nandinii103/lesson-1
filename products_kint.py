import tkinter as tk
window = Tk()
window.title("products")
window.geometry("400x300")
label = Label(text="products of numbers")
window.config(bg = "orange")
num1_label = label(text="Enter the first number: ")
num1_entry = Entry()
num2_label = label(text= "Enter the second number: ")
num2_entry = Entry()

def calculate():
    n1 = num1_entry.get()
    n2 = num2_entry.get()
    text_box.delete("1.0" , END)
    text_box.insert(END, f"Product of {n1} and {n2} is: {product}")
    btn = Button(text="calculate" , command=calculate)

label.pack()
num1_label.pack()
num1_entry.pack()
num2_label.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()






