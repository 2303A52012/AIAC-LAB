'''
generate a list of hallticket numbers of 10 students
The hallticket numbers should be in the format "2303A52XXX" where XXX is a three-digit number
print the generated hallticket numbers
traverse the list and make another list with the hallticket numbers which end with 3 or 5 or 7
print filtered lists
'''
import random
def generate_hallticket_numbers(count):
    """
    This function generates a list of hallticket numbers for a given count of students.
    
    Parameters:
    count (int): The number of hallticket numbers to generate.
    
    Returns:
    list: A list of generated hallticket numbers.
    """
    hallticket_numbers = []
    for _ in range(count):
        # Generate a random three-digit number
        three_digit_number = random.randint(0, 999)
        # Format the number to ensure it is three digits with leading zeros if necessary
        formatted_number = f"{three_digit_number:03}"
        # Create the full hallticket number
        hallticket_number = f"2303A52{formatted_number}"
        hallticket_numbers.append(hallticket_number)
    return hallticket_numbers
def filter_hallticket_numbers(hallticket_numbers):
    """
    This function filters hallticket numbers that end with 3, 5, or 7.
    Parameters:
    hallticket_numbers (list): The list of hallticket numbers to filter.
    Returns:
    list: A list of filtered hallticket numbers.
    """
    filtered_numbers = []
    for number in hallticket_numbers:
        if number[-1] in ['3', '5', '7']: # Check if the last character is 3, 5, or 7
            filtered_numbers.append(number)
    return filtered_numbers
# Example usage
if __name__ == "__main__":
    # Generate hallticket numbers for 10 students
    hallticket_numbers = generate_hallticket_numbers(10)
    print("Generated Hallticket Numbers:")
    print(hallticket_numbers)
    
    # Filter hallticket numbers that end with 3, 5, or 7
    filtered_numbers = filter_hallticket_numbers(hallticket_numbers)
    print("Filtered Hallticket Numbers (ending with 3, 5, or 7):")
    print(filtered_numbers)