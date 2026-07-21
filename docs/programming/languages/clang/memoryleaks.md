---
hide:
  - navigation
  
tags:
  - stack
  - heap
  - global memory
  - gloabl variables

---

# Understanding Memory Leaks in C (Some Scenarios)
*This article assumes a basic understanding of dynamic memory allocation and focuses on memory leak scenarios encountered in professional C programming.*

---
## <font color='green'>Heap is the source of memory leaks</font>

In the previous article on [memory types in c](stackheap.md), we learned that **heap memory** is allocated dynamically using functions such as `malloc()`, `calloc()`, and `realloc()`. Unlike stack memory, heap memory is **not released automatically** when a function returns. Instead, the programmer is responsible for releasing it using `free()`.

If dynamically allocated memory is no longer needed but is never released, it remains allocated even though the program can no longer use it. This problem is known as a **memory leak**.

While a small leak may go unnoticed, repeated leaks in long-running applications can increase memory usage, reduce performance, and eventually cause the program to fail.

In this article, we will learn how memory leaks occur, examine the most common causes, and discuss techniques to prevent them.

---
## <font color='green'>Scenario 1: Forgetting to Call `free()`</font>

The most common cause of a memory leak is **forgetting to release dynamically allocated memory** after it is no longer needed.

When memory is allocated using `malloc()`, `calloc()`, or `realloc()`, it remains allocated until `free()` is called. If the program finishes using the memory but never calls `free()`, the allocated block remains reserved and cannot be reused by the program. This results in a **memory leak**.

**Example**

```c
#include <stdlib.h>

int main(void)
{
    int *ptr = malloc(sizeof(int));

    if (ptr == NULL)
    {
        return 1;
    }

    *ptr = 100;

    /* Use the allocated memory */

    /* free(ptr);  <-- Forgotten */

    return 0;
}
```


In this example, memory is successfully allocated and used, but it is never released. As a result, the allocated memory remains reserved until the program terminates.

> *For a short-lived program, the operating system reclaims the leaked memory when the program exits. However, in long-running applications such as servers, embedded systems, or continuously running services, repeatedly forgetting to call `free()` causes memory usage to grow over time, eventually degrading performance or exhausting the available memory.*

---

## <font color='green'>Scenario 2: Losing the Pointer</font>

A memory leak can occur even if we **do not forget to call `free()`**. If the only pointer that stores the address of an allocated memory block is lost, there is no longer any way to access or release that memory.

In other words, the memory is still allocated, but its address has been lost. Since `free()` requires the original address returned by `malloc()`, the leaked memory can never be released.

**Example**

```c
#include <stdlib.h>

int main(void)
{
    int *ptr = malloc(sizeof(int));

    if (ptr == NULL)
    {
        return 1;
    }

    *ptr = 100;		/* store some data */

    ptr = NULL;      /* Original address is lost */

    /* free(ptr);     Cannot free the allocated memory */

    return 0;
}
```

Initially, `ptr` stores the address returned by `malloc()`. After assigning `NULL` to `ptr`, that address is lost forever. Although the allocated memory still exists in the heap, there is no longer any pointer that refers to it.

This situation results in a **memory leak** because the allocated memory has become **unreachable**.



---

## <font color='green'>Scenario 3: Overwriting the Pointer</font>

Another common cause of memory leaks is **overwriting a pointer that already points to allocated memory**.

When a pointer is assigned the address of a newly allocated memory block, it holds the only reference to that block. If the pointer is later assigned a different address before calling `free()`, the original address is lost. As a result, the first allocated memory block becomes unreachable and cannot be released.

**Example**

```c
#include <stdlib.h>

int main(void)
{
    int *ptr = malloc(sizeof(int));

    if (ptr == NULL)
    {
        return 1;
    }

    /* ptr now points to the first memory block */

    ptr = malloc(sizeof(int));

    if (ptr == NULL)
    {
        return 1;
    }

    /* The first memory block has been leaked */

    free(ptr);

    return 0;
}
```

In this example, the second call to `malloc()` stores a new address in `ptr`, replacing the original one. Since the first address is no longer available, there is no way to call `free()` for the first memory block.

As a result, **the first allocated memory block is leaked**, while only the second block is released.

---

## <font color='green'>Scenario 4: Reassigning a Global Pointer</font>

Memory leaks are not limited to local pointers. A **global pointer** can also cause a memory leak if it is assigned a new memory address before the previously allocated memory is released.

Each time `malloc()` is called, it returns the address of a newly allocated memory block. If a global pointer is reassigned without first calling `free()`, the original address is lost and the previously allocated memory becomes unreachable.

**Example**s

