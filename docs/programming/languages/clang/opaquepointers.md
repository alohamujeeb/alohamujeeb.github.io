---
hide:
  - navigation
  
tags:
  - Opaque Pointers
  
---
# Opaque Pointers in C

*This article is intended for intermediate and advanced C programmers. It explains what opaque pointers are, why they are used to hide implementation details, and how they help create modular and maintainable C libraries.*

---
## <font color='green'>1. What Are Opaque Pointers?</font>

An **opaque pointer** is a pointer to a type whose definition is intentionally hidden from the code using it.

Unlike many programming languages, C does not provide language features such as `private` or `protected` to hide the implementation of a data structure. Instead, C achieves information hiding by taking advantage of its separate compilation model, where a program is divided into multiple source files (`.c`) and header files (`.h`).

Typically:

- The **header file** exposes only the public interface.
- The **implementation file** contains the private implementation.

```text
            Application

            main.c
               │
               ▼
           #include "stack.h"

        +----------------------+
        | Public Interface     |
        | (stack.h)            |
        +----------------------+

               │

        +----------------------+
        | Private              |
        | Implementation       |
        | (stack.c)            |
        +----------------------+
```

Suppose we are writing a stack library.

Instead of exposing the entire structure in the header file, the header contains only a forward declaration.

```c
/* stack.h */

struct Stack;
typedef struct Stack Stack;
```

This tells the compiler that a type named `Stack` exists, but does **not** reveal its members.

Applications including `stack.h` can therefore declare pointers to `Stack`.

```c
Stack *stack;
```

This pointer is called an **opaque pointer** because the type it points to is **opaque**. Its internal representation is hidden from the application.

From the application's perspective, the object looks like this.

```text
Stack *stack
      │
      ▼
+----------------+
|     Stack      |
|      ???       |
+----------------+

The object exists, but its contents are unknown.
```

The actual structure definition is placed in the implementation file instead.

```c
/* stack.c */

struct Stack
{
    int data[100];
    int top;
};
```

Since `main.c` includes only `stack.h`, it never sees this definition.

As a result, the compiler compiling `main.c` knows that `Stack` exists, but does not know:

- its size,
- its members,
- or its memory layout.

Therefore, code such as

```c
stack->top = 0;
```

cannot be compiled because the compiler has never been shown a member named `top`.

The only way for the application to manipulate the object is through functions provided by the library.

```c
Stack *stack = stackCreate();

stackPush(stack, 10);
stackPop(stack);

stackDestroy(stack);
```

> In other words, an opaque pointer is simply a normal C pointer whose pointed-to type is intentionally hidden by placing its definition in a separate implementation file instead of the public header. This technique allows a library to expose a clean public interface while keeping its implementation private.

---
## <font color='green'>2. Creating an Opaque Type</font>

As explained in the previous section, an opaque pointer works because the structure's definition is **split across two files**:

- The **header file** exposes only the public interface.
- The **implementation file** contains the complete structure definition.

This separation prevents application code from knowing how the object is represented internally.

Consider the following header file.

```c
/* stack.h */

struct Stack;
typedef struct Stack Stack;

Stack *stackCreate(void);
void stackDestroy(Stack *stack);

void stackPush(Stack *stack, int value);
int stackPop(Stack *stack);
```

Notice that the header contains only a **forward declaration**.

```c
struct Stack;
```

A forward declaration informs the compiler that a structure named `Stack` exists somewhere, but does not provide its definition.

```text
Compiler Knows

✓ Type name exists
✓ Pointers to it are valid

Compiler Does NOT Know

✗ Size
✗ Members
✗ Memory layout
```

Because the compiler does not know the size of `Stack`, it cannot create an object of that type.

```c
Stack s;      /* Error */
```

However, it **can** create a pointer to `Stack`, because the size of a pointer is known regardless of what it points to.

```c
Stack *stack;     /* OK */
```

The complete definition of the structure is placed in the implementation file.

```c
/* stack.c */

struct Stack
{
    int data[100];
    int top;
};
```

When the compiler compiles `stack.c`, it sees both the forward declaration from `stack.h` and the structure definition above. Therefore, library functions can access the structure's members.

```c
void stackPush(Stack *stack, int value)
{
    stack->data[++stack->top] = value;
}
```

When the compiler compiles an application source file such as `main.c`, it sees only the contents of `stack.h`.

```text
Compiling main.c

#include "stack.h"

        │

        ▼

Compiler Sees

struct Stack;
typedef struct Stack Stack;

...

Compiler Never Sees

struct Stack
{
    int data[100];
    int top;
};
```

As a result, application code cannot access the structure's members.

```c
Stack *stack = stackCreate();

stack->top = 0;      /* Error */
```

The compiler rejects this statement because, while it knows that `stack` points to a `Stack` object, it has never been shown the definition of `struct Stack`.

By separating the public declaration from the private definition, a library exposes only what applications need to use the API while keeping its implementation hidden.

The next section demonstrates how an application uses an opaque pointer to interact with an object without ever knowing its internal representation.

---
## <font color='green'>3. Using an Opaque Pointer</font>

Once an opaque type has been created, an application interacts with the object exclusively through the library's public interface.

