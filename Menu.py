import pandas as pd

class Menu:
    def __init__(self, filepath='menu.xlsx'):
        self.menu_items = self.read_from_excel(filepath)

    def __str__(self):
        return f"{self.drink}: Small (${self.small_price}), Medium (${self.medium_price}), Large (${self.large_price})"

    @staticmethod
    def read_from_excel(filepath):
        df = pd.read_excel(filepath)
        menu_items = []
        for _, row in df.iterrows():
            steps = [row[f'step_{i}'] for i in range(1, 6) if pd.notna(row[f'step_{i}'])]  # Collect non-NaN steps
            menu_item = {
                'drink': row['drink'],
                'prices': (row['price_small'], row['price_medium'], row['price_large']),
                'instructions': steps
            }
            menu_items.append(menu_item)
        return menu_items

    def display_menu(self):
        for item in self.menu_items:
            print(item['drink'], f"Small: ${item['prices'][0]}, Medium: ${item['prices'][1]}, Large: ${item['prices'][2]}")

    def display_drinks_with_numbers(self):
        print("Available Drinks:")
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item['drink']}")

    def find_drink_by_number(self, number):
        if 1 <= number <= len(self.menu_items):
            return self.menu_items[number - 1]
        return None

    def display_instructions(self, drink_item):
        if drink_item:
            print(f"Instructions for making {drink_item['drink']}:")
            for step in drink_item['instructions']:
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
                    print(f"{drink['drink']}: Prices - Small: ${drink['prices'][0]}, Medium: ${drink['prices'][1]}, Large: ${drink['prices'][2]}")
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
                    menu.display_instructions(drink)
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
