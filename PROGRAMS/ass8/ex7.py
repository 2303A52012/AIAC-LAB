# write a function primefactor and cheack the functonality of program using 5 test cases
def primefactor(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
# Test cases
# tc1
print(primefactor(12)) # [2, 2, 3]
# tc2
print(primefactor(28)) # [2, 2, 7]
# tc3
print(primefactor(18)) # [2, 3, 3]
# tc4
print(primefactor(29)) # [29]
# tc5
print(primefactor(100)) # [2, 2, 5, 5]