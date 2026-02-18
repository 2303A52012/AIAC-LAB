'''
write a python program where it cheacks weather the given number is a palindrome or not
input  : a number
output : true if palindrome and false if not

'''
def is_palindrome(num):
    # Convert the number to a string to check for palindrome
    str_num = str(num)
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]
# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check if it is a palindrome: "))# Input number to check for palindrome
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
