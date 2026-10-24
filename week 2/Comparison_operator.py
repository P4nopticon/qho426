print("Please enter the first number.")
first= int(input())
print("Please enter the second number.")
second= int(input())
if first < second:
    print(f"The first number is the smallest!")
elif second < first:
    print(f"The second number is the smallest!")
else:
    print("Both numbers are equal!")