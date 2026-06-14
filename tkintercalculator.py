import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e2e")

def add():
    calculate("+")
def subtract():
    calculate("-")
def multiply():
    calculate("*")
def divide():
    calculate("/")

def calculate(smth):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if smth == "+":
            result = a + b
        elif smth == "-":
            result = a - b
        elif smth == "*":
            result = a * b
        elif smth == "/":
            if b == 0:
                messagebox.showerror("Error", "Can not divide by zero")
                return
            result = a / b

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

tk.Label(root, text=" 1-number:", bg="#1e1e2e", fg="white", font=("Segoe UI", 11)).pack()
entry1 = tk.Entry(root, width=30)
entry1.pack()

tk.Label(root, text=" 2- number:", bg="#1e1e2e", fg="white", font=("Segoe UI", 11)).pack()
entry2 = tk.Entry(root, width=30)
entry2.pack()

tk.Button(root, text="+",width=6,command=add).pack()
tk.Button(root, text="-",width=6, command=subtract).pack()
tk.Button(root, text="*",width=6,command=multiply).pack()
tk.Button(root, text="/",width=6,command=divide).pack()

result_label = tk.Label(root, text="Result: —", bg="#1e1e2e", fg="White", font=("Segoe UI", 13))
result_label.pack()

root.mainloop()