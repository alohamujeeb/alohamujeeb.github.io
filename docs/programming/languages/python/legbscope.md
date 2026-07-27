---
hide:
  - navigation
  
tags:
  - Python Namespaces
  
---

# Python LEGB Rule

Learn how Python searches for variables using the LEGB rule and understand why local, enclosing, global, and built-in names behave the way they do.


---
## <font color='green'>1. The LEGB Rule</font>

When Python encounters a variable name, it searches for it in the following order:

| Letter | Search Location |
|--------|-----------------|
| **L** | Local |
| **E** | Enclosing |
| **G** | Global |
| **B** | Built-in |

As soon as Python finds the variable, it stops searching.

Let's look at each level.

### Local (L)

Python first looks inside the current function.

```python
x = 10

def func():
    x = 20
    print(x)

func()
```

Output

```text
20
```

Python finds `x` inside `func()`, so it never looks anywhere else.

---

### Enclosing (E)

If the current function doesn't have the variable, Python looks in the enclosing function.

```python
x = 10

def outer():
    x = 20

    def inner():
        print(x)

    inner()

outer()
```

Output

```text
20
```

`inner()` doesn't have an `x`, so Python searches the enclosing function `outer()` and finds `20`.

---

### Global (G)

If neither the current nor enclosing function contains the variable, Python searches the global scope.

```python
x = 10

def func():
    print(x)

func()
```

Output

```text
10
```

Since `func()` doesn't define `x`, Python finds it in the global scope.

---

### Built-in (B)

If Python still can't find the name, it searches Python's built-in names.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output

```text
3
```

Neither your program nor your function defines `len`, so Python finds the built-in `len()` function.

---

### What Happens If Python Doesn't Find the Name?

```python
def func():
    print(x)

func()
```

Output

```text
NameError: name 'x' is not defined
```

Python searched every level in the LEGB order:

```
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
   ↓
NameError
```

Since `x` wasn't found anywhere, Python raised a `NameError`.

---
## <font color='green'>2. Variable Scope</font>

A variable is only accessible within the scope in which it is defined.

For example:

```python
x = 10          # Global variable

def func():
    y = 20      # Local variable
    print(x)
    print(y)

func()
```

Output

```text
10
20
```

The global variable `x` can be accessed inside the function because Python finds it during the **Global** step of the LEGB rule.

The local variable `y` is only accessible inside `func()`.

Trying to access `y` outside the function results in an error.

```python
x = 10

def func():
    y = 20

func()

print(y)
```

Output

```text
NameError: name 'y' is not defined
```

The variable `y` was created inside `func()`, so it exists only while that function is executing.

Once the function returns, `y` is no longer accessible.

The following table summarizes the difference.

| Variable | Defined In | Accessible From |
|----------|------------|-----------------|
| Global | Module | Anywhere in the module |
| Local | Function | Only inside that function |


---
## <font color='green'>3. Variable Shadowing</font>

A local variable can have the same name as a global variable.

When this happens, the local variable **shadows** (hides) the global variable while the function is executing.

```python
x = 10

def func():
    x = 20
    print("Inside function:", x)

func()

print("Outside function:", x)
```

Output

```text
Inside function: 20
Outside function: 10
```

Although both variables are named `x`, they are different variables.

When `print(x)` is executed inside `func()`, Python follows the LEGB rule:

```
Looking for x

✓ Local?      Yes (20)

Search stops.
```

Python never reaches the global `x` because it already found a matching name in the local scope.

After `func()` returns, the local variable no longer exists.

When `print(x)` executes outside the function, Python searches again:

```
Looking for x

✓ Global?     Yes (10)

Search stops.
```

The global variable was never modified.

### Another Example

```python
message = "Welcome"

def display():
    message = "Hello"
    print(message)

display()
print(message)
```

Output

```text
Hello
Welcome
```

The local variable `message` hides the global variable with the same name. This behavior is called **variable shadowing**.

> **Tip:** Avoid using the same variable name in different scopes unless you have a good reason. Using descriptive variable names makes your code easier to understand.

