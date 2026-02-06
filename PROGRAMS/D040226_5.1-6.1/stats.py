def statistics_subject(scores_list): # input: list of 60 students marks in a subject
    average_score = sum(scores_list) / len(scores_list)
    max_score = max(scores_list)
    min_score = min(scores_list)
    pass_count = 0
    fail_count = 0
    for i in scores_list:
        if i>=40:
            pass_count += 1
        else:
            fail_count += 1
    return {
        'average_score': average_score,
        'max_score': max_score,
        'min_score': min_score,
        'pass_count': pass_count,
        'fail_count': fail_count
    }
# Example usage
if __name__ == "__main__":
    scores = [55, 70, 45, 30, 90, 85, 60, 75, 40, 20,
              95, 88, 76, 34, 67, 82, 49, 53, 61, 72,
              38, 44, 59, 66, 78, 81, 29, 33, 47, 50,
              91, 87, 73, 64, 39, 41, 54, 68, 79, 83,
              22, 27, 35, 46, 52, 58, 65, 71, 80, 84,
              23, 26, 31, 36, 42, 48, 56, 62, 69, 74]
    stats = statistics_subject(scores)
    print(f"Average Score: {stats['average_score']}")
    print(f"Max Score: {stats['max_score']}")
    print(f"Min Score: {stats['min_score']}")
    print(f"Pass Count: {stats['pass_count']}")
    print(f"Fail Count: {stats['fail_count']}")

'''
Average Score: 57.63333333333333
Max Score: 95
Min Score: 20
Pass Count: 46
Fail Count: 14
'''