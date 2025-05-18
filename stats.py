def count_words(text):
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

def count_characters(text):
    # Convert the text to Lowercase
    text = text.lower()
    
    # Count the number of characters
    char_count = len(text)
    
    return char_count
