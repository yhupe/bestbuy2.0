class Product:
    """Initialization of instance variables is allowed
    only after meeting criteria, otherwise an error is raised"""

    def __init__(self, name, price, quantity):

        if not isinstance(name, str):
            raise TypeError(f"Product name must be a string ('blabla'), got {type(name)} instead.")

        if not name:
            raise ValueError("Name cannot be empty")

        if not isinstance(price, (int, float)):
            raise TypeError(f"Price must be a number (int or float), got {type(price)} instead.")

        if price <= 0:
            raise ValueError("Price cannot be negative or 0")

        if not isinstance(quantity, int):
            raise TypeError(f"Quantity must be a whole number (int), got {type(quantity)} instead.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def is_unlimited(self):
        return False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        promotion_info = f"🎁🎁🎁 PROMOTION: {self.promotion.name}" if self.promotion else ""
        return (f"{self.name}, Price: {self.price} €, "
                f"Quantity: {self.quantity} pcs, {promotion_info}")

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.set_quantity(quantity)
        return total_price

class LimitedProduct(Product):
    """ Sub-class inheriting (from class Product) modified to handle
    products with a maximum order volume such as a shipping fee"""

    def __init__(self, name, price, quantity, maximum = 1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return super().show() + f", (maximum: {self.maximum})"

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise ValueError(f"You can only buy up to {self.maximum} of '{self.name}' per order.")

        return super().buy(quantity)


class NonStockProduct(Product):
    """ Sub-class inheriting (from class Product) modified to handle
    products without the need of stock such as a windows license or e-books etc... """
    def __init__(self, name, price):
        super().__init__(name, price, quantity = 0)

    def show(self):
        return super().show().replace(f"Quantity: {self.quantity} pcs", "(unlimited quantity)")

    def set_quantity(self, quantity):
        raise NotImplementedError("NonStockProduct has unlimited stock and quantity cannot be set")

    def is_unlimited(self):
        return True

    def buy(self, quantity) -> float:
        total_price = quantity * self.price
        return total_price
