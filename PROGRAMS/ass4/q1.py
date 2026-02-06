# write a py program to detect weather the message is spam message or genune message if it is spam message print spam else not spam

def detect_spam(message):
    """
    This function checks whether a given message is spam or not.
    
    Parameters:
    message (str): The message to be checked.
    
    Returns:
    str: A message indicating whether the input message is spam or not.
    """
    # List of common spam keywords
    spam_keywords = ['win', 'prize', 'free', 'click', 'buy now', 'subscribe', 'limited time offer']
    
    # Convert the message to lowercase for case-insensitive comparison
    message_lower = message.lower()
    
    # Check if any spam keyword is present in the message
    for keyword in spam_keywords:
        if keyword in message_lower:
            return "Spam Message"
    
    return "Not a Spam Message"
# Example usage
if __name__ == "__main__":
    user_message = input("Enter a message: ") # Read input message from the user
    result = detect_spam(user_message) # Call the function to check if the message is spam
    print(result) # Print the result

