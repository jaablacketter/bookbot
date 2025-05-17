def get_book_text(file_path):
    
    with open(file_path) as file:
        return file.read()

        file_contents = file.read()
    return file_contents

def main():
   
    # Define the path to the book file
    file_path = 'books/frankenstein.txt'
    
    # Get the text from the book file
    file_contents = get_book_text(file_path)
    
    # Print the first 500 characters of the book text
    print(file_contents)

main()
