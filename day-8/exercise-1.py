import random

number = random.randint(1, 100)

while True:

    user_number = int(input("Type your guess: ").strip())

    if user_number > number:
        print("Your guess was too high.")
    elif user_number < number:
        print("Your guess was too low.")
    elif user_number == number:
        print("You guessed right.")
        break