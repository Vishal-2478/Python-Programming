# file_copy_display.py

# Ask user for file names
source_file = input("Enter source filename: ")
target_file = input("Enter target filename: ")

try:
    # Open the source file in read mode
    with open(source_file, "r") as src:
        data = src.read()

        # (A) Display content on screen
        print("\n===== File Content =====")
        print(data)

    # (B) Write the same data to another file
    with open(target_file, "w") as tgt:
        tgt.write(data)

    print(f"\nData successfully written to '{target_file}'")

except FileNotFoundError:
    print(f"\nFile '{source_file}' not found!")
except Exception as e:
    print(f"\nAn error occurred: {e}")
