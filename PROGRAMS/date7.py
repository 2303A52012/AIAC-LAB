'''factorial of a number using recurtion and not using recurstion which takes only integer and 
which is simple, optimal and developer and tester friendly code'''

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
    
# read input
def read_input():
    try:
        num = int(input("Enter a number to find its factorial: "))
        return num
    except ValueError:
        print("Please enter a valid integer.")
        return None

#main
if __name__ == "__main__":
    num = read_input()
    if num is None:
        exit()
    
    method = input("Choose method - 'yes' for recursion, 'no' for non-recursion: ").strip().lower()
    if method == 'yes':
        print(f"Factorial of {num} using recursion is: {rec_factorial(num)}")
    elif method == 'no':
        print(f"Factorial of {num} using non-recursion is: {non_rec_factorial(num)}")
    else:
        print("Invalid method chosen. Please select 'yes' or 'no'.")
        
    #testing
    assert rec_factorial(5) == 120
    assert non_rec_factorial(5) == 120
    assert rec_factorial(0) == 1
    assert non_rec_factorial(0) == 1
    assert rec_factorial(-3) == "Factorial is not defined for negative numbers"
    assert non_rec_factorial(-3) == "Factorial is not defined for negative numbers"
    print("All tests passed!")

# 