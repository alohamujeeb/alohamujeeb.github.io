---
hide:
  - navigation
  
tags:
  - Garbage Collector in Python
  - Reference Count
  - Reference Cycle
  

---
# Garbage Collection in Python
Learn how Python manages memory automatically using reference counting and garbage collection, and understand how objects are created, tracked, and removed when they are no longer needed.

---
## <font color='green'>1. What Is Memory Management?</font>

Every program uses your computer's memory to store data while it is running. Whenever we create a variable, list, dictionary, or any other object in Python, memory is allocated to store that object.

For example, when you create an integer:

```python
x = 10
```

Python creates an integer object and stores it in memory. The variable `x` then refers to that object.

Conceptually, this looks like:

```text
+-----+
|  x  | ----------------------+
+-----+                       |
                              v
                     +-----------------+
                     | Integer object  |
                     |       10        |
                     +-----------------+
```

As your program runs, Python continuously creates new objects and removes objects that are no longer needed. This process of allocating and releasing memory is known as **memory management**.

Unlike languages such as C or C++, Python manages memory automatically. You do not need to manually allocate memory when creating objects or explicitly free memory when objects are no longer in use.

This automatic memory management helps make Python programs easier to write and reduces common programming errors such as memory leaks and invalid memory access.

In the following sections, you'll learn how Python keeps track of objects using **reference counting** and how the **garbage collector** cleans up objects that can no longer be reached.


---
## <font color='green'>2. Comparing Python Memory Management with C</font>

If you have a background in C, Python's memory management may seem very different. While both languages use your computer's memory, Python hides most of the low-level details from the programmer.

In C, variables store values directly (for primitive types), and the programmer is responsible for allocating and freeing dynamically allocated memory.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int x = 10;                 // Stored directly in the variable
    int *p = malloc(sizeof(int));

    *p = 20;

    printf("%d %d\n", x, *p);

    free(p);                    // Must be freed manually
    return 0;
}
```

If `free()` is forgotten, the allocated memory remains occupied until the program terminates, resulting in a **memory leak**.

In Python, objects are created automatically, and variables simply store references to those objects.

```python
x = 10
numbers = [1, 2, 3]
```

Conceptually:

```text
Namespace

+---------+                +------------------+
|    x    | -------------> | Integer object   |
+---------+                |       10         |
                           +------------------+

+---------+                +------------------+
| numbers | -------------> | List object      |
+---------+                |   [1, 2, 3]      |
                           +------------------+
```

When an object is no longer needed, Python automatically reclaims its memory. In most cases, you do not need to explicitly release memory as you would in C.

The following table summarizes the main differences.

| Feature | C | Python |
|---------|---|--------|
| Variables store | Values (primitive types) or pointers | References to objects |
| Memory allocation | Manual (`malloc`, `calloc`) | Automatic |
| Memory deallocation | Manual (`free`) | Automatic |
| Memory leaks | Possible if memory is not freed | Much less common due to automatic memory management |
| Dangling pointers | Possible | Not exposed to the programmer |
| Programmer responsibility | High | Low |

Although Python manages memory automatically, understanding how objects are created, referenced, and destroyed is still important for writing efficient programs. In the next section, you'll learn how Python keeps track of objects using **reference counting**.

---
## <font color='green'>3. Returning Objects from Functions</font>

Programmers coming from C often wonder what happens when a function returns a locally created object. In C, returning the address of a local variable is unsafe because the variable is destroyed when the function returns.

Python works differently.

A local variable does **not** own the object it refers to. It simply stores a **reference** to that object. When a function returns an object, Python returns the reference to the caller.

Consider the following example:

```python
def create_list():
    numbers = [1, 2, 3]
    return numbers

values = create_list()

print(values)
```

**Output**

```text
[1, 2, 3]
```

When the list is created, the local variable `numbers` refers to it.

```text
Function Frame

+---------+
| numbers | --------+
+---------+         |
                    v
             +---------------+
             | List object   |
             | [1, 2, 3]     |
             +---------------+
```

When `return numbers` is executed, Python returns the **reference** to the list object.

After the function returns, the local variable `numbers` is removed because the function frame is destroyed. However, the object itself is **not** destroyed because the caller now holds a reference to it.

```text
Global Namespace

+--------+
| values | --------+
+--------+         |
                   v
            +---------------+
            | List object   |
            | [1, 2, 3]     |
            +---------------+
```

The list remains in memory because at least one variable (`values`) still refers to it.

You can verify that the returned object is still valid by modifying it.

```python
def create_list():
    numbers = [1, 2, 3]
    return numbers

values = create_list()
values.append(4)

