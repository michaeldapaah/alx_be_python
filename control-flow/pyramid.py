num = int(input("Enter the number of rows for the pyramid: "))

row = 0 

while row < num:
    spaces = num - row - 1
    while spaces > 0:
        print(end=" ")
        spaces -= 1

    star = row + 1
    while star > 0:
        print("*", end=" ")
        star -= 1
    row += 1
    print()  # Newline after each row