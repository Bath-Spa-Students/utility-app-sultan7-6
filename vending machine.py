print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

print()
class VendingMachine:
    def __init__(self):
        self.items = {'D3': {'name': 'Dew', 'price': 3.50, 'quantity': 10},
                      'L6': {'name': 'Lays', 'price': 1.00, 'quantity': 8},
                      'G2': {'name': 'Galaxy', 'price': 2.50, 'quantity': 15},
                      'C1': {'name': 'Chicken Sandwich', 'price': 5.50, 'quantity': 5},
                      'M9': {'name': 'Mai Dubai', 'price': 1.00, 'quantity': 40},
                      'K6': {'name': 'Kit Kat', 'price': 1.50, 'quantity': 20},
                      'B8': {'name': 'Biscuit', 'price': 1.75, 'quantity': 10},
                      'B0': {'name': 'Break', 'price': 2.50, 'quantity': 8},
                      'P7': {'name': 'Protein Bar', 'price': 6.00, 'quantity': 25},
                      'Y4': {'name':'Yippie', 'price': 2.75, 'quantity': 20}}
        self.balance = 0

    def display_items(self):
        print("Available items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    def purchase_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0


def main():
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Items")
        print("2. Insert cash")
        print("3. buy Item")
        print("4. balance")
        print("5. Exit")
        print("____________________________________________________________")

        choice = input("Enter your choice: ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input("Insert money: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            print("Thank you for using the vending machine. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
