import sys

SIZE_OF_LIST = 56

data = [1, 2, 3, 4]
size = sys.getsizeof(data)


id_4 = id(data[-1])
print(id_4)


data.remove(4)
size = sys.getsizeof(data) - SIZE_OF_LIST
print(size)

import ctypes
print (ctypes.cast(id_4, ctypes.py_object).value)

print(data)
