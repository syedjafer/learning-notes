fruits = {"apple", "orange", "lemon", "banana", "papaya"}

# fruits2 = fruits
# fruits.add('pineapple')
#
# print(fruits, fruits2)

fruits2 = fruits.copy()
fruits.add('pineapple')
print(fruits, fruits2)
