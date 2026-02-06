# write a py well commented code to check weather the given number is even or odd

# Function to check if a number is even or odd
def check_even_or_odd(number):
    """
    This function takes an integer as input and returns whether it is even or odd.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    str: A message indicating whether the number is even or odd.
    """
    # Check if the number is divisible by 2
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."
# Example usage
if __name__ == "__main__":
    # Input number from the user
    try:
        user_input = int(input("Enter an integer: "))
        # Call the function and print the result
        result = check_even_or_odd(user_input)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")


