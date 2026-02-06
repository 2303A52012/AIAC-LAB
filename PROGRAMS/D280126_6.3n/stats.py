'''
a python program to calculate basic statistics like
• Minimum, Maximum
• Mean, Median, Mode
• Variance, Standard Deviation
'''
import statistics as stats
def  statistical_operations(tuple_num):

    minimum = min(tuple_num)
    maximum = max(tuple_num)
    mean = stats.mean(tuple_num)
    median = stats.median(tuple_num)
    try:
        mode = stats.mode(tuple_num)
    except stats.StatisticsError:
        mode = "No unique mode found"
    variance = stats.variance(tuple_num)
    std_deviation = stats.stdev(tuple_num)

    return {
        "Minimum": minimum,
        "Maximum": maximum,
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": std_deviation
    }

# Example usage
if __name__ == "__main__":
    data = (10, 20, 20, 30, 40, 50, 60, 70, 80, 90)
    stats_result = statistical_operations(data)
    print("the given data is:", data)
    print("Statistical Operations Results:")
    for key, value in stats_result.items():
        print(f"{key}: {value}")
    
