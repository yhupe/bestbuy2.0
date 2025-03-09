from products import Product, NonStockProduct, LimitedProduct
from store import Store
from promotions import PercentageDiscount, Buy1Get1Free, SecondItemHalfPrice


def main():
    """ Main function that runs the store application. """

    # defining available products
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    bose_earbuds = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel = Product("Google Pixel 7", price=500, quantity=250)
    windows_license = NonStockProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # instantiating of the three discount types
    promo_percentage = PercentageDiscount("Today 30% off!!", 30)
    promo_buy1get1 = Buy1Get1Free("Buy 1 and get the 2nd item for FREE!!")
    promo_second_half_off = SecondItemHalfPrice("50% off the 2nd item!!")

    # applying discounts to available products
    macbook.set_promotion(promo_percentage)
    bose_earbuds.set_promotion(promo_second_half_off)
    google_pixel.set_promotion(promo_buy1get1)

    # adding all products to product list needed to instantiate the store
    product_list = [macbook, bose_earbuds, google_pixel, windows_license, shipping]

    # instantiating the store
    best_buy = Store(product_list)

    while True:
        print("\n     Menu     ")
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
            for index, product in enumerate(best_buy.get_all_products()):
                print(f"{index + 1}: {product.show()}")
            print()

        elif user_input == "2":
            print(f"Total amount of {best_buy.get_total_quantity()} items in store\n")

        elif user_input == "3":
            best_buy.process_order()

        elif user_input == "4":
            break


if __name__ == "__main__":
    main()
