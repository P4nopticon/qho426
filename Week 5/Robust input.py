def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu_and_input():
    print("Please select a direction:")
    options = directions()
    for i in range(len(options)):
        print(f"{i}: {options[i]}")

    while True:
        try:
            choice = int(input(f"Direction (0-{len(options) - 1}): "))
            if 0 <= choice < len(options):
                break
            print(f"Choose a number from 0 to {len(options) - 1}.")
        except ValueError:
            print("Enter a number.")
    return options[choice]


def run_task4():
    route = []
    print("Working out escape route...")
    for _ in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run_task4()