data = {1, 2, 3, 4, 5}
# data.update([10, 12, 34])
# print(data)

# data.update({'a':2, 'b':4, 'c':5})
# print(data)

# data.update('makereading')
# print(data)

print(set([1, 2, 3]))

def customUpdate(values, set_item):
    res = set(values)
    for x in res:
        set_item.add(x)
