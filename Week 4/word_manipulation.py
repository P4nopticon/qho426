def display_box(word):
    middle = f"* {word} *"
    print("*" * len(middle))
    print(middle)
    print("*" * len(middle))
def display_lower(word):
    print(word.lower())
def display_upper(word):
    print(word.upper())
def display_mirrored(word):
    print(f"{word} | {word[::-1]}")
def repeat_word(word):
    count = int(input("How many times? "))
    for index in range(count):
        if index % 2 == 0:
            print(word.upper())
        else:
            print(word.lower())
def run():
    word = input("Enter a word: ")
    print("1 Box | 2 Lower | 3 Upper | 4 Mirror | 5 Repeat")
    choice = input("Choose 1–5: ")
    actions = {
        "1": display_box,
        "2": display_lower,
        "3": display_upper,
        "4": display_mirrored,
        "5": repeat_word,
    }
    if choice in actions:
        actions[choice](word)
    else:
        print("Invalid option")
run()