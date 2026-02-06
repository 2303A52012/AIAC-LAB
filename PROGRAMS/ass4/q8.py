'''
1. generate a list of words
2. traverse the list and calculate the length of each word and store it in a new list
3. analize the new list and return the short if the word length is less than 5 else return long
4. print results
'''
def analyze_word_lengths(words):
    """
    This function analyzes the lengths of words in the provided list.
    
    Parameters:
    words (list): A list of words.
    
    Returns:
    list: A list of tuples containing the word and its length category ("short" or "long").
    """
    results = []
    for word in words:
        length = len(word) # Calculate the length of the word
        if length < 5:
            results.append((word, "short"))
        else:
            results.append((word, "long"))
    return results
# Example usage
if __name__ == "__main__":
    word_list = ["apple", "bat", "cat", "dolphin", "egg", "fish", "goat", "hippopotamus"] # List of words
    length_analysis = analyze_word_lengths(word_list) # Call the function to analyze word lengths
    for word, length_category in length_analysis:
        print(f"{word}: {length_category}") # Print each word with its length category
        
    