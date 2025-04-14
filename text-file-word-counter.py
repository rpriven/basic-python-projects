def count_words(filename):
    """Count the number of words in a text file."""
    try:
        with open(filename, 'r') as file:
            # Read the file content
            content = file.read()
            
            # Split the content into words
            words = content.split()
            
            # Return the count
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Simple command line interface
if __name__ == "__main__":
    filename = input("Enter the path to a text file: ")
    word_count = count_words(filename)
    
    if word_count > 0:
        print(f"The file contains {word_count} words.")
