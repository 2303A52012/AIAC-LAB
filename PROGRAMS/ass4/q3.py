'''
Write a Python program that predicts a student’s grade based on marks obtained in their exam 
like when they get marks in between 
90-100 it should return A , 
80-89 it should return B , 
70-79 it should return C , 
60-69 it should return D , 
below 60 F
'''
def predict_grade(marks):
    """
    This function predicts a student's grade based on the marks obtained in an exam.
    
    Parameters:
    marks (int): The marks obtained by the student.
    
    Returns:
    str: The predicted grade.
    """
    if 90 <= marks <= 100:
        return "Grade: A"
    elif 80 <= marks < 90:
        return "Grade: B"
    elif 70 <= marks < 80:
        return "Grade: C"
    elif 60 <= marks < 70:
        return "Grade: D"
    elif 0 <= marks < 60:
        return "Grade: F"
    else:
        return "Invalid marks. Please enter a value between 0 and 100."
# Example usage
if __name__ == "__main__":
    user_input = input("Enter the marks obtained (0-100): ") # Read input from the user
    if not user_input.isdigit(): # Check if the input is a numeric character
        print("Invalid input. Please enter a valid number between 0 and 100.")
    else:
        marks = int(user_input) # Convert the input to an integer
        result = predict_grade(marks) # Call the function to predict the grade
        print(result) # Print the result

