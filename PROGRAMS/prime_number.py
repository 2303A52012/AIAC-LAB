# generate an optimal py code that checks if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# read input
def read_input():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        return num
    except ValueError:
        print("Please enter a valid integer.")
        return None
# main
if __name__ == "__main__":
    num = read_input()
    if num is not None:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")