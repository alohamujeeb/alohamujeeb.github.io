---
hide:
  - navigation
  
tags:
  - context managers
  - with in Python
  - contextlib
---

# Context Managers

## <font color='green'> 1: Introduction </font>

A **context manager** is a Python feature that automatically manages resources, such as files, database connections, and locks. It performs any required setup before a block of code executes and automatically cleans up afterward, even if an exception occurs.

Context managers are used with Python's built-in **`with`** statement.

### Example

As shown below, without a context manager, we must remember to close the file manually:

```python
f = open("file.txt")
data = f.read()
f.close()
```

However, by using a context manager, Python handles the cleanup automatically:

```python
with open("file.txt") as f:
    data = f.read()
```

In this example:

- `open("file.txt")` opens the file.
- `as f` assigns the opened file object to `f`.
- The code inside the `with` block uses the file.
- When the block ends, the file is automatically closed.

Using the `with` statement makes our code cleaner, safer, and less error-prone because resources are released automatically.

---
## <font color='green'>2: How the `with` Statement Works</font>

The `with` statement is built into Python. Behind the scenes, it relies on a **context manager** to automatically perform setup before a block of code runs and cleanup after it finishes.

A context manager provides two special methods:

- **`__enter__()`** – Called when entering the `with` block. It performs any setup and returns the object assigned after the `as` keyword.
- **`__exit__()`** – Called when leaving the `with` block. It performs cleanup, even if an exception occurs.

Consider the following example:

```python
with open("file.txt") as f:
    data = f.read()
```

Conceptually, Python performs the following steps:

```text
1. Open the file.
2. Call __enter__().
3. Assign the returned object to f.
4. Execute the code inside the with block.
5. Call __exit__() to clean up (close the file).
```

The flow can be visualized as follows:

```text
Enter with block
        │
        ▼
Call __enter__()
        │
        ▼
Execute code inside the block
        │
        ▼
Call __exit__()
        │
        ▼
Continue execution
```

The automatic call to `__exit__()` is what makes context managers useful. It ensures that resources are properly released, even if an exception occurs while executing the code inside the `with` block.


---
## <font color='green'>3: Creating Our Own Context Manager</font>

The `with` statement works with Python's built-in context managers, such as the file object returned by `open()`. However, we can also create our own context managers for our own classes.

To create a custom context manager, define a class with two special methods:

- **`__enter__()`** – Called when entering the `with` block. It performs any setup and returns the object that will be assigned after `as`.
- **`__exit__()`** – Called when leaving the `with` block. It performs cleanup, even if an exception occurs.

### Basic Example

```python
class Demo:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")

with Demo():
    print("Inside the block")
```

**Output**

```text
Start
Inside the block
End
```

In this example:

- `__enter__()` is called before the code inside the `with` block executes.
- The statements inside the `with` block are then executed.
- `__exit__()` is automatically called when the block finishes.

### Practical Example: Timing Code Execution

A common use of a custom context manager is to measure how long a block of code takes to execute.

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"Elapsed time: {elapsed:.3f} seconds")

with Timer():
    time.sleep(2)
    print("Task completed")
```

**Output**

```text
Task completed
Elapsed time: 2.001 seconds
```

In this example:

- `__enter__()` records the start time before the block begins.
- The code inside the `with` block is executed.
- `__exit__()` calculates and displays the elapsed time after the block completes.

This demonstrates how custom context managers can automatically perform setup and cleanup for our own applications, making our code cleaner and easier to maintain.

---
## <font color='green'>4: Creating Context Managers with `contextlib`</font>

Creating a context manager by defining a class with `__enter__()` and `__exit__()` works well. However, for simple tasks, writing an entire class can be unnecessary.

Python's **`contextlib`** module provides the **`@contextmanager`** decorator, which allows us to create a context manager using a generator function.

Instead of implementing `__enter__()` and `__exit__()`, we simply:

- Write the setup code before `yield`.
- Place the `yield` statement where the code inside the `with` block will execute.
- Write the cleanup code after `yield`.

### Example

```python
from contextlib import contextmanager

