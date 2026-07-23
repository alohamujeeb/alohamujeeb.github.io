---
hide:
  - navigation
  
tags:
  - Flexible Array Members
  - FAM
  
---
# Flexible Array Members in C

*This article is intended for intermediate and advanced C programmers. It explains what Flexible Array Members (FAMs) are, why they were introduced in C99, and how they enable structures to represent variable-sized objects using a single contiguous memory allocation.*


---
## <font color='green'>1. What Are Flexible Array Members?</font>

*In C, every object created from the same structure type normally occupies exactly the same amount of memory. This works well when every member has a fixed size. However, some members, such as names, messages, filenames, or network payloads, can vary in length. Flexible Array Members (FAMs), introduced in C99, solve this problem by allowing the final part of a structure to have a size determined when the object is allocated.*

### **Case 1: Fixed Arrays**
Consider a simple structure representing a student.

```c
typedef struct
{
    int id;
    char name[100];
} Student;
```

The `name` member can store up to 100 characters.

```
+------+----------------------------------------+
|  ID  |               Name[100]                |
+------+----------------------------------------+
```

This approach is simple, but it has two obvious disadvantages.

- Most names are much shorter than 100 characters, resulting in wasted memory.
- If a name exceeds 100 characters, it cannot be stored without truncation or risking a buffer overflow.


### **Case 2: Pointers**
A natural alternative is to replace the array with a pointer.

```c
typedef struct
{
    int id;
    char *name;
} Student;
```

Now the name can be any length.

```c
Student *s = malloc(sizeof(Student));

s->id = 1;
s->name = malloc(strlen("Christopher") + 1);

strcpy(s->name, "Christopher");
```

The memory layout becomes

```
            Student object

+------+------------+
|  ID  | name ------+----------+
+------+------------+          |
                               |
                               |
                               v
                  +------------------------+
                  |     "Christopher"      |
                  +------------------------+
```

This eliminates the fixed-size limitation, but introduces a different problem.

The student is now represented by **two separate memory allocations**:

- one allocation for the structure
- another allocation for the name

Consequently:

- two calls to `malloc()` are required,
- two calls to `free()` are required,
- the structure and its name may be located far apart in memory.

In many applications, however, the name is not an independent object. It is simply part of the student.

This is precisely the problem that Flexible Array Members were designed to solve.


### **Case 3: Empty Array (FAM)**

Instead of storing a pointer, the final member is declared as an array with no specified size.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

Although `name` appears to be an ordinary array, no storage is reserved for it when the compiler determines the size of the structure. Instead, the required space is supplied when the structure is allocated.

```c
Student *s =
    malloc(sizeof(Student) + strlen("Christopher") + 1);

s->id = 1;
strcpy(s->name, "Christopher");
```

The resulting memory layout is

```
+------+------------------------+
|  ID  |     "Christopher"      |
+------+------------------------+
^
|
Student object
```

Compared to the pointer-based approach:

- only one memory allocation is required,
- only one call to `free()` is needed,
- the structure and its variable-length data occupy one contiguous block of memory.

Conceptually, a Flexible Array Member allows a structure to represent a **single variable-sized object**, rather than a fixed-size object that points to separately allocated memory.

The following section explains the syntax and language rules governing Flexible Array Members, including why they must appear as the final member of a structure and how they affect the result of the `sizeof` operator.

---
## <font color='green'>2. Declaring Flexible Array Members</font>

A Flexible Array Member is declared by specifying an array with no size as the **last member** of a structure.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

Unlike an ordinary array, the compiler does **not** allocate storage for `name` as part of the structure. Instead, `name` serves as a placeholder indicating that additional storage may follow the fixed portion of the structure.

This is why the declaration is known as a **Flexible Array Member**—its size is determined when the structure is allocated, not when the structure type is defined.

### Flexible Array Members Must Be the Last Member

A Flexible Array Member can appear **only as the final member** of a structure.

For example,

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

is valid.

However,

```c
typedef struct
{
    int id;
    char name[];
    int age;
} Student;
```

