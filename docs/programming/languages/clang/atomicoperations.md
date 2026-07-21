---
hide:
  - navigation
  
tags:
  - Atomic Operations
  
---

# Atomic Operations in C

*This article is intended for intermediate and advanced C programmers. It explains what atomic operations are, why they are important in multithreaded and embedded systems, and how the C11 atomic library provides a safe and efficient way to access shared data.*

---
## <font color='green'>1. What Are Atomic Operations?</font>

An **atomic operation** is an operation that is performed as a single, indivisible unit. Once an atomic operation begins, no other thread or execution context can observe it in a partially completed state or interrupt it before it finishes.

Atomic operations are essential whenever multiple execution contexts access the same data concurrently. These execution contexts may include multiple threads in a multithreaded application or an interrupt service routine (ISR) and the main program in an embedded system.

Consider the following statement:

```c
counter++;
```

Although it appears to be a single operation, it typically consists of several individual steps:

1. Read the current value of `counter` from memory.
2. Increment the value.
3. Write the updated value back to memory.

If another thread or interrupt modifies `counter` between these steps, the final result may be incorrect.

An atomic increment performs the entire operation as a single indivisible action, ensuring that no other execution context can interfere while the operation is in progress. This guarantees that shared data remains consistent even when accessed concurrently.

---
## <font color='green'>2. Why Atomic Operations Are Needed</font>

In many programs, multiple execution contexts may access the same variable at the same time. If one execution context modifies the variable while another is reading or updating it, the program may produce incorrect or unpredictable results.

For example, consider a shared counter that is incremented by two threads:

```c
counter++;
```

Although each thread executes the same statement, the increment operation is not inherently atomic. If both threads read the current value before either writes the updated value back to memory, one of the increments can be lost.

Suppose the value of `counter` is initially `10`:

1. Thread A reads `10`.
2. Thread B reads `10`.
3. Thread A increments the value to `11` and writes it back.
4. Thread B increments its previously read value to `11` and writes it back.

The final value of `counter` is `11` instead of the expected `12`.

This type of error is known as a **race condition**, where the correctness of a program depends on the timing or ordering of concurrent operations.

Atomic operations eliminate this problem by ensuring that shared variables are updated as indivisible operations. Each update completes before another execution context can modify the same data, preventing lost updates and maintaining data consistency.

---
## <font color='green'>3. Atomic Types in C11</font>

The C11 standard introduced the `<stdatomic.h>` header, which provides support for atomic operations and atomic data types. An atomic object guarantees that individual read, write, and read-modify-write operations are performed atomically, preventing data races when accessed concurrently.

There are two common ways to declare an atomic object:

- Using the `_Atomic` type specifier.
- Using one of the predefined atomic type aliases provided by `<stdatomic.h>`.

For example, the following declarations create atomic integer variables:

```c
#include <stdatomic.h>

_Atomic int counter1 = 0;
atomic_int counter2 = 0;
```

Both declarations create an atomic integer and provide the same functionality. The `atomic_int` type is simply a convenience alias for `_Atomic int`.

The C11 standard provides predefined atomic type aliases for the most commonly used integer and character types.

| Atomic Type | Equivalent Type |
|-------------|-----------------|
| `atomic_bool` | `_Atomic bool` |
| `atomic_char` | `_Atomic char` |
| `atomic_schar` | `_Atomic signed char` |
| `atomic_uchar` | `_Atomic unsigned char` |
| `atomic_short` | `_Atomic short` |
| `atomic_ushort` | `_Atomic unsigned short` |
| `atomic_int` | `_Atomic int` |
| `atomic_uint` | `_Atomic unsigned int` |
| `atomic_long` | `_Atomic long` |
| `atomic_ulong` | `_Atomic unsigned long` |
| `atomic_llong` | `_Atomic long long` |
| `atomic_ullong` | `_Atomic unsigned long long` |
| `atomic_char8_t`* | `_Atomic char8_t` |
| `atomic_char16_t` | `_Atomic char16_t` |
| `atomic_char32_t` | `_Atomic char32_t` |
| `atomic_wchar_t` | `_Atomic wchar_t` |
| `atomic_int_least8_t` | `_Atomic int_least8_t` |
| `atomic_uint_least8_t` | `_Atomic uint_least8_t` |
| `atomic_int_least16_t` | `_Atomic int_least16_t` |
| `atomic_uint_least16_t` | `_Atomic uint_least16_t` |
| `atomic_int_least32_t` | `_Atomic int_least32_t` |
| `atomic_uint_least32_t` | `_Atomic uint_least32_t` |
| `atomic_int_least64_t` | `_Atomic int_least64_t` |
| `atomic_uint_least64_t` | `_Atomic uint_least64_t` |
| `atomic_int_fast8_t` | `_Atomic int_fast8_t` |
| `atomic_uint_fast8_t` | `_Atomic uint_fast8_t` |
| `atomic_int_fast16_t` | `_Atomic int_fast16_t` |
| `atomic_uint_fast16_t` | `_Atomic uint_fast16_t` |
| `atomic_int_fast32_t` | `_Atomic int_fast32_t` |
| `atomic_uint_fast32_t` | `_Atomic uint_fast32_t` |
| `atomic_int_fast64_t` | `_Atomic int_fast64_t` |
| `atomic_uint_fast64_t` | `_Atomic uint_fast64_t` |
| `atomic_intptr_t` | `_Atomic intptr_t` |
| `atomic_uintptr_t` | `_Atomic uintptr_t` |
| `atomic_size_t` | `_Atomic size_t` |
| `atomic_ptrdiff_t` | `_Atomic ptrdiff_t` |
| `atomic_intmax_t` | `_Atomic intmax_t` |
| `atomic_uintmax_t` | `_Atomic uintmax_t` |

