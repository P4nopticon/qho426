import random as rnd


def play_guess_the_number():
    minimum = int(input("Please enter the minimum value:\n"))
    maximum = int(input("Please enter the maximum value:\n"))
    secret = rnd.randint(minimum, maximum)
    print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")

    while True:
        guess = int(input())
        if guess == secret:
            break
        if guess < secret:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print("Try again:")
    print("Congratulations! You guessed my number!")


play_guess_the_number()