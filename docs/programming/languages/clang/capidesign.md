---
hide:
  - navigation
  
tags:
  - API Design
  - C API
  
---
# C API Design

*This article is intended for intermediate and advanced C programmers. It discusses the principles of designing clear, consistent, and reusable C library interfaces. It focuses on API design rather than implementation details.*


---
## <font color='green'>1. What Is an API?</font>

An **Application Programming Interface (API)** is a collection of functions, data types, constants, and conventions that define how software components interact. Rather than exposing its internal implementation, a library exposes an API that applications use to access its functionality.

For example, a stack library might provide the following interface:

```c
Stack *stackCreate(void);
void stackDestroy(Stack *stack);

int stackPush(Stack *stack, int value);
int stackPop(Stack *stack, int *value);
```

An application uses these functions without needing to know how the stack is implemented internally.

```text
Application
      │
      ▼
+----------------------+
|      Stack API       |
+----------------------+
      │
      ▼
Library Implementation
```

The API acts as a contract between the library and the application. It specifies:

- Which functions are available.
- What each function does.
- The arguments and return values.
- How resources are managed.
- The responsibilities of both the library and the application.

Importantly, an API describes **what** a library provides, not **how** it is implemented. As long as the API remains unchanged, the library implementation can evolve without requiring changes to application code.

For example, a stack might initially be implemented using an array.

```text
Application
      │
      ▼
Stack API
      │
      ▼
Array-Based Stack
```

Later, the implementation could be replaced with a linked list.

```text
Application
      │
      ▼
Stack API
      │
      ▼
Linked-List Stack
```

Because the application interacts only with the API, no changes are required as long as the behavior of the interface remains the same.

Designing a good API involves much more than choosing function names. A well-designed API should be:

- Clear and easy to understand.
- Consistent in its naming and behavior.
- Flexible enough to support different use cases.
- Difficult to misuse.
- Stable as the library evolves.

These characteristics make libraries easier to learn, integrate, and maintain over time.

The following sections discuss the principles commonly used to design clear, consistent, and reusable C APIs.

---
## <font color='green'>2. Resource Management</font>

Many C libraries manage resources such as dynamically allocated memory, files, sockets, mutexes, or hardware devices. A well-designed API should make it immediately clear who owns these resources and who is responsible for releasing them.

A common convention is that the function that creates a resource has a corresponding function that destroys it.

```c
Stack *stackCreate(void);
void stackDestroy(Stack *stack);
```

This pairing makes the resource lifecycle explicit.

```text
Application
      │
      ▼
stackCreate()

      │
      ▼
   Use Stack

      │
      ▼
stackDestroy()
```

Applications should never be left guessing how a resource is released. If a library allocates memory, the library should normally provide the function that frees it.

For example:

```c
Image *imageLoad(const char *filename);
void imageDestroy(Image *image);
```

This approach ensures that allocation and deallocation use the same implementation. It also allows the library to change how resources are managed without affecting applications.

---

### Define Ownership Clearly

Every API that returns or accepts pointers should clearly define ownership.

For example, after calling

```c
Stack *stack = stackCreate();
```

the application owns the returned object and is responsible for eventually calling

```c
stackDestroy(stack);
```

Likewise, when a pointer is passed to a function, the API should specify whether the library merely uses the object temporarily or assumes ownership of it.

Clearly documenting ownership prevents memory leaks, double frees, and dangling pointers.

---

### Handle Invalid Resources Safely

Applications can accidentally pass invalid pointers or `NULL` to library functions. Whenever practical, APIs should define how such cases are handled.

For example, many C libraries allow destroying a `NULL` pointer.

```c
stackDestroy(NULL);
```

Doing nothing in this case simplifies application code because callers do not need to check every pointer before destroying it.

Similarly, functions should document whether `NULL` is accepted for input parameters or considered a programming error.

---

### Make Resource Lifetimes Obvious

Applications should always know when a resource becomes valid and when it is no longer usable.

```text
Create
   │
   ▼
Valid Resource
   │
   ▼
Destroy
   │
   ▼
Invalid Resource
```

