---
hide:
  - navigation
  
tags:
  - Memory Ownership
  
---

# Memory Ownership in C: Who Is Responsible for Freeing Memory?

*This article is intended for intermediate and advanced C programmers. It explains the concept of memory ownership in C, who is responsible for freeing dynamically allocated memory, and how clearly defining ownership helps prevent common memory-management bugs.*


---
## <font color='green'>1. Why Memory Ownership Matters</font>

When dynamically allocating memory in C, one important question must always be answered:

> **Who is responsible for freeing this memory?**

Consider the following example.

```c
char *buffer = malloc(1024);
```

After the memory has been allocated, several parts of the program may access it.

```text
                 +-----------------------+
                 |  Heap Memory (1024B)  |
                 +-----------------------+
                          ^
                          |
                     buffer (main)
                          ^
                          |
                  process_data()
                          ^
                          |
                  write_to_file()
```

Although multiple functions may use the allocated memory, **only one part of the program should be responsible for releasing it**.

If no one frees the memory, a **memory leak** occurs.

If two different parts of the program both call `free()` on the same memory, a **double-free error** occurs.

If one part of the program frees the memory while another continues to use it, the result is a **dangling pointer**, leading to undefined behavior.

These problems all have the same underlying cause: **it is unclear who owns the allocated memory.**

The concept of **memory ownership** answers this question by clearly defining which part of a program is responsible for releasing dynamically allocated memory. Once ownership is well defined, it becomes much easier to write correct programs and avoid common memory-management bugs.

---
## <font color='green'>2. Ownership Transfer</font>

Memory ownership is not always permanent. As a program executes, the responsibility for freeing dynamically allocated memory may be transferred from one part of the program to another.

Consider the following function.

```c
char *create_buffer(void)
{
    char *buffer = malloc(1024);

    if (buffer == NULL)
        return NULL;

    return buffer;
}
```

Initially, the function owns the allocated memory.

```text
create_buffer()

buffer
   |
   v
+----------------------+
|     Heap Memory      |
+----------------------+
```

When the function returns the pointer,

```c
char *data = create_buffer();
```

ownership is transferred to the caller.

```text
Before return

create_buffer()
      |
      v
+----------------------+
|     Heap Memory      |
+----------------------+

          │
          │ return
          ▼

After return

data
 |
 v
+----------------------+
|     Heap Memory      |
+----------------------+
```

Once the ownership has been transferred:

- The caller becomes responsible for calling `free()`.
- The function that allocated the memory must **not** call `free()` before returning.
- The memory should be freed exactly once by its new owner.

```c
char *data = create_buffer();

if (data != NULL)
{
    /* Use the buffer */

    free(data);
}
```

Ownership transfer is common in C library functions and application programming interfaces (APIs). Whenever a function returns dynamically allocated memory, it is generally understood that the caller becomes responsible for releasing that memory unless the function's documentation specifies otherwise.

---
## <font color='green'>3. Borrowed Pointers (Non-Owning References)</font>

Not every pointer passed to a function transfers ownership. In many cases, a function simply uses the memory without becoming responsible for releasing it.

Consider the following function.

```c
void print_message(const char *message)
{
    printf("%s\n", message);
}
```

The function receives a pointer to a string, but it does **not** own the memory.

```c
char *text = malloc(100);

strcpy(text, "Hello, World!");

print_message(text);
```

The ownership remains with the caller.

```text
                text
                 |
                 v
          +--------------+
          | Heap Memory  |
          +--------------+
                 ^
                 |
         print_message()

Borrowed pointer
```

The `print_message()` function is allowed to read the string, but it must **not** call `free()`.

```c
void print_message(const char *message)
{
    printf("%s\n", message);

    /* Never do this */
    free(message);
}
```

Doing so would release memory that still belongs to the caller.

Later, when the caller attempts to free the same memory,

```c
free(text);
```

a **double-free error** occurs because the memory has already been released.

Borrowing a pointer is one of the most common patterns in C programming. Many standard library functions, including `printf()`, `strlen()`, `strcpy()`, and `memcmp()`, receive pointers to memory that they use temporarily without taking ownership.

Unless a function explicitly documents that ownership is transferred, you should assume that the function is only borrowing the pointer and that the caller remains responsible for calling `free()`.


---
## <font color='green'>4. Common Ownership Mistakes</font>

