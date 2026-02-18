'''
write a py program to detect the emotion of the given message
input: a user message(str)
output: the emotion of the message(str) any one from[‘happy', 'sad', 'angry', 'excited', 'nervous', ’neutral’] 
ex:
input: "I am so happy today!"
output: "happy"
'''
def detect_emotion(message):
    # Define keywords for each emotion
    emotions = {
        'happy': ['happy', 'joy', 'pleased', 'delighted', 'content'],
        'sad': ['sad', 'unhappy', 'depressed', 'down', 'miserable'],
        'angry': ['angry', 'mad', 'furious', 'irritated', 'annoyed'],
        'excited': ['excited', 'thrilled', 'ecstatic', 'overjoyed', 'enthusiastic'],
        'nervous': ['nervous', 'anxious', 'worried', 'tense', 'uneasy'],
        'neutral': ['neutral', 'calm', 'indifferent', 'unemotional']
    }
    
    # Convert the message to lowercase for case-insensitive matching
    message = message.lower()
    
    # Check for keywords in the message and return the corresponding emotion
    for emotion, keywords in emotions.items():
        if any(keyword in message for keyword in keywords):
            return emotion
    
    # If no keywords are found, return neutral
    return 'neutral'
# Example usage
if __name__ == "__main__":
    user_message = input("Enter a message to detect emotion: ")
    emotion = detect_emotion(user_message)
    print(f"The detected emotion is: {emotion}")