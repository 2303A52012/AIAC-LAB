import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    count = 0   # loop counter
    if n <= 1:
        return False, count
    if n <= 3:
        return True, count
    if n % 2 == 0 or n % 3 == 0:
        return False, count
    i = 5
    while i * i <= n:
        count += 1     # loop iteration counted
        if n % i == 0 or n % (i + 2) == 0:
            return False, count
        i += 6
    return True, count


def check_prime():
    try:
        num = int(entry.get())
        result_bool, loop_count = is_prime(num)
        if result_bool:
            text = f"{num} is a Prime Number"
        else:
            text = f"{num} is NOT a Prime Number"
        text += f"\nLoop ran {loop_count} times"
        result.config(text=text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")


root = tk.Tk()
root.title("Prime Number Checker")
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
result = tk.Label(root, text="")
result.pack(pady=5)
check_button = tk.Button(root, text="Check Prime", command=check_prime)
check_button.pack(pady=10)
root.mainloop()
