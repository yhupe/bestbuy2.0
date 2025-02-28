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

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return (f"{self.name}, Price: {self.price} €, "
                f"Quantity: {self.quantity} pcs")

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.set_quantity(quantity)
        return total_price
