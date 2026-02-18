'''
# Bug: Mixed indentation
def func():
x = 5
y = 10
return x+y
Expected Output : Consistent indentation applied.
'''
def func():
    x = 5
    y = 10
    return x+y
print(func())