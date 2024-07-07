from datetime import datetime

# Class representing a single food item
class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name  # Name of the food item
        self.category = category  # Category of the food item
        self.quantity = quantity  # Quantity of the food item
        self.barcode = barcode  # Barcode of the food item
        self.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')  # Expiry date of the food item

    def __repr__(self):
        return f"FoodItem(name={self.name}, category={self.category}, quantity={self.quantity}, barcode={self.barcode}, expiry_date={self.expiry_date.strftime('%Y-%m-%d')})"
