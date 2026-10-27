business_name = "Quick Online Shop"
customer_name = "Su Su"
order_total = 75000
is_paid = True

orders = ["phone case", "charger", "earphones", "power bank"]
new_orders = ["USB cable", "phone stand"]

# Print all variables and data types
print(business_name, type(business_name))
print(customer_name, type(customer_name))
print(order_total, type(order_total))
print(is_paid, type(is_paid))
print(orders, type(orders))
print(new_orders, type(new_orders))

# if else checking order
if order_total >= 50000:
    print("Large Order")
else:
    print("Small order")

# Print first, second and last orders
print(orders[0])
print(orders[1])
print(orders[-1])

# Change charger to fast charger
orders[1] = "fast charger"

# Add screen protector using append()
orders.append("screen protector")

# Add phone holder at index 1 using insert
orders.insert(1, "phone holder")

# Use extend() to add new orders in orders
orders.extend(new_orders)

# Remove earphone use remove()
orders.remove("earphones")

# Use pop() to remove the last item
orders.pop()

# Delete the item at index 0 using del
del orders[0]

# final order
print(orders)