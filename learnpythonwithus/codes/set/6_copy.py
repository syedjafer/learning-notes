fruits = {"apple", "orange", "lemon", "banana", "papaya"}

new_set = fruits.copy()
print(new_set, fruits, id(new_set), id(fruits))

fav_fruits = fruits
print(id(fruits), id(fav_fruits))
fruits.add("pear")
print(fruits, fav_fruits)
