'''
write a python function  to display all happy numbers for user range
'''
import time


def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
def happy_numbers_in_range(start, end):
    happy_numbers = []
    for num in range(start, end + 1):
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers
s=int(input("Enter the start of the range: "))
e=int(input("Enter the end of the range: "))
t1 = time.time()
happy_numbers = happy_numbers_in_range(s, e)
t2 = time.time()
print("Time taken without optimization:", t2 - t1)
print("Happy numbers between", s, "and", e, "are:", happy_numbers)



'''
write a python function  to display all happy numbers for user range
Optimize the above code using set
'''
def is_happy_number_optimized(n, memo):
    original_n = n
    seen = set()
    while n != 1 and n not in seen:
        if n in memo:
            result = memo[n]
            break
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    else:
        result = (n == 1)
    for number in seen:
        memo[number] = result
    return result
def happy_numbers_in_range_optimized(start, end):
    happy_numbers = []
    memo = {}
    for num in range(start, end + 1):
        if is_happy_number_optimized(num, memo):
            happy_numbers.append(num)
    return happy_numbers
t3 = time.time()
happy_numbers_optimized = happy_numbers_in_range_optimized(s, e)
t4 = time.time()
print("Time taken with optimization:", t4 - t3)
print("Optimized happy numbers between", s, "and", e, "are:", happy_numbers_optimized)

'''
Enter the start of the range: 1
Enter the end of the range: 500
Time taken without optimization: 0.0035326480865478516
Happy numbers between 1 and 500 are: [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 
79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 
203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 
326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 
440, 446, 464, 469, 478, 487, 490, 496]
Time taken with optimization: 0.0
Optimized happy numbers between 1 and 500 are: [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68,
70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 
203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 
329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 
464, 469, 478, 487, 490, 496]
'''