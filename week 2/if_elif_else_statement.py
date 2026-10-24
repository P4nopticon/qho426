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