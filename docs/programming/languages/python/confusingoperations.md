---
hide:
  - navigation
  
tags:
  - Confusing Operations in Python
  
---

# **Confusing Operations in Python**
Learn the differences between Python operations and operators that are often confused by beginners and frequently asked in interviews.


---
## <font color='green'>1. `append()` vs `extend()`</font>

`append()` and `extend()` are **methods of the Python `list` type**. Both are used to add elements to a list, but they behave differently.

| Method | Available On | Purpose |
|---------|--------------|---------|
| `append()` | `list` only | Adds a single object to the end of the list. |
| `extend()` | `list` only | Adds each element from an iterable to the end of the list. |

### `append()`

`append()` adds **one object** to the end of the list.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

**Output**

```text
[1, 2, 3, 4]
```

If the object is another list, the **entire list is added as a single element**.

```python
numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)
```

**Output**

```text
[1, 2, 3, [4, 5]]
```

---

### `extend()`

`extend()` expects an **iterable** and adds each of its elements individually.

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
```

**Output**

```text
[1, 2, 3, 4, 5]
```

Since strings are iterable, `extend()` adds one character at a time.

```python
letters = ["A"]

letters.extend("BC")

print(letters)
```

**Output**

```text
['A', 'B', 'C']
```

---

### Summary

| `append()` | `extend()` |
|------------|------------|
| Adds a single object | Adds multiple elements |
| Accepts any object | Expects an iterable |
| Nested lists remain nested | Elements are added individually |
| Available only on `list` | Available only on `list` |


---
## <font color='green'>2. `append()` vs `insert()`</font>

`append()` and `insert()` are **methods of the Python `list` type**. Both add elements to a list, but they differ in **where** the new element is placed.

| Method | Available On | Purpose |
|---------|--------------|---------|
| `append()` | `list` only | Adds an element to the end of the list. |
| `insert()` | `list` only | Inserts an element at a specified index. |

### `append()`

`append()` always adds the new element **at the end** of the list.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

**Output**

```text
[1, 2, 3, 4]
```

---

### `insert()`

`insert(index, object)` inserts the object **before the specified index**.

```python
numbers = [1, 2, 3]

numbers.insert(1, 10)

print(numbers)
```

**Output**

```text
[1, 10, 2, 3]
```

If the index is greater than the list length, the element is added at the end.

```python
numbers = [1, 2, 3]

numbers.insert(100, 4)

print(numbers)
```

**Output**

```text
[1, 2, 3, 4]
```


---
## <font color='green'>3. `remove()` vs `pop()` vs `del`</font>

`remove()` and `pop()` are **methods of the Python `list` type**, whereas `del` is a **Python statement** that can remove items from many types or even delete entire variables.

| Operation | Available On | Purpose |
|-----------|--------------|---------|
| `remove()` | `list` only | Removes the first occurrence of a specified value. |
| `pop()` | `list` only | Removes and returns an element by index. |
| `del` | Lists, dictionaries, variables, and more | Deletes items, slices, or entire objects. |

### `remove()`

`remove(value)` removes the **first matching value** from the list.

```python
numbers = [1, 2, 3, 2]

numbers.remove(2)

print(numbers)
```

**Output**

```text
[1, 3, 2]
```

---

### `pop()`

`pop(index)` removes and **returns** the element at the given index.

```python
numbers = [1, 2, 3]

item = numbers.pop(1)

print(numbers)
print(item)
```

**Output**

```text
[1, 3]
2
```

If no index is given, the last element is removed.

```python
numbers = [1, 2, 3]

numbers.pop()

print(numbers)
```

**Output**

```text
[1, 2]
```

---

### `del`

`del` can remove an item by index, delete a slice, or delete an entire variable.

Delete an item:

```python
numbers = [1, 2, 3]

del numbers[1]

print(numbers)
```

**Output**

```text
[1, 3]
```

Delete a slice:

```python
numbers = [1, 2, 3, 4, 5]

del numbers[1:4]

print(numbers)
```

**Output**

```text
[1, 5]
```

Delete a variable:

```python
x = 10

del x
```


---
## <font color='green'>4. `sort()` vs `sorted()`</font>

`sort()` and `sorted()` are both used to sort data, but they differ in **where they are available** and **whether they modify the original object**.

| Operation | Available On | Purpose |
|-----------|--------------|---------|
| `sort()` | `list` only | Sorts the list in place. |
| `sorted()` | Any iterable | Returns a new sorted list without modifying the original object. |

### `sort()`

`sort()` modifies the original list.

```python
numbers = [3, 1, 2]

numbers.sort()

print(numbers)
```

**Output**

```text
[1, 2, 3]
```

---

### `sorted()`

`sorted()` returns a **new sorted list**, leaving the original object unchanged.

```python
numbers = [3, 1, 2]

result = sorted(numbers)

print(numbers)
print(result)
```

**Output**

```text
[3, 1, 2]
[1, 2, 3]
```

`sorted()` also works with other iterables such as tuples, sets, and strings.

```python
letters = ('c', 'a', 'b')

