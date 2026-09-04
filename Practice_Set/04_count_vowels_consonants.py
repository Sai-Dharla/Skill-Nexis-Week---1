def count_vowels_consonants(text):
    """Counts vowels and consonants in a given string."""
    vowels_count = 0
    consonants_count = 0    
    # Define what counts as a vowel
    vowels = "aeiouAEIOU"   
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1               
    return vowels_count, consonants_count
def main():
    print("--- Vowels and Consonants Counter ---")
    text = input("Enter a string: ")   
    vowels, consonants = count_vowels_consonants(text)    
    print(f"Total Vowels: {vowels}")
    print(f"Total Consonants: {consonants}")
if __name__ == "__main__":
    main()