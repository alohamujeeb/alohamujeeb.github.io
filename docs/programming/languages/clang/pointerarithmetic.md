---
hide:
  - navigation
  
tags:
  - Pointer syntax

---

# Understanding Pointer Arithmetic in C

*This article is intended for intermediate and advanced C programmers. It assumes familiarity with pointers and explains some of the most commonly misunderstood pointer arithmetic operations in C.*

---

## <font color='green'>1. Reading Pointer Expressions</font>

One of the most challenging aspects of learning pointers in C is understanding pointer expressions. Many expressions appear almost identical but perform completely different operations. The difference lies in **how the compiler groups the operators** in the expression.

A useful technique when reading a pointer expression is to **mentally insert parentheses** to show how the compiler interprets the expression. Once the grouping is clear, the meaning usually becomes much easier to understand.

The compiler applies well-defined precedence rules when parentheses are omitted. For example,

```c
*ptr++;
```

is interpreted as

```c
*(ptr++);
```

whereas

```c
(*ptr)++;
```

is interpreted exactly as written because the parentheses explicitly specify the order of evaluation.

Similarly,

```c
*++ptr;
```

is interpreted as

```c
*(++ptr);
```

Although these expressions differ by only a few characters, they perform different operations. Throughout this article, each expression is rewritten by inserting parentheses to show exactly how the compiler interprets it before explaining its behavior.


---

## <font color='green'>2. Incrementing a Pointer vs. Incrementing the Pointed Value</font>

One of the most common sources of confusion in C is determining whether an increment operation modifies the **pointer itself** or the **value pointed to by the pointer**. Although the expressions look similar, they perform entirely different operations.

The following operators are used throughout this section.

| Operator | Precedence | Description |
|----------|------------|-------------|
| `()` | Highest | Parentheses explicitly control how an expression is grouped. |
| `++` (postfix) | Higher than unary operators | Increments its operand after its current value is used. |
| `*` (dereference) | Unary | Accesses the object pointed to by a pointer. |
| `++` (prefix) | Unary | Increments its operand before its value is used. |

Consider the following declarations.

```c
int arr[] = {10, 20, 30};
int *ptr = arr;
```

Initially, `ptr` points to the first element of the array.

```
ptr
 │
 ▼
+----+----+----+
| 10 | 20 | 30 |
+----+----+----+
```

### **Incrementing the Pointer**

The following statement increments the pointer.

```c
ptr++;
```

After execution, `ptr` points to the next element of the array, while the contents of the array remain unchanged.

```c
printf("%d\n", *ptr);    // Output: 20
```

```
Before:

ptr ─────► 10   20   30

After:

ptr ───────────► 20   30
```

Incrementing a pointer is commonly used when traversing an array.

### **Incrementing the Pointed Value**

To increment the value stored at the memory location referenced by the pointer, the pointer must first be dereferenced.

```c
int value = 10;
int *ptr = &value;

(*ptr)++;
```

The parentheses ensure that the dereference operation is applied before the postfix increment operator.

After execution, the pointer still references the same memory location, while the value stored there has increased.

```c
printf("%d\n", value);   // Output: 11
printf("%d\n", *ptr);    // Output: 11
```

```
Before:

ptr ─────► 10

After:

ptr ─────► 11
```

### **Postfix Increment with Dereference**

Now consider the following example.

```c
int arr[] = {10, 20, 30};
int *ptr = arr;

int x = *ptr++;
```

Since the **postfix** increment operator has higher precedence than the unary dereference operator, the compiler interprets the expression as

```c
int x = *(ptr++);
```

Execution proceeds as follows.

1. The value currently pointed to by `ptr` is read.
2. That value is assigned to `x`.
3. The pointer is incremented to point to the next array element.

After execution,

```c
printf("%d\n", x);       // Output: 10
printf("%d\n", *ptr);    // Output: 20
```

```
Before:

ptr ─────► 10   20   30

After:

x = 10

ptr ───────────► 20   30
```

Only the pointer is incremented. The array contents remain unchanged.

### **Prefix Increment with Dereference**

Now consider a similar example that uses the **prefix** increment operator.

```c
int arr[] = {10, 20, 30};
int *ptr = arr;

int x = *++ptr;
```

Since the prefix increment operator and the dereference operator have the same precedence, and unary operators associate from **right to left**, the compiler interprets the expression as

```c
int x = *(++ptr);
```

Execution proceeds as follows.

1. The pointer is incremented to point to the next array element.
2. The value at the new location is read.
3. That value is assigned to `x`.

After execution,

```c
printf("%d\n", x);       // Output: 20
printf("%d\n", *ptr);    // Output: 20
```

```
Before:

ptr ─────► 10   20   30

After:

ptr ───────────► 20   30

x = 20
```

Again, only the pointer is incremented. The array contents remain unchanged.

### **Comparison**

| Expression | Compiler Interprets It As | Effect |
|------------|---------------------------|--------|
| `ptr++` | `(ptr++)` | Increments the pointer. |
| `(*ptr)++` | `((*ptr)++)` | Increments the value pointed to by the pointer. |
| `*ptr++` | `*(ptr++)` | Reads the current value, then increments the pointer. |
| `*++ptr` | `*(++ptr)` | Increments the pointer, then reads the new value. |

Although these expressions differ by only a few characters, they perform entirely different operations. Understanding **what is being incremented** and **when the increment occurs** is essential for reading and writing correct pointer expressions.

