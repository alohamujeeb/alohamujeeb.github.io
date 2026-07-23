---
hide:
  - navigation

tags:
  - Pointer to Pointer

---

# Pointer to Pointer in C: Use Cases

*This article is intended for intermediate and advanced C programmers. It explains why pointer-to-pointer variables are used in C and presents common real-world scenarios where they are required. Rather than focusing solely on the syntax, this article emphasizes the practical problems that pointer-to-pointer variables are designed to solve.*

---
## <font color='green'>1. Why Use a Pointer to a Pointer?</font>

A pointer to a pointer is simply a pointer whose value is the address of another pointer.

The general declaration is:

```c
data_type **pointer_name;
```

For example,

```c
int value = 100;

int *p = &value;    /* Pointer to an integer */
int **pp = &p;      /* Pointer to a pointer */
```

Here,

- `value` stores an integer.
- `p` stores the address of `value`.
- `pp` stores the address of `p`.

This relationship is illustrated below.

```text
+-------+
| value |
|  100  |
+-------+
     ^
     |
     |  p = &value
     |
+-------+
|   p   |
+-------+
     ^
     |
     |  pp = &p
     |
+-------+
|  pp   |
+-------+
```

At first glance, a pointer to a pointer may seem unnecessary. Why would we want a pointer that points to another pointer instead of directly to the data?

The answer is that there are situations where the pointer itself is the object that needs to be accessed or modified.

The most common use cases are:

- Creating dynamically allocated two-dimensional arrays.
- Managing arrays of pointers, such as arrays of strings.
- Allowing a function to modify a pointer owned by the caller.
- Manipulating dynamic data structures such as linked lists and trees.

The following sections explain each of these scenarios and demonstrate why a pointer to a pointer is the appropriate solution.

---
## <font color='green'>2. Use Case 1: Modifying a Pointer Inside a Function</font>

One of the most common reasons for using a pointer to a pointer is to allow a function to modify a pointer owned by the caller.

Consider the following example.

```c
void allocate(int *p)
{
    p = malloc(sizeof(int));
}

int *ptr = NULL;

allocate(ptr);
```

Although `allocate()` assigns memory to `p`, the caller's pointer (`ptr`) remains `NULL`.

Why?

When a function is called, its parameters are passed by value. The pointer `p` is therefore a copy of `ptr`.

```text
Caller                     Function

ptr -----> NULL      p -----> NULL
        (copied)
```

Assigning a new address to `p` changes only the copy. The original pointer owned by the caller is unaffected.

To modify the caller's pointer, the function must receive the **address of the pointer**.

```c
void allocate(int **p)
{
    *p = malloc(sizeof(int));
}

int *ptr = NULL;

allocate(&ptr);
```

Now the relationship becomes:

```text
ptr -----> NULL
 ^
 |
 +--------- p (int **)
```

The function receives the address of `ptr`, allowing it to modify the pointer itself rather than a copy of it.

After the call,

```text
ptr
 |
 v
+------+
| 100  |
+------+
```

Whenever a function needs to allocate memory, change a pointer, or replace one pointer with another, a pointer to a pointer is often the appropriate solution.

---
## <font color='green'>3. Use Case 2: Creating Dynamic Two-Dimensional Arrays</font>

Another common use of a pointer to a pointer is creating a two-dimensional array whose dimensions are not known until the program is running.

Suppose a program asks the user for the number of rows and columns.

```c
int rows, cols;

scanf("%d %d", &rows, &cols);
```

Since the array size is determined at runtime, it cannot be declared as a fixed-size array.

Instead, memory can be allocated dynamically.

```c
int **matrix;

matrix = malloc(rows * sizeof(int *));

for (int i = 0; i < rows; i++)
{
    matrix[i] = malloc(cols * sizeof(int));
}
```

The resulting memory layout is:

```text
               matrix
                  |
                  v
        +-----+-----+-----+
        |  *  |  *  |  *  |
        +--|--+--|--+--|--+
           |     |     |
           |     |     |
           v     v     v

      +---+---+---+   +---+---+---+   +---+---+---+
      |   |   |   |   |   |   |   |   |   |   |   |
      +---+---+---+   +---+---+---+   +---+---+---+
```

The variable `matrix` points to an array of row pointers. Each row pointer, in turn, points to a dynamically allocated row of integers.

Elements are accessed using the familiar array notation.

```c
matrix[1][2] = 25;
```

This expression is equivalent to:

```c
*(*(matrix + 1) + 2) = 25;
```

Because each row is allocated independently, the rows do not need to have the same length. This makes it possible to create **jagged arrays**, where each row contains a different number of elements.

