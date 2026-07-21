---
hide:
  - navigation
  
tags:
  - volatile keyword
  
---

# The `volatile` Keyword in C

*This article is intended for intermediate and advanced C programmers. It explains the purpose of the `volatile` keyword, when it should be used, and how it ensures the compiler always accesses the most recent value of a variable that may change unexpectedly.*

---
## <font color='green'>1. Compiler Optimization Can be Bad</font>

Modern C compilers perform a wide range of optimizations to improve the performance and efficiency of generated code. **One common optimization is to assume that the value of a variable does not change unless the program itself modifies it, hence it is cached**

**In embedded systems, certain variables can change independently of the program's normal execution.** For example, a hardware peripheral may update a status register, an Interrupt Service Routine (ISR) may modify a shared variable, or a Direct Memory Access (DMA) controller may write data directly to memory.

Without additional information, the compiler has no way of knowing that these changes can occur. As a result, it may optimize the code in a way that causes the program to use an outdated value.

> The `volatile` keyword informs the compiler that the value of a variable may change unexpectedly. It instructs the compiler to access the variable from memory whenever it is read or written, rather than relying on previously cached or optimized values.

---
## <font color='green'>2. What is the `volatile` Keyword?</font>

The `volatile` keyword is a type qualifier that tells the compiler a variable's value **may change at any time outside the normal flow of program execution**. As a result, the compiler must always read the variable directly from memory whenever its value is needed and must always write updates back to memory.

For example,

```c
volatile uint32_t status;
```

declares `status` as a volatile variable. Every read or write to `status` is performed exactly as written in the source code, preventing the compiler from optimizing away memory accesses.

Without the `volatile` qualifier, the compiler is free to optimize accesses to a variable. For example, if a variable is read multiple times without being modified by the program, the compiler may read it once, store the value in a CPU register, and reuse that cached value for subsequent accesses.

The `volatile` qualifier prevents this optimization because the variable's value may change unexpectedly between accesses.

Its sole purpose is to ensure that every access to a volatile variable results in an actual memory read or write, allowing the program to observe changes made by hardware or other asynchronous sources.

---
## <font color='green'>3. Common Uses of `volatile`</font>

The `volatile` keyword is primarily used in embedded systems where variables may be modified by hardware or by code executing outside the normal program flow.

The most common use cases are:

### **Memory-Mapped Registers**

Hardware peripherals expose control and status registers through memory-mapped addresses. Since the hardware can update these registers at any time, they should be declared `volatile`.

---

### **Interrupt Service Routines (ISRs)**

Variables shared between the main program and an Interrupt Service Routine (ISR) should be declared `volatile`, since the ISR can modify them asynchronously.

---

### **Direct Memory Access (DMA)**

DMA controllers can transfer data directly to memory without CPU intervention. Buffers or status flags updated by DMA should be declared `volatile` so the program always reads the latest value.

---

### **Hardware Status Flags**

Many embedded applications continuously poll hardware status flags, waiting for an event such as data becoming available or a transmission completing. Declaring these flags as `volatile` ensures that every iteration reads the current hardware value rather than a previously cached value.


---
## <font color='green'>4. What `volatile` Does <u>Not</u> Do</font>

A common misconception is that the `volatile` keyword solves synchronization problems between multiple execution contexts. In reality, `volatile` only affects how the compiler generates code. It does **not** provide any form of synchronization or thread safety.

Specifically, `volatile` does **not**:

- Make an operation atomic.
- Prevent race conditions.
- Guarantee mutual exclusion.
- Synchronize access between multiple threads.
- Replace locks, mutexes, or critical sections.

For example, consider the following statement:

```c
counter++;
```

Even if `counter` is declared as `volatile`, the increment operation is **not atomic**. It typically consists of three separate steps:

	1. Read the current value from memory.
	2. Increment the value.
	3. Write the updated value back to memory.

If an interrupt or another thread modifies `counter` between these steps, the final result may be incorrect.

> The `volatile` keyword simply guarantees that each memory access actually occurs. It does **not** protect the variable from being modified concurrently.

> For shared data accessed by multiple threads or interrupt contexts, `volatile` is often used together with synchronization mechanisms such as critical sections, mutexes, semaphores, or atomic operations.

---
## <font color='green'>5. Summary</font>

The `volatile` keyword informs the compiler that a variable's value may change unexpectedly and therefore should not be optimized by caching its value in a register.

It is commonly used for:

- Memory-mapped hardware registers
- Variables shared with Interrupt Service Routines (ISRs)
- Variables modified by DMA
- Hardware status flags

It is important to remember that `volatile` only affects compiler optimization. It does **not** provide atomic operations, mutual exclusion, thread safety, or protection against race conditions.

Use `volatile` only when a variable can be modified outside the normal flow of program execution. Overusing it can reduce the effectiveness of compiler optimizations and negatively impact performance.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
