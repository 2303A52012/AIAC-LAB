'''
a well commented code to check whether a number is prime or not
a function that read the number from user
check weather the num is a numeric character or not
if no return invalid input
if yes check weather the number is even or multiple of 3 or multiple of 5 if they are return not a prime number
start iterating from 7 to square root of number +1
if the number is multiple of any number in the iteration return not a prime number
if no return prime number
call the fnction and print the result
'''
import math
def is_prime(number): # Function to check if a number is prime
    """
    This function checks whether a given number is prime or not.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    str: A message indicating whether the number is prime or not.
    """
    if number <= 1: # Numbers less than or equal to 1 are not prime
        return f"The number {number} is not a prime number."
    if number == 2 or number == 3 or number == 5: # 2, 3, and 5 are prime numbers
        return f"The number {number} is a prime number."
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0: # Eliminate multiples of 2, 3, and 5
        return f"The number {number} is not a prime number."
    
    for i in range(7, int(math.sqrt(number)) + 1, 2): # Check for factors from 7 to the square root of the number
        if number % i == 0:
            return f"The number {number} is not a prime number." # Found a factor, so it's not prime
    
    return f"The number {number} is a prime number." # No factors found, so it's prime
# Example usage
if __name__ == "__main__":
    user_input = input("Enter a number: ") # Read input from the user
    if not user_input.isdigit(): # Check if the input is a numeric character
        print("Invalid input. Please enter a valid number.")
    else:
        number = int(user_input) # Convert the input to an integer
        result = is_prime(number) # Call the function to check if the number is prime
        print(result) # Print the result
        