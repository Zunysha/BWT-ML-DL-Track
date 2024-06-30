# file_handling.py
filename='data.txt'
def read_file(filename):
    """
    Reads the contents of a file and prints it. 
    Also counts the number of words in the file.
    
    :param filename: Name of the file to read
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Contents:\n")
            print(content)
            word_count = len(content.split())
            print(f"\nNumber of words: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading '{filename}'.")


def write_to_file(filename, content):
    """
    Writes user input to a file.
    
    :param filename: Name of the file to write to
    :param content: Content to write into the file
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to '{filename}'.")
    except IOError:
        print(f"Error: An error occurred while writing to '{filename}'.")


def main():
    # Read from 'data.txt'
    read_file('data.txt')

    # Get user input and write to 'output.txt'
    user_input = input("\nEnter some text to write to 'output.txt': ")
    write_to_file('output.txt', user_input)


if __name__ == "__main__":
    main()
