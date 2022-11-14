fruits = ['apple', 'papaya', 'banana', 'orange', 'pear', 'lemon']

fav_fruits = list(fruits)
# fav_fruits = fruits.copy()

fruits.append('strawberry')

print(fruits, fav_fruits, id(fruits), id(fav_fruits))