is invalid.

The compiler cannot determine where `age` should be placed because the size of `name` is not known when the structure type is defined.

### A Structure Can Have Only One Flexible Array Member

Since a Flexible Array Member must be the last member, a structure can contain **at most one** Flexible Array Member.

The following declaration is invalid.

```c
typedef struct
{
    char firstName[];
    char lastName[];
} Person;
```

There is no way to determine where `lastName` begins because the size of `firstName` is unknown.

### The Flexible Array Member Contributes Nothing to `sizeof`

One of the most important properties of a Flexible Array Member is that it does **not** contribute to the size of the structure.

Consider the following declaration.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

The memory layout known to the compiler is

```text
+------+
|  ID  |
+------+
```

The flexible array member is not included because its size is unknown.

Therefore,

```c
sizeof(Student)
```

returns only the size of the fixed portion of the structure.

This differs from an ordinary array.

```c
typedef struct
{
    int id;
    char name[100];
} Student;
```

whose layout is

```text
+------+----------------------------------------+
|  ID  |               Name[100]                |
+------+----------------------------------------+
```

Here,

```c
sizeof(Student)
```

includes both the `id` member and the 100-byte array because every object of the structure has the same fixed size.

### Flexible Array Members Cannot Be Used as Standalone Objects

Since a Flexible Array Member has no storage of its own, declaring an automatic or static object of the structure type is generally not useful.

```c
Student s;
```

The object contains storage only for the fixed members.

```text
+------+
|  ID  |
+------+
```

There is no space for `name`, so attempting to store characters in it results in undefined behavior.

Instead, structures containing Flexible Array Members are almost always created by dynamically allocating sufficient memory for both the fixed members and the flexible array.

---
## <font color='green'>3. Allocating Structures with Flexible Array Members</font>

Unlike ordinary arrays, a Flexible Array Member does not occupy any storage within the structure itself. Therefore, whenever an object containing a Flexible Array Member is created, sufficient memory must be allocated for both:

- the fixed portion of the structure, and
- the flexible array.

Consider the following structure.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

Suppose we want to store the name `"Christopher"`.

The total memory required is:

- the size of the `Student` structure, and
- enough space for all characters in the name, including the terminating null character.

The allocation is therefore

```c
Student *s =
    malloc(sizeof(Student) +
           strlen("Christopher") + 1);
```

The `+ 1` reserves space for the terminating `'\0'`.

Once allocated, the object can be initialized normally.

```c
s->id = 1;

strcpy(s->name, "Christopher");
```

The resulting memory layout is

```text
+------+------------------------+
|  ID  |     "Christopher"      |
+------+------------------------+
^
|
Student object
```

Although `name` is declared as an array with no specified size, it behaves exactly like an ordinary character array because the additional memory immediately follows the fixed portion of the structure.

For example,

```c
printf("%s\n", s->name);

printf("%zu\n", strlen(s->name));

s->name[0] = 'C';
```

No special syntax is required to access the Flexible Array Member.

### Flexible Array Members Are Not Limited to Characters

Flexible Array Members can store any data type.

For example,

```c
typedef struct
{
    size_t count;
    int values[];
} IntArray;
```

Suppose we want to store ten integers.

```c
IntArray *arr =
    malloc(sizeof(IntArray) +
           10 * sizeof(int));

arr->count = 10;
```

The memory layout becomes

```text
+---------+---------------------------------------+
| count   |           values[10]                  |
+---------+---------------------------------------+
^
|
IntArray object
```

The elements can be accessed exactly like an ordinary array.

```c
for (size_t i = 0; i < arr->count; i++)
{
    arr->values[i] = (int)i;
}
```

Since `values` occupies contiguous memory immediately after the fixed members, array indexing works exactly as expected.

### Deallocating a Structure with a Flexible Array Member

Unlike pointer-based designs, there is no separate allocation for the flexible array.

For example, using a pointer requires two deallocations.

```c
free(s->name);
free(s);
```

However, with a Flexible Array Member, both the structure and its variable-length data belong to the same memory block.

