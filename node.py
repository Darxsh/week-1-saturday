def count_vowels(s):
    #  vowels
    vowels = 'aeiouAEIOU'
    
    count = 0
    
    
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    return count

# Main function to get user input and display the count of vowels
def main():
    # Take input from the user
    s = input("Enter a string: ")
    # Get the count of vowels
    vowel_count = count_vowels(s)
    # Print the count of vowels
    print(f"Number of vowels in '{s}': {vowel_count}")

# Run the main function
if __name__ == "__main__":
    main()
