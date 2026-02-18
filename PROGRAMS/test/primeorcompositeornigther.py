'''
You are a Python programming assistant.
Task: 
Write an optimized Python function that takes a single input number and classifies it as Prime, Composite, or Neither.
Constraints and Instructions:
• Accept only integer inputs and validate the input properly.
• If the number is less than or equal to 1, return "Neither".
• Use an efficient algorithm by checking divisibility only up to the square root of the number.
• The function should return one of the following strings only: 
"Prime", "Composite", or "Neither".
• Do not use external libraries.
Output should be correct and optimized

'''
def classify_number(num):
    # Validate input: Check if the input is an integer
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    
    # Check if the number is less than or equal to 1
    if num <= 1:
        return "Neither"
    
    # Check for primality by testing divisibility up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Composite"
    
    return "Prime"
# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter an integer to classify as Prime, Composite, or Neither: "))# Input number to classify
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)
    
    classification = classify_number(number)
    print(f"{number} is classified as: {classification}")