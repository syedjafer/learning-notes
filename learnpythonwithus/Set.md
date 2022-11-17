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

### Copying Items

#### copy()

```python
fruits = {"apple", "cherry"}
fav_fruits = fruits.copy()
print(fav_fruits)
```

or using `set()`  or `=`


### Mathematical Functions

Usually set in maths is , 

#### Union of sets

Union of two sets will return all the items present in both sets (all items will be present only once). This can be done with either the `|` operator or the `union()` method.

`union` functionality can also be done using the `| ` operator. 

```python
fruits = {"apple", "banana", "orange"}
fav_fruits = {"lemon", "jackfruit", "strawberry"}
response = fruits.union(fav_fruits)
print(response)
```

#### Intersection of sets

The intersection of two sets will return only the common elements in both sets. The intersection can be done using the `&` operator and `intersection()` method. 

The `intersection()` method will return a new set with only the common elements in all the sets. Use this method to find the common elements between two or more sets.

```python
fruits = {"apple", "orange", "banana"}
fav_fruits = {"apple", "jackfruit", "lemon"}

common_fruits = fruits & fav_fruits
print(common_fruits)

common_fruits = fruits.intersection(fav_fruits)
print(common_fruits)

```

-   `intersection()` will not update the original set but `intersection_update()` will update the original set with only the common elements.
-   `intersection()` will have a return value which is the new set with common elements between two or more sets whereas `intersection_update()` will not have any return value.

#### Difference of sets

The difference operation will return the items that are present **only** in the first set i.e the set on which the method is called. This can be done with the help of the `-` operator or the `difference()` method.

```python
fruits = {"apple", "banana", "orange"}
fav_fruits = {"apple", "lemon"}

diff = fruits.difference(fav_fruits)
print(diff)
```

-   The `difference()` method will not update the original set while `difference_update()` will update the original set.
-   The `difference()` method will return a new set with only the unique elements from the set on which this method was called. `difference_update()` will not return anything.

#### symmetric difference

The Symmetric difference operation returns the elements that are unique in both sets. This is the opposite of the intersection. This is performed using the `^` operator or by using the `symmetric_difference()` method.

```python
fruits = {"apple", "banana", "orange"}
fav_fruits = {"apple", "lemon"}

diff = fruits.symmetric_difference(fav_fruits)
print(diff)
```

In addition to the `symmetric_difference()`, there is one more method called **`symmetric_difference_update()`**. There are two main differences between these two methods.

The `symmetric_difference()` method will not update the original set while `symmetric_difference_update()` will update the original set with the unique elements from both sets.

#### Subset

The `issubset()` is used to find whether a set is a subset of another set i.e all the items in the set on which this method is called are present in the set which is passed as an argument.

This method will return true if a set is a subset of another set otherwise, it will return false.

#### Superset

This method determines whether the set is a superset of another set.

It checks whether the set on which the method is called contains all the items present in the set passed as the argument and returns true if the set is a superset of another set; otherwise, it will return false.

#### Disjoint sets

The `isdisjoint()` method will find whether two sets are disjoint i.e there are no common elements. This method will return true if they are disjoint otherwise it will return false.


### Sorting

A set is an unordered collection of data items, so there is no point n sorting it. If you still want to sort it using the `sorted()` method but this method will return the list

The `sorted()` function is used to sort the set. This will return a new list and will not update the original set.

### Builtin functions

1. max()
2. min()
3. all() - boolean ; if all values are true (Non zero and True, non empty string)
4. any() - any value of the set is true; then true. 

6. 