'''
input :2024 output:2024 is a leap year
input :2023 output:2023 is not a leap year
input :2000 output:2000 is a leap year
input :1900 output:1900 is not a leap year
'''
try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter a valid year.")
    exit(1)
    
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    