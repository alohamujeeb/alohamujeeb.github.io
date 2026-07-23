---
hide:
  - navigation
  
tags:
  - Memory Pool
  
---
# Memory Pool in C

*This article is intended for intermediate and advanced C programmers. It explains what memory pools are, why they are used as an alternative to general-purpose dynamic memory allocation, and how they provide fast, predictable, and efficient memory management in performance-critical applications.*

---
## <font color='green'>1. What Is a Memory Pool?</font>

- Dynamic memory allocation using `malloc()` and `free()` is convenient and flexible, making it suitable for many applications. 
- However, repeatedly allocating and deallocating small memory blocks can become inefficient, introduce memory fragmentation, and produce unpredictable execution times. 
- **A Memory Pool addresses these issues by preallocating a large block of memory and managing allocations from that block.**

Consider a program that repeatedly creates and destroys objects.

```c
Student *s = malloc(sizeof(Student));

...

free(s);
```

Every time an object is needed, the program requests memory from the heap.

```
Application

malloc() ───────────────► Heap

free()   ◄───────────────
```

For a few allocations, this approach works perfectly.

However, applications such as embedded systems, network servers, game engines, and real-time software may perform thousands or even millions of allocations during execution.

```
malloc()
malloc()
malloc()
free()
malloc()
free()
malloc()
malloc()
...
```

Each allocation requires the memory allocator to search for a suitable free block, maintain internal bookkeeping information, and eventually reclaim the memory when `free()` is called.

As the number of allocations increases, this can lead to:

- increased allocation overhead,
- memory fragmentation,
- unpredictable allocation times.

### **Solution: Create a Memory Pool**

**In many applications, the maximum amount of memory required is already known.**

For example, suppose an application will never need more than 100 student objects simultaneously.

Instead of repeatedly allocating and freeing memory,

```c
Student *s = malloc(sizeof(Student));

...

free(s);
```

the program can reserve memory for all 100 students when it starts.

```c
Student *pool = malloc(100 * sizeof(Student));

if (pool == NULL)
{
    /* Handle allocation failure */
}
```

This single allocation creates space for 100 student objects.

```text
+-------------------------------------------------------------+
|                     Memory Pool                             |
+-------------------------------------------------------------+
| Student | Student | Student | Student | Student | ...       |
+-------------------------------------------------------------+
```

Whenever a new student object is required, memory is taken directly from the pool.

```
+---------+---------+---------+---------+---------+
|   Free  |   Used  |   Free  |   Free  |   Used  |
+---------+---------+---------+---------+---------+
```

When an object is no longer needed, it is simply returned to the pool instead of being released back to the operating system.

> Conceptually, a Memory Pool is nothing more than a **memory manager built on top of a preallocated block of memory**.

Instead of requesting memory from the heap every time,

```
Application
      │
      ▼
malloc()
      │
      ▼
Heap
```

the application requests memory from its own pool.

```
Application
      │
      ▼
Memory Pool
      │
      ▼
Preallocated Memory
```

The operating system is involved only once—when the pool itself is created.

All subsequent allocations and deallocations are handled by the Memory Pool, making them significantly faster and more predictable than repeated calls to `malloc()` and `free()`.

The following section explains the basic design of a Memory Pool, including how memory is organized into reusable blocks and how free blocks are managed.

---
## <font color='green'>2. Basic Design of a Memory Pool</font>

A Memory Pool is simply a large block of memory that is divided into smaller blocks of equal size. Each block can be allocated to the application when needed and returned to the pool when it is no longer in use.

For example, suppose we reserve memory for 100 `Student` objects.

```c
Student *pool = malloc(100 * sizeof(Student));
```

The memory layout looks like this:

```text
+-----------------------------------------------------------------------+
| Student | Student | Student | Student | Student | ... | Student       |
+-----------------------------------------------------------------------+
```

Initially, every block is available.

```text
+---------+---------+---------+---------+---------+
|  Free   |  Free   |  Free   |  Free   |  Free   |
+---------+---------+---------+---------+---------+
```

As the application requests memory, blocks are marked as being in use.

```text
+---------+---------+---------+---------+---------+
|  Used   |  Free   |  Used   |  Free   |  Used   |
+---------+---------+---------+---------+---------+
```

When an object is no longer needed, the block is simply returned to the pool.

```text
+---------+---------+---------+---------+---------+
|  Used   |  Free   |  Free   |  Free   |  Used   |
+---------+---------+---------+---------+---------+
```

Notice that no memory is returned to the operating system. The block merely changes from **Used** back to **Free**, making it available for future allocations.

### **Fixed-Size Blocks**