print(values)
```

**Output**

```text
[1, 2, 3, 4]
```

This behavior is very different from C.

In C, returning the address of a local variable is invalid because the local variable's memory is released when the function returns.

```c
int* createArray() {
    int numbers[3] = {1, 2, 3};
    return numbers;      // Unsafe
}
```

In Python, objects are **not** tied to the lifetime of local variables. They remain in memory as long as at least one reference to them exists. When the last reference is removed, Python automatically reclaims the object's memory.


---
## <font color='green'>4. Reference Counting</font>

Python uses **reference counting** to keep track of how many variables refer to an object.

Every object maintains a **reference count**, which is the number of active references pointing to it. Whenever a new reference is created, the reference count increases. When a reference is removed, the count decreases.

When the reference count reaches **zero**, the object is no longer accessible, and Python can reclaim the memory occupied by that object.

The following example demonstrates this concept.

```python
def display(numbers):
    print(numbers)

values = [10, 20, 30]

display(values)
```

Initially, the variable `values` refers to the list object.

```text
Global Namespace

+--------+
| values | --------+
+--------+         |
                   v
            +----------------+
            | List object    |
            | [10, 20, 30]   |
            +----------------+

Reference Count = 1
```

When `display(values)` is called, the function parameter `numbers` also refers to the same list object.

```text
Global Namespace             Function Frame

+--------+                   +---------+
| values | --------+         | numbers | ------+
+--------+         |         +---------+       |
                   |                           |
                   +---------------------------+
                                               |
                                               v
                                        +----------------+
                                        | List object    |
                                        | [10, 20, 30]   |
                                        +----------------+

Reference Count = 2
```

Both variables refer to the **same object**. No new list is created.

When the function finishes, its local variable `numbers` is destroyed, removing one reference.

```text
Global Namespace

+--------+
| values | --------+
+--------+         |
                   v
            +----------------+
            | List object    |
            | [10, 20, 30]   |
            +----------------+

Reference Count = 1
```

The list object remains in memory because the global variable `values` still refers to it.

Now consider the following example.

```python
def display(numbers):
    print(numbers)

values = [10, 20, 30]

display(values)

del values
```

After executing `del values`, there are no remaining references to the list object.

```text
(No references)

        +----------------+
        | List object    |
        | [10, 20, 30]   |
        +----------------+

Reference Count = 0
```

Since the reference count has reached **zero**, the object is no longer accessible. Python automatically reclaims the memory used by the list.

Reference counting is one of the primary techniques Python uses for automatic memory management. However, it is not sufficient in every situation. In the next section, you'll learn why Python also includes a **garbage collector** to handle objects involved in reference cycles.


---
## <font color='green'>5. Inspecting the Reference Count</font>

In the previous section, we learned that Python keeps track of how many references point to an object. In **CPython** (the standard Python implementation), you can inspect an object's reference count using the `sys.getrefcount()` function.

> **Note:** `sys.getrefcount()` is intended primarily for debugging and understanding Python's memory management. It is specific to CPython and should not be relied upon in production code.

### Example 1: A Single Reference

```python
import sys

numbers = [1, 2, 3]

print(sys.getrefcount(numbers))
```

**Output**

```text
2
```

You might expect the reference count to be **1**, since only the variable `numbers` refers to the list.

However, `getrefcount()` itself temporarily creates an additional reference while the function is executing.

Conceptually:

```text
numbers  --------+
                 |
                 +------> List object [1, 2, 3]

getrefcount() ---+
```

Therefore, the reported reference count is:

- `numbers` → 1 reference
- Temporary reference created by `getrefcount()` → 1 reference

**Total reported: 2**

---

### Example 2: Creating Another Reference

Now create another variable that refers to the same object.

```python
import sys

numbers = [1, 2, 3]

print(sys.getrefcount(numbers))

other = numbers

print(sys.getrefcount(numbers))
```

**Output**

```text
2
3
```

Conceptually:

```text
numbers  ----+
             |
other    ----+------> List object [1, 2, 3]

getrefcount() (temporary)
```

The reported reference count is now:

- `numbers` → 1 reference
- `other` → 1 reference
- Temporary reference created by `getrefcount()` → 1 reference

**Total reported: 3**

---

### Example 3: Function Parameters Also Create References

When an object is passed to a function, the function parameter becomes another reference to the same object.

```python
import sys

def display(obj):
    print(sys.getrefcount(obj))

numbers = [1, 2, 3]

display(numbers)
```

**Output**

```text
3
```

During the function call, the references are:

```text
numbers  ----+
             |
obj      ----+------> List object [1, 2, 3]

getrefcount() (temporary)
```

The reported reference count is:

- `numbers` → 1 reference
- `obj` → 1 reference
- Temporary reference created by `getrefcount()` → 1 reference

**Total reported: 3**

These examples demonstrate how Python keeps track of every active reference to an object. When the last reference is removed, the reference count becomes zero, allowing Python to reclaim the object's memory.

---
## <font color='green'>6. Why Isn't Reference Counting Enough?</font>

Reference counting works well in most situations. When the last reference to an object is removed, Python can immediately reclaim the memory occupied by that object.

However, there is one important limitation: **reference cycles**.

A reference cycle occurs when two or more objects refer to each other. Even if your program no longer uses those objects, they continue to reference one another, so their reference counts never reach zero.

Consider the following example.

```python
a = []
b = []

