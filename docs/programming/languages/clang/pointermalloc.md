---
hide:
  - navigation
  
tags:
  - Memory Leaks 

---

# Understanding malloc(), calloc(), realloc(), and free()
*This article is intended for intermediate and advanced C programmers. It assumes familiarity with pointers and basic C programming concepts and explains how dynamic memory allocation works using `malloc()`, `calloc()`, `realloc()`, and `free()`.*


---

## <font color='green'>1. Why Dynamic Memory Allocation?</font>

In the  article [Understanding Memory Types in C: Stack, Heap, and Global Memory](stackheap.md), it is explained that the **stack** has a fixed size and is intended for storing local (automatic) variables, while the **heap** provides dynamically allocated memory that can be requested and released during program execution.

In many programs, the amount of memory required is **not known until runtime**. For example, a program may need to allocate memory based on user input, the size of a file, or data received over a network. Since this information is unavailable when the program is compiled, stack allocation is often insufficient.

To solve this problem, the C Standard Library provides a set of functions for **dynamic memory allocation**. These functions allow a program to request memory from the heap when it is needed and release it when it is no longer required.

The four primary dynamic memory allocation functions are:

- `malloc()` – Allocates a block of memory.
- `calloc()` – Allocates and initializes a block of memory.
- `realloc()` – Changes the size of an existing memory block.
- `free()` – Releases previously allocated memory.

---

## <font color='green'>2. `malloc()`</font>

The `malloc()` (**memory allocation**) function allocates a block of memory from the **heap**. The allocated memory is **uninitialized**, meaning it contains whatever values happened to be stored at that memory location previously.

**Syntax**

```c
void *malloc(size_t size);
```

**Parameter**

- `size` – The number of bytes to allocate.

**Return Value**

- Returns a pointer to the beginning of the allocated memory if the allocation succeeds.
- Returns `NULL` if the requested memory cannot be allocated.

**Example**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *ptr = malloc(sizeof(int));

    if (ptr == NULL)
    {
        return 1;
    }

    *ptr = 100;

    printf("%d\n", *ptr);

    free(ptr);

    return 0;
}
```

In this example, `malloc()` allocates enough heap memory to store one integer. The returned pointer is assigned to `ptr`, which is then used to store and retrieve the value `100`. Once the allocated memory is no longer needed, it is released using `free()`.

> **Note:** Since the memory returned by `malloc()` is **uninitialized**, its contents are indeterminate. The allocated memory should always be initialized before it is read.


---

## <font color='green'>3. `calloc()`</font>

The `calloc()` (**contiguous allocation**) function allocates memory from the **heap** for an array of elements. Unlike `malloc()`, it automatically initializes every byte of the allocated memory to **zero**.

**Syntax**

```c
void *calloc(size_t num_elements, size_t element_size);
```

**Parameters**

- `num_elements` – The number of elements to allocate.
- `element_size` – The size, in bytes, of each element.

The total amount of allocated memory is:

```text
num_elements × element_size bytes
```

**Return Value**

- Returns a pointer to the beginning of the allocated memory if the allocation succeeds.
- Returns `NULL` if the requested memory cannot be allocated.

**Example**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *numbers = calloc(5, sizeof(int));

    if (numbers == NULL)
    {
        return 1;
    }

    for (int i = 0; i < 5; i++)
    {
        printf("%d ", numbers[i]);
    }

    free(numbers);

    return 0;
}
```

**Output**

```text
0 0 0 0 0
```

In this example, `calloc()` allocates memory for an array of five integers. Unlike `malloc()`, every element is automatically initialized to zero before the memory is returned.

> **Note:** Use `calloc()` when newly allocated memory should be initialized to zero. If initialization is unnecessary or will be performed manually, `malloc()` is often sufficient.


---

## <font color='green'>4. `realloc()`</font>

The `realloc()` (**reallocation**) function changes the size of a previously allocated memory block. It can increase or decrease the size of memory originally allocated using `malloc()`, `calloc()`, or `realloc()`.