Most memory pools divide memory into blocks of a fixed size.

```text
+---------+---------+---------+---------+
| 64 B    | 64 B    | 64 B    | 64 B    |
+---------+---------+---------+---------+
```

If each `Student` object occupies 64 bytes, then every block can store exactly one `Student`.

This greatly simplifies memory management because every allocation and deallocation involves exactly one block.

### **Tracking Free Blocks**

A Memory Pool must keep track of which blocks are available and which are currently allocated.

Conceptually, each block exists in one of two states.

```text
+---------+
|  Free   |
+---------+

or

+---------+
|  Used   |
+---------+
```

Whenever the application requests memory,

```c
Student *s = pool_alloc(...);
```

the pool locates a free block, marks it as used, and returns its address.

```text
Before Allocation

+---------+---------+---------+
|  Free   |  Used   |  Free   |
+---------+---------+---------+

           │
           ▼

After Allocation

+---------+---------+---------+
|  Used   |  Used   |  Free   |
+---------+---------+---------+
```

Similarly, when the application releases an object,

```c
pool_free(s);
```

the block is marked as free again.

```text
Before Deallocation

+---------+---------+---------+
|  Used   |  Used   |  Free   |
+---------+---------+---------+

           │
           ▼

After Deallocation

+---------+---------+---------+
|  Free   |  Used   |  Free   |
+---------+---------+---------+
```

Exactly how the pool keeps track of free blocks depends on its implementation. Common techniques include free lists, bitmaps, and allocation tables. Regardless of the technique used, the underlying idea remains the same: memory is allocated from a preallocated pool and returned to that same pool for reuse.

---
## <font color='green'>3. Implementing a Simple Memory Pool</font>

Now that we understand the basic design of a Memory Pool, let's implement a simple fixed-size memory pool capable of storing `Student` objects.

For simplicity, the pool will:

- allocate memory only once,
- divide the memory into fixed-size blocks,
- allow blocks to be allocated and returned,
- never request additional memory from the heap.

### Designing the Memory Pool

Suppose we want the pool to store up to 100 students.

```c
#define POOL_SIZE   100

typedef struct
{
    int id;
    char name[50];
} Student;

typedef struct
{
    Student pool[POOL_SIZE];
    bool used[POOL_SIZE];
} StudentPool;
```

The pool contains two arrays:

- `pool` stores the actual student objects.
- `used` indicates whether each object is currently allocated.

Initially, every entry in `used` is `false`.

```
pool

+----+----+----+----+----+
| S0 | S1 | S2 | S3 | S4 |
+----+----+----+----+----+

used

+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
```

---

### Initializing the Pool

Before the pool can be used, every block must be marked as free.

```c
void pool_init(StudentPool *p)
{
    for (int i = 0; i < POOL_SIZE; i++)
    {
        p->used[i] = false;
    }
}
```

After initialization,

```
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
```

every block is available for allocation.

---

### Allocating an Object

Allocation simply searches for the first free block.

```c
Student *pool_alloc(StudentPool *p)
{
    for (int i = 0; i < POOL_SIZE; i++)
    {
        if (!p->used[i])
        {
            p->used[i] = true;
            return &p->pool[i];
        }
    }

    return NULL;
}
```

Suppose the first free block is selected.

```
Before

+-----+-----+-----+-----+-----+
|  F  |  T  |  F  |  F  |  T  |
+-----+-----+-----+-----+-----+

        │
        ▼

After

+-----+-----+-----+-----+-----+
|  T  |  T  |  F  |  F  |  T  |
+-----+-----+-----+-----+-----+
```

The function returns the address of the allocated object.

```c
Student *s = pool_alloc(&studentPool);

if (s != NULL)
{
    s->id = 1;
}
```

If every block is already in use,

```text
+-----+-----+-----+-----+-----+
|  T  |  T  |  T  |  T  |  T  |
+-----+-----+-----+-----+-----+
```

the function returns

```c
NULL
```

indicating that the pool is full.

---

### Returning an Object

Unlike `free()`, returning an object to the pool simply marks the corresponding block as available again.

```c
void pool_free(StudentPool *p, Student *student)
{
    int index = student - p->pool;

    p->used[index] = false;
}
```

Suppose block 2 is returned.

```
Before

+-----+-----+-----+-----+-----+
|  T  |  T  |  T  |  F  |  T  |
+-----+-----+-----+-----+-----+

        │
        ▼

After

+-----+-----+-----+-----+-----+
|  T  |  T  |  F  |  F  |  T  |
+-----+-----+-----+-----+-----+
```

The object is now available for reuse by future calls to `pool_alloc()`.

