hotel_name = "Crown Hotel"
total_rooms = 30
room_price = 50000.0
is_open = True

room_types = ["standard", "deluxe", "family", "suite"]
new_room_types = ["premium", "executive"]

# Print all variables and data types
print(hotel_name, type(hotel_name))
print(total_rooms, type(total_rooms))
print(room_price, type(room_price))
print(is_open, type(is_open))
print(room_types, type(room_types))
print(new_room_types, type(new_room_types))

# if else checking
if total_rooms >= 20:
    print("Enough rooms available")
else:
    print("Limited rooms available")

# Change deluxe to deluxe twin
room_types[1] = "deluxe twin"

# Add single using append()
room_types.append("single")

# Add double at index 1 using insert
room_types.insert(1, "double")

# Use extend() to add new_room_types
room_types.extend(new_room_types)

# reomve family using remove()
room_types.remove("family")

# Use pop() to remove the last item
room_types.pop()

# Delete the item at index 0 using del
del room_types[0]

# final room_type
print(room_types)