import sys

SIZE_OF_LIST = 56

data = [1, 2, 3, 4]
size = sys.getsizeof(data)

print(f'Size of data is {size - SIZE_OF_LIST}')
