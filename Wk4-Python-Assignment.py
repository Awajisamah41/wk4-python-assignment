import sys

def process_file(input_filename, output_filename):
    """
    Reads a file, processes its content (converts to uppercase and counts words),
    and writes the results to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        # Step 1: Read the contents of the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Step 2: Process the content
    # Count the number of words by splitting the content
    word_count = len(content.split())
    
    # Convert all text to uppercase
    processed_content = content.upper()

    # Step 3: Write the processed text and word count to the output file
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(f"--- Processed Content ---\n")
            output_file.write(processed_content)
            output_file.write(f"\n\n--- Summary ---\n")
            output_file.write(f"Total words: {word_count}\n")
            
        # Step 4: Print a success message
        print(f"Success! The content from '{input_filename}' has been processed.")
        print(f"The modified content and word count are saved in '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# --- Main part of the script ---
if __name__ == "__main__":
    # Create the input file with some sample text for the challenge
    sample_text = """Hello, this is a test document.
This challenge is about file handling in Python.
We will count these words and convert them all to uppercase.
Let's see the final result!
"""
    input_file_name = "input.txt"
    output_file_name = "output.txt"
    
    try:
        with open(input_file_name, 'w') as f:
            f.write(sample_text)
        print(f"'{input_file_name}' created with sample content.")
    except Exception as e:
        print(f"Failed to create the input file: {e}")
        sys.exit(1)

    # Call the main processing function
    process_file(input_file_name, output_file_name)
