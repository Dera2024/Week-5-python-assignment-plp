
# Online Python - IDE, Editor, Compiler, Interpreter

def main():
    try:
        # File Creation
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 12345\n")
            file.write("Third line, with another number: 67890\n")
        print("File 'my_file.txt' created and initial lines written successfully.")

        # File Reading and Display
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("Reading content from 'my_file.txt':")
        print(content)

        # File Appending
        with open('my_file.txt', 'a') as file:
            file.write("Appending the first additional line.\n")
            file.write("Appending the second additional line with a number: 54321\n")
            file.write("Appending the third additional line: End of file.\n")
        print("Additional lines appended to 'my_file.txt' successfully.")

        # Reading the file again to display the new content
        with open('my_file.txt', 'r') as file:
            updated_content = file.read()
        print("Updated content from 'my_file.txt':")
        print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operation completed.")

if __name__ == "__main__":
    main()