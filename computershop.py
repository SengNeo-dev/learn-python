shop_name = "Tech World"
staff_name = "Aye Aye"
monthly_sales = 120000
is_registered = True

products = ["laptop", "mouse", "keyboard", "monitor"]
new_products = ["webcam", "headphones"]

# Print all variables and data types
print(shop_name, type(shop_name))
print(staff_name, type(staff_name))
print(monthly_sales, type(monthly_sales))
print(is_registered, type(is_registered))
print(products, type(products))
print(new_products, type(new_products))

# if else checking
if monthly_sales >= 1000000:
    print("Monthly target achieved")
else:
    print("Monthly target not achieved")

# Print first, second and last products
print(products[0])
print(products[1])
print(products[-1])

# Change mouse to wireless mouse
products[1] = "wireless mouse"

#Add printer using append
products.append("printer")

# Add USB cable at index 1 using insert
products.insert(1, "USB cable")

# Use extend() to add new_products in products
products.extend(new_products)

# Use remove() to remove keyboard
products.remove("keyboard")

# Use pop() to remove the last item
products.pop()

# detete item at index 0 using del
del products[0]

# final products
print(products)