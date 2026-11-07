def sum_weights(person, inventory):
    return person + inventory


def calc_avg_weight(person, inventory):
    total = sum_weights(person, inventory)
    return total / 2


# --- Main function ---
def run():
    person = float(input("What is the weight of the person?\n"))
    inventory = float(input("What is the weight of their inventory?\n"))
    choice = input("What would you like to calculate (sum or average)?\n")

    if choice == "sum":
        print(f"The sum of weights is {sum_weights(person, inventory):g}.")
    elif choice == "average":
        print(f"The average weight is {calc_avg_weight(person, inventory):g}.")



run()