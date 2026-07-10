---
tags:
  - function as parameter
---
# **Function As Parameter to a Function**

---

## <font color='green'> 1. Function as a Parameter to Another Function </font>

Passing a function as a parameter is a powerful programming technique that allows you to make your code more flexible and reusable. Instead of hardcoding behavior inside a function, we can pass another function that defines what should happen.

### Why Use It?

- Reuse the same logic with different behaviors.
- Reduce duplicate code.
- Make programs easier to extend and maintain.
- Commonly used in callbacks, event handling, sorting, filtering, and functional programming.

### Basic Syntax

```text
functionA(functionB)
```

Where:
```
- `functionA` is the function that accepts another function.
- `functionB` is the function passed as an argument.
```
---
## <font color='green'>2. Example in Python </font>

```python
def greet(name):
    return f"Hello, {name}!"

def execute(func, value):
    print(func(value))

execute(greet, "Alice")
```

**Output**

```text
Hello, Alice!
```

In this example:
- `execute()` accepts a function (`func`) as its first parameter.
- It calls that function using `func(value)`.

---

## <font color='green'> 3. Passing an Anonymous Function </font>

Instead of defining a separate function, you can pass one directly.


```python
execute(lambda name: f"Hi, {name}!", "Bob")
```


---
## <font color='green'> 4. Real-World Example </font>

Imagine a calculator that performs different operations.


```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 5, 3))        # 8
print(calculate(multiply, 5, 3))   # 15
```

Instead of writing separate calculation functions, `calculate()` can perform any operation that is passed to it.


---
## <font color='green'> 5. Common Use Cases </font>

- Filtering collections.
- Event handlers (button clicks, keyboard input).
- Callbacks for asynchronous operations.
- Data processing pipelines.

---
## <font color='green'> Key Points to Remember </font>

- Functions are **first-class objects** in many programming languages, meaning they can be:
  - Assigned to variables.
  - Passed as arguments.
  - Returned from other functions.
- Passing a function **does not execute it**. You pass its name (or a function reference), and it is executed later by the receiving function.
- This approach promotes reusable, modular, and flexible code.


