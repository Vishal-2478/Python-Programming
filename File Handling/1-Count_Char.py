# WAP to accept filename as an input from user.
# Open file and count number of times a character appears in the file


# Ask user for filename and character
filename = input("Enter filename: ")
char = input("Enter a character to count: ")

# Initialize count
count = 0

try:
    # Open file in read mode
    with open(filename, "r") as file:
        # Read the entire file content
        data = file.read()
        # Count occurrences of the given character
        count = data.count(char)

    print(f"\nCharacter '{char}' appears {count} times in '{filename}'.")

except FileNotFoundError:
    print(f"\nFile '{filename}' not found!")