Therefore, only a single call to `free()` is required.

```c
free(s);
```

>This is one of the primary advantages of Flexible Array Members—they simplify memory management by treating the fixed members and the variable-length data as a single object.

---
## <font color='green'>4. Common Usage Patterns</font>

Flexible Array Members are useful whenever a structure contains data whose size is not known until runtime. Rather than storing a pointer to separately allocated memory, the variable-length data becomes part of the structure itself.

The following are some common applications.

### Variable-Length Strings

One of the simplest uses of a Flexible Array Member is storing strings whose length varies.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

Instead of reserving a large fixed-size array for every student, memory is allocated according to the actual length of the name.

```c
Student *s =
    malloc(sizeof(Student) +
           strlen("Christopher") + 1);
```

Memory layout:

```text
+------+------------------------+
|  ID  |     "Christopher"      |
+------+------------------------+
```

This avoids both wasted memory and the need for a separate allocation for the string.

---

### Variable-Length Binary Buffers

Flexible Array Members are frequently used to store arbitrary binary data.

```c
typedef struct
{
    size_t size;
    uint8_t data[];
} Buffer;
```

Suppose a buffer must store 512 bytes.

```c
Buffer *buf =
    malloc(sizeof(Buffer) + 512);

buf->size = 512;
```

Memory layout:

```text
+---------+--------------------------------------+
|  size   |           512 bytes                  |
+---------+--------------------------------------+
```

Since the data immediately follows the structure, the entire buffer can be treated as a single object.

---

### Network Packets

Network protocols often contain a fixed-size header followed by a payload whose size depends on the packet being transmitted.

```c
typedef struct
{
    uint16_t type;
    uint16_t length;
    uint8_t payload[];
} Packet;
```

Memory layout:

```text
+--------+---------+-----------------------------+
|  type  | length  |          payload            |
+--------+---------+-----------------------------+
```

The `length` field indicates the number of bytes stored in the payload.

This design closely matches the layout of many real network packets and avoids maintaining a separate pointer for the payload.

---

### File or Database Records

Variable-length records are common in file formats and databases.

```c
typedef struct
{
    uint32_t recordId;
    char filename[];
} FileRecord;
```

Different records may contain filenames of different lengths.

```text
Record 1

+-----------+-------------+
| recordId  | "log.txt"   |
+-----------+-------------+

Record 2

+-----------+--------------------------------+
| recordId  | "annual_report_2025.pdf"       |
+-----------+--------------------------------+
```

Although both objects are instances of the same structure type, each occupies only the memory required for its filename.

---

### Custom Containers

Flexible Array Members are commonly used when implementing custom containers whose capacity is determined during creation.

```c
typedef struct
{
    size_t capacity;
    size_t size;
    int elements[];
} Vector;
```

When creating the container, memory is allocated according to the required capacity.

```c
Vector *v =
    malloc(sizeof(Vector) +
           100 * sizeof(int));

v->capacity = 100;
v->size = 0;
```

Memory layout:

```text
+----------+------+----------------------------------+
| capacity | size |         elements[100]            |
+----------+------+----------------------------------+
```

The container metadata and storage occupy one contiguous memory block, simplifying allocation and deallocation.

Flexible Array Members are therefore widely used in systems programming, networking, embedded software, file formats, memory allocators, and other performance-critical applications where variable-length data naturally belongs to the object that owns it.


---
## <font color='green'>5. Advantages and Limitations</font>

Flexible Array Members provide an efficient way to represent variable-sized objects. They reduce memory overhead, improve cache locality, and simplify memory management. However, they also come with several restrictions imposed by the C standard.

### Advantages

#### Efficient Memory Utilization

Unlike fixed-size arrays, a Flexible Array Member occupies only as much memory as is actually required.

For example,

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

A student named `"Tom"` occupies less memory than a student named `"Christopher"` because each object is allocated according to the actual length of the name.

This avoids the wasted space associated with large fixed-size arrays.

---

#### Single Memory Allocation

A pointer-based design requires two allocations.

