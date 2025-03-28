def print_file_contents(file_path):
    """Prints the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please check the file path.")

def copy_file(source_path, destination_path):
    """Copies the contents of one file to another without using shutil."""
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        
        print(f"File copied from {source_path} to {destination_path}")
    except FileNotFoundError:
        print("Source file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_write_file(file_path, new_content):
    """Reads the contents of a file, writes new content to it, and then displays updated content."""
    try:
        # Read the current content
        print("Current file content:")
        with open(file_path, 'r') as file:
            print(file.read())
        
        # Write new content
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("New content written to the file.")
        
        # Display updated content
        print("Updated file content:")
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Modify these paths and content as needed
    file_path = "example.txt"
    copy_destination = "example_copy.txt"
    new_content = "This is the new content for the file."

    # Print file contents
    print("** Print File Contents **")
    print_file_contents(file_path)

    # Copy a file
    print("\n** Copy File **")
    copy_file(file_path, copy_destination)

    # Read and write a file
    # print("\n** Read and Write File **")
    # read_write_file(file_path, new_content)