If the existing memory block cannot be expanded in its current location, `realloc()` allocates a new block of the requested size, copies the existing data to the new location, releases the old memory block, and returns the address of the new block.

**Syntax**

```c
void *realloc(void *ptr, size_t new_size);
```

**Parameters**

- `ptr` – Pointer to the previously allocated memory block.
- `new_size` – The new size, in bytes, of the memory block.

**Return Value**

- Returns a pointer to the resized memory block if the operation succeeds.
- Returns `NULL` if the memory cannot be reallocated. In this case, the original memory block remains unchanged.

**Example**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *numbers = malloc(5 * sizeof(int));

    if (numbers == NULL)
    {
        return 1;
    }

    numbers = realloc(numbers, 10 * sizeof(int));

    if (numbers == NULL)
    {
        return 1;
    }

    free(numbers);

    return 0;
}
```

In this example, memory is initially allocated for five integers. Later, `realloc()` resizes the allocation so that it can store ten integers. The returned pointer should always be used because the memory block may have been moved to a different location.

> **Note:** Never assign the return value of `realloc()` directly to the original pointer without checking for `NULL`. If reallocation fails, the original pointer is lost, resulting in a memory leak.

```c
int *temp = realloc(numbers, 10 * sizeof(int));

if (temp != NULL)
{
    numbers = temp;
}
```


---

## <font color='green'>5. `free()`</font>

The `free()` function releases memory that was previously allocated using `malloc()`, `calloc()`, or `realloc()`. Once the memory has been released, it becomes available for future allocations.

**Syntax**

```c
void free(void *ptr);
```

**Parameter**

- `ptr` – Pointer to a memory block previously allocated using `malloc()`, `calloc()`, or `realloc()`.

**Return Value**

The `free()` function does not return a value.

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

    free(ptr);

    return 0;
}
```

In this example, the memory allocated by `malloc()` is released using `free()` after it is no longer needed.

> **Important:** Calling `free()` releases the allocated memory, **not the pointer itself**. After the call, the pointer still contains the same memory address, but that address is no longer valid. Dereferencing the pointer after it has been freed results in **undefined behavior**.

For this reason, it is good practice to assign `NULL` to a pointer after calling `free()` if the pointer will continue to exist.

```c
free(ptr);
ptr = NULL;
```


---

## <font color='green'>6. Choosing the Right Function</font>

The four dynamic memory allocation functions each serve a different purpose. Choosing the appropriate function depends on how the allocated memory will be used.

| Function | Purpose | Memory Initialized? |
|----------|---------|---------------------|
| `malloc()` | Allocates a block of memory | No |
| `calloc()` | Allocates memory for an array of elements | Yes (initialized to zero) |
| `realloc()` | Resizes a previously allocated memory block | Existing data is preserved up to the smaller of the old and new sizes |
| `free()` | Releases previously allocated memory | Not applicable |

In general:

- Use `malloc()` when you need to allocate memory and will initialize it yourself.
- Use `calloc()` when you want the allocated memory to be initialized to zero.
- Use `realloc()` when the size of an existing memory block needs to change.
- Use `free()` to release dynamically allocated memory once it is no longer needed.

Using these functions correctly helps prevent common programming errors such as **memory leaks** and **dangling pointers**, while ensuring that memory is managed efficiently throughout the lifetime of a program.


---

## <font color='green'>7. Summary</font>

Dynamic memory allocation enables C programs to request and release memory during program execution, making it possible to work with data whose size is not known until runtime.

This article introduced the four primary dynamic memory allocation functions provided by the C Standard Library:

- `malloc()` allocates an uninitialized block of memory.
- `calloc()` allocates memory and initializes it to zero.
- `realloc()` changes the size of an existing memory block.
- `free()` releases previously allocated memory so it can be reused.

Correct use of these functions is essential for writing reliable C programs. Every successful memory allocation should eventually be matched with a corresponding call to `free()`, and pointers returned by allocation functions should always be checked before use.

Understanding how these functions work lays the foundation for effective memory management and helps prevent common programming errors such as **memory leaks** and **dangling pointers**.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
