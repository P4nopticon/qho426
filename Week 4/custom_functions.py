def listen():
    sound = input("What sound did you hear?\n")
    print(f"That was a loud sound!")


def identify():
    response = input("What do you see?\n")
    if response == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

def escape_by(plan) :
    if plan == "escape by jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")

    elif plan == "cross the bridge ahead":
        print ("That might just work! Let's go!")
    else:
        print ("we cannot escape that way! The boulder is in the way!")

escape_by("jumping over")
escape_by("running around")
escape_by("cross the bridge ahead")