city_1 = ('London', 'UK', 8.99)
city_2 = ('Freetown', 'Sierra Leone', 7.8)
city_3 = ('Cape Town', 'South Africa', 8.6)

capitals = [('London', 'UK', 8.99), ('Freetown', 'Sierra Leone', 7.8), ('Cape Town', 'South Africa', 8.6)]

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])


user_data = ('Donnie', 'American', 1992, {202.5, 217.3, 209.7})

# Convert the set to a list, add the new value, and convert it back to a set
temp_set = user_data[3].copy()  # Create a copy of the set
temp_set.add(205.8)  # Add the new value

# Create a new tuple with the updated set
user_data = (user_data[0], user_data[1], user_data[2], temp_set)

print(user_data)
