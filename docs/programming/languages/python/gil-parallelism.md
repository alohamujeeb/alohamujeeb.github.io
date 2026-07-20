---
hide:
  - navigation
  
tags:
  - GIL
  - Concurrency in Python
  - Parallelism in Python
---

# Understanding GIL and Parllelism in Python

---
## <font color='green'>1. The Surprise </font>

Multithreading has been part of Python for decades. The standard library provides a `threading` module, making it easy to create multiple threads.

Most developers assume that creating multiple threads means their program will automatically run on multiple CPU cores.

If we're using **CPython**, the most widely used Python interpreter, that assumption is often wrong.

> <font color='red'> We can create multiple threads, yet our Python code may still not execute in parallel. </font>

The reason lies in a CPython feature called the **Global Interpreter Lock (GIL)**.

Before we understand the GIL, we first need to understand the difference between **concurrency** and **parallelism**.


---
## <font color='green'> 2. Concurrency vs Parallelism </font>

The terms **concurrency** and **parallelism** are often used interchangeably, but they describe two different concepts.

**Concurrency** is the ability to make progress on multiple tasks during the same period of time. The tasks may not execute simultaneously; instead, the system rapidly switches between them, giving the appearance that they are running together.

For example, a single CPU core can execute multiple threads by quickly switching from one thread to another. Each thread makes progress, but only one thread is executing at any instant.

**Parallelism**, on the other hand, means multiple tasks are executing at the exact same time. This requires multiple execution units, such as multiple CPU cores.

A simple way to think about the difference is:

- **Concurrency** is about managing multiple ta<strong><font> [Threading in Python](threading.md)</font></strong>sks.
- **Parallelism** is about executing multiple tasks simultaneously.

This distinction is important because a program can be highly concurrent without being parallel. As we'll see, this is exactly how CPU-bound multithreaded programs behave in CPython

---
## <font color='green'> 3. Threads and CPU Cores </font>

To understand why CPython behaves the way it does, we first need to understand how threads normally work.

A **thread** is the smallest unit of execution within a process. A single process can contain multiple threads, each capable of executing a different sequence of instructions.

Modern operating systems schedule threads independently. If a machine has multiple CPU cores, the operating system can assign different threads to different cores, allowing them to execute simultaneously.

For example, a program that creates four CPU-intensive threads on a four-core processor would typically have one thread executing on each core.

```
Process

├── Thread 1  →  Core 1
├── Thread 2  →  Core 2
├── Thread 3  →  Core 3
└── Thread 4  →  Core 4
```

This is how multithreading works in many programming languages, and it's what most developers expect when they write multithreaded code.

If Python creates real operating-system threads, why doesn't a CPU-bound Python program behave the same way?

The answer lies in how **CPython executes Python code**.

---
## <font color='green'> 4. The Global Interpreter Lock (GIL) </font>

CPython does create **real operating-system threads**. The operating system is free to schedule those threads on different CPU cores.

However, before a thread can execute **Python bytecode**, it must first acquire the **Global Interpreter Lock (GIL)**.

> <font color='red'>The GIL is a mutex that allows only one thread at a time to execute Python bytecode within a single CPython process. </font>

This means that while multiple threads may exist, only one of them can actively execute Python code at any given moment. The remaining threads must wait until the GIL becomes available.

```
                CPython Process

Thread 1 ─┐
Thread 2 ─┼──► Global Interpreter Lock (GIL) ───► Python Bytecode
Thread 3 ─┤
Thread 4 ─┘
```


---
## <font color='green'> 5. Pure Python vs Native Extensions </font>

The GIL only affects code executed by the Python interpreter.

This means there are two broad categories of code in a Python program:

- **Pure Python code**, which is executed by the Python interpreter.
- **Native code**, implemented in C or C++, which is executed outside the interpreter (However, they are called FROM WITHIN the pure python code)


>When our program is executing pure Python code, only one thread can execute at a time within a CPython process.

>However, many popular libraries, such as NumPy and OpenCV, perform most of their work in optimized C or C++ code. These libraries can release the GIL while performing long-running computations, allowing multiple CPU cores to be utilized.


---
## <font color='green'> 6. Examples: Pure Python vs Native Libraries </font>

At this point, the distinction should be clear: **the GIL only restricts the execution of Python bytecode**. Therefore, whether a multithreaded Python program can utilize multiple CPU cores depends on **what the threads are actually executing**.

