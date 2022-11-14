
#### Declaring

```python
listex = [] // support multi data types.

listex = [1, 2, 3, 4, 'syed', 'jafer', 2.3]
```

For printing, 

```python
print(listex)
```

List items are ordered, changeable, and allow duplicate values. List items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.


1. **Allow Duplicates**
Since lists are indexed, lists can have items with the same value:

```python
fruits = ['apple', 'orange', 'apple', 'banana']
print(fruits)
```

2. **List Length**
To determine how many items a list has, use the `len()` function:

```python
fruits = ['apple', 'orange', 'apple', 'banana']
print(len(fruits))
```

3. **List Items - Data Types**

List items can be of any data type:

```python
list1 = ["apple", "banana", "cherry"]  
list2 = [1, 5, 7, 9, 3]  
list3 = [True, False, False]
```

4. **Type of List**
From Python's perspective, lists are defined as objects with the data type 'list':

```python
mylist = ["apple", "banana", "cherry"]  
print(type(mylist))
```

5. List Constructor
It is also possible to use the list() constructor when creating a new list.

```python
fruits = list(("apple", "banana", "cherry")) 
print(fruits)
```

### Accessing List Items

List items are indexed and you can access them by referring to the index number:

```python
fruits = ["apple", "banana", "cherry"]  
print(fruits[1])
```

### Negative Indexing

Negative indexing means start from the end. `-1` refers to the last item, `-2` refers to the second last item etc.

```python
fruits = ["apple", "banana", "cherry"]  
print(fruits[-1])
```

### Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  
print(fruits[2:5])
```

>**Note:** The search will start at index 2 (included) and end at index 5 (not included).


> list[start:end]


```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  
print(thislist[:4])
```

Even negative indexing will work, 

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  
print(fruits[-4:-1])
```


```python
fruits = ["apple", "banana", "cherry"]  
if "apple" in thislist:  
  print("Yes, 'apple' is in the fruits list")
```

### Change List Items

```python
fruits = ["apple", "banana", "cherry"]  
fruits[1] = "blackcurrant"  
print(fruits)
```

changing a range of values, 

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]  
fruits[1:3] = ["blackcurrant", "watermelon"]  
print(fruits)
```

If you insert _more_ items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.


### List Functions - Methods

1. **insert()**

```python
list.insert(index, value)
```


Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

2. **append()**

```python
fruits = ["apple", "banana", "cherry"]  
fruits.append("orange")  
print(fruits)
```

**Equivalents:** 

`a[len(a):] = [x]`.

3. **extend()**

```python
fruits = ["apple", "banana", "cherry"]  
fruits_fav = ["mango", "pineapple", "papaya"]  
fruits.extend(fruits_fav)  
print(fruits)
```


### Removing


1. **remove()**
 removes the first occurence 
```python
thislist = ["apple", "banana", "cherry"]  
thislist.remove("banana")  
print(thislist)
```

2. **pop()**
The `pop()` method removes the specified index.

```python
fruits = ["apple", "banana", "cherry"]  
fruits.pop(1)  
print(fruits)
```

3. **del()**
It removes the particular index; also the whole lists. 

```python
fruits = ["apple", "banana", "cherry"]  
del fruits[0]  
print(fruits)
```

4. **clear()**

```python
fruits = ["apple", "banana", "cherry"]  
fruits.clear()  
print(fruits)
```

### Sorting

```python
states = ['Tamil Nadu', 'Kerala', 'Andra', 'Telengana']
states.sort()
print(states)
```

reverse descending, 

```python
states = ['Tamil Nadu', 'Kerala', 'Andra', 'Telengana']
states.sort(reverse=True)
print(states)
```

case sensitive, 

```python
states = ['Tamil Nadu', 'Kerala', 'Andra', 'Telengana']
states.reverse()
print(states)
```


### Copy

Need of Copy

```python
states = ['Tamil Nadu', 'Kerala', 'Andra', 'Telengana']
copied_states = states.copy()
print(copied_states)
```

or list(states)

