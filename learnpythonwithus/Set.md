A set is a collection which is _unordered_, _unchangeable*_, and _unindexed_.
Since it doesnot maintain the order, we can't be using the index. 

#### Declaring

We need to use the set() constructor or {} (if we are having one or more numbers). If you want to declare the empty set we should use only set()

#### Length

```python
fruits = {"apple", "banana", "cherry"}  
print(len(thisset))
```


#### Support Different Datatypes

It will be supporting different data types in a same set. 


```python
set1 = {"abc", 34, True, 40, "male"}
print(set1)
```

#### Type 

From Python's perspective, sets are defined as objects with the data type 'set':

```python
fruits = set(["apple", "banana", "cherry"])
print(type(fruits))
```


### Accessing Items

You cannot access items in a set by referring to an index or a key.
For printing the values one-by-one we can use `for` loop. 

```python
fruits = {"apple", "banana", "cherry"}  
for x in fruits:  
  print(x)
```

#### In 
We can check if the value present in the set using '**in**' 

```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)
```

### Removing Items

#### remove()

If the element is present then it will remove, else it will **throw error.** 

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("apple")
```

#### discard()

Same as remove, but even if the word is not present, it will fail safe. 

```python
fruits = {"apple", "cherry"}  
fruits.discard("banana")
print(thisset)
```

#### pop()

pop will remove the last item, since we dont know which is the last item, we cant be sure which element to be deleted. 

```python
fruits = {"apple", "cherry"}
removed_element = fruits.pop()
print(fruits, removed_element)
```

#### clear()

To remove all elements from set. 
```python
fruits = {"apple", "cherry"}
print(fruits.clear())
```

#### del()

To delete the object itself, 

```python
fruits = {"apple", "cherry"}
del fruits
print(fruits)
```

