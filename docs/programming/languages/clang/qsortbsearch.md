---
hide:
  - navigation
  
tags:
  - qsort in C
  - bsearch in C
  
---
# Built-in Sorting and Searching Libraries in C: `qsort()` and `bsearch()`

*This article is intended for intermediate and advanced C programmers. It introduces the standard sorting and searching facilities provided by the C Standard Library, explains why generic callback functions are required, and demonstrates how to use `qsort()` and `bsearch()` to sort and search arrays of arbitrary data types.*

---
## <font color='green'>1. Sorting and Searching in the C Standard Library</font>

Sorting and searching are two of the most fundamental operations performed on collections of data. Whether processing arrays of integers, strings, or structures, programs frequently need to arrange data in a particular order or locate specific elements efficiently.

> Unlike C++, whose Standard Template Library (STL) provides a rich collection of generic algorithms, the C Standard Library includes only two generic algorithms for working with arrays:

- `qsort()` — Sorts the elements of an array.
- `bsearch()` — Performs a binary search on a sorted array.

These two functions are declared in the `<stdlib.h>` header.

```c
#include <stdlib.h>
```

The C Standard Library does **not** provide generic implementations of many other common algorithms, such as finding, counting, reversing, transforming, or copying elements. When such functionality is required, C programmers typically implement the algorithms themselves or use third-party libraries.

Both `qsort()` and `bsearch()` are designed to work with **arrays of any data type**. Instead of being limited to integers or strings, they operate on raw memory and rely on user-supplied callback functions to compare elements.

```text
             Array of Any Data Type
                     │
                     ▼
                +-----------+
                |  qsort()  |
                +-----------+
                     │
                     ▼
          Comparison Callback Function
                     │
                     ▼
              Elements Ordered


             Sorted Array
                   │
                   ▼
              +-----------+
              | bsearch() |
              +-----------+
                   │
                   ▼
        Comparison Callback Function
                   │
                   ▼
           Matching Element
```


---
## <font color='green'>2. Using `qsort()`</font>

The `qsort()` function sorts the elements of an array according to a user-defined comparison function.

Its prototype is defined in `<stdlib.h>`.

```c
void qsort(void *base,
           size_t num_elements,
           size_t element_size,
           int (*compare)(const void *, const void *));
```

The parameters are:

| Parameter | Description |
|-----------|-------------|
| `base` | Pointer to the first element of the array. |
| `num_elements` | Number of elements in the array. |
| `element_size` | Size of each element in bytes, typically obtained using `sizeof()`. |
| `compare` | Pointer to a user-defined comparison function. Whenever `qsort()` needs to determine the relative order of two elements, it calls this function. The function compares the two elements and returns a value indicating which one should appear first in the sorted array. |

The first three parameters tell `qsort()` where the array is located, how many elements it contains, and the size of each element. The final parameter tells `qsort()` **how the elements should be compared**.

Whenever `qsort()` needs to compare two elements, it calls the comparison function supplied by the programmer.

```text
                qsort()
                   │
                   │
        Needs to compare two elements
                   │
                   ▼
      compare(element1, element2)
                   │
          Returns an integer
                   │
        ┌──────────┼──────────┐
        │          │          │
      < 0          0         > 0
        │          │          │
        ▼          ▼          ▼
 element1      elements    element2
 comes before   are equal  comes before
 element2                  element1
```

The comparison function must have the following prototype.

```c
int compare(const void *a, const void *b);
```

The two parameters point to the elements being compared. Since they are declared as `const void *`, the comparison function must cast them to the appropriate data type before accessing their values.

The function returns:

| Return Value | Meaning |
|-------------:|---------|
| Less than `0` | The first element should appear before the second. |
| `0` | Both elements are considered equal. |
| Greater than `0` | The first element should appear after the second. |

The following example sorts an array of integers in ascending order.

