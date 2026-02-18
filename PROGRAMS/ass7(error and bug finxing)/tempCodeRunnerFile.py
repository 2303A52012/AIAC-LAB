# Bug: Shallow copy issue
import copy
a=[2,[4,6,9],10]
b=a.copy.deepcopy(a)
#b[1][2][0]=100
b[1][2]=100
print(a)