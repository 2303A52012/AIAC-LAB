# a gui application which finds all prime numbers in a given range
import tkinter as tk
from tkinter import messagebox
def is_prime(n):
    if n <= 1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def calculate_primes():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        if start > end:
            messagebox.showerror("Error", "Start of range must be less than or equal to end of range")
            return
        primes = find_primes_in_range(start, end)
        result_text = f"Prime numbers between {start} and {end}:\n" + ", ".join(map(str, primes)) if primes else "No prime numbers found in this range."
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for the range")
# GUI setup
root = tk.Tk()
root.title("Primes in Range Finder")
label = tk.Label(root, text="Enter the range to find prime numbers:")
label.pack(pady=10)

start_label = tk.Label(root, text="Start:")
start_label.pack()
start_entry = tk.Entry(root)
start_entry.pack(pady=5)
end_label = tk.Label(root, text="End:")
end_label.pack()
end_entry = tk.Entry(root)
end_entry.pack(pady=5)
calc_button = tk.Button(root, text="Find Primes", command=calculate_primes)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)
root.mainloop()