The following table summarizes some common examples.

| Pure Python (GIL Applies) | Native Libraries (GIL Can Be Released) |
|----------------------------|----------------------------------------|
| `for` loops | `numpy.matmul()` |
| List comprehensions | `numpy.dot()` |
| Dictionary processing | `cv2.GaussianBlur()` |
| String manipulation | `cv2.Canny()` |
| Recursive functions | `hashlib.sha256()` |
| JSON parsing | `zlib.compress()` |

In the left column, the work is performed by the Python interpreter, so multiple threads must take turns executing Python bytecode.

In the right column, the heavy computation is delegated to optimized native C/C++ code. These libraries can release the GIL while performing long-running computations, allowing multiple CPU cores to be utilized.

This is why two Python threads executing a simple `for` loop behave very differently from two Python threads executing `numpy.matmul()` or `cv2.GaussianBlur()`.

---
## <font color='green'> 7. GIL is only in CPython </font>

Most common interpreter implementation of Pythbon is **CPython** (besides few others, such as JPython)

One important point is that the **GIL is not a feature of the Python language itself**. It is a design decision of **CPython**, the reference implementation and by far the most widely used Python interpreter.

Several other Python implementations exist, including:

- **Jython**, which runs on the Java Virtual Machine (JVM)
- **IronPython**, which runs on the .NET Common Language Runtime (CLR)
- **PyPy**, an alternative implementation focused on performance
- **GraalPy**, which runs on GraalVM

Some of these implementations do not use the traditional GIL found in CPython and therefore can execute Python threads differently.

However, CPython remains the dominant implementation because of its extensive ecosystem and compatibility with popular libraries such as NumPy, Pandas, SciPy, OpenCV, TensorFlow, and PyTorch.

For this reason, when developers discuss "Python's GIL," they are almost always referring to **CPython's GIL**.

---
## <font color='green'> 8. Achieving True Parallelism in Python </font>

Although the GIL limits the parallel execution of Python bytecode within a single CPython process, it does **not** mean Python programs cannot utilize multiple CPU cores.

There are several common approaches:

| Workload | Recommended Approach |
|----------|----------------------|
| I/O-bound (network, files, databases) | Threads or `asyncio` |
| CPU-bound, pure Python | Multiple processes (`multiprocessing`) |
| CPU-bound using NumPy, OpenCV, etc. | Threads that run native code (not bytecode) |

The key idea is simple:

- **Threads and Asynchio** are excellent for I/O-bound workloads because they allow other threads to make progress while one thread is waiting.
- **Multiple processes** achieve true parallelism for CPU-bound pure Python code because each process has its own Python interpreter and its own GIL.
- **Native libraries** such as NumPy and OpenCV can execute in parallel because the computationally intensive work is performed outside the Python interpreter.

Ultimately, the GIL is not a limitation of Python itself. It is a characteristic of CPython's execution model. Understanding when it applies, and when it doesn't, allows us to choose the appropriate approach for writing efficient and scalable Python applications.

---
## <font color='green'> Summary </font>

Let's recap the main ideas:

- **Concurrency** and **parallelism** are not the same thing.
- Operating systems can execute multiple threads simultaneously across multiple CPU cores.
- **CPython** creates real operating-system threads, but only one thread can execute **Python bytecode** at a time because of the **Global Interpreter Lock (GIL)**.
- The GIL only affects code executed by the Python interpreter.
- Native libraries such as **NumPy** and **OpenCV** can release the GIL and perform computations in parallel.
- The GIL is a characteristic of **CPython**, not the Python language itself.
- True parallelism for pure Python code can be achieved using **multiple processes**, while native libraries often provide parallelism within a single process.

Understanding where the GIL applies, and where it doesn't, is essential for writing efficient Python applications and choosing the right concurrency model for our workload.


---
## <font color='green'> What's Next? </font>

This article focused on the concepts behind Python's concurrency model.

In a follow-up articles in this regars, we'll build practical examples covering:

- Threading
- Thread pools
- Multiprocessing
- `asyncio`
- Synchronization primitives
- Race conditions
- Performance profiling
- CPU utilization
- Real-world concurrency patterns

---
## References

<strong><font> [Threading in Python](threading.md)</font></strong>

<strong><font> [Python Interpreters-CPython/JPython](python-implementations.md)</font></strong>

