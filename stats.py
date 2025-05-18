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

    # dictionary to count the number of times a character appears
def count_characters_frequency(text): 

    # Convert the text to lowercase
    text = text.lower()    
    
    # Create a dictionary to store character frequencies
    character_count = {}

    # Count each indiidual charater in text
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
    
def sort_character_frequency(character_count):
    result = []
    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_characters:
        result.append({"char": char, "num": count})
    return result
    
    
   
