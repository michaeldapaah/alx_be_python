import random

random_numbers = [random.randint(1, 10) for i in range(20)]

print(random_numbers)

unique_numbers = set(random_numbers)
print(unique_numbers)

