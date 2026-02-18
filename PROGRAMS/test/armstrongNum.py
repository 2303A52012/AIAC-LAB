'''
write a py program to cheack wheather the given number is an armstrong number or not
input : a number
output : true if armstrong number and false if not
handle the exceptions for invalid input and edge cases
Ex: 1. input : 153
    output : 153 is an armstrong number (1^3 + 5^3 + 3^3 = 153)
    2. input : 123
    output : 123 is not an armstrong number (1^3 + 2^3 + 3^3 = 36)    
    3. input : 9474
    output : 9474 is an armstrong number (9^4 + 4^4 + 7^4 + 4^4 = 9474)
    4. input 123
    output : 123 is not an armstrong number (1^3 + 2^3 + 3^3 = 36)
'''

def is_armstrong(num):
    # Convert the number to a string to iterate through its digits
    str_num = str(num)
    # Calculate the number of digits in the number
    num_digits = len(str_num)
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == num
# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check if it is an Armstrong number: "))# Input number to check for Armstrong number
    except ValueError:
        print("Invalid input. Please enter an integer.")
        exit(1)
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

