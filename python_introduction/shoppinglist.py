shopping_list = ["milk", "eggs", "bread", "butter"]
item_found = False

while not item_found:
    item = input("Enter an item to search for int the shopping list or (type 'q' to quit): ")
    if item.lower() == 'q':
        print("Exiting the search.")
        break
    if item in shopping_list:
        item_found = True
        print(f"{item} is in the shopping list.")

    else:
        print(f"{item} is not in the shopping list. Try again.")