# Write a Python program that detects the emotion of a sentence like 'happy', 'sad', 'angry', 'excited', 'nervous', 'neutral' like "iam very happy today" it should return happy
def detect_emotion(sentence):
    """
    This function detects the emotion expressed in a given sentence.
    
    sentence (str): The sentence to be analyzed.
    
    Returns:
    str: A message indicating the detected emotion.
    """
    # Dictionary mapping keywords to emotions
    emotion_keywords = {
        'happy': ['happy', 'joyful', 'elated', 'pleased', 'content'],
        'sad': ['sad', 'unhappy', 'sorrowful', 'dejected', 'downcast'],
        'angry': ['angry', 'mad', 'furious', 'irate', 'annoyed'],
        'excited': ['excited', 'thrilled', 'eager', 'enthusiastic', 'overjoyed'],
        'nervous': ['nervous', 'anxious', 'worried', 'tense', 'apprehensive'],
        'neutral': ['neutral', 'indifferent', 'unemotional', 'calm', 'composed']
    }
    
    # Convert the sentence to lowercase for case-insensitive comparison
    sentence_lower = sentence.lower()
    
    # Check for keywords in the sentence and determine the emotion
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in sentence_lower:
                return f"The detected emotion is: {emotion.capitalize()}"
    
    return "The detected emotion is: Neutral"
# Example usage
if __name__ == "__main__":
    user_sentence = input("Enter a sentence: ") # Read input sentence from the user
    result = detect_emotion(user_sentence) # Call the function to detect emotion
    print(result) # Print the result
