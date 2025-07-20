pattern = int(input("Enter the size of the pattern: "))

i = 1
while i <= pattern:
    for j in range(pattern):
        print("*", end="")
    print()  # Newline after each row
    i += 1