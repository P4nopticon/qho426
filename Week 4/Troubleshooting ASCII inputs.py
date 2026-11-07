from sys import excepthook

try:
    code= abs(int(input("ASCII code:")))
    if code in range(32, 127):
        print(chr(code))
    else:
        print("Not printable ASCII")
except ValueError:
    print("Please enter a whole number")
