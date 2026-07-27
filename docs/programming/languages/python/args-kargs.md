---
hide:
  - navigation
  
tags:
  - args
  - kwargs
  - variable parameters
---

# Understanding `*args` and `**kwargs` in Python

Python provides several ways to pass arguments to functions. As your programs become more complex, you'll encounter situations where the number of arguments is unknown or where passing arguments by position becomes inconvenient.

This article introduces the four common ways of passing arguments to Python functions:

1. Fixed positional arguments
2. Fixed keyword arguments
3. Variable positional arguments (`*args`)
4. Variable keyword arguments (`**kwargs`)

---

## <font color='green'>1. Method 1 – Fixed Positional Arguments</font>

Every Python programmer starts by writing functions that accept a fixed number of positional arguments.

For example, suppose we want to multiply two numbers.

```python
def multiply(x, y):
    return x * y
```

We call the function by supplying exactly two arguments.

```python
result = multiply(4, 5)
print(result)
```

Output

```text
20
```

Here, Python maps the arguments based on their **position**.

| Parameter | Value |
|-----------|------:|
| x | 4 |
| y | 5 |

The first argument (`4`) is assigned to `x`, and the second argument (`5`) is assigned to `y`.

This works perfectly because the function expects **exactly two arguments**.

---

## <font color='green'>2. Method 2 – Fixed Keyword Arguments</font>

Instead of relying on the position of arguments, Python also allows arguments to be passed using their **parameter names**.

For example,

```python
multiply(x=4, y=5)
```

produces the same result as

```python
multiply(4, 5)
```

One advantage of keyword arguments is that **the order no longer matters**.

For example,

```python
multiply(y=5, x=4)
```

still produces

```text
20
```

Python matches the values using the parameter names.

Conceptually,

```text
x = 4
y = 5
```

instead of

```text
1st argument → x
2nd argument → y
```

Keyword arguments make code easier to read and reduce mistakes caused by incorrect ordering.

However, there is still one limitation.

The function still expects a **fixed number of parameters**.

If we define

```python
def multiply(x, y):
    return x * y
```

we must always supply values for `x` and `y`.

What if we don't know beforehand how many arguments will be passed?

---

## <font color='green'>3. Method 3 – Variable Positional Arguments (`*args`)</font>

Suppose we want to write a function that adds numbers.

If we define

```python
def add(a, b):
    return a + b
```

it works only for two numbers.

```python
add(10, 20)
```

But what if tomorrow we need to add three numbers?

```python
add(10, 20, 30)
```

Python raises an error because the function accepts only two parameters.

We could rewrite it.

```python
def add(a, b, c):
    return a + b + c
```

But then someone wants to add four numbers.

```python
add(10, 20, 30, 40)
```

Again, the function must be rewritten.

Eventually we realize the real problem.

> We don't know beforehand how many positional arguments the caller will provide.

Python solves this using `*args`.

```python
def add(*numbers):
    print(numbers)
```

Now we can call the function with any number of positional arguments.

```python
add(5)
```

Output

```text
(5,)
```

```python
add(5, 10)
```

Output

```text
(5, 10)
```

```python
add(5, 10, 15, 20, 25)
```

Output

```text
(5, 10, 15, 20, 25)
```

Instead of expecting a fixed number of arguments, Python automatically **packs all positional arguments into a tuple**.

Conceptually,

```text
5
10
15
20

      │
      ▼

Python packs them into

      │
      ▼

(5, 10, 15, 20)
```

**The tuple is created automatically by Python.**

---

## <font color='green'>4. Method 4 – Variable Keyword Arguments (`**kwargs`)</font>

`*args` solves the problem of an unknown number of **positional arguments**.

Now consider another situation.

Suppose we're writing a function to create a student record.

Different students may provide different information.

One student may supply

```python
name="Alice"
```

Another may supply

```python
name="Alice"
age=20
```

Another may supply

```python
name="Alice"
age=20
city="Singapore"
phone="12345678"
email="alice@example.com"
```

Notice that the problem is no longer the **number** of arguments.

Instead, we don't know **which keyword arguments** the caller will provide.

Python solves this using `**kwargs`.

```python
def create_student(**details):
    print(details)
```