---
## <font color='green'>4. The `global` Keyword</font>

By default, assigning a value to a variable inside a function creates a **local** variable.

```python
count = 0

def increment():
    count = count + 1

increment()
```

Output

```text
UnboundLocalError: local variable 'count' referenced before assignment
```

Why did this happen?

When Python sees the assignment

```python
count = count + 1
```

it assumes `count` is a **local** variable.

However, the local variable doesn't have a value yet, so Python raises an error.

To modify the global variable instead, use the `global` keyword.

```python
count = 0

def increment():
    global count
    count = count + 1

increment()

print(count)
```

Output

```text
1
```

The statement

```python
global count
```

tells Python that `count` refers to the global variable instead of creating a new local one.

Without `global`, Python creates a new local variable whenever you assign a value inside a function.

### When Should You Use `global`?

Although `global` is sometimes necessary, it should be used sparingly.

Functions that modify global variables are often harder to understand, test, and reuse.

Whenever possible, prefer passing values as function arguments and returning the updated result instead.

```python
def increment(count):
    return count + 1

count = 0
count = increment(count)

print(count)
```

Output

```text
1
```

This approach avoids modifying global state and makes the function more predictable.


---
## <font color='green'>5. The `nonlocal` Keyword</font>

The `global` keyword lets you modify a global variable.

But what if you want to modify a variable in an **enclosing function** instead?

Consider the following example.

```python
def outer():
    count = 0

    def increment():
        count = count + 1
        print(count)

    increment()

outer()
```

Output

```text
UnboundLocalError: local variable 'count' referenced before assignment
```

Although `count` exists in `outer()`, Python treats

```python
count = count + 1
```

as creating a new local variable inside `increment()`.

Since the local variable doesn't have a value yet, Python raises an error.

To tell Python that you want to use the variable from the enclosing function, use the `nonlocal` keyword.

```python
def outer():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

outer()
```

Output

```text
1
```

The statement

```python
nonlocal count
```

tells Python to use the variable from the nearest enclosing function instead of creating a new local variable.

### Another Example

```python
def outer():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Hi"

    inner()
    print(message)

outer()
```

Output

```text
Hi
```

Without `nonlocal`, assigning a value to `message` inside `inner()` would create a new local variable, leaving the variable in `outer()` unchanged.

> **Note:** The `nonlocal` keyword only works with variables defined in an enclosing function. It cannot be used to access global variables. For global variables, use the `global` keyword instead.



---
## <font color='green'>6. `global` vs `nonlocal`</font>

Both `global` and `nonlocal` allow you to modify variables that are defined outside the current function. The difference is **where Python looks for the variable**.

| Keyword | Refers To | Used In |
|---------|-----------|---------|
| `global` | A variable in the global scope | Any function |
| `nonlocal` | A variable in the nearest enclosing function | Nested functions |

### Using `global`

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output

```text
1
```

Here, `count` belongs to the global scope, so the `global` keyword tells Python to modify that variable.

---

### Using `nonlocal`

```python
def outer():
    count = 0

    def increment():
        nonlocal count
        count += 1

    increment()
    print(count)

outer()
```

Output

```text
1
```

Here, `count` belongs to the enclosing function `outer()`, so the `nonlocal` keyword tells Python to modify that variable.

---

### Comparison

The following diagram shows which variable each keyword refers to.

```
Global Scope
┌───────────────────────────────┐
│ count = 0                     │
│                               │
│ outer()                       │
│ ┌───────────────────────────┐ │
│ │ count = 10                │ │
│ │                           │ │
│ │ inner()                   │ │
│ │ ┌───────────────────────┐ │ │
│ │ │                       │ │ │
│ │ └───────────────────────┘ │ │
│ └───────────────────────────┘ │
└───────────────────────────────┘

global count
      │
      └────────────► Global count (0)

nonlocal count
      │
      └────────────► Enclosing count (10)
```

### Which One Should You Use?

