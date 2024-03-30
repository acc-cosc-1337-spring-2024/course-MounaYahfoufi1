class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"Added/Updated: {item} with quantity {quantity}.")

    def remove_inventory_widget(self, item):
        if item in self.inventory:
            del self.inventory[item]  # Remove item completely
            print(f"Removed: {item} from inventory.")
            return True
        else:
            print("Item not found or quantity insufficient")
            return False

