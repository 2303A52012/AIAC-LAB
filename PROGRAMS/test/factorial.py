'''
write a pyrhon program to calculate the factorial of a given number

    input : a number
    
    output : factorial of the given number

    Ex: input : 5
        output : 120 (5*4*3*2*1)
'''
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:# Recursive case: return n multiplied by the factorial of (n-1)
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number to calculate its factorial: "))# Input number to calculate factorial
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        exit(1)
    if number < 0:# Edge case: if the input is a negative integer
        print("Please enter a non-negative integer.")
    else:    
        print(f"The factorial of {number} is {factorial(number)}.")