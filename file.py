def modify_content(content):
    """Modify the content (example: convert to uppercase)"""
    return content.upper()

try:
    # Ask user for the filename
    filename = input("Enter the filename to read: ")

    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except IOError:
    print("Error: Could not read/write the file. Check file permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
