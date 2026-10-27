# Small Shop Inventory
shop_name = "Smart Shop"
owner = "Mg Mg"
total_sales = 250000
is_open = True

products = ["rice", "oil", "sugar", "milk"]
new_products = ["coffee", "tea"]

# Print all variables with data types
print(shop_name, type(shop_name))
print(owner, type(owner))
print(total_sales, type(total_sales))
print(is_open, type(is_open))
print(products, type(products))
print(new_products, type(new_products))

# if else checking
if total_sales >= 20000:
    print("Sales target achieved")
else:
    print("Sales target not achieved")


# Print first, sencond and last products
print(products[0])
print(products[1])
print(products[-1])

# Change sugar to salt
products[2] = "salt"
print(products)

# Add eggs use append()
products.append("eggs")
print(products)

# Add bread in index using insert
products.insert(1, "bread")
print(products)

# Add all item from new_products using extend()
products.extend(new_products)
print(products)

# Remove oil using remove()
products.remove("oil")
print(products)

# Remove last products using pop()
products.pop()
print(products)

# Delete item at index 0 using del
del products[0]
print(products)

#final products 
print(products)