#Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
product = ("Laptop", 50000,"Black" ,"Samsung","Electronics")
print("product is: ", product)

#Access and print the second element of the tuple product.
print('second element of the product is: ', product[1])

#Slice and print the last two elements of the product tuple.
print('the last two elements of the product tuple is: ', product[3:5])

#Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in product:
    print("Yes, 'Electronics' is present in the product tuple.")
 
#Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
prices = (1000, 1500, 1200, 1100, 900)
count_1000 = prices.count(1000)
print("1000 appears", count_1000, "time(s) in the prices tuple.")

#Find and print the maximum and minimum price from the prices tuple.
print("Maximum price:", max(prices))
print("Minimum price:", min(prices))
 
#Use a loop to print each item from the product tuple on a new line.
for item in product:
    print(item)
 
#Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print("Updated product tuple:", product)

#Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
product = product + ("In Stock",)
print("Product with stock info:", product) 

#Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
product_list = list(product)
if "Electronics" in product_list:
    product_list.remove("Electronics")
product = tuple(product_list)
print("Product after removing 'Electronics':", product)
 
#Unpack the tuple product into three variables and print each variable.
name, price, color = product[0], product[1], product[2]
print("Name:", name)
print("Price:", price)
print("Color:", color)

#Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
product1 = ("Laptop", 55000, "Black")
product2 = ("Phone", 30000, "Silver")
product3 = ("Tablet", 20000, "White")

nested_products = (product1, product2, product3)
second_product_name = nested_products[1][0]
print("Name of the second product:", second_product_name)