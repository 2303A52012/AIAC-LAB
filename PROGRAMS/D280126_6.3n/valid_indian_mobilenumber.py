
'''
write a python program that validates Indian mobile numbers using functions
a valid Indian mobile number must start with 6, 7, 8, or 9 and must be 10 digits long.
'''
def is_valid_indian_mobile_number(mobile_number):
    # Check if the length of the mobile number is 10
    if len(mobile_number) != 10:
        return False
    # Check if all characters are digits
    if not mobile_number.isdigit():
        return False
    # Check if the first digit is 6, 7, 8, or 9
    if mobile_number[0] not in '6789':
        return False
    return True
# Example usage
if __name__ == "__main__":
    test_numbers = [
        "9876543210",
        "1234567890",
        "8765432109",
        "5678901234",
        "9988776655",
        "abcdefghij",
        "912345678"
    ]
    for number in test_numbers:
        if is_valid_indian_mobile_number(number):
            print(f"{number} is a valid Indian mobile number.")
        else:
            print(f"{number} is not a valid Indian mobile number.")

'''
op:
9876543210 is a valid Indian mobile number.
1234567890 is not a valid Indian mobile number.
8765432109 is a valid Indian mobile number.
5678901234 is not a valid Indian mobile number.
9988776655 is a valid Indian mobile number.
abcdefghij is not a valid Indian mobile number.
912345678 is not a valid Indian mobile number.
'''