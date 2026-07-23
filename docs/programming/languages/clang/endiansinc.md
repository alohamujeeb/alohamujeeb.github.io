---
hide:
  - navigation
  
tags:
  - Endians in C
  - Big Endian
  - Little Endians
  
---
# Endianness in C: Understanding Big-Endian and Little-Endian

*This article is intended for intermediate and advanced C programmers. It explains what endianness is, the difference between big-endian and little-endian byte ordering, why endianness matters when working with binary data, and how to detect the byte order of a system in C.*

---
## <font color='green'>1. What Is Endianness?</font>

Computers store data in memory as a sequence of bytes. For data types that occupy a single byte, such as `char`, the order of bytes is not important because there is only one byte to store.

However, multi-byte data types, such as `short`, `int`, `long`, `float`, and `double`, consist of two or more bytes. When storing these values in memory, the system must decide **the order in which the bytes are placed**.

This ordering of bytes is known as **endianness**.

For example, consider the following 32-bit integer.

```c
int value = 0x12345678;
```

The value consists of four bytes.

```text
+------+------+------+------+
| 0x12 | 0x34 | 0x56 | 0x78 |
+------+------+------+------+
```

When these bytes are stored in memory, there are two possible arrangements.

```text
Big-Endian

          Lower Address                     Higher Address
                │                                  │
                ▼                                  ▼
           +------+------+------+------+
Memory --> | 0x12 | 0x34 | 0x56 | 0x78 |
           +------+------+------+------+
              MSB                     LSB
```

```text
Little-Endian

          Lower Address                     Higher Address
                │                                  │
                ▼                                  ▼
           +------+------+------+------+
Memory --> | 0x78 | 0x56 | 0x34 | 0x12 |
           +------+------+------+------+
              LSB                     MSB
```

In both cases, the integer still has the value **0x12345678**. The only difference is **how its bytes are arranged in memory**.

Endianness affects **only the memory representation** of multi-byte objects. It does **not** change the numeric value itself.

Understanding endianness is important when exchanging binary data between different computer systems, reading or writing binary file formats, implementing communication protocols, or interpreting raw memory. 

> If two systems use different byte orders, multi-byte values must be interpreted using the correct byte ordering to ensure interoperability.

The next section examines the two byte-ordering schemes—**big-endian** and **little-endian**—in more detail.

---
## <font color='green'>2. Big-Endian vs Little-Endian</font>

As discussed in the previous section, there are two common ways to arrange the bytes of a multi-byte object in memory.

A system is said to be **big-endian** if it stores the **most significant byte (MSB)** at the lowest memory address. Conversely, a system is **little-endian** if it stores the **least significant byte (LSB)** at the lowest memory address.

The names simply describe **which end of the value appears first in memory**:

| Byte Order | First Byte Stored |
|------------|-------------------|
| Big-Endian | Most significant byte (MSB) |
| Little-Endian | Least significant byte (LSB) |

For example, consider the 32-bit integer:

```c
int value = 0x12345678;
```

Its four bytes are:

```text
+------+------+------+------+
| 0x12 | 0x34 | 0x56 | 0x78 |
+------+------+------+------+
```

A big-endian system stores these bytes in the same order, while a little-endian system stores them in reverse order.

```text
Big-Endian
Memory --> |12|34|56|78|

Little-Endian
Memory --> |78|56|34|12|
```

Modern desktop and server processors based on the **x86** and **x86-64** architectures use little-endian byte ordering. Some other processor architectures use big-endian byte ordering, while others can operate in either mode.

The next section explains why these different byte orders matter when exchanging binary data between systems.


## <font color='green'>3. Why Endianness Matters</font>

For most C programs, endianness is largely invisible. As long as data is created and consumed on the same system, the underlying byte order does not usually affect program behavior.

However, endianness becomes important whenever binary data is exchanged between systems or interpreted outside the process that created it.

### Binary File Formats

Many applications store data in binary files for efficiency. If a program writes multi-byte values directly to a file, the byte order of those values depends on the system's endianness.

For example, suppose a little-endian system writes the integer `0x12345678` to a binary file.

```text
Binary File

+------+------+------+------+
| 0x78 | 0x56 | 0x34 | 0x12 |
+------+------+------+------+
```

If the file is later read on a big-endian system without accounting for the different byte order, the value may be interpreted incorrectly.

