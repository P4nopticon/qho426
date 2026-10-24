import numbers

print("What type of book is this")
book = input()
if book == "adventure":
    print("I like adventure books!")
print("Finished reading book!")


print("Please enter the activity to be performed.")
activity = input()
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")
print("Activity completed!")

print("Towards which direction should I go (up, down left or right)?")
direction = input()
if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in an downward direction!")
elif direction == "left":
    print("I am moving left!")
elif direction == "right":
    print("I am moving right!")
else:
    print("Unknown direction!")

print("Please enter a whole number")
number = int(input())
if number % 2 == 0:
    print(f"The number {number} is even!.")
else:
    print(f"The number {number} is odd!.")

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
