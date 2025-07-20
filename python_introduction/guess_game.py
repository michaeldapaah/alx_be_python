
import random

secret_number = random.randint(1,10)

while True:
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print("Try to guess it!")
    guess = int(input("Guess a number between 1 to 10: "))

    match guess:
        case 1 if guess == secret_number:
                print("Congratulations, you guessed it right!")
        case 2 if guess > secret_number:
                print("Your guess is too high.")
        case _ if guess < secret_number:
                print("Your guess is too low.")

    print(f"The secret number was {secret_number}.")
    play_again = input("Do you want to play again? (yes/no)")

    if play_again != "Yes".lower():
        print("Thanks for playing!")
        break