The next section examines the commonly confused expressions `*ptr++`, `*++ptr`, `++*ptr`, and `(*ptr)++`, showing exactly how the compiler groups each expression and why each one behaves differently.
tr)++` in greater detail, showing exactly how the compiler groups each expression and why each one behaves differently.

---

## <font color='green'>3. Pointer Arithmetic</font>

Unlike ordinary integer arithmetic, pointer arithmetic is based on the **size of the object** that a pointer references rather than individual bytes. 

When a pointer is incremented or decremented, the compiler automatically adjusts its address so that it points to the next or previous object of the appropriate type.

For example,

```c
int arr[] = {10, 20, 30, 40};
int *ptr = arr;
```

Initially,

```
ptr
 │
 ▼
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
```

### **Adding an Integer to a Pointer**

Adding an integer to a pointer moves the pointer forward by that many elements.

```c
ptr = ptr + 2;
```

After execution, `ptr` points to the third element of the array.

```c
printf("%d\n", *ptr);    // Output: 30
```

```
Before: ptr ─────► 10   20   30   40

After: ptr ─────────────────► 30   40
```

Notice that the pointer moved by **two integers**, not two bytes.

The compiler automatically calculates the correct address by multiplying the offset by `sizeof(int)`.

### **Subtracting an Integer from a Pointer**

Subtracting an integer moves the pointer backward.

```c
ptr = ptr - 1;
```

If `ptr` previously pointed to the third element, it now points to the second element.

```c
printf("%d\n", *ptr);    // Output: 20
```

```
Before:

ptr ─────────────────► 30   40

After:

ptr ───────────► 20   30   40
```

Again, the compiler adjusts the address according to the size of the pointed type.

### **Why `ptr + 1` Does Not Add One Byte**

Suppose an `int` occupies four bytes.

```
Address        Value

1000           10
1004           20
1008           30
1012           40
```

If

```c
int *ptr = arr;
```

then

```c
ptr + 1
```

produces a pointer whose address is

```
1000 + sizeof(int)

= 1004
```

Similarly,

```c
ptr + 2
```

produces

```
1000 + 2 × sizeof(int)

= 1008
```

The compiler performs this scaling automatically for every pointer type.

For example,

| Pointer Type | `ptr + 1` Advances By |
|--------------|----------------------:|
| `char *` | 1 byte |
| `short *` | `sizeof(short)` bytes |
| `int *` | `sizeof(int)` bytes |
| `double *` | `sizeof(double)` bytes |

This automatic scaling allows the same arithmetic expression to work correctly regardless of the type being referenced.


---

## <font color='green'>4. Subtracting Two Pointers</font>

Two pointers can be subtracted if they both point into the **same array** (or one past its last element).

```c
int arr[] = {10, 20, 30, 40};

int *p1 = &arr[1];
int *p2 = &arr[3];

ptrdiff_t diff = p2 - p1;

printf("%td\n", diff);      // Output: 2
```

The result is **not** the number of bytes between the pointers. Instead, it is the **number of array elements separating them**.

```
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
       ^         ^
      p1        p2

Difference = 2 elements
```

The result of pointer subtraction has the type `ptrdiff_t`, which is defined in `<stddef.h>`.

---

## <font color='green'> 5. Valid Pointer Arithmetic </font>

The C language allows pointer arithmetic only within the bounds of the same array object.

For a pointer into an array, the following operations are valid.

- `ptr + n`
- `ptr - n`
- `ptr++`
- `ptr--`
- `ptr2 - ptr1` (when both pointers refer to the same array)

These operations allow a pointer to move between elements of an array while remaining valid.

### **One-Past-the-End Pointer**

A pointer is permitted to point **one element past the end** of an array.

```c
int arr[] = {10, 20, 30};

int *ptr = arr + 3;
```

Although `ptr` does not point to a valid array element, the pointer itself is valid.

This is commonly used when traversing arrays.

```c
for (int *p = arr; p < arr + 3; p++)
{
    printf("%d\n", *p);
}
```

The loop terminates when `p` becomes the one-past-the-end pointer.

<font color='red'> Although a one-past-the-end pointer is valid, dereferencing it is **undefined behavior**.</font>

```c
int *ptr = arr + 3;

printf("%d\n", *ptr);      // Undefined behavior
```

Similarly, moving a pointer before the first array element is also undefined.

```c
int *ptr = arr - 1;        // Undefined behavior
```

Pointer arithmetic is only defined while the resulting pointer remains within the same array object or one element beyond its end.

Attempting to move outside these limits results in undefined behavior, even if the program appears to work on a particular system.

---
## **Summary**

The following points summarize the key concepts of pointer arithmetic.

| Operation | Result |
|-----------|--------|
| `ptr + n` | Produces a pointer `n` elements after `ptr`. |
| `ptr - n` | Produces a pointer `n` elements before `ptr`. |
| `ptr++` | Advances the pointer to the next element. |
| `ptr--` | Moves the pointer to the previous element. |
| `ptr2 - ptr1` | Returns the number of elements between two pointers in the same array. |

Remember the following rules when performing pointer arithmetic:

- Pointer arithmetic is performed in units of the pointed type, **not bytes**.
- The compiler automatically scales the offset by `sizeof(type)`.
- Pointer arithmetic is only valid within the bounds of the same array object.
- A pointer may legally point **one element past the end** of an array, but it must never be dereferenced.
- Moving a pointer outside the array bounds or dereferencing an invalid pointer results in **undefined behavior**.

Understanding these rules helps ensure that pointer arithmetic is both correct and portable across different systems and data types.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
