def process_file():
    # Ask user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., reverse each line)
        lines = content.splitlines()
        modified_lines = [line[::-1] for line in lines]
        modified_content = "\n".join(modified_lines)

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as file:
            file.write(modified_content)

        print(f"✅ Success! Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
process_file()
