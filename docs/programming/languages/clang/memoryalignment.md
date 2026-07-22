---
hide:
  - navigation
  
tags:
  - Memory Alignment
  - Padding
  
---


# Memory Alignment and Padding in C

*This article is intended for intermediate and advanced C programmers. It explains the concepts of memory alignment and structure padding, why modern processors require aligned memory access, how compilers insert padding into structures, and how alignment affects memory usage, performance, and embedded software design.*

---
## <font color='green'>1. Why is Memory Alignment Needed?</font>

Modern processors access memory more efficiently when data is stored at certain memory addresses. These addresses are called **aligned addresses**. <font color='red'> the actual reason lies in digital hardware design, which we do not go into details here </font>

For example, a processor may prefer that:

- A 2-byte object begins at an address divisible by 2.
- A 4-byte object begins at an address divisible by 4.
- An 8-byte object begins at an address divisible by 8.

> When data is stored at these addresses, the processor can usually **read or write the entire object with a single memory access.**

>If the data begins at an unaligned address, the processor may need multiple memory accesses to retrieve the same object. On some processors, unaligned accesses are slower, while on others they may even generate a hardware exception.

To avoid these problems, compilers automatically arrange data so that each object starts at an address that satisfies its alignment requirement. This process is known as **memory alignment**.

When structures contain members with different alignment requirements, the compiler may insert unused bytes between members. These unused bytes are called **padding**, and they ensure that each member is correctly aligned.

## **Example**

When working with structures in C, programmers often assume that the size of a structure is simply the sum of the sizes of its individual members. However, this is not always the case.

For example,

```c
struct Example
{
    char c;
    int i;
};
```

At first glance, it appears that the size of this structure should be:

- `char` : 1 byte
- `int` : 4 bytes

Therefore, many programmers expect the structure to occupy **5 bytes**.

However, on most modern systems,

```c
sizeof(struct Example)
```

returns **8 bytes**, not **5 bytes**.

A simplified view of the memory layout is shown below.

```text
Byte Offset

+------+------+------+------+------+------+------+------+
|  c   | Pad  | Pad  | Pad  |          i                |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

> The three unused bytes are known as **padding**. They are automatically inserted by the compiler to satisfy the memory alignment requirements of the target processor.

---
## <font color='green'>2. Alignment Requirements of Data Types</font>

Every data type has an **alignment requirement**, which specifies the memory address at which an object of that type should begin.

On many systems, the alignment requirement is equal to the size of the data type, although this is **not guaranteed by the C standard** and may vary depending on the processor and compiler.

For example, a typical system may have the following alignment requirements:

| Data Type | Size (bytes) | Typical Alignment (bytes) |
|-----------|-------------:|--------------------------:|
| `char`    | 1 | 1 |
| `short`   | 2 | 2 |
| `int`     | 4 | 4 |
| `float`   | 4 | 4 |
| `double`  | 8 | 8 |


The C11 standard introduced the `_Alignof` operator, which can be used to determine the alignment requirement of a data type.

```c
printf("%zu\n", _Alignof(int));
printf("%zu\n", _Alignof(double));
```

On a typical system, this might produce:

```text
4
8
```

This means:

- A `char` object can begin at **any** memory address.
- A `short` object should begin at an address divisible by **2**.
- An `int` or `float` should begin at an address divisible by **4**.
- A `double` should begin at an address divisible by **8**.



The following diagram illustrates this concept.

```text
Memory Addresses

          0    1    2    3    4    5    6    7    8
          |----|----|----|----|----|----|----|----|

char   :  ✓    ✓    ✓   ✓    ✓    ✓    ✓    ✓    ✓
short  :  ✓         ✓         ✓         ✓
int    :  ✓                   ✓                   ✓
double :  ✓                                       ✓
```

The ✓ marks indicate the addresses at which each data type would typically be aligned.

The compiler uses these alignment requirements when laying out variables and structures in memory. If a member would otherwise begin at an address that does not satisfy its alignment requirement, the compiler inserts **padding bytes** before that member.


> The alignment values shown in this article are typical for many 32-bit and 64-bit systems, but they may differ depending on the processor architecture, ABI, and compiler.

---
## <font color='green'>3. Structure Padding</font>

Let's revisit the structure introduced earlier.

```c
struct Example
{
    char c;
    int i;
};
```

The `char` member occupies only one byte, so it is placed at offset **0**.

```text
Byte Offset

+------+
|  c   |
+------+
   0
```

The next available byte is offset **1**. However, the `int` member typically requires **4-byte alignment**, which means it should begin at an address divisible by **4**.

Since offset **1** is not divisible by **4**, the compiler inserts three padding bytes before the `int` member.

```text
Byte Offset

+------+------+------+------+------+------+------+------+
|  c   | Pad  | Pad  | Pad  |          i         |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

As a result:

- `c` occupies offset **0**.
- Padding occupies offsets **1**, **2**, and **3**.
- `i` begins at offset **4**, satisfying its alignment requirement.

Consequently,

```c
sizeof(struct Example)
```

returns **8 bytes** instead of **5 bytes**.

Notice that the padding bytes do not belong to any structure member. They are inserted solely to ensure that the `int` member starts at a properly aligned memory address.

---
### **3.1 How Member Order Affects Padding**

The amount of padding inserted into a structure depends on the order in which its members are declared.

Consider the following structures.

**Example 1**

```c
struct Example1
{
    char c;
    int i;
};
```

Memory layout:

