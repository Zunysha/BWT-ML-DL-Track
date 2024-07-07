from datetime import datetime
from food_item import FoodItem

# Class representing the inventory of food items
class Inventory:
    def __init__(self):
        self.food_items = []  # List to store food items

    # Add a food item to the inventory
    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    # Edit an existing food item in the inventory
    def edit_food_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.food_items:
            if item.barcode == barcode:
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

    # Delete a food item from the inventory by barcode
    def delete_food_item(self, barcode):
        for item in self.food_items:
            if item.barcode == barcode:
                self.food_items.remove(item)
                return True  # Return True if item is found and deleted
        return False  # Return False if no item with the given barcode is found

    # Search for food items by barcode or name
    def search_food_item(self, barcode=None, name=None):
        if barcode:
            return [item for item in self.food_items if item.barcode == barcode]
        if name:
            return [item for item in self.food_items if item.name == name]
        return []

    # Get food items that are near their expiry date
    def get_near_expiry_items(self, days_threshold=7):
        today = datetime.now()
        near_expiry_items = [item for item in self.food_items if (item.expiry_date - today).days <= days_threshold]
        return near_expiry_items
