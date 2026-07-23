---
hide:
  - navigation
  
tags:
  - volatile keyword
  - Atomic Operation

  
---

# `volatile` Is Not Thread Synchronization in C

*This article is a short sequel to the previous article, [`volatile` Keyword in C](volatilekeyword.md) and [Atomic Operations in C](atomicoperations.md). It explains why the `volatile` qualifier does not provide thread synchronization or mutual exclusion, and discusses the appropriate mechanisms for writing thread-safe programs.*

---
## <font color='green'>1. `volatile` Does Not Prevent Race Conditions</font>

Consider two threads that increment the same shared variable.

```c
volatile int counter = 0;

/* Thread A */
counter++;

/* Thread B */
counter++;
```

At first glance, it may appear that declaring `counter` as `volatile` makes this code safe. However, `counter++` is **not** a single operation. It typically consists of three separate steps:

```text
Read counter
Increment the value
Write the new value back
```

Now suppose both threads execute these steps at nearly the same time.

```text
Initial value: counter = 0

Thread A                  Thread B
---------                 ---------
Read 0
                           Read 0
Increment to 1
                           Increment to 1
Write 1
                           Write 1

Final value: counter = 1
```

Although both threads incremented the counter, the final value is **1** instead of **2**. One increment has been lost because both threads read the same initial value before either thread wrote the result back.

Declaring `counter` as `volatile` does not prevent this situation. The compiler performs every read and write as required, but it cannot prevent another thread from accessing the variable at the same time.

This type of error is known as a **race condition**. Although `volatile` ensures that every read and write is performed as written, it does not make those operations atomic or coordinate access between threads.

> To safely share data between threads, synchronization mechanisms such as atomic operations, mutexes, or semaphores must be used.


---
## <font color='green'>2. The Correct Solution-1  (Use Atomic Operations)</font>

If multiple threads share a variable, the variable must be protected using an appropriate synchronization mechanism. The choice depends on how the variable is accessed.

For simple operations such as incrementing a counter, an **atomic operation** is often the simplest solution.

```c
#include <stdatomic.h>

atomic_int counter = 0;

/* Thread A */
atomic_fetch_add(&counter, 1);

/* Thread B */
atomic_fetch_add(&counter, 1);
```

Unlike `counter++` on a `volatile` variable, the increment is performed atomically. No updates are lost, even when multiple threads execute the operation simultaneously.

For more complex operations involving multiple shared variables or larger critical sections, synchronization primitives such as mutexes or semaphores should be used instead.

> **`volatile` prevents compiler optimizations. Atomic operations and synchronization primitives prevent race conditions.**


---
## <font color='green'>3. The Correct Solution-2 (Use Thread Synchronization)</font>

When multiple threads perform more complex operations or access multiple shared variables, atomic operations are often insufficient. In these situations, a synchronization mechanism such as a **mutex** should be used.

For example,

```c
#include <pthread.h>

int counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

/* Thread A */
pthread_mutex_lock(&mutex);
counter++;
pthread_mutex_unlock(&mutex);

/* Thread B */
pthread_mutex_lock(&mutex);
counter++;
pthread_mutex_unlock(&mutex);
```

A mutex allows only one thread to execute the protected code at a time. If one thread has already locked the mutex, any other thread attempting to lock it must wait until the mutex is released.

As a result, the two `counter++` operations cannot execute simultaneously, preventing race conditions and ensuring that both increments are applied correctly.

> **Atomic operations protect individual operations. Thread synchronization protects critical sections.**


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
