def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        modified_content = content.upper()
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"File modified and saved as '{output_filename}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred while handling the file: {e}")

input_filename = "input.txt"
output_filename = "output.txt"
read_and_write_file(input_filename, output_filename)


def safe_read_file():
    filename = input("Please enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred while reading the file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

safe_read_file()
