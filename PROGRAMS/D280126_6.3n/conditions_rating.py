'''
write a python using nested if-elif-else conditions to classify online shopping feedback 
as Positive,Neutral, or Negative based on a numerical rating (1–5).
'''
def classify_feedback(rating):
    if rating >= 4 and rating <= 5:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    elif rating >= 1 and rating <= 2:
        return "Negative"
    else:
        return "Invalid rating. Please enter a rating between 1 and 5."
    
# rewrite the same program using dictionary-based or match-case structure.
def classify_feedback_dict(rating):
    feedback_dict = {
        (4, 5): "Positive",
        (3, 3): "Neutral",
        (1, 2): "Negative"
    }
    for key in feedback_dict:
        if rating >= key[0] and rating <= key[1]:
            return feedback_dict[key]
    return "Invalid rating. Please enter a rating between 1 and 5."

def classify_feedback_match(rating):
    match rating:
        case 4 | 5:
            return "Positive"
        case 3:
            return "Neutral"
        case 1 | 2:
            return "Negative"
        case _:
            return "Invalid rating. Please enter a rating between 1 and 5."


# Example usage
if __name__ == "__main__":
    ratings = range(0, 7)  # Testing ratings from 0 to 6
    print("Using nested if-elif-else:")
    for rate in ratings:
        classification = classify_feedback(rate)
        print(f"Rating: {rate} - Feedback: {classification}")
    print("\nUsing dictionary-based approach:")
    for rate in ratings:
        classification_dict = classify_feedback_dict(rate)
        print(f"Rating: {rate} - Feedback (Dict): {classification_dict}")
    print("\nUsing match-case approach:")
    for rate in ratings:
        classification_match = classify_feedback_match(rate)
        print(f"Rating: {rate} - Feedback (Match): {classification_match}")
        