> **Note:** `atomic_char8_t` is available only when `char8_t` is supported by the implementation.

Atomic objects can also be created from user-defined types using the `_Atomic` type specifier.

For example:

```c
typedef struct
{
    int x;
    int y;
} Point;

_Atomic Point position;
```

Whether operations on user-defined atomic types are lock-free depends on the compiler and target architecture.

Once an object has been declared as atomic, it should be accessed using the atomic functions provided by `<stdatomic.h>`, such as `atomic_load()`, `atomic_store()`, and `atomic_fetch_add()`, which are discussed in the following sections.

---
## <font color='green'>4. Performing Atomic Operations</font>

The `<stdatomic.h>` header provides a collection of functions for safely reading, writing, and modifying atomic objects. These operations guarantee that the access is performed atomically, preventing interference from other execution contexts.

Some of the most commonly used atomic operations are shown below.

### Reading an Atomic Value

The `atomic_load()` function atomically reads the value of an atomic object.

```c
#include <stdatomic.h>

atomic_int counter = 10;

int value = atomic_load(&counter);
```

### Writing an Atomic Value

The `atomic_store()` function atomically writes a new value to an atomic object.

```c
#include <stdatomic.h>

atomic_int counter = 10;

atomic_store(&counter, 20);
```

### Exchanging Values

The `atomic_exchange()` function replaces the current value with a new value and returns the previous value.

```c
#include <stdatomic.h>

atomic_int counter = 10;

int old = atomic_exchange(&counter, 20);
```

After execution, `old` contains `10` and `counter` contains `20`.

### Compare-and-Exchange

The `atomic_compare_exchange_*()` functions compare the current value of an atomic object with an expected value. If they match, the object is updated atomically; otherwise, no update is performed.

This operation is widely used to implement lock-free data structures and synchronization algorithms.


---
## <font color='green'>5. Common Atomic Operations</font>

In addition to reading and writing atomic objects, the C11 atomic library provides functions that perform common arithmetic and bitwise operations atomically. These functions are especially useful when multiple threads or execution contexts modify the same shared variable.

The following table summarizes the most commonly used atomic operations provided by `<stdatomic.h>`.

| Function | Description |
|----------|-------------|
| `atomic_load()` | Atomically reads the value of an atomic object. |
| `atomic_store()` | Atomically writes a new value to an atomic object. |
| `atomic_exchange()` | Atomically replaces the current value with a new value and returns the previous value. |
| `atomic_compare_exchange_*()` | Atomically compares the current value with an expected value and updates it if they match. |
| `atomic_fetch_add()` | Atomically adds a value to an atomic object and returns the previous value. |
| `atomic_fetch_sub()` | Atomically subtracts a value from an atomic object and returns the previous value. |
| `atomic_fetch_and()` | Performs an atomic bitwise AND operation and returns the previous value. |
| `atomic_fetch_or()` | Performs an atomic bitwise OR operation and returns the previous value. |
| `atomic_fetch_xor()` | Performs an atomic bitwise XOR operation and returns the previous value. |

### Atomic Load

The `atomic_load()` function atomically reads the value of an atomic object.

```c
#include <stdatomic.h>

atomic_int counter = 10;

int value = atomic_load(&counter);
```

After execution, `value` contains `10`.

### Atomic Store

The `atomic_store()` function atomically writes a new value to an atomic object.

```c
#include <stdatomic.h>

atomic_int counter = 10;

atomic_store(&counter, 20);
```

After execution, `counter` contains `20`.

### Atomic Exchange

The `atomic_exchange()` function atomically replaces the current value of an atomic object with a new value and returns the previous value.

```c
#include <stdatomic.h>

atomic_int counter = 10;

int previous = atomic_exchange(&counter, 20);
```

After execution:

- `previous` contains `10`.
- `counter` contains `20`.

### Compare-and-Exchange

The `atomic_compare_exchange_strong()` function compares the current value of an atomic object with an expected value. If the values match, the object is updated atomically.

```c
#include <stdatomic.h>
#include <stdbool.h>

atomic_int counter = 10;
int expected = 10;

bool success = atomic_compare_exchange_strong(
    &counter,
    &expected,
    20
);
```

