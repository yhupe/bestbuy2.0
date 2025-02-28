from products import Product
from store import Store

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

iphone = Product("Iphone 15 Pro 256 GB", price=1099, quantity=1000)
cannabis = Product("1st grade PREMIUM Cannabis", price=20, quantity=50)

best_buy.add_product(iphone)
best_buy.add_product(cannabis)
best_buy.remove_product(cannabis)


def start(store):
    """ Within a while loop, interface to present Menu 1-4 and available
    products to the user. Some error handling which is not being
    handled inside the two classes is handled in the start function"""

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
        user_input = input("Please choose a number: ")
        print()

        if user_input == "1":
            for index, product in enumerate(best_buy.products):
                print(f"{index + 1}: {product.show()}")
            print()

        if user_input == "2":
            quantity = 0

            for product in best_buy.products:
                quantity += product.quantity

            print(f"Total amount of {quantity} items in store\n")

        if user_input == "3":
            shopping_list = []
            temporary_stock = {product: product.get_quantity() for product
                               in best_buy.products}

            while True:

                for index, product in enumerate(best_buy.products):
                    print(f"{index + 1}: {product.name}, "
                          f"Price: {product.price} €, "
                          f"Quantity: {temporary_stock[product]} pcs")

                print("\nPress enter to quit order process ...\n")
                product_number = (input("Which product # do you want?: ")
                                  .strip())

                if product_number == "":
                    break

                try:
                    product_number = int(product_number)

                    if (product_number <= 0 or product_number >
                            len(best_buy.products)):
                        print("\nInvalid product number!\n")
                        continue

                    order_quantity = (
                        int(input("\nWhat amount do you want?: ").strip()))

                    if order_quantity <= 0:
                        print("\nQuantity must be positive!\n")
                        continue

                    selected_product = best_buy.products[product_number - 1]

                    if order_quantity > temporary_stock[selected_product]:
                        print(f"\nNot enough items in stock - only "
                              f"{temporary_stock[selected_product]} left!\n")
                        continue

                    temporary_stock[selected_product] -= order_quantity
                    shopping_list.append((selected_product, order_quantity))
                    print(f"\n{selected_product.name} (qty: {order_quantity})"
                          f" added to your basket!\n")

                except ValueError:
                    print("\nYou must enter valid numbers!\n")

            if shopping_list:
                total_price = best_buy.order(shopping_list)
                print(f"\nOrder complete! Total price: {total_price} €\n")
            else:
                print("Your shopping basket is empty. Shopping process stopped")

        if user_input =="4":
            break


start(best_buy)

