'''
write a python program to find the all the armstrong number in the given range using for loop and digit power logic.
'''
import time as t
# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Return whether the sum equals the original number
    return sum_of_powers == num

# Function to find all Armstrong numbers in a given range
def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
# Define the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
# Find and print all Armstrong numbers in the defined range
st=t.time()
armstrong_numbers = find_armstrong_numbers(start_range, end_range)
et=t.time()
print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")
print(f"start time is:{st} and end time is:{et}")
print("The time taken to execute the code is:",et-st)


'''
optimize the armstrong numbers code using list comprehension.
'''
def find_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if sum(int(digit) ** len(str(num)) for digit in str(num)) == num]# Define the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
# Find and print all Armstrong numbers in the defined range
st=t.time()
armstrong_numbers = find_armstrong_numbers(start_range, end_range)
et=t.time()
print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")
print(f"start time is:{st} and end time is:{et}")
print("The time taken to execute the code is:",et-st)

'''
Enter the start of the range: 1
Enter the end of the range: 1000
Armstrong numbers between 1 and 1000: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
start time is:1769596450.144456 and end time is:1769596450.144456
The time taken to execute the code is: 0.0
Enter the start of the range: 1
Enter the end of the range: 1000
Armstrong numbers between 1 and 1000: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
start time is:1769596453.9183116 and end time is:1769596453.9183116
The time taken to execute the code is: 0.0
'''