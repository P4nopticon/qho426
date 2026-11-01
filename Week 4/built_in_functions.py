print("Program started!")

letter= input ("please enter a letter:\n")

if len(letter)== 1:
    acsii_code= ord(letter)
    print(f"The ASCII code for {letter} is {acsii_code}")

else:
    print("Please enter exactly one character.")

print("Program end!")