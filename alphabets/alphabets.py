# Get user input
user_input = input("Enter a character: ")

# Check if the input is a single character
if len(user_input) == 1:
    # Check if it's an alphabet
    if user_input.isalpha():
        print(f"'{user_input}' is an alphabet.")
    else:
        print(f"'{user_input}' is not an alphabet.")
else:
    print("Please enter only a single character.")