```c
#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    if (*x < *y)
        return -1;

    if (*x > *y)
        return 1;

    return 0;
}

int main(void)
{
    int numbers[] = {42, 15, 73, 8, 29};

    size_t count = sizeof(numbers) / sizeof(numbers[0]);

    qsort(numbers,
          count,
          sizeof(numbers[0]),
          compare_ints);

    for (size_t i = 0; i < count; i++)
        printf("%d ", numbers[i]);

    return 0;
}
```

Output:

```text
8 15 29 42 73
```

> The same `qsort()` function can sort arrays of integers, floating-point values, strings, structures, or any other data type. Only the comparison function needs to change to describe how elements of that type should be ordered.


---
## <font color='green'>3. Using `bsearch()`</font>

The `bsearch()` function performs a **binary search** on a sorted array to locate a specific element.

Its prototype is defined in `<stdlib.h>`.

```c
void *bsearch(const void *key,
              const void *base,
              size_t num_elements,
              size_t element_size,
              int (*compare)(const void *, const void *));
```

The parameters are:

| Parameter | Description |
|-----------|-------------|
| `key` | Pointer to the value being searched for. |
| `base` | Pointer to the first element of the sorted array. |
| `num_elements` | Number of elements in the array. |
| `element_size` | Size of each element in bytes, typically obtained using `sizeof()`. |
| `compare` | Pointer to a user-defined comparison function. Whenever `bsearch()` compares the search key with an array element, it calls this function to determine whether the key is smaller, equal to, or greater than the element. |

Unlike a linear search, which examines elements one by one, `bsearch()` repeatedly divides the search range in half until the element is found or no elements remain.

```text
           Sorted Array
                 │
                 ▼
            +-----------+
            | bsearch() |
            +-----------+
                 │
                 ▼
      compare(key, middle_element)
                 │
       ┌─────────┼─────────┐
       │         │         │
      < 0        0        > 0
       │         │         │
       ▼         ▼         ▼
 Search left   Found   Search right
    half                  half
```

The comparison function has the same prototype used by `qsort()`.

```c
int compare(const void *a, const void *b);
```

The first parameter points to the search key, while the second parameter points to an element in the array.

The function returns:

| Return Value | Meaning |
|-------------:|---------|
| Less than `0` | The search key is less than the array element. |
| `0` | The search key matches the array element. |
| Greater than `0` | The search key is greater than the array element. |

The following example searches for an integer in a sorted array.

```c
#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    if (*x < *y)
        return -1;

    if (*x > *y)
        return 1;

    return 0;
}

int main(void)
{
    int numbers[] = {8, 15, 29, 42, 73};
    int key = 29;

    size_t count = sizeof(numbers) / sizeof(numbers[0]);

    int *result = bsearch(&key,
                          numbers,
                          count,
                          sizeof(numbers[0]),
                          compare_ints);

    if (result != NULL)
        printf("Found: %d\n", *result);
    else
        printf("Not found\n");

    return 0;
}
```

Output:

```text
Found: 29
```

> **Important:** `bsearch()` assumes that the array is already sorted according to the same comparison function. If the array is not sorted, or if a different comparison function is used, the result is undefined.

---
## <font color='green'>4. Summary</font>

Unlike C++, whose Standard Template Library (STL) provides a rich collection of generic algorithms, the C Standard Library includes only two generic algorithms for working with arrays: `qsort()` and `bsearch()`.

The `qsort()` function sorts the elements of an array, while `bsearch()` performs a binary search on a sorted array. Both functions are declared in `<stdlib.h>` and are designed to work with arrays of any data type.

Rather than knowing the type of the array elements, `qsort()` and `bsearch()` rely on user-defined comparison functions to determine how elements should be compared. This makes them flexible enough to work with integers, floating-point values, strings, structures, and other data types.

Although the C Standard Library provides only these two generic algorithms, they are sufficient for many common sorting and searching tasks encountered in C programs.

---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