a.append(b)
b.append(a)
```

The objects now reference each other.

```text
+---------+                 +---------+
| List A  | --------------> | List B  |
|         | <-------------- |         |
+---------+                 +---------+
```

Suppose the variables `a` and `b` are removed.

```python
del a
del b
```

Although the variables no longer exist, the two list objects still reference each other.

```text
        +---------+                 +---------+
        | List A  | --------------> | List B  |
        |         | <-------------- |         |
        +---------+                 +---------+
```

Since each object is still being referenced by the other, their reference counts do not become zero. Reference counting alone cannot determine that these objects are no longer useful.

To solve this problem, Python includes a **garbage collector** that periodically searches for unreachable objects involved in reference cycles. Once it determines that no part of the program can access those objects, it safely removes them and reclaims their memory.

In the next section, you'll learn how Python's garbage collector detects and removes these unreachable reference cycles.


---
## <font color='green'>7. Garbage Collection</font>

To handle reference cycles, Python includes a **garbage collector**. Its job is to identify objects that are no longer reachable by your program, even if they still reference one another.

Unlike reference counting, which works continuously, the garbage collector runs **periodically**. During each run, it searches for groups of objects that are no longer accessible from your program and reclaims the memory occupied by those objects.

Python provides the built-in `gc` module for interacting with the garbage collector.

### Example: Forcing Garbage Collection

The following example creates a reference cycle and then explicitly runs the garbage collector.

```python
import gc

a = []
b = []

a.append(b)
b.append(a)

del a
del b

collected = gc.collect()

print(f"Objects collected: {collected}")
```

**Output**

```text
Objects collected: 2
```

The exact number may vary depending on your Python environment and whether other unreachable objects exist.

In this example:

1. Two list objects are created.
2. Each list stores a reference to the other, forming a reference cycle.
3. The variables `a` and `b` are deleted.
4. Although the variables no longer exist, the two lists still reference each other.
5. Calling `gc.collect()` detects that the objects are unreachable and releases their memory.

Conceptually, before garbage collection:

```text
        +---------+                 +---------+
        | List A  | --------------> | List B  |
        |         | <-------------- |         |
        +---------+                 +---------+

(No variables refer to either object.)
```

After garbage collection:

```text
Objects reclaimed

        (memory released)
```

In normal programs, you do **not** need to call `gc.collect()` manually. Python automatically runs the garbage collector when necessary.

The `gc` module is mainly useful for debugging, testing, or investigating memory-related issues.

---
## <font color='green'>8. Best Practices</font>

Python's automatic memory management means that you rarely need to think about allocating or freeing memory. However, following a few best practices can help you write efficient and maintainable programs.

### 1. Let Python Manage Memory

In most cases, you do not need to manually release memory. When an object is no longer referenced, Python automatically reclaims its memory.

```python
numbers = [1, 2, 3]

# Use the list...

numbers = None    # Remove the reference
```

Once there are no remaining references to the list, Python can reclaim the memory.

---

### 2. Be Careful with Shared References

Assigning one variable to another does **not** create a copy.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

**Output**

```text
[1, 2, 3, 4]
```

If you need an independent object, create a copy instead.

---

### 3. Remove References to Large Objects When They Are No Longer Needed

If your program creates large objects that are no longer required, removing the last reference allows Python to reclaim their memory sooner.

```python
large_data = [0] * 1_000_000

# Process the data...

del large_data
```

This is especially useful in long-running applications.

---

### 4. Avoid Unnecessary Global Variables

Global variables remain alive for as long as the program (or module) continues to reference them.

Whenever possible, keep objects local to the functions that use them.

```python
def process():
    data = [1, 2, 3]
    # Work with the data
```

When the function finishes, the local variable is removed, allowing the object to be reclaimed if no other references exist.

---

### 5. Use the `gc` Module for Debugging, Not Routine Programming

The `gc` module is useful for investigating memory-related issues and detecting reference cycles.

```python
import gc

gc.collect()
```

However, manually calling `gc.collect()` is rarely necessary because Python automatically runs the garbage collector when needed.

By understanding how Python manages object references and memory, you can write programs that are both efficient and easier to reason about, without worrying about manually allocating or freeing memory.

---
## <font color='green'>9. Summary</font>

- Python automatically manages memory, so programmers do not need to manually allocate or free memory.
- Variables store **references** to objects, not the objects themselves.
- Objects remain in memory as long as at least one reference points to them.
- Returning an object from a function returns a reference, allowing the object to remain alive after the function exits.
- Python uses **reference counting** to keep track of how many references point to each object.
- In CPython, the `sys.getrefcount()` function can be used to inspect an object's reference count for debugging purposes.
- Reference counting alone cannot reclaim objects involved in **reference cycles**.
- Python's **garbage collector** detects and removes unreachable reference cycles, preventing memory from being permanently occupied.
- In normal programs, Python's automatic memory management is sufficient, and manual garbage collection is rarely required.


---
## **Relevant Links**

[Python Material on this website](index.md)