Using a resource after it has been destroyed results in undefined behavior. A well-designed API clearly documents these lifetime rules so that applications can manage resources safely.

---

Resource management is one of the most important aspects of C API design. By clearly defining how resources are created, owned, used, and destroyed, an API becomes easier to understand and significantly more difficult to misuse.

---
## <font color='green'>3. Encapsulation with Opaque Types</font>

A good API exposes only the functionality that applications need while hiding implementation details. This separation allows the library to evolve internally without affecting the applications that use it.

In C, this is commonly achieved using **[opaque types](opaquepointers.md)**.

For example, a stack library may expose the following declarations in its header file.

```c
struct Stack;
typedef struct Stack Stack;

Stack *stackCreate(void);
void stackDestroy(Stack *stack);

int stackPush(Stack *stack, int value);
int stackPop(Stack *stack, int *value);
```

The application knows that a `Stack` exists, but it cannot access its members because the structure definition is hidden.

```text
Application

Stack *

      │

      ▼

+----------------------+
|      Stack API       |
+----------------------+

      │

      ▼

Library Implementation

struct Stack
{
    ...
};
```

Only the library's implementation file contains the full definition of `struct Stack`.

As a result, applications interact with the object exclusively through the API.

---

### Hide Implementation Details

Suppose the stack is initially implemented using a dynamically allocated array.

```text
Stack
 ├── int *data
 ├── size
 └── capacity
```

Later, the implementation changes to a linked list.

```text
Stack
 ├── Node *top
 └── size
```

Because the structure is hidden, no application code needs to change. The public API remains exactly the same.

---

### Preserve API Stability

Exposing structure members creates a dependency between the application and the library.

For example:

```c
stack->size++;
```

Once applications begin accessing members directly, changing the structure layout can break existing code.

Using an opaque type prevents this dependency. The library remains free to modify its internal representation while preserving the public interface.

---

### Enforce Correct Usage

Opaque types encourage applications to interact with objects through library functions rather than manipulating internal data directly.

Instead of writing

```c
stack->size = 0;
```

the application calls

```c
stackClear(stack);
```

This allows the library to validate arguments, maintain internal consistency, and enforce any invariants required by the implementation.

---

Encapsulation is a key principle of C API design. By exposing only an opaque type and a well-defined set of functions, a library separates its public interface from its implementation, resulting in APIs that are easier to maintain, extend, and evolve over time.

The next section discusses how well-designed APIs report errors consistently and predictably.

---
## <font color='green'>4. Error Handling</font>

Errors are inevitable. Files may not exist, memory allocation may fail, network connections may be interrupted, or applications may pass invalid arguments. A well-designed API should report these errors consistently and allow applications to respond appropriately.

There is no single error handling mechanism in C, but successful APIs adopt a clear and consistent strategy.

---

### Return Status Codes

One of the most common approaches is to return a status code indicating whether an operation succeeded.

For example:

```c
int stackPush(Stack *stack, int value);
```

The function might return

- `0` on success.
- A non-zero error code on failure.

The application can then determine whether the operation completed successfully.

```c
if (stackPush(stack, value) != 0)
{
    /* Handle error */
}
```

Using return codes makes error handling explicit and avoids hidden control flow.

---

### Return Objects or `NULL`

Functions that create or retrieve objects often return a pointer.

If the operation fails, they commonly return `NULL`.

```c
Image *imageLoad(const char *filename);
```

The application verifies the result before using it.

```c
Image *image = imageLoad("photo.jpg");

if (image == NULL)
{
    /* Handle error */
}
```

This convention is widely used throughout the C standard library and many third-party libraries.

---

### Use Output Parameters

Some functions need to return both a status code and a result.

A common solution is to return the status directly while writing the result through an output parameter.

```c
int stackPop(Stack *stack, int *value);
```

```text
          stackPop()

          │
          ├── Return Status
          │
          └── Write Result
                │
                ▼
             *value
```

This separates the operation's success or failure from the data it produces.

---

### Report Errors Consistently

