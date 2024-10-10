

# File Creation: Create and write to a file
try:
    # Step 1: Create a new text file and write initial content
    with open("my_file.txt", 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("40 is a number.\n")
        file.write("Python is interesting to learn is an example of a string with words.\n")
    print("File created and initial content written.")

    # Step 2: Read and display the contents of the file
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nInitial content of the file:")
        print(content)

    # Step 3: Open the file in append mode and add more lines
    with open("my_file.txt", 'a') as file:
        file.write("This is an appended line.\n")
        file.write("A line with even numbers between 0 and 9: 0,2,4,6,8.\n")
        file.write("There are five odd number between zero and nine is an example of an appended line with text.\n")
    print("\nAdditional lines appended to the file.")

    # Step 4: Read and display the updated content of the file
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)

# Error Handling: Catch and manage potential file-related exceptions
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied. You do not have access to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operation completed.")