---

This implementation demonstrates the fundamental idea behind a Memory Pool. Although it uses a simple boolean array to track free blocks, the allocation and deallocation process requires no calls to `malloc()` or `free()` after the pool has been initialized.

In practice, more sophisticated memory pools often replace the boolean array with a free list or other data structures to achieve constant-time allocation and deallocation.


---
## <font color='green'>4. Allocation Strategies</font>

The previous section implemented a simple Memory Pool using an array of boolean values to indicate whether a block was free or in use.

Although easy to understand, this approach requires scanning the entire pool to locate a free block.

```c
for (int i = 0; i < POOL_SIZE; i++)
{
    if (!pool->used[i])
    {
        ...
    }
}
```

As the pool grows larger, the time required to find a free block also increases.

For this reason, practical memory pools use more efficient allocation strategies.

### Boolean Array

The simplest approach is to maintain a separate array indicating whether each block is available.

```text
Pool

+----+----+----+----+----+
| B0 | B1 | B2 | B3 | B4 |
+----+----+----+----+----+

Used

+-----+-----+-----+-----+-----+
|  T  |  F  |  T  |  F  |  F  |
+-----+-----+-----+-----+-----+
```

During allocation, the allocator searches for the first entry marked `false`.

Advantages:

- Simple to implement
- Easy to understand
- Suitable for small pools

Disadvantages:

- Requires searching the array
- Allocation time increases as the pool grows

---

### Free List

A more efficient technique is to maintain a **free list**.

Instead of searching every block, each free block stores a pointer to the next available block.

Initially,

```text
Free List

+----+     +----+     +----+     +----+
| B0 | --> | B1 | --> | B2 | --> | B3 | --> NULL
+----+     +----+     +----+     +----+
```

Allocation simply removes the first block from the list.

```text
Before

Head
 |
 v
+----+ --> +----+ --> +----+
| B0 |     | B1 |     | B2 |
+----+     +----+     +----+

After

Head
 |
 v
+----+ --> +----+
| B1 |     | B2 |
+----+     +----+

Allocated: B0
```

Returning a block is equally simple.

The block is inserted back at the beginning of the list.

```text
Before

Head
 |
 v
+----+ --> +----+
| B1 |     | B2 |
+----+     +----+

Return B0

Head
 |
 v
+----+ --> +----+ --> +----+
| B0 |     | B1 |     | B2 |
+----+     +----+     +----+
```

Since no searching is required, both allocation and deallocation execute in constant time.

---

### Fixed-Size vs Variable-Size Pools

Most memory pools use **fixed-size blocks**.

```text
+--------+--------+--------+--------+
| 64 B   | 64 B   | 64 B   | 64 B   |
+--------+--------+--------+--------+
```

Every allocation returns exactly one block.

This design is simple, efficient, and commonly used for objects of the same type.

Some applications, however, require objects of different sizes.

For example,

```text
32 B
128 B
256 B
512 B
```

Supporting variable-sized allocations significantly increases the complexity of the allocator because it must locate suitably sized free regions and manage block splitting and merging.

Many allocators therefore maintain multiple fixed-size pools instead of a single variable-size pool.

For example,

```text
Pool A → 32-byte blocks

Pool B → 64-byte blocks

Pool C → 128-byte blocks

Pool D → 256-byte blocks
```

When memory is requested, the allocator selects the smallest pool capable of satisfying the request.

This combines the simplicity of fixed-size pools with the flexibility of supporting different allocation sizes.

---

### Pool Expansion

Some memory pools have a fixed capacity.

```text
+----+----+----+----+
| B0 | B1 | B2 | B3 |
+----+----+----+----+
```

Once every block is allocated, additional allocation requests fail.

```c
Student *s = pool_alloc(pool);

if (s == NULL)
{
    /* Pool exhausted */
}
```

Other implementations allow the pool to expand by allocating another group of blocks.

```text
Pool 1

+----+----+----+----+

        +

Pool 2

+----+----+----+----+
```

This approach increases flexibility while still preserving the advantages of pool-based allocation.

---

Different allocation strategies involve different trade-offs between simplicity, memory overhead, allocation speed, and scalability. For small embedded systems, a simple fixed-size pool may be sufficient. Larger systems often use free lists and multiple fixed-size pools to provide predictable, constant-time allocation with minimal fragmentation.

---
## <font color='green'>5. Advantages and Limitations</font>

Memory Pools provide an efficient alternative to general-purpose dynamic memory allocation, particularly when objects are frequently created and destroyed. However, like any memory management technique, they involve trade-offs and are not suitable for every application.

