---
hide:
  - navigation
  
tags:
  - Python Variables
  - Python References

---

# **Variables Store References, Not Values in Python**
Learn one of Python's most important concepts by understanding how variables reference objects instead of storing values, and why this affects assignment, mutability, copying, and object identity.

---
## <font color='green'>1. References vs Value?" What does it mean?</font>

When learning Python, it's common to think that a variable **stores a value**. In reality, a Python variable stores a **reference** to an object in memory, not the object itself.

A **reference** is like a link or pointer that tells Python where the object is located. When you assign a value to a variable, Python creates an object (if needed) and makes the variable refer to that object.

```python
x = 10
```

Conceptually, Python treats the assignment like this:

```text
+-----+      references      +-----------------+
|  x  | -------------------> | Integer object  |
+-----+                      |       10        |
                             +-----------------+
```

Here:

- `x` is a variable.
- `10` is an integer object.
- `x` stores a reference to the integer object `10`, not the value itself.

You can verify this using the built-in `id()` function, which returns the identity of an object.

```python
x = 10

print(id(x))
```

**Output**

```text
140714205673304
```

The exact number will differ each time you run the program, but it uniquely identifies the object during its lifetime.

If another variable is assigned to `x`, both variables refer to the same object.

```python
x = 10
y = x

print(id(x))
print(id(y))
```

**Output**

```text
140714205673304
140714205673304
```

This can be visualized as follows:

```text
+-----+
|  x  | -----------+
+-----+            |
                   |
+-----+            |
|  y  | -----------+
+-----+            |
                   v
          +-----------------+
          | Integer object  |
          |       10        |
          +-----------------+
```

Both `x` and `y` store references to the **same object**, which is why they have the same object ID.

---
## <font color='green'>2. Assignment Creates a New Reference, Not a Copy</font>

A common misconception is that assigning one variable to another creates a copy of the object. In Python, assignment simply creates a **new reference** to the same object.

Consider the following example:

```python
numbers = [1, 2, 3]
other = numbers
```

Conceptually, the assignment looks like this:

```text
+---------+
| numbers | -----------+
+---------+            |
                       |
+-------+              |
| other | ------------ +
+-------+              |
                       v
              +------------------+
              |   List object    |
              |   [1, 2, 3]      |
              +------------------+
```

Both `numbers` and `other` refer to the **same list object**. No new list is created.

You can verify this using the `id()` function.

```python
numbers = [1, 2, 3]
other = numbers

print(id(numbers))
print(id(other))
```

**Output**

```text
140714205673104
140714205673104
```

Since both variables have the same object ID, they reference the same object.

If you modify the list using one variable, the change is visible through the other variable because both variables point to the same object.

```python
numbers = [1, 2, 3]
other = numbers

other.append(4)

print(numbers)
print(other)
```

**Output**

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

The list was modified only once, but both variables show the updated contents because they reference the same list object.

This behavior often surprises beginners who expect `other = numbers` to create a copy. In reality, it simply creates another reference to the existing object.


---
## <font color='green'>3. Creating an Independent Copy</font>

So far, you've seen that assigning one variable to another does **not** create a new object. Both variables simply refer to the same object.

If you want each variable to have its **own copy** of the object, you must create one explicitly.

For lists, the simplest way is to use the `copy()` method.

```python
numbers = [1, 2, 3]
other = numbers.copy()
```

Conceptually, the objects now look like this:

```text
+---------+                  +------------------+
| numbers | ---------------->|   List object    |
+---------+                  |   [1, 2, 3]      |
                             +------------------+

+-------+                    +------------------+
| other | -----------------> |   List object    |
+-------+                    |   [1, 2, 3]      |
                             +------------------+
```

Although both lists contain the same values, they are different objects in memory.

You can verify this using the `id()` function.

```python
numbers = [1, 2, 3]
other = numbers.copy()

print(id(numbers))
print(id(other))
```

**Output**

```text
140714205673104
140714205673488
```

The exact numbers will differ on your system, but the IDs are different, confirming that two separate list objects were created.

Now, modifying one list does not affect the other.

```python
numbers = [1, 2, 3]
other = numbers.copy()

other.append(4)

print(numbers)
print(other)
```

**Output**

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Unlike assignment, `copy()` creates a new list object, allowing each variable to be modified independently.


---
## <font color='green'>4. Learn More About Copying Objects</font>

In this article, we learned that assigning one variable to another creates a new **reference** to the same object—it does **not** create a copy.

If you need to create an independent copy of an object, Python provides several ways to do so. Understanding when to use a shallow copy versus a deep copy is an important topic on its own.

For a detailed explanation, see:

- [Shallow vs Deep Copy](shallowdeepcopy.md)


---
## <font color='green'>5. Why Is This Important?</font>

Understanding that variables store **references** instead of values helps explain many behaviors in Python that often confuse beginners.

For example, it explains:

- Why assigning one list to another does **not** create a copy.
- Why changes made through one variable can appear when accessing the object through another variable.
- Why `copy()` is needed when you want an independent object.
- Why `==` and `is` produce different results.
- Why mutable and immutable objects behave differently.

This concept is also the foundation for several advanced Python topics, including object identity, function arguments, copying objects, and memory management.

Once you understand that variables store references, many seemingly confusing behaviors in Python become much easier to reason about.


---
## <font color='green'>6. Summary</font>

- Python variables store **references** to objects, not the objects themselves.
- Assigning one variable to another creates a new reference to the same object; it does **not** create a copy.
- Multiple variables can refer to the same object in memory.
- The `id()` function can be used to determine whether two variables reference the same object.
- Modifying a shared mutable object through one variable is visible through all variables that reference it.
- To work with an independent object, you must create a copy explicitly.
- Understanding object references is essential for mastering topics such as object identity, mutability, copying, and function arguments in Python.


---
## **Relevant Links**

[Python Material on this website](index.md)