@contextmanager
def demo():
    print("Start")
    yield
    print("End")

with demo():
    print("Inside the block")
```

**Output**

```text
Start
Inside the block
End
```

In this example:

- The code before `yield` behaves like `__enter__()`.
- The `yield` statement temporarily pauses the function and allows the code inside the `with` block to execute.
- After the `with` block finishes, execution resumes after `yield`, behaving like `__exit__()`.

The execution flow is illustrated below:

```text
Enter with block
        │
        ▼
Run code before yield
        │
        ▼
      yield
        │
        ▼
Execute code inside the with block
        │
        ▼
Run code after yield
        │
        ▼
Continue execution
```

> <font color='red'> **Note:** In a contextlib context manager, yield replaces the need to explicitly define __enter__() and __exit__(). The code before yield performs setup, while the code after yield performs cleanup.</font>


### Practical Example: Temporarily Changing the Working Directory

The following context manager temporarily changes the current working directory. When the `with` block finishes, it automatically returns to the original directory.

```python
import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    original = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original)

print("Before:", os.getcwd())

with change_directory("/tmp"):
    print("Inside:", os.getcwd())

print("After:", os.getcwd())
```

**Output**

```text
Before: /home/user
Inside: /tmp
After: /home/user
```

In this example:

- The current directory is saved before changing it.
- The code inside the `with` block runs in the new directory.
- When the block finishes, the original directory is restored automatically.

> <font color='red'> Notice that yield is placed inside a try...finally block. This guarantees that the cleanup code (os.chdir(original)) executes even if an exception occurs inside the with block. </font>


### When should we use contextlib?

If our context manager only needs simple setup and cleanup logic, contextlib is usually the preferred approach because it is shorter, easier to read, and avoids creating an entire class.

---
## <font color='green'>5: Common Context Managers</font>

Python's standard library provides many built-in context managers that help manage common resources safely and efficiently. The following table lists some of the most commonly used context managers.

| Context Manager | Purpose |
|-----------------|---------|
| `open()` | Opens and automatically closes a file. |
| `threading.Lock()` | Acquires and releases a thread lock. |
| `tempfile.TemporaryDirectory()` | Creates and removes a temporary directory. |
| `tempfile.NamedTemporaryFile()` | Creates and removes a temporary file. |
| `contextlib.suppress()` | Suppresses specified exceptions. |
| `contextlib.redirect_stdout()` | Redirects `print()` output to another stream or file. |
| `decimal.localcontext()` | Temporarily changes decimal precision or rounding. |
| `sqlite3.connect()` | Automatically commits or rolls back transactions and closes the database connection. |
| `contextlib.ExitStack()` | Manages multiple context managers dynamically. |


### 5.1 Opening a File

```python
with open("data.txt") as f:
    text = f.read()
```

The file is automatically closed when the `with` block finishes.


### 5.2 Using a Thread Lock

```python
from threading import Lock

lock = Lock()

with lock:
    print("Critical section")
```

The lock is automatically released when the block exits.


### 5.3 Creating a Temporary Directory

```python
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    print(temp_dir)
```

The temporary directory is automatically deleted after use.


### 5.4 Creating a Temporary File

```python
from tempfile import NamedTemporaryFile

with NamedTemporaryFile() as temp_file:
    print(temp_file.name)
```

The temporary file is automatically removed when the `with` block ends.


### 5.5 Suppressing Exceptions

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    with open("missing.txt") as f:
        print(f.read())

print("Program continues...")
```

If `missing.txt` does not exist, the exception is ignored and the program continues executing.


### 5.6 Redirecting Standard Output

```python
from contextlib import redirect_stdout

with open("output.txt", "w") as f:
    with redirect_stdout(f):
        print("Hello, World!")
```

The output of `print()` is written to `output.txt` instead of the console.


### 5.7 Changing Decimal Precision

