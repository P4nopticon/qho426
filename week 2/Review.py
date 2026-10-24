print("choose: cave, forest or home")
place= input()
if place == "cave" or place == "forest":
    print("Take a torch? yes/no")
    torch = input()
    if torch == "yes" and not (place == "home"):
        print("Explore carefully!")
    else:
        print("Return before dark.")
elif place == "home":
    print("You are safe.")
else:
    print("Unknown destination.")
