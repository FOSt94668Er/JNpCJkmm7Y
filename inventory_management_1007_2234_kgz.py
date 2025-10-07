# 代码生成时间: 2025-10-07 22:34:45
import pandas as pd

"""
Inventory Management System using Python and Pandas

This script provides functionality for managing an inventory system.
It allows adding, removing, and updating inventory items, as well as
displaying the current inventory.

Attributes:
    None

Methods:
    load_inventory: Loads the inventory from a CSV file.
    add_item: Adds a new item to the inventory.
    remove_item: Removes an item from the inventory.
    update_item: Updates the quantity of an item in the inventory.
    display_inventory: Displays the current inventory.
"""


class InventoryManagement:
    def __init__(self, file_path):
        """Initialize the InventoryManagement class with a file path."""
        self.file_path = file_path
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load the inventory from a CSV file."""
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            return pd.DataFrame(columns=['Item', 'Quantity'])
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{self.file_path}' is empty.")
            return pd.DataFrame(columns=['Item', 'Quantity'])
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame(columns=['Item', 'Quantity'])

    def add_item(self, item, quantity):
        """Add a new item to the inventory."""
        if item in self.inventory['Item'].values:
            print(f"Error: Item '{item}' already exists in the inventory.")
        else:
            self.inventory = self.inventory.append({'Item': item, 'Quantity': quantity}, ignore_index=True)
            self.save_inventory()

    def remove_item(self, item):
        """Remove an item from the inventory."""
        try:
            self.inventory = self.inventory[self.inventory['Item'] != item]
            self.save_inventory()
        except KeyError:
            print(f"Error: Item '{item}' not found in the inventory.")

    def update_item(self, item, quantity):
        """Update the quantity of an item in the inventory."""
        try:
            self.inventory.loc[self.inventory['Item'] == item, 'Quantity'] = quantity
            self.save_inventory()
        except KeyError:
            print(f"Error: Item '{item}' not found in the inventory.")

    def display_inventory(self):
        """Display the current inventory."""
        print(self.inventory)

    def save_inventory(self):
        """Save the inventory to a CSV file."""
        try:
            self.inventory.to_csv(self.file_path, index=False)
        except Exception as e:
            print(f"An unexpected error occurred while saving the inventory: {e}")

# Example usage
if __name__ == '__main__':
    inventory_file_path = 'inventory.csv'
    inventory_manager = InventoryManagement(inventory_file_path)
    inventory_manager.add_item('Widget', 100)
    inventory_manager.add_item('Gadget', 50)
    inventory_manager.update_item('Widget', 150)
    inventory_manager.remove_item('Gadget')
    inventory_manager.display_inventory()