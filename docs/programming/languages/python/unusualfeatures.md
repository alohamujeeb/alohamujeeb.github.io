---
tags:
  - Python Data Types
---
# Python Features That May Be Unfamiliar to C/Java Programmers
(Quick reference)

Python was designed with simplicity and readability in mind. As a result, it differs from traditional programming languages such as C, C++, Java, and JavaScript in several ways. This section highlights some of the most notable differences.

---
## 1. No Traditional `switch` Statement

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

## 2. No Curly Braces

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

## 3. No Semicolons

Statements do not require semicolons.

```python
x = 5
y = 10
print(x + y)
```

Although semicolons are allowed, they are rarely used.

---

## 4. Dynamic Typing

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

## 5. Everything Is an Object

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

## 6. No `++` or `--` Operators

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

## 7. No `do...while` Loop

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

## 8. Different `for` Loop

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

## 9. Lists Instead of Arrays

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

## 10. Multiple Assignment

Python allows multiple variables to be assigned in one statement.

```python
a, b = 5, 10
```

Variables can also be swapped without using a temporary variable.

```python
a, b = b, a
```

---

## 11. Easy Iteration

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

## 12. List Comprehensions

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

## 13. Functions Can Return Multiple Values

A function can return more than one value.

```python
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(10, 3)
```

---

## 14. No Mandatory `main()` Function

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

## 15. Rich Built-in Data Structures

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

## 16. Exception Handling

Python uses exceptions to handle errors.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

This separates normal program logic from error-handling logic.

---

## 17. Functions Are First-Class Objects

Functions can be assigned to variables and passed as arguments.

```python
def greet():
    print("Hello")

f = greet
f()
```

This enables powerful programming techniques such as callbacks and higher-order functions.

---

# Summary

| Feature | Traditional Languages (C/Java) | Python |
|----------|-------------------------------|--------|
| Code blocks | Curly braces `{}` | Indentation |
| Statement terminator | Semicolon (`;`) | Not required |
| Variable declaration | Explicit types | Dynamic typing |
| `switch` statement | Yes | `match-case` (Python 3.10+) or `if-elif` |
| Increment/Decrement | `++`, `--` | `+= 1`, `-= 1` |
| `do...while` loop | Yes | No |
| Arrays | Fixed-size arrays | Dynamic lists |
| `for` loops | Counter-based | Iterator-based |
| Multiple assignment | Limited | Supported |
| Memory management | Manual (C) or automatic (Java) | Automatic |
| `main()` function | Required | Optional |
| Functions | Procedures/functions | First-class objects |

---

## Key Takeaways

- Python emphasizes **readability** over complex syntax.
- Indentation replaces curly braces.
- Dynamic typing reduces boilerplate code.
- Built-in data structures simplify programming.
- Python encourages writing concise, expressive, and maintainable code.
- Many common tasks require significantly fewer lines of code than in traditional programming languages.
