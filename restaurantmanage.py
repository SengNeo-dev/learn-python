restaurant_name = "Golden Restaurant"
daily_customers = 45
daily_income = 35000.0
is_open = True

menu = ["fried rice", "noodles", "soup", "salad"]
new_menu = ["coffee", "juice"]

# Print all variables and data types
print(restaurant_name, type(restaurant_name))
print(daily_customers, type(daily_customers))
print(daily_income, type(daily_income))
print(is_open, type(is_open))
print(menu, type(menu))
print(new_menu, type(new_menu))

# if else checking
if daily_customers >= 40:
    print("Good customer traffic")
else:
    print("Need more customers")

# Print first, third, and last menu
print(menu[0])
print(menu[2])
print(menu[-1])

# Change soup to chicken soup
menu[2] = "chicken soup"
print(menu)

# Add burger using append()
menu.append("burger")
print(menu)

# Add pizza at index using insert
menu.insert(1, "pizza")
print(menu)

# Add new_menu in menu using extend()
menu.extend(new_menu)
print(menu)

# Remove salad using remove()
menu.remove("salad")
print(menu)

# remove last item using pop()
menu.pop()
print(menu)

# Delete item at index using del
del menu[0]
print(menu)

# final products
print(menu)