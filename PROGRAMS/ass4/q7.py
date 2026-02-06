'''
1. generate a list of studnts names
2. travers the list and make another list with reversed names
3. compare both lists if the original name and reversed name are same then print the name and -> palindrome
4. if not same print the name and -> not a palindrome
'''
def check_palindromes(names):
    """
    This function checks which names in the provided list are palindromes.
    
    Parameters:
    names (list): A list of student names.
    
    Returns:
    list: A list of tuples containing the name and whether it is a palindrome or not.
    """
    results = []
    for name in names:
        reversed_name = name[::-1] # Reverse the name
        if name.lower() == reversed_name.lower(): # Compare original and reversed names (case insensitive)
            results.append((name, "-> palindrome"))
        else:
            results.append((name, "-> not a palindrome"))
    return results
# Example usage
if __name__ == "__main__":
    student_names = ["Anna", "Bob", "Cathy", "David", "Eve", "Hannah", "John"] # List of student names
    palindrome_results = check_palindromes(student_names) # Call the function to check for palindromes
    for name, result in palindrome_results:
        print(f"{name} {result}") # Print each name with its palindrome status