If `counter` is equal to `expected`, it is updated to `20` and `success` is `true`. Otherwise, `counter` remains unchanged, `success` is `false`, and `expected` is updated with the current value of `counter`.

### Atomic Addition

The `atomic_fetch_add()` function atomically adds a value to an atomic object and returns its previous value.

```c
#include <stdatomic.h>

atomic_int counter = 0;

int previous = atomic_fetch_add(&counter, 1);
```

After execution:

- `previous` contains `0`.
- `counter` contains `1`.

### Atomic Subtraction

The `atomic_fetch_sub()` function atomically subtracts a value from an atomic object.

```c
atomic_fetch_sub(&counter, 1);
```

Like `atomic_fetch_add()`, this operation is performed atomically, ensuring that concurrent updates to the shared variable are not lost.

### Atomic Bitwise Operations

The C11 atomic library also provides atomic bitwise operations, including:

- `atomic_fetch_and()`
- `atomic_fetch_or()`
- `atomic_fetch_xor()`

These operations are commonly used when manipulating shared status flags or hardware control bits.

For example, the following statement atomically sets bit 2 of `flags`:

```c
atomic_fetch_or(&flags, 0x04);
```

Similarly, the following statement atomically clears bit 2 of `flags`:

```c
atomic_fetch_and(&flags, ~0x04);
```

The following statement atomically toggles bit 2 of `flags`:

```c
atomic_fetch_xor(&flags, 0x04);
```

These functions eliminate the need to perform separate read-modify-write sequences, which could otherwise introduce race conditions when shared data is accessed concurrently.



---
## <font color='green'>6. Atomic Operations in Embedded Systems</font>

Atomic operations are not only useful in multithreaded applications but also play an important role in embedded systems. A common scenario involves shared variables that are accessed by both the main program and an Interrupt Service Routine (ISR).

For example, an ISR may increment a counter each time a hardware event occurs, while the main program periodically reads and processes the accumulated events.

```c
#include <stdatomic.h>

atomic_int event_count = 0;

void Timer_IRQHandler(void)
{
    atomic_fetch_add(&event_count, 1);
}

int main(void)
{
    while (1)
    {
        if (atomic_load(&event_count) > 0)
        {
            atomic_fetch_sub(&event_count, 1);

            /* Process one event */
        }
    }
}
```

Without atomic operations, both the ISR and the main program could attempt to update `event_count` simultaneously, potentially resulting in lost updates or inconsistent data.

Although the C11 atomic library provides a standardized interface for atomic operations, support depends on the compiler and target architecture. Some embedded compilers provide full support for `<stdatomic.h>`, while others offer only partial support or rely on hardware-specific instructions.

For targets that do not support C11 atomics, critical sections protected by temporarily disabling interrupts are commonly used to ensure atomic access to shared data.

---
## <font color='green'>7. Alternatives to C11 Atomic Operations</font>

Prior to the introduction of the C11 standard, the C language did not provide a standardized mechanism for performing atomic operations. As a result, programmers relied on platform-specific synchronization techniques to safely access shared data.

Some of the most common alternatives include:

| Technique | Description |
|-----------|-------------|
| **Mutexes** | Commonly used in multithreaded applications to ensure that only one thread accesses shared data at a time. |
| **Critical Sections** | Frequently used in embedded systems by temporarily disabling interrupts while accessing shared data. |
| **Compiler Intrinsics** | Compiler-specific atomic functions, such as GCC's `__atomic_*()` and `__sync_*()` built-in functions, or Microsoft's `_Interlocked*()` functions. |
| **Hardware Instructions** | Some processors provide dedicated atomic instructions that are accessed through compiler intrinsics or assembly language. |

These techniques are still widely used today, particularly on systems where the C11 atomic library is not fully supported. However, they often reduce portability because they depend on the operating system, compiler, or processor architecture.

The `<stdatomic.h>` library introduced by C11 provides a standardized and portable interface for performing atomic operations. On supported platforms, the compiler translates these operations into the most appropriate synchronization mechanism, allowing the same source code to be used across different architectures with minimal modification.


---
## <font color='green'>8. Summary</font>

Atomic operations are essential for safely accessing shared data in concurrent applications and embedded systems. Unlike ordinary read-modify-write operations, atomic operations are performed as indivisible units, preventing interference from other execution contexts.

The C11 standard introduced the `<stdatomic.h>` library, providing a portable set of atomic types and operations for reading, writing, and modifying shared objects. These facilities help eliminate race conditions and improve the reliability of software that relies on concurrent access to shared data.

In embedded systems, atomic operations are particularly useful when data is shared between the main program and Interrupt Service Routines (ISRs). Where supported, the C11 atomic library provides a standardized solution for managing shared data. On platforms without C11 atomic support, equivalent protection is often achieved using critical sections or hardware-specific synchronization mechanisms.

By understanding and correctly using atomic operations, developers can write safer, more robust, and more maintainable C programs.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
