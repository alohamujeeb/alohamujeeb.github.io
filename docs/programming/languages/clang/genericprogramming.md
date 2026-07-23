---
hide:
  - navigation
  
tags:
  - void *
  - Generic Programming
  
---
# Generic Programming with `void *` in C

*This article is intended for intermediate and advanced C programmers. It explains how C achieves generic programming using `void *`, how generic functions operate on objects of different types, and the limitations of this approach.*

---
## <font color='green'>1. What Is Generic Programming?</font>

Generic programming is a programming technique in which a single function or algorithm can operate on objects of **different data types** instead of being limited to one specific type.

Consider a function that swaps two integers.

```c
void swapInt(int *a, int *b);
```

This function can only swap `int` objects. If you also need to swap `float`, `double`, or `char` values, you must write separate functions for each type.

```c
void swapInt(int *a, int *b);
void swapFloat(float *a, float *b);
void swapDouble(double *a, double *b);
void swapChar(char *a, char *b);
```

Although these functions perform exactly the same operation, they differ only in the data type they operate on. Writing separate implementations for every data type leads to unnecessary code duplication.

Generic programming solves this problem by allowing a single function to work with multiple data types.

For example, instead of writing different swap functions for every type, we can write one generic swap function.

```c
void swap(void *a, void *b, size_t size);
```

The same function can then be used to swap integers, floating-point values, structures, or any other object type.

```text
             swap()

          +-------------+
 int      |             |
 float -->|             |
 double ->|   Generic   |
 char ----|   Function  |
 struct ->|             |
          +-------------+
```

Unlike languages such as C++, which provide **templates** for generic programming, the C language has no built-in support for generic functions. Instead, C achieves generic programming primarily through the use of **`void *`**, which can represent the address of any object type.

Many functions in the C Standard Library rely on this technique. For example, both `qsort()` and `bsearch()` operate on arrays of arbitrary object types by using `void *` pointers instead of pointers to specific data types.

The next section explains what a `void *` pointer is and how it enables generic programming in C.


---
## <font color='green'>2. Understanding `void *`</font>

A **`void *`**, also known as a **generic pointer**, is a pointer that can hold the address of an object of any data type.

For example, the following `void *` pointers store the addresses of different types of objects.

```c
int i = 10;
float f = 3.14f;
double d = 2.71828;
char c = 'A';

void *ptr;

ptr = &i;
ptr = &f;
ptr = &d;
ptr = &c;
```

Unlike pointers such as `int *` or `float *`, a `void *` does not carry any information about the type of object it points to.

```text
           +-----------+
int * ---->|    int    |
           +-----------+

float * -->+----------+
            |  float  |
            +----------+

void * ----> ?
```

The compiler knows that an `int *` points to an integer and that a `float *` points to a floating-point value. However, when a pointer is declared as `void *`, the compiler knows only that it points to **some object**, not what type of object it is.

For this reason, a `void *` cannot be dereferenced directly.

```c
void *ptr = &i;

printf("%d\n", *ptr);    // Error
```

Before accessing the object, the pointer must first be converted to the appropriate pointer type.

```c
printf("%d\n", *(int *)ptr);
```

Similarly, if the pointer refers to a `float`, it must be cast to a `float *`.

```c
printf("%f\n", *(float *)ptr);
```

Pointer arithmetic is also not permitted on a `void *`.

```c
ptr++;    // Error
```

This is because pointer arithmetic depends on the size of the object being pointed to. Since a `void *` has no associated object type, the compiler does not know how many bytes should be added when the pointer is incremented.

To perform pointer arithmetic, the pointer must first be converted to a pointer of a known type.

```c
int *ip = ptr;
ip++;
```

or, when manipulating raw memory,

```c
unsigned char *cp = ptr;
cp++;
```

Using `unsigned char *` advances the pointer by exactly one byte, making it ideal for generic memory manipulation.

The next section demonstrates how `void *` can be used to implement generic functions that operate on objects of different data types.


---
## <font color='green'>3. Writing Generic Functions (An example)</font>

The primary advantage of using `void *` is that it enables the creation of functions that operate on objects of different data types.

As an example, consider implementing a generic swap function. Unlike a type-specific swap function, a generic swap function should be capable of swapping two objects regardless of their type.

To accomplish this, the function must receive:

- A pointer to the first object.
- A pointer to the second object.
- The size of each object.

Its prototype is therefore:

```c
void swap(void *a, void *b, size_t size);
```

The `size` parameter specifies how many bytes must be exchanged between the two objects.

```text
           +-----------+
a -------->| Object 1  |
           +-----------+
                ▲
                │ size bytes
                ▼
           +-----------+
b -------->| Object 2  |
           +-----------+
```

Since the function does not know the actual object type, it cannot use `int *`, `float *`, or `double *` to access the data. Instead, it treats each object simply as a sequence of bytes.

To do this, the pointers are converted to `unsigned char *`, allowing the function to access one byte at a time.

```c
void swap(void *a, void *b, size_t size)
{
    unsigned char *p = a;
    unsigned char *q = b;

    while (size--)
    {
        unsigned char temp = *p;
        *p++ = *q;
        *q++ = temp;
    }
}
```

Suppose two integers are swapped.

```c
int x = 10;
int y = 20;

swap(&x, &y, sizeof(int));
```

Internally, the function exchanges the bytes of the two integers.

```text
Before

x                    y
+----+----+----+----+    +----+----+----+----+
| xx | xx | xx | xx |    | yy | yy | yy | yy |
+----+----+----+----+    +----+----+----+----+

          Byte-by-byte Swap

After

x                    y
+----+----+----+----+    +----+----+----+----+
| yy | yy | yy | yy |    | xx | xx | xx | xx |
+----+----+----+----+    +----+----+----+----+
```

