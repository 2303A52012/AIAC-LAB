# write a python function DecimalToBinary that returns the binary representation of a given decimal number. 
def DecimalToBinary(n):
    '''
    returns the binary representation of a given decimal number
    >>> DecimalToBinary(10)
    '1010'
    >>> DecimalToBinary(0)
    '0111'
    >>> DecimalToBinary(5)
    '101'
    '''
    if not isinstance(n, int):
        return "float numbers are not supported."
    if n < 0:
        return "Negative numbers are not supported."
    elif n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary