from products import Product, NonStockProduct, LimitedProduct
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = Store(product_list)


def start(store):
    while True:
        print("     Menu     ")
        print(10 * " - ")
        print('''
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
        ''')
        print(10 * " - ")
        user_input = input("Please choose a number: ").strip()
        print()

        if user_input == "1":
            for index, product in enumerate(store.products):
                print(f"{index + 1}: {product.show()}")
            print()

        elif user_input == "2":
            quantity = sum(product.quantity for product in store.products if not product.is_unlimited())
            print(f"Total amount of {quantity} items in store\n")

        elif user_input == "3":
            shopping_list = []

            for index, product in enumerate(store.products):
                print(f"{index + 1}: {product.show()}")
            print()

            while True:
                print("\nPress enter to quit order process ...\n")
                product_number = input("Which product # do you want?: ").strip()

                if product_number == "":
                    break

                try:
                    product_number = int(product_number)

                    if not (1 <= product_number <= len(store.products)):
                        print("\nInvalid product number!\n")
                        continue

                    order_quantity = int(input("\nWhat amount do you want?: ").strip())

                    if order_quantity <= 0:
                        print("\nQuantity must be positive!\n")
                        continue

                    selected_product = store.products[product_number - 1]

                    if not selected_product.is_unlimited and order_quantity > selected_product.quantity:
                        print(f"\nYou can only buy {selected_product.maximum} of '{selected_product.name}' per order.\n")
                        continue

                    shopping_list.append((selected_product, order_quantity))

                    print(f"\n{selected_product.name} (qty: {order_quantity}) added to your basket!\n")

                except ValueError as e:
                    print(f"\nError: {e}\n")

            if shopping_list:
                total_price = sum(selected_product.price * quantity for selected_product, quantity in shopping_list)
                print(f"\nOrder complete! Total price: {total_price} €\n")
            else:
                print("Your shopping basket is empty. Shopping process stopped.")

        elif user_input == "4":
            break


start(best_buy)
