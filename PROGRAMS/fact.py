# Program to calculate the factorial of a number using an iterative approach
# Uses loops only, with comments explaining each step

def calculate_factorial(n):
	"""Calculate factorial iteratively."""
	result = 1
	for i in range(2, n + 1):  # Loop from 2 to n
		result *= i
	return result

if __name__ == "__main__":
	# Take input from the user
	number = int(input("Enter a number: "))

	# Check if the number is negative
	if number < 0:
		print("Factorial does not exist for negative numbers.")
	elif number == 0:
		print("The factorial of 0 is 1.")
	else:
		# Call the function and print the result
		fact = calculate_factorial(number)
		print(f"The factorial of {number} is {fact}")