Now every keyword argument is automatically collected into a dictionary.

```python
create_student(
    name="Alice",
    age=20,
    city="Singapore"
)
```

Output

```python
{
    'name': 'Alice',
    'age': 20,
    'city': 'Singapore'
}
```

Conceptually,

```text
name = Alice
age = 20
city = Singapore

        │
        ▼

Python packs them into

        │
        ▼

{
    'name': 'Alice',
    'age': 20,
    'city': 'Singapore'
}
```

### Why a Dictionary?

Keyword arguments consist of **name-value pairs**.

For example,

```text
name  → Alice
age   → 20
city  → Singapore
```

A dictionary is designed to store key-value pairs, making it the natural choice for `**kwargs`.

---

## <font color='green'>5. Comparison of the Four Methods</font>

| Method | Example | Fixed Number? | Stored As |
|---------|---------|---------------|-----------|
| Fixed positional | `multiply(4, 5)` | ✅ Yes | Individual variables |
| Fixed keyword | `multiply(x=4, y=5)` | ✅ Yes | Individual variables |
| Variable positional | `add(*numbers)` | ❌ No | Tuple |
| Variable keyword | `create_student(**details)` | ❌ No | Dictionary |

---

## <font color='green'>6. Can `*args` and `**kwargs` Be Used in Any Function?</font>

Yes.

They are not restricted to any special type of function.

You can use them in:

- ordinary functions
- helper functions
- class methods
- decorators
- a `main()` function

For example,

```python
def main(*args, **kwargs):
    print(args)
    print(kwargs)

main(10, 20, language="Python")
```

Output

```text
(10, 20)
{'language': 'Python'}
```

`main()` is just another Python function. If it makes sense for your program to accept a variable number of positional or keyword arguments, you can use `*args` and `**kwargs` exactly as you would in any other function.

---
## <font color='green'>7. `*args` and `**kwargs` in Command-Line Programs</font>

Command-line programs can accept input in two ways:

1. **Positional arguments**
2. **Named (keyword) options**

The first naturally maps to `*args`, while the second maps to `**kwargs`.

### Example 1 – Positional Arguments (`*args`)

Suppose the program is executed as

```bash
python demo.py Alice 25 Singapore
```

Here, the values `Alice`, `25`, and `Singapore` are positional arguments because they are identified only by the order in which they appear.

```python
import sys

def main(*args):
    print(args)

if __name__ == "__main__":
    main(*sys.argv[1:])
```

Output

```text
('Alice', '25', 'Singapore')
```

### **Note on sys.argv**

* Python provides the **`sys`** module to access information related to the running program.

* **`sys.argv`** is a list that stores the command-line arguments passed to the program.

* **`sys.argv[0]`** contains the name (or path) of the Python program being executed.

* **`sys.argv[1:]`** contains only the arguments entered by the user.

* In this example, we use **`sys.argv[1:]`** to skip the program name and pass only the user-supplied arguments to `main()`.

* If required, we could also use **`sys.argv[0]`**, for example, to display or log the program's filename.



### Example 2 – Named Arguments (`**kwargs`)

Many command-line programs also support named options.

For example,

```bash
python demo.py --name Alice --age 25 --city Singapore
```

A command-line parser (such as Python's `argparse` module) converts these named options into a dictionary.

```python
options = {
    "name": "Alice",
    "age": "25",
    "city": "Singapore"
}

def main(**kwargs):
    print(kwargs)

main(**options)
```


Output

```text
{
    'name': 'Alice',
    'age': '25',
    'city': 'Singapore'
}
```

These examples show the relationship between command-line input and Python function parameters:

- Positional command-line arguments naturally map to `*args`.
- Named command-line options naturally map to `**kwargs`.

---
## Summary

- Python supports both positional and keyword arguments.
- Positional arguments are matched by **order**.
- Keyword arguments are matched by **parameter name**.
- Use `*args` when you don't know how many positional arguments will be supplied. Python packs them into a **tuple**.
- Use `**kwargs` when you don't know which keyword arguments will be supplied. Python packs them into a **dictionary**.
- `*args` and `**kwargs` can be used in any Python function, including ordinary functions, class methods, decorators, and `main()`.


---
## **Relevant Links**

[Python Material on this website](index.md)