The application first obtains an opaque pointer, typically by calling a function that creates the object.

```c
Stack *stack = stackCreate();
```

Although `stack` is an ordinary pointer, the application has no knowledge of the object it points to.

```text
Application

Stack *stack
      │
      ▼
+------------------+
|   Stack Object   |
|        ?         |
|        ?         |
|        ?         |
+------------------+

The application's only handle to the object
is the opaque pointer.
```

Instead of accessing the object's members directly, the application passes the opaque pointer to library functions.

```c
stackPush(stack, 10);
stackPush(stack, 20);

int value = stackPop(stack);

stackDestroy(stack);
```

Each library function receives the opaque pointer and performs the requested operation.

```text
              Stack *stack
                    │
                    ▼
      +---------------------------+
      |     stackPush()           |
      |     stackPop()            |
      |     stackDestroy()        |
      +---------------------------+
                    │
                    ▼
          Hidden Stack Structure
```

From the application's perspective, the opaque pointer is simply a handle that identifies a particular object. The application never needs to know how that object is implemented.

Since the application's source file includes only the public header, attempting to access the structure directly results in a compilation error.

```c
stack->top = 0;      /* Error */
```

The compiler rejects this statement because it has never seen the definition of `struct Stack`.

The correct way to manipulate the object is through the library's API.

```c
Stack *stack = stackCreate();

stackPush(stack, 10);
stackPush(stack, 20);

while (!stackIsEmpty(stack))
{
    printf("%d\n", stackPop(stack));
}

stackDestroy(stack);
```

This approach gives the library complete control over the object's internal state. The application can create, use, and destroy the object, but it cannot accidentally modify its implementation details.

The next section discusses the advantages and limitations of using opaque pointers in C libraries.

---
## <font color='green'>4. Advantages and Limitations</font>

Opaque pointers are widely used in C libraries because they separate a library's public interface from its private implementation. This makes the library easier to maintain and allows its implementation to evolve without affecting application code.

However, this technique also introduces some trade-offs.

### Advantages

#### Information Hiding

The primary advantage of opaque pointers is that they hide the internal representation of an object.

Applications know that an object exists, but they do not know how it is implemented.

```text
Application

Stack *
   │
   ▼
+----------------+
|    Hidden      |
| Implementation |
+----------------+
```

This prevents applications from depending on implementation details.

---

#### Implementation Can Change

Since applications never see the structure definition, the library developer can modify it without changing the public API.

For example, an initial implementation might use a fixed-size array.

```c
struct Stack
{
    int data[100];
    int top;
};
```

A later version could switch to dynamic storage.

```c
struct Stack
{
    int *data;
    int top;
    int capacity;
};
```

As long as the public functions remain unchanged, applications continue to compile and work without modification.

---

#### Smaller Public Headers

Because the structure definition is omitted from the header, the public interface contains only the declarations needed by applications.

```text
stack.h

✓ Type declaration
✓ Function declarations

stack.c

✓ Structure definition
✓ Implementation
```

This keeps the public interface clean and focused.

---

#### Controlled Access

Applications cannot accidentally modify the object's internal state.

Instead of writing

```c
stack->top = 100;
```

they must use library functions such as

```c
stackPush(stack, value);
stackPop(stack);
```

The library therefore remains responsible for maintaining the object's consistency.

### Limitations

#### Dynamic Allocation Is Common

Since applications do not know the size of the hidden structure, they cannot create objects directly.

```c
Stack stack;      /* Error */
```

Instead, objects are typically created by library functions that allocate memory.

```c
Stack *stack = stackCreate();
```

Although this is the most common approach, it is a design choice rather than a language requirement.

---

#### No Direct Member Access

Because the structure definition is hidden, applications cannot access or modify its members.

```c
stack->top = 0;      /* Error */
```

Every operation must be performed through the library's API.

---

#### Additional Function Calls

Operations that could otherwise be performed by directly accessing structure members must instead be carried out through function calls.

```text
Without Opaque Pointer

stack.top

        │

With Opaque Pointer

stackTop(stack)
```

This introduces an extra level of indirection between the application and the object.

The next section summarizes the key ideas behind opaque pointers and their role in designing reusable C libraries.

---
## <font color='green'>5. Summary</font>

Opaque pointers are a common technique for implementing **information hiding** in C libraries.

Unlike languages that provide language-level access control, C relies on its separate compilation model to hide implementation details. The public header exposes only a forward declaration of a type, while the complete structure definition is kept in the implementation file.

In this article, we covered:

- An opaque pointer is a pointer to a type whose definition is intentionally hidden from application code.
- The public header contains only a forward declaration of the type and the library's API.
- The complete structure definition resides in the implementation (`.c`) file and is visible only when compiling the library.
- Because application code never sees the structure definition, it cannot determine the object's size or access its members directly.
- Applications interact with the object exclusively through functions provided by the library.
- This separation allows the library's internal implementation to change without affecting code that uses the library.

Although an opaque pointer is just an ordinary C pointer, the type it points to is intentionally incomplete outside the library. This simple technique enables C libraries to expose a clean public interface while keeping implementation details private, making code easier to maintain, extend, and evolve over time.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
