#
from dictionary import Inventory

def main():
    inventory = Inventory()

    while True:
        # Print the menu
        print("\nInventory Menu\n")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        
        # Get user's choice
        choice = input("Enter your choice: ").strip()
        
        # Handle the user's choice
        if choice == '1':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_inventory(item, quantity)
        elif choice == '2':
            item = input("Enter the item name to delete: ")
            inventory.remove_inventory_widget(item)
        elif choice == '3':
            print("Exiting the inventory system.")
            break  # Exit the loop, thus ending the program
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == '__main__':
    main()