```c
Student *s = malloc(sizeof(Student));

s->name = malloc(strlen(name) + 1);
```

With a Flexible Array Member, both the structure and its variable-length data are allocated together.

```c
Student *s =
    malloc(sizeof(Student) +
           strlen(name) + 1);
```

This reduces allocation overhead and simplifies memory management.

---

#### Improved Cache Locality

Since the flexible array immediately follows the fixed members of the structure, all related data resides in one contiguous memory block.

```text
+------+----------------------------+
|  ID  |           Name             |
+------+----------------------------+
```

Sequential access is generally more cache-friendly than accessing separately allocated memory through pointers.

---

#### Simplified Deallocation

Pointer-based structures require multiple calls to `free()`.

```c
free(s->name);
free(s);
```

A structure containing a Flexible Array Member requires only one.

```c
free(s);
```

This reduces the likelihood of memory leaks and simplifies ownership.

---

### Limitations

#### Must Be the Last Member

A Flexible Array Member must always be the final member of a structure.

```c
typedef struct
{
    int id;
    char name[];
} Student;
```

Attempting to place another member after the flexible array is not permitted.

---

#### Only One Flexible Array Member

Since it must appear last, a structure can contain only one Flexible Array Member.

The following declaration is invalid.

```c
typedef struct
{
    char firstName[];
    char lastName[];
} Person;
```

---

#### Dynamic Allocation Is Required

A Flexible Array Member has no storage unless additional memory is allocated.

Therefore,

```c
Student s;
```

creates storage only for the fixed members.

Attempting to use

```c
strcpy(s.name, "John");
```

results in undefined behavior because no memory exists for the flexible array.

---

#### The Programmer Must Calculate the Allocation Size

The compiler does not automatically determine how much memory should be allocated.

The programmer must explicitly calculate the required size.

```c
Student *s =
    malloc(sizeof(Student) +
           strlen(name) + 1);
```

Allocating too little memory results in undefined behavior.

---

#### Cannot Be Resized Automatically

A Flexible Array Member does not grow or shrink automatically.

If more space is required, the entire object must be reallocated.

```c
s = realloc(s,
            sizeof(Student) +
            newLength + 1);
```

Since the structure and its flexible array form a single memory block, both are resized together.

---

Flexible Array Members are an excellent choice when variable-length data naturally belongs to the structure that owns it. They are widely used in systems programming, networking, embedded software, file formats, and custom memory allocators because they combine efficiency with a simple and intuitive memory layout.

The next section concludes the discussion with a summary of the key concepts covered in this article.

---
## <font color='green'>6. Summary</font>

In this article, you learned how **Flexible Array Members (FAMs)** provide an efficient way to represent variable-sized objects in C by allowing the final member of a structure to have a size determined when the object is allocated.

The key concepts covered include:

- Every object created from an ordinary structure type normally has the same size.
- Fixed-size arrays are simple but may waste memory or impose unnecessary size limits.
- Using pointers removes the size limitation but requires separate memory allocations for the structure and its variable-length data.
- A Flexible Array Member is declared as an array with no specified size and must appear as the last member of a structure.
- A Flexible Array Member contributes nothing to the result of the `sizeof` operator.
- Objects containing Flexible Array Members must be dynamically allocated with sufficient space for both the fixed members and the flexible array.
- The flexible array behaves like an ordinary array once the object has been allocated.
- Since the structure and its variable-length data occupy a single contiguous memory block, only one allocation and one deallocation are required.
- Flexible Array Members are commonly used for variable-length strings, binary buffers, network packets, file records, and custom containers.
- Although Flexible Array Members improve memory efficiency and cache locality, they require careful allocation size calculations and can only appear as the final member of a structure.

Flexible Array Members are a simple yet powerful feature introduced in C99. They allow programmers to model variable-length data as part of a single object instead of managing multiple related memory allocations. When used appropriately, they lead to cleaner data structures, simpler memory management, and more efficient programs, making them a valuable tool in systems programming, networking, embedded software, and performance-critical applications.











---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
