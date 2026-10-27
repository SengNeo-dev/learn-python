store_name = "Fashion House"
staff_count = 5
monthly_income = 850000.0
is_open = True

clothes = ["shirt", "jeans", "jacket", "dress"]
new_clothes = ["skirt", "hoodie"]

# Print all variables and data types
print(store_name, type(store_name))
print(staff_count, type(staff_count))
print(monthly_income, type(monthly_income))
print(is_open, type(is_open))
print(clothes, type(clothes))
print(new_clothes, type(new_clothes))

# if else checking
if monthly_income >= 800000:
    print("Income target achieved")
else:
    print("Income target not achieved")

# Print first, third and last items
print(clothes[0])
print(clothes[1])
print(clothes[3])

# Change jeans to black jeans
clothes[1] = "black jeans"

# Add sweater using append()
clothes.append("sweater")

# Add T-shirt at index 1 using insert
clothes.insert(1, "T-shirt")

# Use extend() to add new_clothes in clothes
clothes.extend(new_clothes)

# Remove jacket using remove()
clothes.remove("jacket")

# Use pop() to remove last item
clothes.pop()

# Delete item at index 0 using del
del clothes[0]

# final products
print(clothes)