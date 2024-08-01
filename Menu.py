import pandas as pd

class Menu:
    def __init__(self, drink, small_price, medium_price, large_price):
        self.drink = drink
        self.small_price = small_price
        self.medium_price = medium_price
        self.large_price = large_price

    def __str__(self):
        return f"{self.drink}: Small (${self.small_price}), Medium (${self.medium_price}), Large (${self.large_price})"

    @classmethod
    def read_from_excel(cls, filepath):
        df = pd.read_excel(filepath)
        menu_items = []
        for index, row in df.iterrows():
            menu_item = cls(row['Drink'], row['Price Small'], row['Price Medium'], row['Price Large'])
            menu_items.append(menu_item)
        return menu_items

    @staticmethod
    def display_menu(menu_items):
        for item in menu_items:
            print(item)

# Example usage
menu_items = Menu.read_from_excel('path_to_your_excel_file.xlsx')
Menu.display_menu(menu_items)