The same function can also swap other object types.

```c
float f1, f2;
swap(&f1, &f2, sizeof(float));

double d1, d2;
swap(&d1, &d2, sizeof(double));

struct Point p1, p2;
swap(&p1, &p2, sizeof(struct Point));
```

> <font color='red'>Because the function operates only on bytes, it does not need to know the type of object being exchanged. The caller simply provides the addresses of the objects together with their size.</font>

---
## <font color='green'>4. Generic Programming in the C Standard Library</font>

The C Standard Library makes extensive use of generic programming through `void *`. Rather than providing separate functions for every data type, many library functions operate on objects of arbitrary types.

Two well-known examples are:

- `qsort()` – Sorts an array.
- `bsearch()` – Searches a sorted array.

Their prototypes are:

```c
void qsort(void *base,
           size_t num,
           size_t size,
           int (*compare)(const void *, const void *));

void *bsearch(const void *key,
              const void *base,
              size_t num,
              size_t size,
              int (*compare)(const void *, const void *));
```

Notice that neither function knows the type of objects stored in the array. Instead, the caller provides:

- The address of the first element.
- The number of elements.
- The size of each element.
- A comparison function.

```text
            Generic Library Function

               +------------------+
Base Pointer -->|                  |
Element Count ->|                  |
Element Size -->|                  |
Callback ------>|                  |
               +------------------+
                        │
                        ▼
           Operates on Any Object Type
```

Because the library does not know the type of each element, it cannot perform pointer arithmetic directly on a `void *`.

Instead, it treats the array as a sequence of bytes. Knowing the size of each element, it can locate any element by advancing the appropriate number of bytes.

```text
Array in Memory

+---------+---------+---------+---------+
| Element | Element | Element | Element |
|    0    |    1    |    2    |    3    |
+---------+---------+---------+---------+
      <---- size ---->
```

Similarly, the comparison callback receives its arguments as `const void *`.

```c
int compare(const void *a, const void *b);
```

Since the callback knows the actual type of the array elements, it converts the pointers to the appropriate type before accessing the objects.

For example, when sorting integers:

```c
int compare(const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    return (*x > *y) - (*x < *y);
}
```

> The use of `const void *` prevents the comparison function from modifying the elements being compared.

By combining `void *`, object sizes, and callback functions, the C Standard Library provides generic algorithms that work with virtually any object type while requiring only a single implementation.

The next section discusses the advantages and limitations of this approach to generic programming.

---
## <font color='green'>5. Advantages and Limitations</font>

Using `void *` enables C programmers to write functions that are independent of specific data types. This approach provides a simple form of generic programming and is widely used throughout the C Standard Library. However, it also has some drawbacks.

### Advantages

#### Code Reusability

A single generic function can operate on many different object types, eliminating the need to write separate implementations for each type.

For example, a generic swap function can be used with integers, floating-point values, characters, and structures.

```c
swap(&i, &j, sizeof(int));
swap(&x, &y, sizeof(float));
swap(&p1, &p2, sizeof(struct Point));
```

This reduces code duplication and makes programs easier to maintain.

#### Type Independence

Generic functions do not depend on a particular data type. As long as the caller supplies the object's address and size, the same function can operate on any object.

This flexibility allows library functions such as `qsort()` and `bsearch()` to work with virtually any data type.


### Limitations

#### No Compile-Time Type Checking

Since every object pointer can be converted to a `void *`, the compiler cannot verify that the correct object type is being used.

For example, passing the wrong object size may lead to incorrect behavior.

```c
double value = 3.14;

/* Incorrect size */
swap(&value, &other, sizeof(int));
```

Such errors are usually detected only at runtime.

#### Manual Type Casting

Before a generic pointer can be dereferenced, it must be converted back to the appropriate pointer type.

```c
const int *p = ptr;
```

The responsibility for performing the correct cast lies entirely with the programmer.

#### Additional Parameters

Generic functions often require extra information that type-specific functions do not.

For example, a generic swap function requires the object size, while `qsort()` and `bsearch()` require both the object size and a comparison callback.

```text
Type-Specific Function

swapInt(int *, int *)

        │

        ▼

Generic Function

swap(void *, void *, size_t)
```

#### Less Readable

Because generic functions rely on `void *`, explicit casts, and object sizes, they are often more difficult to read and understand than equivalent type-specific functions.

The next section summarizes the key concepts discussed in this article.

---
## <font color='green'>6. Summary</font>

Generic programming enables a single function or algorithm to operate on objects of different data types, reducing code duplication and improving code reusability.

Since the C language does not provide templates or generics like some other programming languages, it achieves generic programming primarily through the use of **`void *`** pointers. A `void *` can hold the address of any object, allowing generic functions to manipulate objects without knowing their types at compile time.

In this article, you learned:

- A **`void *`** is a generic pointer that can point to any object type.
- A `void *` must be converted to the appropriate pointer type before it can be dereferenced.
- Pointer arithmetic cannot be performed directly on a `void *` because the size of the referenced object is unknown.
- Generic functions typically accept one or more `void *` pointers together with the size of the objects they operate on.
- The C Standard Library uses this technique to implement generic functions such as `qsort()` and `bsearch()`, which can operate on arrays of virtually any object type.
- Although generic programming with `void *` improves code reuse, it requires explicit type casting and does not provide compile-time type safety.

Despite these limitations, generic programming with `void *` remains one of the most powerful techniques in C. It forms the foundation of many standard library functions and enables programmers to write flexible, reusable code that can operate on a wide variety of data types.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
