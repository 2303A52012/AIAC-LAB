# a gui application of python which says weather the enterd num is even or odd
import tkinter as tk
from tkinter import messagebox
def check_even_odd():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            res = f"{num} is Even"
        else:
            res = f"{num} is Odd"
        result.config(text=res)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")
root = tk.Tk()
root.title("Even or Odd Checker")
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
result = tk.Label(root, text="")
result.pack(pady=5)
check_button = tk.Button(root, text="Check", command=check_even_odd)
check_button.pack(pady=10)
root.mainloop()