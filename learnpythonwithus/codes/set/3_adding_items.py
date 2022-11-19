# fruits = {"apple", "orange", "lemon", "mango", "banana"}
#
# # Adding a new item
# print(fruits)
# fruits.add("pineapple")
# print(fruits)

# Extending a set
fruits = {"apple", "orange", "lemon", "mango", "banana"}
fav_fruits = {"pineapple", "strawberry"}

fruits.update(fav_fruits)
print(fruits, fav_fruits)
