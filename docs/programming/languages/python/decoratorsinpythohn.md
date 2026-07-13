---
hide:
  - navigation
  
tags:
  - Decorators
  
---
# Understanding Python Decorators

---
## <font color='green'> 1. Introduction </font>

Decorators are one of Python's most elegant and powerful features.

They allow developers to modify or extend the behavior of functions or methods without changing their original source code. 

Although the `@decorator` syntax often appears intimidating to beginners, decorators are built upon concepts that are fundamental to Python: **functions as first-class objects**, **higher-order functions**, and **closures**.

This writing explains decorators from first principles, gradually building the necessary foundation before introducing decorator syntax and practical applications.


### 1.1 Higher-Order Functions

A **higher-order function** is a function that satisfies **at least one** of the following conditions:

1. It **accepts one or more functions as arguments**, or
2. It **returns a function as its result**.

In other words, a higher-order function either **operates on functions** or **produces functions**.

This concept is possible because **functions are first-class objects** in Python. Since functions can be assigned to variables, passed as arguments, and returned from other functions, they can be manipulated just like any other object.

### Example 1: Accepting a Function as an Argument

```python
def greet():
    print("Hello!")

def execute(func):
    func()

execute(greet)
```

Here, `execute()` is a higher-order function because it accepts another function (`greet`) as its argument.

---

### Example 2: Returning a Function

```python
def outer():

    def inner():
        print("Inside inner")

    return inner

my_function = outer()

my_function()
```

In this example, `outer()` is also a higher-order function because it returns another function (`inner`).


---

## <font color='green'> 2. What Is a Decorator? </font>

**A decorator is simply a function that takes another function as input, adds some additional behavior, and returns a new function.**

In other words, a decorator **wraps** an existing function with extra functionality while leaving the original function unchanged.

Instead of modifying a function directly, decorators create a new version that executes additional code before, after, or even instead of the original function.

Conceptually:

```text
Original Function
        │
        ▼
   Decorator
        │
        ▼
Enhanced Function
```

---

## <font color='green'> 3. Why Do We Need Decorators? </font>

Suppose multiple functions require the same repetitive logic, such as:

- Logging
- Authentication
- Measuring execution time
- Input validation
- Error handling
- Caching

<font color='red'> Without decorators, each function would contain duplicate code.</font>

For example:

```python
def add(a, b):
    print("Starting add")
    result = a + b
    print("Finished add")
    return result

def multiply(a, b):
    print("Starting multiply")
    result = a * b
    print("Finished multiply")
    return result
```

**Notice that both functions repeat the same logging statements.**

Decorators solve this problem by moving the repeated behavior into a reusable wrapper.

---
## <font color='green'>4. The Foundation of Decorators</font>

To understand decorators, we must first understand three important Python concepts.

### 4.1. Functions Are First-Class Objects

In Python, functions are objects.

This means they can be:

- Assigned to variables
- Passed as arguments
- Returned from other functions
- Stored inside collections

Example:

```python
def greet():
    print("Hello")

message = greet

message()
```

The variable `message` now references the same function as `greet`.

---

### 4.2 Functions Can Accept Other Functions

Since functions are objects, they can be passed as arguments.

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

The `execute()` function accepts another function and calls it.

Functions that accept other functions are known as **higher-order functions**.

---

### 4.3 Functions Can Return Other Functions

Functions may also create and return other functions.

```python
def outer():

    def inner():
        print("Inside inner")

    return inner

my_function = outer()

my_function()
```

The returned function can be stored and called later.

This capability is one of the key building blocks of decorators.

---

## <font color='green'> 4. Closures </font>

In addition to higher-order functions, closures are another key concept related to decorators. A closure allows a function to remember variables from its enclosing scope, which is one of the mechanisms that makes decorators possible.

Consider the following example:

```python
def outer(name):

    def inner():
        print(f"Hello {name}")

    return inner

greet_john = outer("John")

greet_john()
```

The inner function remembers the value of `name` from the scope of the `outer` function which encompasses `inner`

This behavior is called a **closure**.

