'''
1. take age of the person as input
2. if age is less than 0 or greater than 120 print invalid input
3. if age is more than or equal to 18 print eligible to vote
4. if age is less than 18 print not eligible to vote
5. check for non numeric character and print invalid input
'''
def check_voting_eligibility(age):
    """
    This function checks whether a person is eligible to vote based on their age.
    
    Parameters:
    age (int): The age of the person.
    
    Returns:
    str: A message indicating whether the person is eligible to vote or if the input is invalid.
    """
    if not (0 <= age <= 120): # Check if age is in the valid range
        return "Invalid input. Please enter a valid age between 0 and 120."
    
    if age >= 18: # Check if age is 18 or older
        return "Eligible to vote."
    else:
        return "Not eligible to vote."
# Example usage
if __name__ == "__main__":
    user_input = input("Enter your age: ") # Read input from the user
    if not user_input.isdigit(): # Check if the input is a numeric character
        print("Invalid input. Please enter a valid age between 0 and 120.")
    else:
        age = int(user_input) # Convert the input to an integer
        result = check_voting_eligibility(age) # Call the function to check voting eligibility
        print(result) # Print the result
