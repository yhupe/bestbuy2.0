import products

class Store:
    """ It seems to be best practice to set iterable objects to none by default
     because otherwise it's likely that instances share the same list.
     If no product is provided, an empty list is assigned"""

    def __init__(self, products= None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):

        counter = 0

        for product in self.products:
            counter += products.Product.get_quantity(product)

        return counter

    def get_all_products(self):
        return self.products

    def order(self, shopping_list):

        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