### **Advantages**

#### Fast Allocation and Deallocation

Since memory has already been reserved, allocating an object simply involves selecting a free block.

```c
Student *s = pool_alloc(&pool);
```

Similarly, deallocation only returns the block to the pool.

```c
pool_free(&pool, s);
```

No calls to `malloc()` or `free()` are required after the pool has been initialized, making allocation significantly faster.

---

#### Predictable Execution Time

General-purpose memory allocators may require varying amounts of time depending on the state of the heap.

A Memory Pool, especially one implemented using a free list, typically performs allocation and deallocation in constant time.

```text
pool_alloc()

        ↓

Free List

B0 → B1 → B2 → ...
```

This predictable behavior makes Memory Pools particularly suitable for:

- embedded systems,
- real-time applications,
- game engines,
- network servers.

---

#### Reduced Memory Fragmentation

General-purpose heaps may become fragmented after repeated allocations and deallocations of varying sizes.

```text
+----+----+----+----+----+----+
|Used|Free|Used|Free|Used|Free|
+----+----+----+----+----+----+
```

Memory Pools avoid this problem by repeatedly reusing the same preallocated blocks.

```text
+----+----+----+----+----+----+
|Free|Used|Free|Used|Free|Used|
+----+----+----+----+----+----+
```

Since block sizes are fixed, fragmentation is greatly reduced or eliminated.

---

#### Improved Cache Locality

Objects allocated from the same pool are typically located close together in memory.

```text
+----+----+----+----+----+
|Obj1|Obj2|Obj3|Obj4|Obj5|
+----+----+----+----+----+
```

This often improves CPU cache performance compared to allocations scattered throughout the heap.

---

### **Limitations**

#### Fixed Capacity

A Memory Pool has a limited number of blocks.

```text
+----+----+----+----+
|Used|Used|Used|Used|
+----+----+----+----+
```

Once every block has been allocated,

```c
Student *s = pool_alloc(&pool);
```

returns

```c
NULL
```

unless the implementation supports pool expansion.

---

#### Potential Memory Waste

If a pool is much larger than necessary, unused blocks remain reserved for the lifetime of the pool.

For example, allocating space for 1,000 objects when only 100 are ever used results in unnecessary memory consumption.

---

#### Fixed Block Size

Most Memory Pools allocate blocks of a single size.

```text
64 B

64 B

64 B

64 B
```

If an object is smaller than the block size, some memory is wasted.

If an object is larger than the block size, it cannot be allocated from that pool.

Supporting multiple object sizes usually requires multiple pools or a more sophisticated allocator.

---

#### Increased Implementation Complexity

Using `malloc()` and `free()` requires little effort because memory management is handled by the standard library.

A Memory Pool, however, must implement its own:

- initialization,
- allocation,
- deallocation,
- free block management,
- error handling.

Although conceptually simple, maintaining a custom allocator introduces additional implementation and testing effort.

---

Memory Pools are most beneficial when:

- many objects of similar size are allocated,
- allocation speed is important,
- predictable execution time is required,
- memory fragmentation must be minimized.

For general-purpose applications with infrequent allocations or objects of widely varying sizes, the standard heap allocator is often the simpler and more appropriate choice.

---
## <font color='green'>6. Summary</font>

Memory Pools provide an efficient alternative to general-purpose dynamic memory allocation by reserving a block of memory in advance and reusing it throughout the lifetime of an application.

Instead of repeatedly calling `malloc()` and `free()`, allocations are satisfied from a preallocated pool of memory, resulting in faster and more predictable performance.

The key ideas presented in this article are:

- A Memory Pool allocates a large block of memory once and divides it into smaller reusable blocks.
- Objects are allocated from the pool and returned to the same pool when no longer needed.
- Fixed-size blocks simplify memory management and help reduce memory fragmentation.
- Different allocation strategies, such as boolean arrays and free lists, offer different trade-offs between simplicity and performance.
- Memory Pools are particularly useful for applications that require frequent allocation and deallocation of objects with predictable timing.

Memory Pools are widely used in systems where performance and deterministic behavior are important, including:

- Embedded systems
- Real-time software
- Game engines
- Network servers
- High-performance libraries

Although they offer significant advantages, Memory Pools also have limitations. Choosing an appropriate pool size, managing free blocks, and supporting objects of different sizes require careful design. For many general-purpose applications, the standard heap allocator remains the simplest and most flexible choice.

Understanding Memory Pools provides valuable insight into how memory allocators work internally and how specialized allocators can be designed for specific workloads. They are an excellent example of trading generality for speed, predictability, and efficient memory reuse.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
