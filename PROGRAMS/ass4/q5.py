'''
write a python program to find wheather the studnet is pased or failed
1. take the input from the user as marks 
2. the range of enterd marks should be in between 0-100
3. if marks are not in the range print invalid input
4. if in range check whether the marks are greater than or equal to 40
5. if yes print passed else print failed
6. cheack for the non numeric character and print invalid input
'''
def check_pass_fail(marks):
    """
    This function checks whether a student has passed or failed based on the marks obtained.
    
    Parameters:
    marks (int): The marks obtained by the student.
    
    Returns:
    str: A message indicating whether the student has passed or failed, or if the input is invalid.
    """
    if not (0 <= marks <= 100): # Check if marks are in the valid range
        return "Invalid input. Please enter marks between 0 and 100."
    
    if marks >= 40: # Check if marks are greater than or equal to 40
        return "Passed"
    else:
        return "Failed"
# Example usage
if __name__ == "__main__":
    user_input = input("Enter the marks obtained (0-100): ") # Read input from the user
    if not user_input.isdigit(): # Check if the input is a numeric character
        print("Invalid input. Please enter a valid number between 0 and 100.")
    else:
        marks = int(user_input) # Convert the input to an integer
        result = check_pass_fail(marks) # Call the function to check pass/fail status
        print(result) # Print the result
    