- Use **`global`** when you need to modify a variable defined in the global scope.
- Use **`nonlocal`** when you need to modify a variable defined in the nearest enclosing function.
- If you only need to read a variable, **neither keyword is required**. Python automatically follows the LEGB rule to find it.


---
## <font color='green'>7. Common Pitfalls</font>

Understanding the LEGB rule helps explain many common programming mistakes.

### Pitfall 1: Shadowing Built-in Functions

Python searches the global scope before the built-in scope.

```python
print = "Hello"

print("Python")
```

Output

```text
TypeError: 'str' object is not callable
```

The global variable `print` hides Python's built-in `print()` function.

The same problem can occur with other built-in names such as `len`, `list`, `dict`, and `str`.

```python
list = [1, 2, 3]

numbers = list((4, 5, 6))
```

Output

```text
TypeError: 'list' object is not callable
```

Avoid using built-in names for your own variables.

---

### Pitfall 2: Assuming a Function Modifies a Global Variable

```python
count = 0

def increment():
    count = 1

increment()

print(count)
```

Output

```text
0
```

The assignment creates a new local variable. The global variable remains unchanged.

Use the `global` keyword if you intentionally want to modify the global variable.

---

### Pitfall 3: Accessing a Local Variable Outside Its Scope

```python
def greet():
    message = "Hello"

greet()

print(message)
```

Output

```text
NameError: name 'message' is not defined
```

The variable `message` exists only while `greet()` is executing.

---

### Pitfall 4: Expecting an Enclosing Variable to Change Automatically

```python
def outer():
    count = 0

    def inner():
        count = 1

    inner()
    print(count)

outer()
```

Output

```text
0
```

The assignment inside `inner()` creates a new local variable.

Use `nonlocal` if you want to modify the variable in the enclosing function.

---

Most name-related errors in Python can be explained by remembering one simple rule:

> **Python always follows the LEGB search order when resolving names.**



---
## <font color='green'>8. Best Practices</font>

Following a few simple practices can help you avoid many name-related bugs.

### Use Descriptive Variable Names

Choose meaningful variable names to reduce the chance of accidentally shadowing variables from other scopes.

```python
# Good
student_count = 25

# Avoid
count = 25
```

---

### Avoid Global Variables

Global variables can be modified from anywhere in the program, making code harder to understand and maintain.

Instead of modifying global variables, pass values as function arguments and return the result.

```python
def increment(count):
    return count + 1

count = 0
count = increment(count)
```

---

### Don't Shadow Built-in Names

Avoid using built-in function names such as `print`, `list`, `dict`, `str`, `int`, or `len` as variable names.

```python
# Avoid
list = [1, 2, 3]

# Better
numbers = [1, 2, 3]
```

---

### Keep Variables in the Smallest Possible Scope

Declare variables only where they are needed.

Keeping variables local makes your code easier to read, test, and maintain.

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total
```

---

### Use `global` and `nonlocal` Sparingly

Although `global` and `nonlocal` are useful in certain situations, overusing them can make code difficult to follow.

Whenever possible, prefer passing values between functions using parameters and return values.

---

By following these practices, your code will be easier to understand, less prone to bugs, and simpler to maintain.



---
## <font color='green'>9. Summary</font>

In this article, you learned how Python resolves names using the **LEGB rule**.

- **L (Local):** Python first searches the current function.
- **E (Enclosing):** If the name isn't found, Python searches the nearest enclosing function.
- **G (Global):** Next, Python searches the current module.
- **B (Built-in):** Finally, Python searches Python's built-in names.

As soon as Python finds the name, the search stops.

You also learned that:

- **Scope** determines where a name can be accessed.
- A local variable can **shadow** a variable with the same name in an outer scope.
- Use the **`global`** keyword to modify a variable in the global scope.
- Use the **`nonlocal`** keyword to modify a variable in the nearest enclosing function.
- Avoid shadowing built-in names such as `print`, `list`, and `len`.

Understanding the LEGB rule makes it easier to explain common errors such as `NameError` and `UnboundLocalError`, and helps you predict how Python resolves names in different scopes.



---
## **Relevant Links**

[Python Material on this website](index.md)

