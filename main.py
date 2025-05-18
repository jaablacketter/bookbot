def get_book_text(file_path):
    
    with open(file_path) as file:
        return file.read()

        file_contents = file.read()
    return file_contents

def main():
   # Import the count_words function from the stats module
    from stats import count_words
    from stats import count_characters
    from stats import count_characters_frequency
    from stats import sort_character_frequency
    
    # Define the path to the book file
    file_path = 'books/frankenstein.txt'

    # Get the text from the book file
    file_contents = get_book_text(file_path)

    # Count the number of words in the book
    word_count = count_words(file_contents) 
   
    # Count the number of characters in the book
    char_count = count_characters(file_contents)

    # Print the word count
    print(f"{word_count} words found in the document")
    
    # Print the character count
    print(f"{char_count} characters found in the document")

    #print character dictionary
    char_count_dict = count_characters_frequency(file_contents) 
    print(f"{char_count_dict} characters found in the document")

    #print the sorted character frequency
   # sorted_characters = sort_character_frequency(char_count_dict)
   # print(f"{sorted_characters} characters found in the document")
    print("============ BOOKBOT ============") 
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_character_frequency(char_count_dict)
    for item in sorted_characters:
        char = item["char"]
        num = item["num"]   
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()
