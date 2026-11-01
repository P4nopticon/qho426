print("Program Started!")

# Prompt the user and convert input to a positive integer
user_input = input("Please enter an ASCII code:\n ")
code = abs(int(user_input))

# Check if the code falls within the printable ASCII range (32 to 126 inclusive)
if code in range(32, 126):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print(f"Error: {code} is outside the valid printable ASCII range (32-126).")

print("Program Ended!")