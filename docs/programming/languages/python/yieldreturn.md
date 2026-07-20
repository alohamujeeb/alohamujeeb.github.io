---
hide:
  - navigation
  
tags:
  - return in python
  - yield

---
# Generator Functions- `yield` and `return` in Python

---
## <font color='green'>1. `return` statment</font>

The `return` statement is one of the first concepts every programmer learns. It marks the end of a function's execution and sends the computed result back to the caller.

For most functions, this behavior is exactly what we want.

```python
def square(n):
    return n * n

result = square(5)
print(result)      # 25
```

- Once `return` is executed, the function terminates. No further statements in the function are executed.

- This works perfectly when a function needs to produce a single result. But what if the function needs to produce multiple values?

A common approach is to collect the values in a list and return the list after all values have been generated.

```python
def squares(n):
    result = []

    for i in range(1, n + 1):
        result.append(i * i)

    return result

print(squares(5))
# [1, 4, 9, 16, 25]
```

### The Limitation of `return`

Although the first square (`1`) is computed during the first iteration of the loop, it is not immediately available to the caller. The function continues executing, appending every computed value to the list. Only after the loop finishes does the `return` statement execute, returning the complete list.

This reveals an important characteristic of `return`: **a function can return only once**. If multiple values need to be produced, they must first be collected into a container such as a list, tuple, or dictionary.

> <font color='red'>But what if we want to produce each value as soon as it is computed, instead of waiting for the entire collection to be built? This is exactly the problem that the `yield` keyword solves.</font>

---
## <font color='green'> 2. Generator functions is solution</font>

A function containing one or more `yield` statements is called a **generator function**.

Unlike a regular function, calling a generator function does **not** execute its body immediately. Instead, it returns a **generator object**.

```python
def squares(n):
    for i in range(1, n + 1):
        yield i * i

numbers = squares(5)

print(numbers)
```

Output:
```
<generator object squares at 0x...>
```

A generator object is a special object that produces values on demand. It keeps track of the function's execution and produces the next value whenever requested.

Values are obtained by calling next().

```
numbers = squares(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

output
```
1
4
9
```


---
## <font color='green'>3. What Happens Behind the Scenes?</font>

A normal function executes from the first statement to the `return` statement. Once `return` is encountered, control goes back to the caller and the function's execution is over.

```text
Caller ──► Function ──► return ──► Caller
```

A generator function behaves differently. When it encounters a `yield` statement, it **temporarily suspends** its execution instead of terminating.

```text
Caller ──► Generator ──► yield ──► Caller
              ▲                    │
              └──── next() ◄───────┘
```

The important point is that the generator does **not** start over when `next()` is called again. Instead, Python preserves the generator's execution state, including:

- the current instruction,
- the values of local variables,
- the loop state, and
- the call stack for that generator.

> When `next()` is called, execution resumes **exactly after the previous `yield` statement**.

For example,

```python
def squares(n):
    for i in range(1, n + 1):
        print(f"Computing square of {i}")
        yield i * i
```

```python
numbers = squares(3)

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

**Output**

```text
Computing square of 1
1
Computing square of 2
4
Computing square of 3
9
```

Notice that the loop does **not** restart from `i = 1` every time `next()` is called. Python remembers that the generator had already paused after the previous `yield` and simply continues with the next iteration.

We can think of a generator as having **its own execution context**. Control alternates between the caller and the generator:

1. The caller invokes `next()`.
2. The generator runs until it reaches a `yield`.
3. Control returns to the caller with the yielded value.
4. The next call to `next()` resumes the generator from exactly where it paused.

Unlike a normal function, which has a single uninterrupted execution, a generator repeatedly **yields control to its caller and later regains it**, allowing both the caller and the generator to make progress one step at a time.

---
## <font color='green'>4. When to Use `yield`</font>

The `yield` keyword is most useful when a function needs to produce a **sequence of values**, rather than a single result.

Typical use cases include:

### **Processing Large Datasets**

If a function generates thousands or millions of values, creating a list of all values may consume a significant amount of memory. A generator produces one value at a time, allowing values to be processed without storing the entire sequence.

### **Reading Files**

When reading a large file, it is often unnecessary to load the entire file into memory. A generator can yield one line at a time as the file is read.

```python
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line
```

### **Generating Sequences**

Generators are well suited for sequences such as Fibonacci numbers, prime numbers, countdowns, or any series where the next value can be computed from the previous one.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

### **Building Data Pipelines**

Generators can be chained together so that the output of one generator becomes the input of another. This allows data to be processed step by step without creating intermediate lists.

> **Rule of Thumb**
>
> - Use **`return`** when a function produces **one final result**.
> - Use **`yield`** when a function produces **a sequence of values**, especially when those values can be generated one at a time.


