
#Expected Output: Correct unpacking or using _ for extra values.
a,b, _ = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
a,b,*_= (1, 2, 3, 8)
print(a)  # Output: 1
print(b)  # Output: 2

a, b, *c, = (1, 2, 3, 8)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 8]