'''generate a well commented python program for finf the febanochii series using recurtion
explain base cases , edge cases and recursive calls.
parameters n as number of terms in febanochii series
return the febanochii series up to n terms
'''
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:# Recursive case: return the sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
if __name__ == "__main__":
    try:
        terms = int(input("Enter the number of terms in the Fibonacci series: "))# Number of terms in the Fibonacci series
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        exit(1)
    if terms <= 0:# Edge case: if the input is not a positive integer
        print("Please enter a positive integer.")
    else:    
        print(f"Fibonacci series up to {terms} terms:")
        for i in range(terms):
            print(fibonacci(i), end=" ")


'''
Enter the number of terms in the Fibonacci series: i
Invalid input. Please enter a positive integer.
PS C:\Users\CHANDRAKALA\OneDrive\Desktop\plp\AIAC> python -u "c:\Users\CHANDRAKALA\OneDrive\Desktop\plp\AIAC\playground\D040226_5.1-6.1\febanochii.py"
Enter the number of terms in the Fibonacci series: -9
Please enter a positive integer.
PS C:\Users\CHANDRAKALA\OneDrive\Desktop\plp\AIAC> python -u "c:\Users\CHANDRAKALA\OneDrive\Desktop\plp\AIAC\playground\D040226_5.1-6.1\febanochii.py"
Enter the number of terms in the Fibonacci series: 10
Fibonacci series up to 10 terms:
0 1 1 2 3 5 8 13 21 34
'''