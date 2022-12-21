# () closed paranthesis
# data = (1, 2, 3)
# print(data, type(data))
#
# data = ()
# print(data, type(data))
#
# data = (1,)
# print(data, type(data))

# constructor

# List to tuple
# data = tuple([1, 2, 3])
# print(data, type(data))
#
# # Set to tuple
# data = tuple({1, 2, 3})
# print(data, type(data))
#
# # dict
# data = tuple({"name": "makereading"})
# print(data, type(data))


list1 = [1, 2, 3, 4]
print(id(list1))

list2 = list(list1)
print(id(list2))

tuple1 = (1, 2, 3, 4)
print(id(tuple1))

tuple2 = tuple(tuple1)
print(id(tuple2))
