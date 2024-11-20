# def print_file_contents(file_path):
#     """Print the contents of a file."""
#     with open(file_path, 'r') as file:
#         contents = file.read()
#         print("Contents of the file:")
#         print(contents)

def copy_file(source_path, destination_path):
    """Copy a file from source to destination."""
    with open(source_path, 'r') as source_file:
        contents = source_file.read()
    
    with open(destination_path, 'w') as dest_file:
        dest_file.write(contents)

    print(f"File copied from '{source_path}' to '{destination_path}'.")
    
    with open(destination_path, 'r') as dest_file:
        contents = dest_file.read()
        print(contents)
# def read_write_file(file_path, text_to_write):
#     """Read a file, append text, and print the updated contents."""
#     with open(file_path, 'r') as file:
#         contents = file.read()
#         print("Current contents of the file:")
#         print(contents)

#     with open(file_path, 'a') as file:
#         file.write(text_to_write + '\n')

#     with open(file_path, 'r') as file:
#         updated_contents = file.read()
#         print("Updated contents of the file:")
#         print(updated_contents)

if __name__ == "__main__":
    file_to_read = 'example.txt'
    copied_file = 'copied_example.txt'
    text_to_append = "This is a new line added to the file."

    # print_file_contents(file_to_read)
    copy_file(file_to_read, copied_file)
    # read_write_file(file_to_read, text_to_append)
