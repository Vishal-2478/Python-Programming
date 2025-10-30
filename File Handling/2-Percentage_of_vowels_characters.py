# WAP that reads data from a file and calculates percentage of vowels and consonants in the file

filename = input("Enter filename: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
total_letters = 0

try:
    with open(filename, "r") as file:
        data = file.read()

        for ch in data:
            if ch.isalpha():  # Check if it's a letter
                total_letters += 1
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

    if total_letters == 0:
        print("\nNo alphabetic characters found in file.")
    else:
        vowel_percentage = (vowel_count / total_letters) * 100
        consonant_percentage = (consonant_count / total_letters) * 100

        print(f"\nTotal letters: {total_letters}")
        print(f"Vowels: {vowel_count} ({vowel_percentage:.2f}%)")
        print(f"Consonants: {consonant_count} ({consonant_percentage:.2f}%)")

except FileNotFoundError:
    print(f"\nFile '{filename}' not found!")