> A closure is a function that retains access to variables from its enclosing scope even after that scope has finished executing.

Decorators rely heavily on closures because the wrapper function needs to remember the original function it is wrapping.

---

## <font color='green'> 5. Building a Simple Decorator </font>

Let's create our first decorator.

```python
def logger(func):

    def wrapper():
        print("Starting function")

        func()

        print("Function completed")

    return wrapper
```

Now define a simple function.

```python
def greet():
    print("Hello")
```

Decorate it manually.

```python
greet = logger(greet)

greet()
```

Output:

```text
Starting function
Hello
Function completed
```

Notice that the original `greet()` function remains unchanged.

Instead, it has been replaced by the wrapper returned by the decorator.

---

### 5.1 Understanding the Wrapper Function

The wrapper acts as an intermediary between the caller and the original function.

```text
Caller
   │
   ▼
Wrapper
   │
   ▼
Original Function
```

The wrapper can execute code:

- Before the function
- After the function
- Around the function
- Or even prevent the function from executing

This flexibility makes decorators extremely useful.

---

## <font color='green'> 6. The `@` Syntax </font>

Instead of manually writing

```python
greet = logger(greet)
```

Python provides cleaner syntax.

```python
@logger
def greet():
    print("Hello")
```

Python automatically translates this into

```python
def greet():
    print("Hello")

greet = logger(greet)
```

> The `@` symbol is simply syntactic sugar. No special magic occurs behind the scenes.

---

## <font color='green'>7. Handling Function Arguments</font>

Our first decorator only worked for functions that **did not accept any parameters**.

Consider the following function:

```python
def add(a, b):
    return a + b
```

If we tried to decorate this function using our previous `logger` decorator, Python would raise a `TypeError` because the wrapper was defined without any parameters.

A decorator should be flexible enough to wrap **any function**, regardless of the number or type of arguments it accepts.

The standard solution is to use `*args` and `**kwargs`.

- `*args` collects all positional arguments into a tuple.
- `**kwargs` collects all keyword arguments into a dictionary.

By forwarding these arguments to the original function, the decorator becomes generic.

```python
def logger(func):

    def wrapper(*args, **kwargs):

        print("Starting function")

        result = func(*args, **kwargs)

        print("Finished function")

        return result

    return wrapper
```

Now we can decorate any function.

```python
@logger
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

**Output**

```text
Starting function
Finished function
30
```

Let's see another example with keyword arguments.

```python
@logger
def introduce(name, age=25):
    print(f"My name is {name} and I am {age} years old.")

introduce(name="Alice", age=30)
```

**Output**

```text
Starting function
My name is Alice and I am 30 years old.
Finished function
```

Because the wrapper uses `*args` and `**kwargs`, it doesn't need to know anything about the function it is wrapping. It simply forwards all received arguments to the original function.

This makes the decorator reusable for functions with:

- No arguments
- One argument
- Multiple positional arguments
- Keyword arguments
- Default parameter values
- A combination of positional and keyword arguments

This is why nearly all production-quality decorators define their wrapper as:

```python
def wrapper(*args, **kwargs):
    ...
```

It is the most flexible approach and allows a single decorator to work with virtually any function signature.

---

## <font color='green'> 8. Returning Values </font>

A common beginner mistake is forgetting to return the original function's result.

Incorrect:

```python
def wrapper(*args, **kwargs):
    func(*args, **kwargs)
```

Correct:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```

Without returning the result, every decorated function returns `None`.

---

## <font color='green'> 9. Decorators with Arguments </font>

Sometimes decorators themselves need configuration.

Example:

```python
@repeat(3)
def greet():
    print("Hello")
```

This requires an additional layer of nesting.

```python
def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

Execution order becomes:

```text
repeat(3)
      │
      ▼
 decorator
      │
      ▼
 wrapper
      │
      ▼
 original function
```

### 9.1  Why Do Parameterized Decorators Need an Extra Layer?

A common question when learning decorators is:

> **Why do we need an extra `decorator()` function? Why can't we simply pass `times` as a parameter to `wrapper()`?**

For example, why is the decorator written like this?

```python
def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

