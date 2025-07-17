from sweet_shop import SweetShop

def menu():
    shop = SweetShop()
    
    while True:
        print("\n==== Sweet Shop Menu ====")
        print("1. Add Sweet")
        print("2. Remove Sweet")
        print("3. Restock Sweet")
        print("4. Sell Sweet")
        print("5. Check Inventory")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter sweet name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            shop.add_sweet(name, qty, price)

        elif choice == '2':
            name = input("Enter sweet name to remove: ")
            shop.remove_sweet(name)

        elif choice == '3':
            name = input("Enter sweet name to restock: ")
            qty = int(input("Enter quantity to add: "))
            shop.restock_sweet(name, qty)

        elif choice == '4':
            name = input("Enter sweet name to sell: ")
            qty = int(input("Enter quantity to sell: "))
            shop.sell_sweet(name, qty)

        elif choice == '5':
            inventory = shop.get_inventory()
            print("Current Inventory:")
            for sweet, info in inventory.items():
                print(f"{sweet} - Quantity: {info['quantity']}, Price: {info['price']}")

        elif choice == '6':
            print("Exiting Sweet Shop. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
