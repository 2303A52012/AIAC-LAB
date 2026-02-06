'''factorial of a number using recurtion and not using recurstion which takes only integer and 
which is simple, optimal and developer friendly code with a GUI interface'''
import tkinter as tk
from tkinter import messagebox
# Factorial without recursion
def non_rec_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Factorial with recursion
def rec_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * rec_factorial(n - 1)
def calculate_factorial():
    try:
        num = int(entry.get())
        method = method_var.get()
        if method == 'recursion':
            result = rec_factorial(num)
        else:
            result = non_rec_factorial(num)
        result_label.config(text=f"Factorial: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")
# GUI setup
root = tk.Tk()
root.title("Factorial Calculator")
label = tk.Label(root, text="Enter a number:")

label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
method_var = tk.StringVar(value='recursion')
rec_radio = tk.Radiobutton(root, text="Recursion", variable=method_var, value='recursion')
rec_radio.pack()
non_rec_radio = tk.Radiobutton(root, text="Non-Recursion", variable=
method_var, value='non_recursion')
non_rec_radio.pack()
calc_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)
root.mainloop()
