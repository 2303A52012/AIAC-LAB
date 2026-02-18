def repeat_text(n):
    return "Hello" * int(n)  # Bug: TypeError due to string multiplication; fixed by converting n to an integer
print(repeat_text(3.5))
print(repeat_text("2"))
print(repeat_text(4))

'''In the original code, we were trying to multiply the string "Hello" by a 
float (3.5) and a string ("2"),which is not allowed in Python. By converting n
to an integer using int(n), we can successfully perform the string multiplication 
without any errors. 
This allows us to repeat the text "Hello" the specified number of times, 
even if the input is a float or a string that can be converted to an integer.
'''