print("Program Started!")
print("Please enter an ASCII code:")
code = abs(int(input()))
if code in range(32, 127):
    character= chr(code)
    pri