---
hide:
  - navigation
  
tags:
  - Pointers and Arrays

---

# Pointers and Array Names in C
*This article is intended for intermediate and advanced C programmers. It assumes familiarity with pointers and explains the relationship between array names, pointers, and pointer arithmetic in C.*


---

## <font color='green'>1. Array Names and Pointers</font>

Arrays and pointers are closely related in C, which often leads to the misconception that they are the same thing. Although an array name can frequently be used as if it were a pointer, an array and a pointer are fundamentally different language constructs.

Understanding this relationship makes pointer arithmetic much easier to understand.

Consider the following array.

```c
int arr[] = {10, 20, 30, 40};
```

The array occupies four consecutive `int` objects in memory.

```
          arr
           │
           ▼
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
```

---
## <font color='green'>2. The Array Name</font>

In most expressions, the array name is automatically converted to a pointer to its first element.

Therefore,

```c
arr
```

is converted by the compiler to

```c
&arr[0]
```

For example,

```c
printf("%d\n", *arr);      // Output: 10
```

dereferences the pointer to the first array element.


---
## <font color='green'> 3. Arrays Are Not Pointers </font>

Although an array name is often converted to a pointer, an array is **not** a pointer.

**The value of Array name can NOT change, but value of pointer variable can change**

For example,

```c
int arr[4];
int *ptr = arr;
```

The following statement is valid because `ptr` is a pointer.

```c
ptr++;
```

However,

```c
arr++;
```

<font color='red'> is illegal. </font>

The array name represents the entire array object and is not a modifiable lvalue. Consequently, its value cannot be changed.



---
## <font color='green'>4. Using Pointer Arithmetic with an Array Name</font>

Since `arr` behaves like a pointer to the first element, pointer arithmetic can be applied directly to it.

**Note that we are NOT changing the value of `arr` (value of array name cannot change)**

```c
arr + 1
```

points to the second element.

```c
arr + 2
```

points to the third element.

```
arr
 │
 ▼
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
  ▲    ▲    ▲    ▲
arr  arr+1 arr+2 arr+3
```

Notice that the array itself never moves. Pointer arithmetic simply produces a pointer to another element of the array.

---
## <font color='green'>5. Dereferencing an Offset</font>

Once a pointer has been obtained using pointer arithmetic, it can be dereferenced.

For example,

```c
*(arr + 2)
```

accesses the third element.

```c
printf("%d\n", *(arr + 2));    // Output: 30
```

This is exactly equivalent to

```c
arr[2]
```

### <font color='green'>`arr[i]` and `*(arr + i)` are equivalent </font>

Array subscripting is defined in terms of pointer arithmetic.

The expression

```c
arr[i]
```

is interpreted by the compiler as

```c
*(arr + i)
```

For example,

```c
printf("%d\n", arr[3]);        // Output: 40
printf("%d\n", *(arr + 3));    // Output: 40
```

Both expressions access exactly the same memory location.

This explains why arrays and pointers appear to behave similarly when accessing array elements.

---
## <font color='green'>6. Using a Pointer to Traverse an Array </font>

Pointer arithmetic is commonly used when processing arrays.

```c
int *ptr = arr;

while (ptr < arr + 4)
{
    printf("%d\n", *ptr);
    ptr++;
}
```

Execution proceeds as follows.

```
Iteration 1   ptr ─────► 10
Iteration 2   ptr ─────────► 20
Iteration 3   ptr ─────────────► 30
Iteration 4   ptr ─────────────────► 40
```

Each increment advances the pointer to the next array element.


---

## <font color='green'> 7. Summary </font>

The following table summarizes the relationship between array names, pointers, and pointer arithmetic.

| Expression | Meaning |
|------------|---------|
| `arr` | In most expressions, converted to a pointer to the first element. |
| `&arr[0]` | Address of the first element. |
| `arr + i` | Pointer to element `i`. |
| `*(arr + i)` | Value stored in element `i`. |
| `arr[i]` | Equivalent to `*(arr + i)`. |

Remember the following key points:

- An array and a pointer are **not** the same thing.
- In most expressions, the compiler automatically converts an array name to a pointer to its first element.
- Pointer arithmetic can therefore be performed directly on an array name.
- Array subscripting (`arr[i]`) is defined in terms of pointer arithmetic (`*(arr + i)`).
- Although an array name often behaves like a pointer, it is **not** a modifiable lvalue, so expressions such as `arr++` are illegal.

Understanding the relationship between array names and pointers makes it easier to read pointer expressions, perform pointer arithmetic correctly, and write efficient code for processing arrays in C.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
