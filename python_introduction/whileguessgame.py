import random
secret_code = random.randint(1, 10)

guess = 0
count_guess = 0

while guess != secret_code:
    count_guess = count_guess + 1
    guess = int(input("please enter you guess number: "))

print(f"you guessed the secret code in {count_guess} tries")