import pandas as pd
from docx import Document

class Menu:
    def __init__(self, menu_filepath='menu.xlsx', instructions_filepath='how to make drinks.docx'):
        self.menu_items = self.read_from_excel(menu_filepath)
        self.instructions = self.read_instructions(instructions_filepath)

    def __str__(self):
        return f"{self.drink}: Small (${self.small_price}), Medium (${self.medium_price}), Large (${self.large_price})"

    @classmethod
    def from_row(cls, drink, small_price, medium_price, large_price):
        instance = cls.__new__(cls)  # Create a new instance without calling __init__
        instance.drink = drink
        instance.small_price = small_price
        instance.medium_price = medium_price
        instance.large_price = large_price
        return instance

    @staticmethod
    def read_from_excel(filepath):
        df = pd.read_excel(filepath)
        menu_items = []
        for index, row in df.iterrows():
            menu_item = Menu.from_row(row['Drink'], row['Price Small'], row['Price Medium'], row['Price Large'])
            menu_items.append(menu_item)
        return menu_items

    @staticmethod
    def read_instructions(filepath):
        document = Document(filepath)
        instructions = {}
        current_drink = None
        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            if text and text.endswith(":"):
                current_drink = text[:-1].strip()  # Remove the colon and any trailing whitespace
            elif current_drink and text:
                if current_drink not in instructions:
                    instructions[current_drink] = []
                instructions[current_drink].append(text)
        return instructions

    def display_menu(self):
        for item in self.menu_items:
            print(item)

    def display_drinks_with_numbers(self):
        print("Available Drinks:")
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item.drink}")

    def find_drink_by_number(self, number):
        if 1 <= number <= len(self.menu_items):
            return self.menu_items[number - 1]
        return None

    def display_instructions(self, drink_name):
        if drink_name in self.instructions:
            print(f"Instructions for making {drink_name}:")
            for step in self.instructions[drink_name]:
                print(f"- {step}")
        else:
            print("Instructions not found for this drink.")

def main():
    menu = Menu()
    while True:
        print("\n1. Print All Menu Items")
        print("2. Print Specific Drink Prices")
        print("3. Show How to Make a Specific Drink")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            menu.display_menu()

        elif choice == '2':
            menu.display_drinks_with_numbers()
            try:
                drink_number = int(input("Enter the drink number from the list above: "))
                drink = menu.find_drink_by_number(drink_number)
                if drink:
                    print(drink)
                else:
                    print("Invalid drink number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            menu.display_drinks_with_numbers()
            try:
                drink_number = int(input("Enter the drink number from the list above: "))
                drink = menu.find_drink_by_number(drink_number)
                if drink:
                    menu.display_instructions(drink.drink)
                else:
                    print("Invalid drink number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