To ensure interoperability, many binary file formats define a fixed byte order that all implementations must follow.

### Network Communication

When computers exchange binary data over a network, they must agree on how multi-byte values are represented.

If one system sends data using little-endian ordering while another expects big-endian ordering, the received values will be interpreted incorrectly unless the byte order is converted.

For this reason, communication protocols typically specify a standard byte order for transmitted data.

### Raw Memory Inspection

Endianness is also important when examining the memory representation of objects.

Tools such as debuggers, memory dump utilities, and hexadecimal editors display the actual bytes stored in memory. Understanding the system's byte order helps interpret these bytes correctly.

```text
Integer Value

0x12345678

Little-Endian Memory

+------+------+------+------+
| 0x78 | 0x56 | 0x34 | 0x12 |
+------+------+------+------+
```

Without knowledge of the system's endianness, the byte sequence shown in memory can easily be misinterpreted.

In the next section, we'll see how to determine a system's byte order using standard C.

---
## <font color='green'>4. Detecting Endianness in C</font>

A simple way to determine a system's byte order is to examine the memory representation of a multi-byte object.

The C Standard guarantees that the **object representation** of any object can be inspected through a pointer to `unsigned char`. Since an `unsigned char` occupies exactly one byte, examining successive bytes reveals how the object is stored in memory.

The following program determines whether the host system is big-endian or little-endian.

```c
#include <stdio.h>

int main(void)
{
    unsigned int value = 0x01020304;
    unsigned char *p = (unsigned char *)&value;

    if (p[0] == 0x01)
        printf("Big-endian\n");
    else if (p[0] == 0x04)
        printf("Little-endian\n");
    else
        printf("Unknown byte order\n");

    return 0;
}
```

The program initializes an integer with the value `0x01020304` and then examines its first byte in memory.

If the first byte is `0x01`, the most significant byte is stored first, indicating a **big-endian** system.

```text
          Lower Address                     Higher Address
                │                                  │
                ▼                                  ▼
           +------+------+------+------+
Memory --> | 0x01 | 0x02 | 0x03 | 0x04 |
           +------+------+------+------+
```

If the first byte is `0x04`, the least significant byte is stored first, indicating a **little-endian** system.

```text
          Lower Address                     Higher Address
                │                                  │
                ▼                                  ▼
           +------+------+------+------+
Memory --> | 0x04 | 0x03 | 0x02 | 0x01 |
           +------+------+------+------+
```

This technique is commonly used in diagnostic programs, debugging tools, and low-level software that needs to adapt its behavior based on the host system's byte ordering.

The final section summarizes the key concepts discussed in this article.

---
## <font color='green'>5. Endianness on Modern Architectures</font>

The byte order used by a program depends on the **target architecture**, not the C language itself.

- **Intel x86** and **x86-64** processors always use **little-endian** byte ordering.
- **ARM** processors typically operate in **little-endian** mode, which is the default on modern desktop, mobile, and embedded systems. However, the ARM architecture also supports **big-endian** operation on many implementations.
- Some architectures, such as **PowerPC** and **MIPS**, have implementations that support either **big-endian** or **little-endian** operation, while others support only one of the two.

Most modern personal computers, smartphones, and servers therefore use **little-endian** byte ordering.

It is important to note that endianness is determined by the target hardware (or its application binary interface), not by the C compiler. A compiler generates code that follows the byte order of the target platform.

---
## <font color='green'>6. Summary</font>

Endianness defines the order in which the bytes of a multi-byte object are stored in memory. While it has no effect on single-byte data types, it determines how data types such as `short`, `int`, `long`, `float`, and `double` are represented in memory.

This article introduced the two most common byte-ordering schemes:

- **Big-endian**, where the most significant byte is stored first.
- **Little-endian**, where the least significant byte is stored first.

Although the memory layouts differ, the numeric value represented by the object remains the same.

For most C programs, endianness is transparent because data is created and consumed on the same system. However, it becomes important when working with binary file formats, communication protocols, raw memory, or any application that exchanges binary data between systems with different byte orders.

Finally, you learned how to determine a system's byte order by examining the object representation of a multi-byte value through an `unsigned char *`, a technique commonly used in low-level and systems programming.

Understanding endianness is an essential part of writing portable C programs that correctly interpret binary data across different computer architectures.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
