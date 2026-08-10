---
hide:
  - navigation
  
tags:
  - shallow copy
  - deep copy
---

# Understanding Shallow vs Deep Copy in Python

---
## <font color='green'> 1. Copying objects in Python: `=` operator and `.copy()` </font>

A Python variable **does not contain the object itself**. Instead, it holds a **reference** to an object in memory.

> *A note for Java programmers: This concept of objects/references is similar to used in Java (in case you are familiar with Java).*


## Reference Assignment

Consider this example:

```python
a = [1, 2, 3]
b = a
```

><font color='red'> Many beginners assume that `b` becomes a new copy of the list. That's **not** what happens. Instead, both variables point to the **same object**. </font>

```text
Variables                  Memory

+---+                      +----------------+
| a | -------------------> |  [1, 2, 3]     |
+---+                      +----------------+
                              ^
                              |
+---+                         |
| b | ------------------------+
+---+
```

Since there's only **one list object**, modifying it through either variable affects the same object.

```python
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

The memory now looks like this:

```text
Variables                  Memory

+---+                      +-------------------+
| a | -------------------> | [1, 2, 3, 4]      |
+---+                      +-------------------+
                              ^
                              |
+---+                         |
| b | ------------------------+
+---+
```

Notice that **no new object was created**. Both variables still refer to the same list.



### Solution: use `list.copy()`

The problem with `=` is that it doesn't create a new object. If all we want is an independent copy of a list, Python provides the `list.copy()` method.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

This time, modifying `b` does **not** affect `a`.

The reason is that `list.copy()` creates a **new outer list**.

```text
Variables                  Memory

+---+                      +----------------+
| a | -------------------> |  [1, 2, 3]     |
+---+                      +----------------+

+---+                      +-------------------+
| b | -------------------> | [1, 2, 3, 4]      |
+---+                      +-------------------+
```

> <font color='red'>Lists (and other containers) are copied using **.copy()** instead of **=** operator. This behavious is called **shallow copy**</font>


### What About Integers?

This behavior is often confusing because it appears different for basic data types like integers.

```python
x = 10
y = x

y += 5

print(x)  # 10
print(y)  # 15
```

At first glance, it may seem that integers are copied automatically. That's not what happens.

Initially, both variables reference the same integer object.

```text
Variables                  Memory

+---+                      +------+
| x | -------------------> |  10  |
+---+                      +------+
                              ^
                              |
+---+                         |
| y | ------------------------+
+---+
```

> However, integers are **immutable**. They cannot be modified in place. The expression `y += 5` creates a **new integer object** (`15`) and updates `y` to reference it.

```text
Variables                  Memory

+---+                      +------+
| x | -------------------> |  10  |
+---+                      +------+

+---+                      +------+
| y | -------------------> |  15  |
+---+                      +------+
```


> Lists, dictionaries, sets, and most collections are **mutable**, meaning their contents can be changed without creating a new object. This is why copying becomes important for collections but is rarely a concern for immutable objects like integers, floats, strings, and tuples.

---
## <font color='green'>2. Shallow Copy</font>

## Issue with Shallow Copy

At first glance, this looks like the perfect solution. However, `list.copy()` creates a new outer list, but the nested objects are still shared between the original and the copy. This behavior is known as a **shallow copy**.

Consider a list containing other lists.

```python
original = [
    [1, 2],
    [3, 4]
]

copied = original.copy()
```

> This time, two outer lists are created, but the inner lists are **not copied**.

Now modify **ONE** of the nested lists (<font color='red'> but **BOTH** get modified </font>)

```python
copied[0].append(99)

print("original =", original)
print("copied   =", copied)
```

Output:

```text
original = [[1, 2, 99], [3, 4]]
copied   = [[1, 2, 99], [3, 4]]
```


### Inner objects are not copied

Although `original` and `copied` are different outer lists, the **inner lists are still the same objects**.

Let's verify that.

```python
original = [
    [1, 2],
    [3, 4]
]

copied = original.copy()

copied[0].append(10)

print(original)
print(copied)
```

Output:

```text
[[1, 2, 10], [3, 4]]
[[1, 2, 10], [3, 4]]
```

> Appending `10` to `copied[0]` also changes `original[0]` because both outer lists refer to the **same inner list object**. A shallow copy creates a new outer list, but the objects inside it are **shared**.


---
## <font color='green'>3. Deep Copy (a Solution to Nested Objects)</font>

A **deep copy** creates a completely independent copy of an object, including **all nested objects**. Unlike a shallow copy, none of the inner objects are shared between the original and the copy.

Python provides the `deepcopy()` function in the `copy` module.

```python
from copy import deepcopy

original = [
    [1, 2],
    [3, 4]
]

copied = deepcopy(original)

copied[0].append(10)

print(original)
print(copied)
```

Output:

```text
[[1, 2], [3, 4]]
[[1, 2, 10], [3, 4]]
```

This time, modifying `copied[0]` does **not** affect `original[0]` because `deepcopy()` creates new copies of both the outer list and all nested objects.

As a result, `original` and `copied` are completely independent.

---
## <font color='green'>4. Lists and Other Collections</font>

Shallow and deep copying are **not limited to lists**. The same concepts apply to other Python collections that can contain nested objects, such as:

- Lists
- Dictionaries
- Sets
- Tuples (when they contain mutable objects)

For example, a shallow copy of a dictionary copies only the dictionary itself. Any nested lists, dictionaries, or other mutable objects are still shared.

Whenever a collection contains **nested mutable objects**, a shallow copy copies only the outer container. If you need a completely independent copy of the entire structure, use `deepcopy()`.

---
## <font color='green'>Summary</font>

- Variables store **references** to objects, not the objects themselves.
- Using `=` creates another reference to the same object.
- A **shallow copy** creates a new outer container, but the nested objects are still shared.
- Modifying a shared nested object affects both the original and the shallow copy.
- A **deep copy** creates new copies of the outer container and all nested objects, making the copy completely independent.
- Whenever you need to duplicate a nested data structure without sharing any objects, use `copy.deepcopy()`.
- Shallow and deep copies are mainly used with **collections** (such as lists, dictionaries, sets, and nested tuples). 
- For basic immutable data types like `int`, `float`, `str`, and `bool`, the `=` operator is sufficient because their values cannot be modified in place.

---
## **Relevant Links**

[Python Material on this website](index.md)

