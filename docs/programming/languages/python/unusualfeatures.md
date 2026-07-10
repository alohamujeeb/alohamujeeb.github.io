---
tags:
  - Python Data Types
---
# Python Features That May Be Unfamiliar to C/Java Programmers
(Quick reference)

Python was designed with simplicity and readability in mind. As a result, it differs from traditional programming languages such as C, C++, Java, and JavaScript in several ways. This section highlights some of the most notable differences.

---
## <font color='green'>1. No Traditional `switch` Statement</font>

Older versions of Python do not have a `switch` statement. Instead, they use `if-elif-else`.

```python
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Unknown")
```

Starting with **Python 3.10**, Python introduced `match-case`, which provides functionality similar to a switch statement while supporting more advanced pattern matching.

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Unknown")
```

---
## <font color='green'>2. No Curly Braces</font>

Most programming languages use curly braces (`{}`) to define code blocks. Python uses **indentation** instead.

### C / Java

```c
if (x > 0) {
    printf("Positive");
}
```

### Python

```python
if x > 0:
    print("Positive")
```

Consistent indentation is mandatory in Python.

---

## <font color='green'>3. No Semicolons</font>

Statements do not require semicolons.

```python
x = 5
y = 10
print(x + y)
```

Although semicolons are allowed, they are rarely used.

---

## <font color='green'>4. Dynamic Typing</font>

Variables do not require explicit type declarations.

### C

```c
int age = 20;
float price = 9.99;
```

### Python

```python
age = 20
price = 9.99
```

Python automatically determines the data type at runtime.

---

## <font color='green'>5. Everything Is an Object</font>

In Python, nearly everything is an object, including integers, strings, functions, and classes.

```python
x = 5
print(type(x))
```

Output:

```text
<class 'int'>
```

---

## <font color='green'>6. No `++` or `--` Operators</font>

Python does not support increment or decrement operators.

### C

```c
i++;
++i;
i--;
```

### Python

```python
i += 1
i -= 1
```

---

## <font color='green'>7. No `do...while` Loop</font>

Python does not include a `do...while` loop.

### C

```c
do {
    printf("Hello");
} while (x < 5);
```

### Python Equivalent

```python
while True:
    print("Hello")

    if x >= 5:
        break
```

---

## <font color='green'>8. Different `for` Loop</font>

Traditional languages typically use a counter-controlled loop.

### C

```c
for (int i = 0; i < 5; i++)
```

### Python

```python
for i in range(5):
    print(i)
```

The expression `range(5)` generates:

```text
0 1 2 3 4
```

---

## <font color='green'>9. Lists Instead of Arrays</font>

Python's built-in collection is the **list**, which is dynamic and flexible.

```python
numbers = [1, 2, 3]
numbers.append(4)
```

Lists can also contain different data types.

```python
items = [1, "hello", 3.14, True]
```

---

## <font color='green'>10. Multiple Assignment</font>

Python allows multiple variables to be assigned in one statement.

```python
a, b = 5, 10
```

Variables can also be swapped without using a temporary variable.

```python
a, b = b, a
```

---

## <font color='green'>11. Easy Iteration</font>

Instead of looping through indexes, Python usually iterates directly over elements.

Instead of:

```python
for i in range(len(names)):
    print(names[i])
```

Use:

```python
for name in names:
    print(name)
```

If both the index and value are needed:

```python
for index, name in enumerate(names):
    print(index, name)
```

---

## <font color='green'>12. List Comprehensions</font>

Python provides concise syntax for creating lists.

Traditional approach:

```python
squares = []

for x in range(10):
    squares.append(x * x)
```

Using a list comprehension:

```python
squares = [x * x for x in range(10)]
```

---

## <font color='green'>13. Functions Can Return Multiple Values</font>

A function can return more than one value.

```python
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(10, 3)
```

---

## <font color='green'>14. No Mandatory `main()` Function</font>

Python programs execute from top to bottom.

```python
print("Hello")
print("World")
```

For larger programs, the following convention is commonly used:

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```

This is optional but considered good practice.

---

## <font color='green'>15. Rich Built-in Data Structures</font>

Python includes several powerful built-in data structures.

```python
# List
numbers = [1, 2, 3]

# Tuple (immutable)
point = (2, 5)

# Set
unique = {1, 2, 3}

# Dictionary
student = {
    "name": "Alice",
    "age": 20
}
```


---

## <font color='green'>16. Functions Are First-Class Objects</font>

Functions can be assigned to variables and passed as arguments.

```python
def greet():
    print("Hello")

f = greet
f()
```

This enables powerful programming techniques such as callbacks and higher-order functions.


