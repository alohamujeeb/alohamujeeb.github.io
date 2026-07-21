---
hide:
  - navigation
  
tags:
  - Undefined Behavious
  
---

# Undefined Behaviour in C
*This article is intended for intermediate and advanced C programmers. It explains what undefined behaviour is, why it occurs, how compiler optimizations are affected by it, and how to write reliable C programs that avoid invoking undefined behaviour.*

---
## <font color='green'>1. What is Undefined Behaviour?</font>

The C language standard defines the behaviour of most language constructs precisely. However, <font color='red'>there are certain situations where the standard intentionally imposes **no requirements** on how a program should behave</font>. Such situations are known as **undefined behaviour (UB)**.

When a program executes code that results in undefined behaviour, the C standard no longer guarantees the outcome. The program may appear to work correctly, produce unexpected results, crash, or exhibit entirely different behaviour depending on the compiler, optimization level, or target architecture.

Understanding undefined behaviour is essential for writing reliable, portable, and predictable C programs. The following sections examine what "undefined" actually means, how it differs from other forms of implementation-dependent behaviour, and some of the most common sources of undefined behaviour in C.

For example, consider the following program:

```c
#include <stdio.h>

int main(void)
{
    int numbers[5] = {10, 20, 30, 40, 50};

    printf("%d\n", numbers[10]);

    return 0;
}
```

The array `numbers` contains **five elements**, with valid indices ranging from `0` to `4`. Accessing `numbers[10]` is **out of bounds** and results in **undefined behaviour**.

Although the program will typically compile without any errors or warnings, its behaviour is not defined by the C standard. It may print an unexpected value, appear to work correctly, crash, or produce different results when compiled with another compiler or optimization level.

---
## <font color='green'>2. Common Examples of Undefined Behaviour</font>

Undefined behaviour can occur in many different situations. Some of the most common examples include:

| Undefined Behaviour | Description |
|----------------------|-------------|
| Array out-of-bounds access | Accessing an element outside the valid range of an array. |
| Dereferencing a null pointer | Attempting to read from or write to a `NULL` pointer. |
| Dereferencing a dangling pointer | Accessing memory through a pointer that no longer refers to a valid object. |
| Using an uninitialized variable | Reading the value of a local variable before it has been initialized. |
| Signed integer overflow | Producing a value outside the range of a signed integer type. |
| Division by zero | Dividing an integer by zero. |
| Invalid shift operations | Shifting by a negative amount or by an amount greater than or equal to the width of the type. |
| Modifying an object multiple times in one expression | For example, `i = i++ + 1;`. |

These examples represent only a subset of the situations that result in undefined behaviour. The C standard defines many other operations as undefined, and programmers should always consult the language specification or compiler documentation when in doubt.


---
## <font color='green'>3. Why Undefined Behaviour Is Dangerous</font>

- **One of the biggest dangers of undefined behaviour is that a program may appear to work correctly** during development and testing. This can give programmers a false sense of confidence that the code is correct when, in reality, it relies on behaviour that is not defined by the C standard.

- **Undefined behaviour can also produce different results depending on the compiler, optimization level, operating system, or processor architecture**. A program that appears to work on one system may fail unexpectedly on another without any changes to the source code.

- Modern compilers further increase the risk by performing aggressive optimizations. Because the C standard allows compilers to assume that undefined behaviour never occurs, they may reorder, eliminate, or transform code in ways that produce surprising results when undefined behaviour is present.

For these reasons, undefined behaviour is often difficult to detect and debug. The error may not appear immediately and can manifest itself far from the point where the undefined behaviour actually occurred.

> To write reliable, portable, and maintainable C programs, undefined behaviour should always be treated as a programming error and avoided whenever possible.



---
## <font color='green'>4. How to Avoid Undefined Behaviour</font>

Although undefined behaviour cannot always be detected by the compiler, many programming practices can significantly reduce the risk of introducing it into a program.

Some recommended practices include:

- Always initialize variables before using them.
- Ensure that array indices remain within valid bounds.
- Never dereference `NULL` or invalid pointers.
- Avoid using pointers after the memory they reference has been freed.
- Check for arithmetic operations that may overflow or divide by zero.
- Be cautious when performing pointer arithmetic.
- Compile with compiler warnings enabled and address any reported issues.
- Use static analysis tools and runtime sanitizers when available to detect potential problems during development.

Perhaps the most important practice is to write code that strictly follows the rules defined by the C standard. Code that relies on compiler-specific behaviour or assumptions may appear to work on one system but fail unexpectedly on another.

By following good programming practices and understanding the situations that lead to undefined behaviour, developers can write C programs that are more reliable, portable, and easier to maintain.

---
## <font color='green'>5. Summary</font>

Undefined behaviour is one of the most important concepts for every C programmer to understand. It occurs when a program performs an operation for which the C standard defines no required behaviour.

Unlike syntax or compilation errors, undefined behaviour often goes undetected during compilation and may even appear to work correctly during testing. However, once it occurs, the program's behaviour is no longer predictable and may vary between compilers, optimization levels, or hardware platforms.

By recognizing common sources of undefined behaviour and following good programming practices, developers can write C programs that are more reliable, portable, and maintainable.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
