n = int(input("Enter the number of rows for the triangle: "))

for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")
    print()  # Newline after each row