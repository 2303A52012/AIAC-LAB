# write a python program that generates anamorphic nums in range of 1 to 1000 using for loop in functions
import time as t
def is_anamorphic(num):
    square = num * num
    num_str = str(num)
    square_str = str(square)
    return square_str.endswith(num_str)

def generate_anamorphic_numbers(start, end):
    
    anamorphic_numbers = []
    for num in range(start, end + 1):
        if is_anamorphic(num):
            anamorphic_numbers.append(num)
    return anamorphic_numbers

# write a python program that generates anamorphic nums in range of 1 to 1000 using while loop in functions
def generate_anamorphic_numbers_while(start, end):
    anamorphic_numbers_while = []
    i = start
    while i <= end:
        if is_anamorphic(i):
            anamorphic_numbers_while.append(i)
        i += 1
    return anamorphic_numbers_while

# Example usage
if __name__ == "__main__":
    start_range = 1
    end_range = 1000
    start_time = t.time()
    anamorphic_nums_for = generate_anamorphic_numbers(start_range, end_range)
    print("Anamorphic numbers using for loop:", anamorphic_nums_for)
    end_time = t.time()
    print(f"start: {start_time}, end: {end_time}")
    print("Time taken using for loop:", end_time - start_time)
    st=t.time()
    anamorphic_nums_while = generate_anamorphic_numbers_while(start_range, end_range)
    print("Anamorphic numbers using while loop:", anamorphic_nums_while)
    et=t.time()
    print(f"start: {st}, end: {et}")
    print("Time taken using while loop:", et - st)
