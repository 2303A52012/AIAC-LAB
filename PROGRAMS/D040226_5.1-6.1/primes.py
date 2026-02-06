'''
Generate a well commented Python code for two prime-checking methods and explain
how the optimized version improves performance.
'''
def is_prime_basic(n):
    """Check if a number is prime using a basic method."""
    if n <= 1: # numbers less than or equal to 1 are not prime
        return False
    for i in range(2, n): # check for factors from 2 to n-1
        if n % i == 0:
            return False # found a factor
    return True # no factors found, n is prime

def is_prime_optimized(n): # optimized version
    """Check if a number is prime using an optimized method."""
    if n <= 1: # numbers less than or equal to 1 are not prime
        return False
    if n <= 3: # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0: # eliminate multiples of 2 and 3
        return False
    i = 5 # start checking from 5
    while i * i <= n: # check for factors from 5 to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False # found a factor
        i += 6 # check only numbers of the form 6k ± 1
    return True # no factors found, n is prime
# Example usage
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 29, 97, 100]
    print("Basic Prime Check:")
    for num in test_numbers:
        print(f"{num} is prime: {is_prime_basic(num)}") # checking with basic method
    print("\nOptimized Prime Check:")
    for num in test_numbers: 
        print(f"{num} is prime: {is_prime_optimized(num)}") # checking with optimized method
'''
The optimized version improves performance by reducing the
number of checks needed to determine if a number is prime.
Instead of checking all numbers up to n-1, it only checks up 
to the square root of n and skips even numbers and multiples 
of 3 after initial checks. This significantly decreases the 
number of iterations for larger numbers.

'''

'''
Basic Prime Check:
1 is prime: False
2 is prime: True
3 is prime: True
4 is prime: False
5 is prime: True
16 is prime: False
17 is prime: True
18 is prime: False
19 is prime: True
20 is prime: False
29 is prime: True
97 is prime: True
100 is prime: False

Optimized Prime Check:
1 is prime: False
2 is prime: True
3 is prime: True
4 is prime: False
5 is prime: True
16 is prime: False
17 is prime: True
18 is prime: False
19 is prime: True
20 is prime: False
29 is prime: True
97 is prime: True
100 is prime: False
'''
