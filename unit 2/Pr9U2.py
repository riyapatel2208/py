# Function to split text into words
def split_text_into_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()  # Split the text into words
    return words

# Function to join words to form sentences
def join_words_to_sentences(words):
    return ' '.join(words)  # Join the words into a single sentence

# File paths
input_file = 'ex.txt'  # Input file containing the text
output_file = 'output.txt'  # Output file to save the sentences

# Process the files
try:
    # Step 1: Read and split text into words
    words = split_text_into_words(input_file)
    
    # Step 2: Join the words to form sentences
    sentence = join_words_to_sentences(words)
    
    # Step 3: Write the sentence to the output file
    with open(output_file, 'w') as file:
        file.write(sentence)
    
    print(f"Text has been processed and saved to {output_file}.")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")