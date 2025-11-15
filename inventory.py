item_list = []
item_prices = {}
def price_check(prompt):
    while True:
        price = input(prompt)
        if price.isdigit():
            return price
        else:
            print("Invalid input! Price must be an integer.")


while True:
    print("\n===== INVENTORY MENU ====="
          "\n [1] Add Item"
          "\n [2] Update Price"
          "\n [3] Exit")

    choice = input("Choice: ")

    match choice:
        case "1":
            item_name = input("\nEnter item name: ")

            if item_name in item_list:
                print("Item already exists in the inventory!")
            else:
                price = price_check("Enter price: ")
                item_list.append(item_name)
                item_prices[item_name] = price
                print("Item added successfully!")

        case "2":
            item_name = input("\nEnter item name to update: ")

            if item_name in item_list:
                new_price = price_check("Enter new price: ")
                item_prices[item_name] = new_price
                print("Price updated successfully!")
            else:
                print("Item not found in the inventory.")

        case "3":
            print("Exiting system...")
            break

        case _:
            print("Invalid choice! Please enter 1-3 choices only.")