Instead of something like:

```python
def repeat(func):

    def wrapper(times, *args, **kwargs):

        for _ in range(times):
            func(*args, **kwargs)

    return wrapper
```

The answer lies in **when decorators are executed**.

---

### 9.2 Understanding Normal Decorators

Consider a simple decorator:

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Finished")
        return result

    return wrapper
```

When we write:

```python
@logger
def greet():
    print("Hello")
```

Python automatically translates it into:

```python
def greet():
    print("Hello")

greet = logger(greet)
```

Notice that `logger()` receives exactly **one argument** (the function being decorated)

```text
logger(greet)
```

This is why its signature is:

```python
def logger(func):
```

---

### 9.3 What Happens with `@repeat(3)`?

Now consider a decorator that accepts a parameter:

```python
@repeat(3)
def greet():
    print("Hello")
```

Python translates this into:

```python
greet = repeat(3)(greet)
```

This is very different.

There are **two function calls** happening:

```text
repeat(3)
        │
        ▼
returns decorator

decorator(greet)
        │
        ▼
returns wrapper
```

Because there are **two function calls**, we need **two outer functions** before we reach the wrapper.

---

### 9.4 Why Can't `wrapper()` Accept `times`?

Suppose we write:

```python
def repeat(func):

    def wrapper(times, *args, **kwargs):

        for _ in range(times):
            func(*args, **kwargs)

    return wrapper
```

Now decorate a function:

```python
@repeat
def greet():
    print("Hello")
```

When we call:

```python
greet()
```

Python actually executes:

```python
wrapper()
```

However, `wrapper()` expects:

```python
wrapper(times, *args, **kwargs)
```

Where is Python supposed to get the value of `times`?

It has no value to pass.

Python raises:

```text
TypeError:
wrapper() missing 1 required positional argument: 'times'
```

---

### 9.5 What If We Call `greet(3)`?

Suppose we try:

```python
greet(3)
```

Now `3` becomes an argument to the **decorated function**, not to the decorator.

In other words:

```text
Decorator Configuration
        ≠
Function Arguments
```

These are completely different things.

The decorator should be configured **once**, while the function may be called **many times**.

---

### 9.6 Understanding the Two Phases

A parameterized decorator works in two completely different phases.

**Phase 1 — Decoration Time:**

This happens only once, when Python loads the file.

```python
@repeat(3)
```

becomes

```python
repeat(3)
```

which creates a decorator that permanently remembers:

```text
times = 3
```

---
**Phase 2 — Runtime:**

Every time the function is called:

```python
greet()
```

Python executes:

```python
wrapper()
```

Notice that `wrapper()` never receives `times`.

Instead, it already **remembers** `times` because of the closure created by the outer function.

---

### 9.6 Why the Extra Layer?

For a normal decorator:

```text
logger
      │
      ▼
 function
      │
      ▼
 wrapper
```

For a parameterized decorator:

```text
repeat(3)
        │
        ▼
 decorator
        │
        ▼
 function
        │
        ▼
 wrapper
```

The extra layer exists because the decorator itself must first be **configured** before it can receive the function.

---

### 9.7 A Helpful Mental Model

Think of `repeat(3)` as a **decorator factory**.

Its only job is to create a customized decorator.

```python
repeat(3)
```

returns:

```python
decorator
```

That decorator permanently remembers:

```text
times = 3
```

Later, Python executes:

```python
decorator(greet)
```

which creates the wrapper.

Finally, every function call executes:

```python
greet()
```

which actually runs:

```python
wrapper()
```

Since `wrapper()` is a **closure**, it already has access to `times`.

---

### 9.8 Complete Execution Flow

```text
repeat(3)
      │
      ▼
creates decorator
      │
      ▼
decorator(greet)
      │
      ▼
creates wrapper
      │
      ▼
greet()
      │
      ▼