```python
from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 4
    print(Decimal("1") / Decimal("7"))
```

The precision change only applies within the `with` block.


### 5.8 Using a SQLite Database Connection

```python
import sqlite3

with sqlite3.connect("users.db") as conn:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER)"
    )
```

The transaction is committed automatically if successful, or rolled back if an exception occurs. The database connection is then closed.


---
## <font color='green'>6. Managing Multiple Context Managers</font>

Sometimes, a program needs to work with multiple resources at the same time, such as several files, database connections, or network sockets.

If the number of resources is known in advance, we can simply list multiple context managers in a single `with` statement.

### Example: Known Number of Resources

```python
with open("a.txt") as file1, open("b.txt") as file2:
    print(file1.read())
    print(file2.read())
```

This works well because there are exactly two files.

However, what if the number of files is not known until the program is running?

For example, suppose we have a list of filenames:

```python
files = ["a.txt", "b.txt", "c.txt", "d.txt"]
```

<font color='red'> We cannot write: </font>

```python
with open(file1), open(file2), open(file3), open(file4):
    ...
```

because the number of files is determined dynamically.

This is where **`contextlib.ExitStack`** becomes useful.

### Example: Dynamic Number of Files

Suppose we want to open every file in a list. Since the number of files is only known at runtime, `ExitStack` is a convenient way to manage them.

```python
from contextlib import ExitStack

files = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    opened_files = []

    for filename in files:
        f = stack.enter_context(open(filename))  #open is the context manager(many are opened)
        opened_files.append(f)

    for f in opened_files:
        print(f.read())

print("All files have been closed.")
```

In this example:

- `ExitStack()` creates a context manager that manages multiple resources.
- `stack.enter_context(open(filename))` opens each file and registers it with the `ExitStack`.
- The files remain open while the code is inside the `with ExitStack()` block.
- When the `with ExitStack()` block ends, `ExitStack` automatically closes every opened file.

This works regardless of whether there are 3 files, 30 files, or even 300 files.


### Another Example: Mixing Different Context Managers

`ExitStack` is not limited to files. It can manage different types of context managers together.

```python
from contextlib import ExitStack
from tempfile import TemporaryDirectory

with ExitStack() as stack:
    temp_dir = stack.enter_context(TemporaryDirectory()) #context manager type 1: TemporaryDirectory
    file = stack.enter_context(open("log.txt", "w"))  #context manager type 2: open

    print("Temporary directory:", temp_dir)
    file.write("Logging started...")
```

Here, `ExitStack` manages:

- A temporary directory.
- A file.

When the `with` block finishes:

- The file is automatically closed.
- The temporary directory is automatically deleted.

> **When should we use `ExitStack`?**
>
> <font color='red'>Use `ExitStack` when the number or type of context managers is not known until runtime. It provides a flexible way to manage multiple resources while still ensuring that all cleanup operations are performed automatically.</font>

---
## <font color='green'>7. Summary</font>

Context managers provide a clean and reliable way to manage resources in Python. Instead of manually performing setup and cleanup, the `with` statement ensures that resources are handled automatically, making our code safer and easier to read.

In this article, we learned:

- What a context manager is and why it is useful.
- How to use the built-in `with` statement.
- How `__enter__()` and `__exit__()` work behind the scenes.
- How to create our own context managers using a class.
- How to create simpler context managers with `contextlib` and `yield`.
- Some of the most commonly used context managers in Python.
- How to use `ExitStack` to manage multiple context managers dynamically.

As a general rule:

- Use `with` whenever we work with resources that need to be cleaned up, such as files, locks, database connections, or temporary files.
- Use a **class-based context manager** when our setup and cleanup logic is complex or requires maintaining state.
- Use **`contextlib`** when we only need simple setup and cleanup logic.
- Use **`ExitStack`** when the number or type of context managers is determined at runtime.

By using context managers consistently, we programs become cleaner, more reliable, and less prone to resource leaks. They are one of Python's most useful features for writing safe and maintainable code.


---

