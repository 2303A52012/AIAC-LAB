'''
write a python function to display strong numbers with user given range.
'''
import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
    return sum_of_factorials == num
def display_strong_numbers(start, end):
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers
# Example usage:
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: ")) 
t1=time.time()
strong_numbers_in_range = display_strong_numbers(start_range, end_range)
t2=time.time()
print(f"Time taken: {t2-t1} seconds")
print(f"Strong numbers between {start_range} and {end_range}: {strong_numbers_in_range}")


'''
write a python function to display strong numbers with given range. 
optimized version precomputing factorials.
'''

import time
def precompute_factorials():
    factorials = {}
    for i in range(10):
        factorials[i] = factorial(i)
    return factorials
def is_strong_number_optimized(num, factorials):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorials[digit]
        temp //= 10
    return sum_of_factorials == num
def display_strong_numbers_optimized(start, end):
    factorials = precompute_factorials()
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number_optimized(num, factorials):
            strong_numbers.append(num)
    return strong_numbers
# Example usage:
t1=time.time()
strong_numbers_in_range_optimized = display_strong_numbers_optimized(start_range, end_range)
t2=time.time()
print(f"Time taken (optimized): {t2-t1} seconds")
print(f"Strong numbers between {start_range} and {end_range} (optimized): {strong_numbers_in_range_optimized}")

'''
Enter the start of the range: 1
Enter the end of the range: 1000
Time taken: 0.005503654479980469 seconds
Strong numbers between 1 and 1000: [1, 2, 145]
Time taken (optimized): 0.0 seconds
Strong numbers between 1 and 1000 (optimized): [1, 2, 145]
'''