```c
#include <stdlib.h>

int *buffer = NULL;      /* Global pointer */

void allocateBuffer(void)
{
    buffer = malloc(100 * sizeof(int));
}

int main(void)
{
    allocateBuffer();    /* First allocation */

    allocateBuffer();    /* Previous allocation is leaked */

    free(buffer);        /* Frees only the second allocation */

    return 0;
}
```

After the first call to `allocateBuffer()`, `buffer` points to an allocated memory block. During the second call, `buffer` is assigned the address of a new memory block without first releasing the original one.

As a result, the first memory block becomes unreachable and cannot be freed, causing a **memory leak**. Only the second allocation is released when `free(buffer)` is called.

---

## <font color='green'>Scenario 5: Forgetting to Free Dynamic Data Structures</font>

Memory leaks become more common when working with **dynamic data structures** such as linked lists, trees, and graphs. These structures are built by repeatedly allocating memory for individual nodes.

When the data structure is no longer needed, **every dynamically allocated node must be released**. Freeing only the first node, or forgetting to free the structure altogether, leaves the remaining nodes allocated in the heap.

**Example**

```c
struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = malloc(sizeof(struct Node));
head->next = malloc(sizeof(struct Node));

/* ... Use the linked list ... */

free(head);      /* Second node is never freed */
```

<font color='red'> In this example, only the first node is released. The second node remains allocated, but no pointer refers to it after the first node is freed. </font> As a result, the second node becomes unreachable, causing a **memory leak**.

When using dynamic data structures, every node allocated with `malloc()` should eventually be released. For example, a linked list is typically freed by traversing the list and freeing each node one at a time.



---

## <font color='green'>Consequences of Memory Leaks</font>

A single memory leak may not immediately cause a program to fail. In fact, **if a short-lived program leaks a small amount of memory, the operating system typically reclaims the leaked memory when the program terminates.**

>However, memory leaks become a serious problem in **long-running applications** such as servers, databases, web browsers, and embedded systems. Every leaked memory block remains allocated for the lifetime of the program. As more memory leaks occur, the amount of available heap memory gradually decreases.

Over time, excessive memory leaks can lead to:

- Increased memory usage.
- Reduced system performance.
- Failure of future memory allocation requests.
- Program crashes or unexpected termination.

For this reason, every dynamically allocated memory block should eventually be released using `free()` once it is no longer needed.


---

## <font color='green'>Preventing Memory Leaks</font>

Although memory leaks are common, they can usually be avoided by following a few simple programming practices.

- **Release every allocated memory block.** Every successful call to `malloc()`, `calloc()`, or `realloc()` should eventually have a corresponding call to `free()`.

- **Do not lose the pointer.** Before assigning a new value to a pointer, ensure that any memory it currently references has already been released.

- **Free dynamic data structures completely.** When using linked lists, trees, or other dynamically allocated structures, every allocated node should be released before the program exits or the structure is discarded.

- **Set pointers to `NULL` after calling `free()`.** Although this does not prevent memory leaks, it helps avoid accidentally using a pointer that refers to memory that has already been released.

- **Use memory debugging tools.** Tools such as **Valgrind** and **AddressSanitizer (ASan)** can detect memory leaks and help identify where they occur during program execution.

By consistently following these practices, programmers can significantly reduce memory leaks and write safer, more reliable C programs.


---

## <font color='green'>Summary</font>

Unlike stack and global memory, **heap memory** is managed manually by the programmer. Every successful call to `malloc()`, `calloc()`, or `realloc()` allocates memory that remains reserved until it is explicitly released using `free()`.

A **memory leak** occurs whenever allocated heap memory becomes **unreachable before it is freed**. This can happen in several ways, including:

- Forgetting to call `free()`.
- Losing the only pointer to the allocated memory.
- Overwriting a pointer before releasing the memory it references.
- Reassigning global pointers without freeing the previous allocation.
- Failing to release every dynamically allocated node in data structures such as linked lists and trees.

Although small memory leaks may not immediately affect short-lived programs, repeated leaks in long-running applications can gradually consume available memory, reduce performance, and eventually cause allocation failures or program crashes.

By carefully managing dynamically allocated memory and ensuring that every allocation has a corresponding `free()`, programmers can avoid memory leaks and build efficient, reliable C programs.

> <font color='red'>Memory leaks become particularly challenging when working with complex dynamic data structures such as linked lists, trees, and graphs. These structures often consist of many interconnected dynamically allocated nodes, making it easy to overlook one or more allocations during cleanup. As a result, ensuring that every allocated node is properly released can become a difficult programming task.</font>


---
**Relevant Links**

[Understanding Memory Types in C: Stack, Heap, and Global Memory](stackheap.md)


