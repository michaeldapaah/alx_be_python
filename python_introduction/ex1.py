even_count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        even_count += 1

print(f'We have {even_count } even numbers')