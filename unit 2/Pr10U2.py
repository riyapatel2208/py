def find_and_replace(file_path, old_word, new_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        updated_content = content.replace(old_word, new_word)
        
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print(f"Replaced all occurrences of '{old_word}' with '{new_word}' in {file_path}.")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'example.txt'
find_and_replace(file_path, 'gujarat', 'gujrat')