An API should avoid mixing unrelated error handling conventions.

For example, if most functions return status codes, introducing functions that terminate the program or print error messages can make the API unpredictable.

Instead, applications should remain responsible for deciding how errors are handled.

```text
Library
    │
    ├── Detect Error
    └── Report Error

Application
    │
    └── Decide What To Do
```

This separation keeps the library reusable in many different environments, from command-line utilities to graphical applications and embedded systems.

> Error handling is an essential part of API design. By reporting errors consistently, separating error reporting from error handling, and allowing applications to decide how to respond, a library becomes more predictable, reusable, and easier to integrate.


---
## <font color='green'>5. Extensibility with Callbacks</font>

A well-designed API should be flexible enough to support different application requirements without requiring modifications to the library itself. One of the most common techniques for achieving this flexibility in C is the use of callbacks.

Rather than hard-coding application-specific behavior, a library allows the application to provide one or more callback functions that are invoked at appropriate times.

For example, a library that processes an array might expose the following interface:

```c
void process(int *array,
             size_t size,
             void (*callback)(int));
```

The application provides the callback.

```c
void printNumber(int value)
{
    printf("%d\n", value);
}

process(values, size, printNumber);
```

During execution, the library controls when the callback is invoked.

```text
Application
      │
      ▼
process(values, printNumber)

      │
      ▼

Library

      │
      ├── printNumber(10)
      ├── printNumber(20)
      └── printNumber(30)
```

This separation allows the library to remain generic while giving applications complete control over the operation performed for each element.

---

### Avoid Hard-Coding Behavior

Suppose a library always prints every value it processes.

```c
void process(int *array, size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        printf("%d\n", array[i]);
    }
}
```

This implementation is useful only for printing.

Using a callback makes the same function reusable for many different tasks.

```text
          process()

              │
     ┌────────┼────────┐
     ▼        ▼        ▼
  print()   sum()   write()
```

Only the callback changes; the processing algorithm remains unchanged.

---

### Provide User Context

Callbacks often need access to application-specific data.

Instead of relying on global variables, many APIs accept a user-defined context pointer.

```c
void process(int *array,
             size_t size,
             void (*callback)(int, void *),
             void *userData);
```

Whenever the callback is invoked, the library passes the same `userData` pointer back to the application.

```text
process()

      │
      ├── callback(10, userData)
      ├── callback(20, userData)
      └── callback(30, userData)
```

This allows callbacks to maintain state while keeping the library independent of application-specific data.

---

### Document Callback Behavior

Whenever an API accepts callbacks, it should clearly specify:

- When callbacks are invoked.
- How often they may be invoked.
- Whether they may terminate an operation.
- Whether the library stores the callback for later use.

These details allow applications to implement callbacks correctly and avoid lifetime or ownership issues.

---

Callbacks are a powerful extensibility mechanism for C APIs. By allowing applications to supply custom behavior while the library controls when that behavior is executed, callbacks make libraries more reusable, adaptable, and easier to extend without changing their implementation.

The final section summarizes the key principles of good C API design.

---
## <font color='green'>6. Summary</font>

A well-designed API provides a clear and stable interface between a library and the applications that use it. By carefully defining how functionality is exposed, an API allows the library to evolve while minimizing the impact on existing applications.

In this article, you learned:

- An API defines how applications interact with a library without exposing its implementation.
- Resource management should clearly specify how resources are created, owned, used, and destroyed.
- Opaque types separate a library's public interface from its implementation, allowing internal changes without affecting application code.
- Error handling should follow a consistent strategy that allows applications to detect and respond to failures.
- Callbacks make APIs more flexible by allowing applications to supply custom behavior while the library controls when that behavior is executed.

Good API design is not about exposing as much functionality as possible. Instead, it is about exposing a small, consistent, and well-documented interface that is easy to understand, difficult to misuse, and stable as the library evolves.

Although the examples in this article focused on C, these design principles apply to almost every successful software library. A carefully designed API improves usability, encourages correct usage, and makes software easier to maintain over time.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
