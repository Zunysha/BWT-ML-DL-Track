# Food Inventory Management System

- Complete project with all features is present in modules folder 

## Overview

This project is a Food Inventory Management System designed to help users manage their food inventory efficiently. It includes functionality to add, remove, and search for food items, as well as generate inventory reports and save/load data to/from a CSV file.

## Features

- **Add Food Items**: Add new food items to the inventory with details such as name, category, quantity, barcode, and expiry date.
- **Remove Food Items**: Remove items from the inventory using their barcode.
- **Search Food Items**: Search for items by barcode, name, or category.
- **Edit The food Items**: Edit the items which user wants to in inventory.
- **Near Expiry Items**: Retrieve items that are near their expiry date within a specified number of days.
- **Near Expiry Items using generators**: Retrieve items that are near their expiry date within a specified number of days using generators.
- **Generate Reports**: Generate reports summarizing the inventory, including total items, near-expiry items, low stock items, and a category summary.
- **Iterate**: Iterate through inventory items.
- **Save/Load Data**: Save the inventory data to a CSV file and load it back when needed.

## Project Structure

The project contains the following files:

- `file_manager.py`: Handles saving and loading inventory data to/from a CSV file.
- `food_item.py`: Defines the `FoodItem` class.
- `inventory.py`: Manages a collection of `FoodItem` objects and provides methods for inventory operations.
- `inventory.csv`: Sample CSV file containing inventory data.

