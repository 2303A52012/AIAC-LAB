def combine(list):
    return "Numbers: " + str(list)
print(combine([1, 2, 3]))
print(combine([4, 5, 6]))
print(combine([7, 8, 9]))

'''
why did we get the error in the previous code?
previous code:
def combine():
    return "Numbers: " + [1, 2, 3]
print(combine())
The error occurred because we were trying to concatenate a string ("Numbers: ") with a list ([1, 2, 3]),
which is not allowed in Python.
To fix this error, we need to convert the list to a string before concatenating it with the other string.
In the corrected code, we use the str() function to convert the list [1, 2, 3] into its string representation, 
allowing us to successfully concatenate it with "Numbers: " and produce the expected output.
'''