```text
+------+------+------+------+------+------+------+------+
|  c   | Pad  | Pad  | Pad  |          i         |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

```c
sizeof(struct Example1) == 8
```

---

**Example 2**

```c
struct Example2
{
    int i;
    char c;
};
```

Memory layout:

```text
+------+------+------+------+------+------+------+------+
|          i         |  c   | Pad  | Pad  | Pad  |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

```c
sizeof(struct Example2) == 8
```

Although the padding has moved to the end of the structure, the total size remains **8 bytes**.

---

**Example 3**

```c
struct Example3
{
    char  c1;
    char  c2;
    int   i;
};
```

Memory layout:

```text
+------+------+------+------+------+------+------+------+
| c1   | c2   | Pad  | Pad  |          i         |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

```c
sizeof(struct Example3) == 8
```

Since the two `char` members occupy the first two bytes, only **two** padding bytes are required before the `int`.

These examples show that **the order of structure members directly affects where padding is inserted and how much padding is required**.

In the next section, we will see how simply rearranging the members of a structure can reduce padding and improve memory utilization.

### 3.2 Reducing Padding by Reordering Members

In many cases, the amount of padding in a structure can be reduced simply by changing the order of its members.

Consider the following structure.

```c
struct Example1
{
    char  c;
    int   i;
    short s;
};
```

A typical memory layout is shown below.

```text
+------+------+------+------+------+------+------+------+------+------+
|  c   | Pad  | Pad  | Pad  |          i         |    s     | Pad  |
+------+------+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7      8      9
                                                   10     11
```

```c
sizeof(struct Example1) == 12
```

Now consider the same members arranged differently.

```c
struct Example2
{
    int   i;
    short s;
    char  c;
};
```

Its memory layout becomes:

```text
+------+------+------+------+------+------+------+------+
|          i         |    s     |  c   | Pad  |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

```c
sizeof(struct Example2) == 8
```

Simply reordering the members has reduced the structure size from **12 bytes** to **8 bytes**.

A common guideline is to declare structure members from the **largest alignment requirement to the smallest**. Although this does not always produce the smallest possible structure, it often minimizes padding and improves memory utilization.

---
## <font color='green'>4. Tail Padding and Arrays of Structures</font>

In the previous examples, we saw that padding may appear **between** structure members. However, the compiler may also insert padding **at the end** of a structure. This is known as **tail padding**.

Consider the following structure.

```c
struct Example
{
    int   i;
    short s;
    char  c;
};
```

The memory layout is shown below.

```text
+------+------+------+------+------+------+------+------+
|          i         |    s     |  c   | Pad  |
+------+------+------+------+------+------+------+------+
  0      1      2      3      4      5      6      7
```

Although the members occupy only **7 bytes**, the structure size is **8 bytes**.

```c
sizeof(struct Example) == 8
```

The final padding byte is called **tail padding**.

### Why is Tail Padding Needed?

Tail padding ensures that every element in an array of structures begins at the proper alignment boundary.

For example,

```c
struct Example arr[3];
```

The memory layout of the array is shown below.

```text
           Structure 0              Structure 1              Structure 2

+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------++
|          i         |    s     |  c   | Pad  |          i         |    s     |  c   | Pad  |          i         |    s     |  c   | Pad  |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------++
```

Notice that every structure begins at an address that is a multiple of **4**. As a result, the `int` member of every structure is naturally aligned.

If the compiler did **not** insert the tail padding, the second structure would begin immediately after the seventh byte of the first structure. Its `int` member would then be misaligned, defeating the purpose of alignment.

Therefore, tail padding is inserted to ensure that every element in an array of structures satisfies the alignment requirements of its members.


---
## <font color='green'>5. Packed Structures</font>

By default, the compiler inserts padding bytes to satisfy the alignment requirements of the target processor. In some applications, however, it is desirable to remove this padding so that the structure occupies the minimum possible memory.

Such structures are known as **packed structures**.

Many compilers provide extensions to disable padding. For example,

```c
#pragma pack(push, 1)

struct Example
{
    char c;
    int  i;
};

#pragma pack(pop)
```

or

```c
struct __attribute__((packed)) Example
{
    char c;
    int  i;
};
```

With packing enabled, the memory layout becomes:

```text
+------+------+------+------+------+
|  c   |          i               |
+------+------+------+------+------+
  0      1      2      3      4
```

Now,

```c
sizeof(struct Example) == 5
```

because no padding bytes are inserted.

### **Should Packed Structures Always Be Used?**

<font color='red'>The answer is **No**.</font>

Removing padding may reduce memory usage, but it also causes some members to become unaligned. As discussed earlier, unaligned memory accesses can:

- Reduce performance.
- Require multiple memory accesses.
- Cause hardware exceptions on some processors.

Therefore, packed structures should be used only when the exact memory layout is more important than performance.

Typical applications include:

- Communication protocols.
- Network packets.
- File formats.
- Memory-mapped hardware registers (when required by the hardware specification).

For ordinary application code, allowing the compiler to insert padding is usually the best choice because it produces structures that are naturally aligned and efficient to access.


---
## <font color='green'>6. Summary</font>

- Modern processors access memory more efficiently when data is stored at aligned addresses.
- Every data type has an alignment requirement that determines where it should begin in memory.
- To satisfy these alignment requirements, the compiler may insert unused bytes called **padding**.
- The amount of padding depends on the order of the members within a structure.
- Reordering structure members can often reduce padding and decrease the overall structure size.
- The compiler may also insert **tail padding** so that every element of an array of structures begins at a properly aligned address.
- Packed structures remove padding but may result in slower memory accesses or hardware exceptions on some processors.
- For most applications, allowing the compiler to insert padding produces the best balance between correctness and performance.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory management, pointers, embedded C programming etc.)