wrapper()
```

Notice that `times` is captured during the **first step** and is available to `wrapper()` without needing to be passed as an argument.

---

### 9.8 Key Takeaway

A parameterized decorator requires an extra function because there are **two separate operations**:

1. Configure the decorator (e.g., `repeat(3)`).
2. Apply the configured decorator to a function (e.g., `decorator(greet)`).

The wrapper is only responsible for executing the decorated function. It is **not** responsible for receiving configuration values such as `times`.

This is why parameterized decorators always follow the three-layer structure:

```python
def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            ...

        return wrapper

    return decorator
```

Once we remember that:

```python
@repeat(3)
def greet():
    ...
```

is equivalent to:

```python
greet = repeat(3)(greet)
```

the need for the extra layer becomes much easier to understand.


---

## <font color='green'> 10. Preserving Function Metadata </font>

When a function is decorated, Python replaces the original function with the wrapper.

As a result:

```python
print(greet.__name__)
```

may output

```text
wrapper
```

instead of

```text
greet
```

To preserve the original function's metadata, Python provides `functools.wraps`.

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Running")

        return func(*args, **kwargs)

    return wrapper
```

Using `@wraps` preserves the function name, documentation string, annotations, and other metadata.

Professional decorators should almost always use `@wraps`.

---

## <font color='green'> 11. Multiple Decorators </font>

A function may have more than one decorator.

```python
@timer
@logger
def calculate():
    pass
```

This is equivalent to

```python
calculate = timer(logger(calculate))
```

Decorators are applied from the bottom upward.

Execution order:

```text
Caller
   │
   ▼
Timer
   │
   ▼
Logger
   │
   ▼
Original Function
```

Understanding this order is important when combining decorators.

---

## <font color='green'> 12. Built-in Decorators </font>

Python provides several decorators in its standard library.

## `@staticmethod`

Defines a method that does not receive the instance (`self`) or class (`cls`).

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

---

## `@classmethod`

Receives the class itself as the first argument.

```python
class Employee:

    count = 0

    @classmethod
    def total(cls):
        return cls.count
```

---

## `@property`

Allows methods to behave like attributes.

```python
class Circle:

    @property
    def area(self):
        return 3.14 * self.radius ** 2
```

Instead of writing

```python
circle.area()
```

we simply write

```python
circle.area
```

This produces cleaner and more intuitive interfaces.

---

## <font color='gree'> 13. Real-World Uses of Decorators </font>

Decorators are heavily used in professional Python development.

Common applications include:

- Logging function execution
- Measuring execution time
- Caching expensive computations
- Authentication and authorization
- Input validation
- Retry mechanisms
- Rate limiting
- Transaction management
- API routing in web frameworks
- Unit testing

Many popular frameworks, including Flask, Django, and FastAPI, rely extensively on decorators to define routes, middleware, permissions, and application behavior.

---

##  <font color='green'> 13. Common Mistakes </font>

Beginners frequently encounter the following issues:

- Forgetting to return the wrapper function.
- Forgetting to return the original function's result.
- Not using `*args` and `**kwargs`.
- Omitting `functools.wraps`, causing metadata loss.
- Believing that the `@` syntax introduces new language behavior when it is merely shorthand for reassignment.

Understanding these pitfalls helps avoid subtle bugs.

---

##  <font color='green'> 14. Best Practices </font>

When writing decorators:

- Keep decorators focused on a single responsibility.
- Always use `functools.wraps`.
- Support arbitrary arguments using `*args` and `**kwargs`.
- Return the wrapped function's result.
- Avoid placing unrelated business logic inside decorators.
- Use descriptive names that clearly indicate the decorator's purpose.

---

##  <font color='green'> Summary </font>

Decorators are a design pattern implemented using Python's support for higher-order functions and closures. They provide a clean and reusable mechanism for extending function behavior without modifying existing code.

At their core, decorators simply take a function, wrap it with additional functionality, and return a new function. The `@decorator` syntax is merely a convenient shorthand for replacing a function with its decorated version.

Although decorators initially appear complex, they become intuitive once the underlying concepts—first-class functions, higher-order functions, closures, and function wrapping—are understood.

Mastering decorators is an important milestone in becoming a proficient Python developer, as they are widely used throughout the Python ecosystem and form the foundation of many modern libraries and frameworks.
