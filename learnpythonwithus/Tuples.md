can**Tuples are ordered collections of heterogeneous data that are unchangeable**. Heterogeneous means tuple can store variables of all types.

### Properties
- Ordered
- Unchangeable
- Heterogeneous
- Contains Duplicate


### Declaring

1.  **Using parenthesis ():** A tuple is created by enclosing comma-separated items inside rounded brackets.
2.  Using a `tuple()` constructor: Create a tuple by passing the comma-separated items inside the `tuple()`.


```python
data = (1, 2, 3, 4, 5)
print(type(data))
```

While declaring empty tuple, 

```python
data = ()
```

While declaring tuple with only one value, we must need to specify the comma `,`

```python
data = (1)
print(type(data))
```

### Data Type
tuple contains different types of the data types. 

1. Create a tuple with a single item

In Python, we can create a tuple by packing a group of variables. Packing can be used when we want to collect multiple values in a single variable. Generally, this operation is referred to as tuple packing.

Similarly, we can unpack the items by just assigning the tuple items to the same number of variables. This process is called “Unpacking.”

Tuple is immutable with mutable and immutable datatypes. Its also called as immutable lists. 

### Builtin functions

1. Length
2. max
3. min
4. type
5. any
6. all
7. index
8. count


```python
fruits = ("apple", "fruits", "orange")
print(len(fruits))
```


```python
fruits = ("apple", 1, 0.4, [1, 2, 3], {"name":"makereading"})
print(fruits)
```


```python
fruits = ("apple", 1, 0.4, [1, 2, 3], {"name":"makereading"})
print(type(fruits))
```


```python
fruits = ("apple", 1, 0.4, [1, 2, 3])
print(fruits[0])
```


```python
fruits = ("apple", 1, 0.4, "a")
for val in fruits:
	print(val)
```

### Accessing Elements in a list

1. Negative Indexing
2. Positive Indexing
3. Slicing will return a tuple

###  Adding 
We can't add since its immutable. 

### Removing
pop or remove wont work. 

del - works. 