print(sorted(letters))
```

**Output**

```text
['a', 'b', 'c']
```



---
### Summary

| `sort()` | `sorted()` |
|-----------|------------|
| List method | Built-in function |
| Available only on `list` | Works with any iterable |
| Modifies the original list | Returns a new sorted list |
| Returns `None` | Returns the sorted list |


**What type of functions are they?**

| Operation | Type | Available On |
|-----------|------|--------------|
| `sort()` | Instance method | `list` objects only |
| `sorted()` | Built-in function | Any iterable |


---
### Summary

| `remove()` | `pop()` | `del` |
|-------------|----------|--------|
| Removes by value | Removes by index | Deletes by index, slice, or entire object |
| Returns nothing | Returns the removed element | Returns nothing |
| List method | List method | Python statement |
| Available only on `list` | Available only on `list` | Works with many object types |




---

### Summary

| `append()` | `insert()` |
|------------|------------|
| Adds an element at the end | Adds an element at a specified position |
| Takes one argument: `object` | Takes two arguments: `index`, `object` |
| Faster for adding to the end | Existing elements may be shifted |
| Available only on `list` | Available only on `list` |



---
## <font color='green'>5. `is` vs `==`</font>

`is` and `==` are both used to compare objects, but they compare **different things**.

- `==` checks whether two objects have the **same value**.
- `is` checks whether two variables refer to the **same object in memory**.

| Operator | Purpose |
|----------|---------|
| `==` | Compares the values of two objects. |
| `is` | Compares the identity (memory reference) of two objects. |

### `==`

Use `==` when you want to check whether two objects contain the same value.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
```

**Output**

```text
True
```

Although `list1` and `list2` are different objects, they contain the same values.

---

### `is`

Use `is` when you want to check whether two variables refer to the **same object**.

```python
list1 = [1, 2, 3]
list2 = list1

print(list1 is list2)
```

**Output**

```text
True
```

Both variables refer to the same list object.

If two variables refer to different objects, `is` returns `False`, even if their values are equal.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 is list2)
```

**Output**

```text
False
```

---

### When should you use `is`?

The most common use of `is` is to compare an object with `None`.

```python
name = None

if name is None:
    print("No name provided")
```

Using `is None` is the recommended Python style.



---
### Summary

| `==` | `is` |
|------|------|
| Compares values | Compares object identity |
| Checks if values are equal | Checks if both variables refer to the same object |
| Used for most comparisons | Commonly used with `None` |
| May return `True` for different objects with equal values | Returns `True` only for the exact same object |


---
## <font color='green'>6. `=` vs `==` vs `is`</font>

`=`, `==`, and `is` look similar, but they serve completely different purposes in Python.

| Operator | Type | Purpose |
|----------|------|---------|
| `=` | Assignment operator | Assigns a value to a variable. |
| `==` | Comparison operator | Checks whether two values are equal. |
| `is` | Identity operator | Checks whether two variables refer to the same object. |

### `=`

The assignment operator stores a reference to an object in a variable. See [Variables are references](variablesarereferences.md)


```python
x = 10
y = x

print(x)
print(y)
```

**Output**

```text
10
10
```

Here, `=` does **not** compare anything. It simply assigns a value (or object reference) to a variable.

---

### `==`

The equality operator compares the **values** of two objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

**Output**

```text
True
```

Although `a` and `b` are different objects, they contain the same values.

---

### `is`

The identity operator compares whether two variables refer to the **same object**.

```python
a = [1, 2, 3]
b = a

print(a is b)
```

**Output**

```text
True
```

If the variables refer to different objects, `is` returns `False`, even if their values are equal.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

**Output**

```text
False
```

---
## <font color='green'>Key Takeaways</font>

- `append()` and `extend()` are list methods used to add elements, but `append()` adds a single object while `extend()` adds elements from an iterable.
- `append()` always adds to the end of a list, whereas `insert()` adds an element at a specified position.
- `remove()` deletes an element by value, `pop()` removes and returns an element by index, and `del` deletes items, slices, or entire objects.
- `sort()` is a **list instance method** that sorts the original list, while `sorted()` is a **built-in function** that returns a new sorted list from any iterable.
- `==` compares the values of two objects, whereas `is` compares whether two variables refer to the same object in memory.
- `=` assigns a value or object reference to a variable, `==` compares values, and `is` compares object identity.

Understanding these differences will help you write clearer Python code, avoid common beginner mistakes, and confidently answer many Python interview questions.



---
### Summary

| `=` | `==` | `is` |
|-----|------|------|
| Assigns a value to a variable | Compares values | Compares object identity |
| Assignment operator | Comparison operator | Identity operator |
| Does not return `True` or `False` | Returns `True` or `False` | Returns `True` or `False` |
| Used to create or update variables | Used for value comparison | Commonly used with `None` |




---
## **Relevant Links**

[Python Material on this website](index.md)

