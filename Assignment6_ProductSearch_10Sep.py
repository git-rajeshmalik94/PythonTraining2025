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
