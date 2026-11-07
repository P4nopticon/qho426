print("Program Started!")
print("Please enter a standard character:")
letter=input()
if len(letter)== 1:
    value= ord(letter)
    print(f"The ASCII value of {letter} is {value}")
else:
    print("Error: enter exactly one character.")
print("Program Ended!")