```text
               matrix
                  |
                  v
        +-----+-----+-----+
        |  *  |  *  |  *  |
        +--|--+--|--+--|--+
           |     |     |
           |     |     |
           v     v     v

      +---+---+       +---+---+---+---+---+       +---+
      |   |   |       |   |   |   |   |   |       |   |
      +---+---+       +---+---+---+---+---+       +---+
```

A pointer to a pointer is appropriate here because the top-level object is an array of pointers, with each pointer referencing a separate block of memory.

---
## <font color='green'>4. Use Case 3: Managing Arrays of Pointers</font>

A pointer to a pointer is also used when working with an array whose elements are themselves pointers.

A common example is an array of strings.

```c
char *names[] =
{
    "Mujeeb",
    "Ciang",
    "Shyam"
};
```

Each element of the array is a pointer to the first character of a string.

The memory layout looks like this.

```text
              names
                |
                v
      +-----+-----+-----+
      |  *  |  *  |  *  |
      +--|--+--|--+--|--+
         |     |     |
         |     |     |
         v     v     v

     "Mujeeb" "Ciang" "Shyam"
```

Since `names` is the address of the first element of an array of pointers, its type is:

```c
char **
```

This allows the array to be traversed using pointer arithmetic.

```c
char **p = names;

printf("%s\n", *p);       /* Mujeeb   */
printf("%s\n", *(p + 1)); /* Ciang     */
printf("%s\n", *(p + 2)); /* Shyam */
```

### 4.1 `argv` in the `main()`

One of the most common uses of this concept is the `argv` parameter of the `main()` function.

```c
int main(int argc, char *argv[])
{
    ...
}
```

The declaration above is equivalent to:

```c
int main(int argc, char **argv)
{
    ...
}
```

When a program is executed as:

```text
program input.txt output.txt
```

the memory layout is conceptually:

```text
               argv
                 |
                 v
       +-----+-----+-----+
       |  *  |  *  |  *  |
       +--|--+--|--+--|--+
          |     |     |
          |     |     |
          v     v     v

     "program"
     "input.txt"
     "output.txt"
```

Each command-line argument is a string, and `argv` points to an array of pointers to those strings. A pointer to a pointer is therefore the natural type for representing the collection.


---
## <font color='green'>5. Use Case 4: Manipulating Dynamic Data Structures</font>

Pointer-to-pointer variables are frequently used when implementing dynamic data structures such as linked lists and trees.

Consider a simple singly linked list.

```c
struct Node
{
    int value;
    struct Node *next;
};
```

The list is identified by a pointer to its first node.

```c
struct Node *head = NULL;
```

Suppose we want to insert a new node at the beginning of the list.

If the insertion function receives only a copy of `head`, any changes made to it affect only the local copy.

```c
void insert(struct Node *head, int value)
{
    ...
}
```

Since `head` is passed by value, assigning a new node to it does not change the caller's pointer.

Instead, the function must receive the address of `head`.

```c
void insert(struct Node **head, int value)
{
    struct Node *newNode = malloc(sizeof(struct Node));

    newNode->value = value;
    newNode->next = *head;

    *head = newNode;
}
```

The function is called as follows.

```c
struct Node *head = NULL;

insert(&head, 10);
insert(&head, 20);
insert(&head, 30);
```

After these calls, the list contains:

```text
head
 |
 v
+----+    +----+    +----+
| 30 |--->| 20 |--->| 10 |---> NULL
+----+    +----+    +----+
```

The function updates the caller's `head` pointer each time a new node is inserted.

The same technique is used when:

- inserting or deleting nodes in linked lists,
- updating the root of a tree,
- modifying the head of a queue or stack,
- and implementing many other dynamic data structures.

In all of these cases, the pointer identifying the structure may need to change. Passing a pointer to that pointer allows the function to update it directly.

---
## <font color='green'>6. Summary</font>

A pointer to a pointer is simply a pointer whose value is the address of another pointer.

Although the syntax may initially appear confusing, the concept becomes straightforward once you recognize the situations in which another level of indirection is required.

This article presented four common use cases.

| Use Case | Why a Pointer to a Pointer is Needed |
|----------|---------------------------------------|
| Modifying a pointer inside a function | The function must update the caller's pointer. |
| Dynamic two-dimensional arrays | The top-level object is an array of row pointers. |
| Arrays of pointers | The collection contains pointers rather than data objects. |
| Dynamic data structures | Functions often need to update pointers such as the head of a list or the root of a tree. |

A useful way to think about pointer-to-pointer variables is to ask the following question:

> **Is the object I want to access or modify itself a pointer?**

If the answer is **yes**, then a pointer to a pointer is often the correct solution.

Understanding this principle makes it much easier to recognize when `T **` is appropriate, rather than simply memorizing syntax or specific programming patterns.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
