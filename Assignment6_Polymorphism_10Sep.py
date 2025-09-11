#Assignment: 1
#Scenario:
#You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
#Q1. Product Search System (Static Polymorphism)
#Problem Statement:
#Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
 
#Requirements:
#Use default arguments and/or *args, **kwargs to simulate method overloading.
 
#Allow the following types of searches:
 
#Only by name
 
#Name and category
 
#Name, category, and price range




class ProductSearch:
    def search_product(self, name = None, category = None, priceRange = None):
        if name and category and priceRange:
            print(f"Searching product by name = {name}, category = {category} and price range = {priceRange}")
        elif name and category:
            print(f"Searching product by name = {name}, category = {category}")
        elif name:
            print(f"Searching product by name = {name}")
        else:
            print("Showing all available products")


product = ProductSearch()
product.search_product('Smart Phone', 'Smart Gadegts', 20000)
product.search_product('Tablet', 'Smart Gadegts')
product.search_product('TV')

print('*************First Assignment Completed******************')

#Assignment: 2
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
cart.add_products(('mobile', 2), ('tablet', 3), ('mobile', 5))
cart.show_cart()

print('*************Second Assignment Completed******************')




# Q3. Discount Application (Static Polymorphism)
 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts:
 
# Flat discount
# Percentage discount
# Buy One Get One
 
# Use static polymorphism to overload the method using default parameters or *args

class Discount:
    def apply_discount(self, flat = None, percentage = None, BuyOneGetOne = None):
        if (flat is not None and percentage is None and BuyOneGetOne is None):
            print("Apply flat discout")
        elif (percentage is not None and BuyOneGetOne is None):
            print("Apply percentahe discount")
        elif (BuyOneGetOne is not None):
            print("Apply Buy One Get One dicount")
        else:
            print("No discount is applied")


discount = Discount()
discount.apply_discount("flat")
discount.apply_discount(None, "percentage")
discount.apply_discount(None, None, "BuyOneGetOne")
print("************************Third assignment completed*****************************")


# Q4. Payment System (Dynamic Polymorphism)
 
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
 
# Requirements:
# Override pay() method in each class to simulate different payment methods

class Payment:
    def pay(self):
        print("Pay payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Make a credit card payment")

class UPIPayment(Payment):
    def pay(self):
        print("Make a UPI payment")

class CODPayment(Payment):
    def pay(self):
        print("Make a COD payment")


payment_mothods = [CreditCardPayment(), UPIPayment(), CODPayment()]
for item in payment_mothods:
    item.pay()

print("************************Fourth assignment completed*****************************")