Memory ownership bugs usually occur when the ownership rules are violated. In most cases, the problem is not the allocation itself but confusion about **who is responsible for releasing the memory**.

The following are some of the most common ownership mistakes in C programs.

### Forgetting to Free Allocated Memory

If the owner never releases the allocated memory, the memory becomes permanently unavailable until the program terminates.

```c
char *buffer = malloc(100);

if (buffer == NULL)
    return;

/* Use the buffer */

return;        /* Forgot to free(buffer) */
```

```text
buffer
  |
  v
+----------------------+
|     Heap Memory      |
+----------------------+

Owner disappears

Result: Memory Leak
```

Since the owner failed to call `free()`, the allocated memory can no longer be reclaimed.

---

### Freeing Memory More Than Once

A memory block should be released exactly once.

```c
char *buffer = malloc(100);

free(buffer);
free(buffer);
```

```text
Allocated Memory
       |
       v
+----------------------+
|     Heap Memory      |
+----------------------+

First free()   ✓
Second free()  ✗

Result: Undefined Behavior
```

Once `free()` has been called, ownership ends. Calling `free()` again attempts to release memory that has already been deallocated.

---

### Freeing Borrowed Memory

A function that borrows a pointer must never assume ownership of it.

```c
void print_message(char *message)
{
    printf("%s\n", message);

    free(message);      /* Wrong */
}

int main(void)
{
    char *text = malloc(100);

    print_message(text);

    free(text);

    return 0;
}
```

```text
Owner: main()

      text
       |
       v
+----------------------+
|     Heap Memory      |
+----------------------+
       ^
       |
print_message()

Borrowed pointer
```

`print_message()` only borrowed the pointer. Calling `free()` inside the function releases memory that still belongs to the caller.

---

### Using Memory After It Has Been Freed

Once memory has been released, the pointer becomes invalid.

```c
char *buffer = malloc(100);

free(buffer);

printf("%s\n", buffer);
```

```text
buffer
  |
  v
+----------------------+
|    Freed Memory      |
+----------------------+

Result: Dangling Pointer
```

Accessing memory after it has been freed results in undefined behavior because the allocation no longer exists.

---

Although these mistakes appear different, they all originate from the same problem: **the ownership of the allocated memory is unclear or violated**. Clearly defining who owns each allocation—and ensuring that only the owner calls `free()`—eliminates most memory-management bugs in C programs.

---
## <font color='green'>5. Memory Ownership Best Practices</font>

The following practices make dynamic memory management easier to understand, maintain, and debug.

### Clearly Define Ownership

Every dynamically allocated memory block should have exactly one owner. The owner is responsible for calling `free()`, while other parts of the program should only borrow the pointer.

---

### Pair Allocation and Deallocation

Whenever memory is allocated, there should be a clearly defined place where it is released.

```text
malloc()
    │
    ▼
Use Memory
    │
    ▼
free()
```

Thinking about allocation and deallocation as a pair makes it much less likely that memory will be leaked.

---

### Use a Create-Process-Destroy Lifecycle

Many C libraries follow a simple lifecycle for dynamically allocated objects.

```text
Create  ─────►  Process  ─────►  Destroy
   │               │                │
malloc()      Use the object      free()
```

The object is created, used by one or more functions, and finally released by a dedicated cleanup function. Centralizing allocation and cleanup makes ownership easier to understand and reduces memory-management errors.

---

### Document Ownership Transfer

If a function takes ownership of a pointer, make that behavior explicit in its documentation or naming.

For example, a function named

```c
take_buffer(char *buffer);
```

more clearly suggests ownership transfer than

```c
process_buffer(char *buffer);
```

Clear ownership rules make APIs easier to use correctly.

---

### Release Memory Exactly Once

Every dynamically allocated memory block should be released exactly once by its current owner.

Failing to release memory causes memory leaks, while releasing it more than once results in undefined behavior.



---
## <font color='green'>6. Summary</font>

Memory ownership defines which part of a program is responsible for releasing dynamically allocated memory.

The key ideas are:

- Every allocation should have exactly one owner.
- Ownership may be transferred to another part of the program.
- Borrowed pointers may use memory but must never call `free()`.
- Memory should be released exactly once by its current owner.

Most memory-management bugs—including memory leaks, double-free errors, and dangling pointers—occur because ownership is unclear or violated.

By clearly defining ownership throughout a program, dynamic memory becomes predictable, easier to reason about, and significantly less error-prone.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
