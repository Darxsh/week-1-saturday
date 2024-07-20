# Function to reverse number
def reverse_number(num):
    # Convert the number to string, reverse the string, and convert it back to integer
    reversed_num = int(str(num)[::-1])
    return reversed_num

# Main function 
def main():
    # input from the user
    num = int(input("Enter a number: "))
    #  reversed number
    reversed_num = reverse_number(num)
    # Print the reversed number
    print(f"Reversed Number: {reversed_num}")

if __name__ == "__main__":
    main()
