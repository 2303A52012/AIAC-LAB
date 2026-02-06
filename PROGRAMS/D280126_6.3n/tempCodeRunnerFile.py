'''
write a python funcyion that displays all perfect numbers in range from 1 to 1000
'''
import time
import math
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
def display_perfect_numbers():
    perfect_numbers = []
    for num in range(1, 1001):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers
if __name__ == "__main__":
    t1 = time.time()
    perfect_numbers = display_perfect_numbers()
    t2 = time.time()
    print("Time taken to find perfect numbers:", t2 - t1, "seconds")
    print("Perfect numbers between 1 and 1000 are:", perfect_numbers)

'''
write a python funcyion that displays all perfect numbers in range from 1 to 1000 optimized using divisor check only up to square root of n
'''

def is_perfect_number_optimized(n):
    if n < 2:
        return False
    sum_of_divisors = 1  # 1 is a divisor of all n > 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors == n
def display_perfect_numbers_optimized():
    perfect_numbers = []
    for num in range(1, 1001):
        if is_perfect_number_optimized(num):
            perfect_numbers.append(num)
    return perfect_numbers
if __name__ == "__main__":
    t1 = time.time()
    perfect_numbers_optimized = display_perfect_numbers_optimized()
    t2 = time.time()
    print("Time taken to find perfect numbers (optimized):", t2 - t1, "seconds")
    print("Perfect numbers between 1 and 1000 (optimized) are:", perfect_numbers_optimized)