from datetime import datetime, timedelta

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')

    def __repr__(self):
        return f"FoodItem(name={self.name}, category={self.category}, quantity={self.quantity}, barcode={self.barcode}, expiry_date={self.expiry_date.strftime('%Y-%m-%d')})"

class Inventory:
    def __init__(self):
        self.items = []  # List to store inventory items

    def add_item(self, food_item):
        self.items.append(food_item)  # Add a new item to inventory
        print(f"Added {food_item.name} to inventory.")

    def edit_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.items:
            if item.barcode == barcode:
                # Update item details if provided
                if name: item.name = name
                if category: item.category = category
                if quantity: item.quantity = quantity
                if expiry_date: item.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
                print(f"Updated item with barcode {barcode}.")
                return
        print(f"Item with barcode {barcode} not found.")

    def delete_item(self, barcode): 
        # Check if any item with the given barcode exists
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                print(f"Deleted item with barcode {barcode}.")
                return
        print(f"No record found for this barcode.")

    def search_item(self, search_term):
        # Search for an item by barcode or name
        for item in self.items:
            if item.barcode == search_term or item.name == search_term:
                print(item)
                return item
        print(f"Item {search_term} not found.")
        return None

    def get_near_expiry_items(self, days=7):
        # Get items that will expire within a given number of days
        near_expiry = []
        for item in self.items:
            if item.expiry_date <= datetime.now() + timedelta(days=days):
                near_expiry.append(item)
        return near_expiry

    def display(self):
        # Display all items in inventory
        if self.items:
            for item in self.items:
                print(item)
        else:
            print("No items in inventory.")

    def __str__(self):
        # Return string representation of all items in inventory
        return "\n".join([str(item) for item in self.items])

def main():
    inventory = Inventory()

    # Sample data
    inventory.add_item(FoodItem('Apple', 'Fruit', 10, '123', '2024-07-15'))


    while True:
        print("\nInventory Management System")
        print("1. Add Food Item")
        print("2. Edit Food Item")
        print("3. Delete Food Item")
        print("4. Search Food Item")
        print("5. Display Near Expiry Items")
        print("6. Display All Items")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter food item name: ")
            category = input("Enter food item category: ")
            quantity = int(input("Enter food item quantity: "))
            barcode = input("Enter food item barcode: ")
            expiry_date = input("Enter food item expiry date (YYYY-MM-DD): ")
            inventory.add_item(FoodItem(name, category, quantity, barcode, expiry_date))

        elif choice == '2':
            barcode = input("Enter the barcode of the food item to edit: ")
            print("Leave fields blank if you do not wish to change them.")
            name = input("Enter new name (or press Enter to skip): ")
            category = input("Enter new category (or press Enter to skip): ")
            quantity = input("Enter new quantity (or press Enter to skip): ")
            expiry_date = input("Enter new expiry date (YYYY-MM-DD) (or press Enter to skip): ")
            inventory.edit_item(barcode, name if name else None, category if category else None, int(quantity) if quantity else None, expiry_date if expiry_date else None)

        elif choice == '3':
            barcode = input("Enter the barcode of the food item to delete: ")
            inventory.delete_item(barcode)

        elif choice == '4':
            search_term = input("Enter barcode or name to search: ")
            inventory.search_item(search_term)

        elif choice == '5':
            days = int(input("Enter the number of days for near expiry threshold: "))
            near_expiry_items = inventory.get_near_expiry_items(days)
            if near_expiry_items:
                for item in near_expiry_items:
                    print(item)
            else:
                print("No near expiry items found.")

        elif choice == '6':
            inventory.display()

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
