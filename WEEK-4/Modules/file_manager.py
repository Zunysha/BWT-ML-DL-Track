import csv
from food_item import FoodItem
from inventory import Inventory

# Function to save inventory to a CSV file
def save_to_csv(inventory):
    filename = 'inventory.csv'
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry Date'])
            for item in inventory.food_items:
                writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date.strftime('%Y-%m-%d')])
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

# Function to load inventory from a CSV file
def load_from_csv():
    inventory = Inventory()
    filename = 'inventory.csv'
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.add_food_item(FoodItem(
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
    return inventory
