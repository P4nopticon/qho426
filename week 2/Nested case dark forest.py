# Retrieve type of adventure from user
print("What type of adventure should I have?")
adventure = input()

# Determine route
if adventure == "scary" or adventure == "short":
    print("Entering the dark forest!")

    # Retrieve hearing response from user
    print("What did I hear?")
    heard = input()

    # Retrieve sight response from user
    print("What did I see?")
    seen = input()

    # Nested condition: check responses in the dark forest
    if heard == "grrr" and seen == "two red eyes":
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue.")

elif adventure == "safe" or adventure == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")