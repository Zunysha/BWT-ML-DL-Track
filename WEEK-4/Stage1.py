from datetime import datetime
import csv

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
        self.food_items = []  # List to store food items

    def add_food_item(self, food_item):
        self.food_items.append(food_item)  # Add a new food item to the inventory

    def edit_food_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.food_items:
            if item.barcode == barcode:
                # Update food item details if provided
                if name is not None:
                    item.name = name
                if category is not None:
                    item.category = category
                if quantity is not None:
                    item.quantity = quantity
                if expiry_date is not None:
                    item.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
                return True
        return False

    def delete_food_item(self, barcode):
    # Delete food item from the inventory by barcode if it exists
        for item in self.food_items:
            if item.barcode == barcode:
                self.food_items.remove(item)
                return True  # Return True if item is found and deleted
        return False  # Return False if no item with the given barcode is found

    def search_food_item(self, barcode=None, name=None):
        # Search for a food item by barcode or name
        if barcode:
            return [item for item in self.food_items if item.barcode == barcode]
        if name:
            return [item for item in self.food_items if item.name == name]
        return []

    def get_near_expiry_items(self, days_threshold=7):
        # Get items that are near expiry within a given number of days
        today = datetime.now()
        near_expiry_items = [item for item in self.food_items if (item.expiry_date - today).days <= days_threshold]
        return near_expiry_items

    def save_to_csv(self, filename):
        # Save inventory to a CSV file
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry Date'])
                for item in self.food_items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date.strftime('%Y-%m-%d')])
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    def load_from_csv(self, filename):
        # Load inventory from a CSV file
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.food_items = []
                for row in reader:
                    self.food_items.append(FoodItem(
                        name=row['Name'],
                        category=row['Category'],
                        quantity=int(row['Quantity']),
                        barcode=row['Barcode'],
                        expiry_date=row['Expiry Date']
                    ))
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except Exception as e:
            print(f"An error occurred while loading from CSV: {e}")

def display_menu():
    # Display the main menu options
    print("\nInventory Management System")
    print("1. Add Food Item")
    print("2. Edit Food Item")
    print("3. Delete Food Item")
    print("4. Search Food Item")
    print("5. Display Near Expiry Items")
    print("6. Exit")

def get_food_item_details():
    # Get food item details from user input
    name = input("Enter food item name: ")
    category = input("Enter food item category: ")
    quantity = int(input("Enter food item quantity: "))
    barcode = input("Enter food item barcode: ")
    expiry_date = input("Enter food item expiry date (YYYY-MM-DD): ")
    return FoodItem(name, category, quantity, barcode, expiry_date)

def main():
    inventory = Inventory()
    filename = 'inventory.csv'
    
    # Load inventory from CSV
    inventory.load_from_csv(filename)
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Add a new food item
            food_item = get_food_item_details()
            inventory.add_food_item(food_item)
            inventory.save_to_csv(filename)
            print("Food item added successfully.")
        
        elif choice == '2':
            # Edit an existing food item
            barcode = input("Enter the barcode of the food item to edit: ")
            print("Leave fields blank if you do not wish to change them.")
            name = input("Enter new name (or press Enter to skip): ")
            category = input("Enter new category (or press Enter to skip): ")
            quantity = input("Enter new quantity (or press Enter to skip): ")
            expiry_date = input("Enter new expiry date (YYYY-MM-DD) (or press Enter to skip): ")
            
            if inventory.edit_food_item(
                barcode,
                name=name if name else None,
                category=category if category else None,
                quantity=int(quantity) if quantity else None,
                expiry_date=expiry_date if expiry_date else None
            ):
                inventory.save_to_csv(filename)
                print("Food item edited successfully.")
            else:
                print("Food item not found.")
        
        elif choice == '3':
    # Delete a food item
            barcode = input("Enter the barcode of the food item to delete: ")
            if inventory.delete_food_item(barcode):
                inventory.save_to_csv(filename)
                print("Food item deleted successfully.")
            else:
                print("No record found for this barcode.")

        
        elif choice == '4':
            # Search for a food item
            search_type = input("Search by barcode (b) or name (n)? ")
            if search_type == 'b':
                barcode = input("Enter barcode: ")
                results = inventory.search_food_item(barcode=barcode)
            elif search_type == 'n':
                name = input("Enter name: ")
                results = inventory.search_food_item(name=name)
            else:
                print("Invalid choice.")
                continue

            if results:
                for item in results:
                    print(item)
            else:
                print("No food items found.")
        
        elif choice == '5':
            # Display near expiry items
            days_threshold = int(input("Enter the number of days for near expiry threshold: "))
            near_expiry_items = inventory.get_near_expiry_items(days_threshold)
            if near_expiry_items:
                for item in near_expiry_items:
                    print(item)
            else:
                print("No near expiry items found.")
        
        elif choice == '6':
            # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
