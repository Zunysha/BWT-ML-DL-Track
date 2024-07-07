from inventory import Inventory
from food_item import FoodItem
from file_manager import save_to_csv, load_from_csv

# Display the menu options
def display_menu():
    print("\nInventory Management System")
    print("1. Add Food Item")
    print("2. Edit Food Item")
    print("3. Delete Food Item")
    print("4. Search Food Item")
    print("5. Display Near Expiry Items")
    print("6. Display Near Expiry Items Using Generator")
    print("7. Exit")

# Get food item details from the user
def get_food_item_details():
    name = input("Enter food item name: ")
    category = input("Enter food item category: ")
    quantity = int(input("Enter food item quantity: "))
    barcode = input("Enter food item barcode: ")
    expiry_date = input("Enter food item expiry date (YYYY-MM-DD): ")
    return FoodItem(name, category, quantity, barcode, expiry_date)

# Main function to run the inventory management system
def main():
    inventory = load_from_csv()  # Load inventory from CSV file
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            food_item = get_food_item_details()
            inventory.add_food_item(food_item)
            save_to_csv(inventory)
            print("Food item added successfully.")
        
        elif choice == '2':
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
                save_to_csv(inventory)
                print("Food item edited successfully.")
            else:
                print("Food item not found.")
        
        elif choice == '3':
            barcode = input("Enter the barcode of the food item to delete: ")
            if inventory.delete_food_item(barcode):
                save_to_csv(inventory)
                print("Food item deleted successfully.")
            else:
                print("Food item not found.") 
        
        elif choice == '4':
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
            days_threshold = int(input("Enter the number of days for near expiry threshold: "))
            near_expiry_items = inventory.get_near_expiry_items(days_threshold)
            if near_expiry_items:
                for item in near_expiry_items:
                    print(item)
            else:
                print("No near expiry items found.")
        
        elif choice == '6':
            days_threshold = int(input("Enter the number of days for near expiry threshold: "))
            near_expiry_items = list(inventory.near_expiry_generator(days_threshold))
            if near_expiry_items:
                for item in near_expiry_items:
                    print(item)
            else:
                print("No near expiry items found using generator.")


        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
