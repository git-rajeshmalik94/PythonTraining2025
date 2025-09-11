#Cart System with Quantity Variations (Static Polymorphism)
 
#Problem Statement:
#Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
#Requirements:
 
#Add multiple products at once with name and quantity
 
#Simulate static polymorphism using variable arguments

class Cart:
    def __init__(self):
        self.items = {}  # Dictionary to store items: {product_name: quantity}

    def add_products(self, *args):
        # Handle *args: expecting tuples of (product, quantity)
        for item in args:
            if isinstance(item, tuple) and len(item) == 2:
                product, quantity = item
                self._add_product(product, quantity)
            else:
                print(f"Ignoring invalid item: {item}")

    

    def _add_product(self, product, quantity):
        # Add or update product quantity
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Current cart contents:")
            for product, quantity in self.items.items():
                print(f" - {product}: {quantity}")


cart = Cart()
cart.add_products(('mobile', 2), ('tablet', 3))
cart.show_cart()
