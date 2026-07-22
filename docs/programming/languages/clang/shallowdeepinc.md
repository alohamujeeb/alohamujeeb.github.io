---
hide:
  - navigation
  
tags:
  - Shallow Copy in C
  - Deep Copy in C
  
---

# Understanding Shallow and Deep Copy in C

*This article is intended for intermediate and advanced C programmers. It explains the concepts of shallow and deep copy, how they differ, and why understanding the distinction is essential when working with pointers, structures, and dynamically allocated memory in C.*

---

## <font color='green'>1. Copying a Structure</font>

In C, one structure can be copied to another using the assignment operator.

For example,

```c
struct Point
{
    int x;
    int y;
};

struct Point p1 = {10, 20};
struct Point p2 = p1;
```

After the assignment, `p2` contains a copy of every member of `p1`. Since the structure contains only ordinary data members, the two structures are completely independent.

<font color='red'>However, not all structures contain only ordinary data members. A structure may also contain one or more pointers.</font>

Structure assignment still copies every member. However, copying a pointer is fundamentally different from copying an ordinary data member.

Understanding this difference leads to the concepts of **shallow copy** and **deep copy**, which are essential when working with pointers and dynamically allocated memory.

---

## <font color='green'>2. Shallow Copy</font>

Consider the following structure, which contains a pointer to an integer.

```c
struct Number
{
    int *value;
};

int x = 100;

struct Number num1;
num1.value = &x;

struct Number num2 = num1;
```

The assignment

```c
struct Number num2 = num1;
```

copies all the members of `num1` into `num2`. Since `value` is a pointer, the address stored in `num1.value` is copied into `num2.value`. The integer being pointed to is **not** copied.

As a result, both `num1.value` and `num2.value` point to the same integer `x`.

```text
        +--------+
num1 -->| value  |----+
        +--------+    |
                      v
                    +-----+
                    | 100 |
                    +-----+
                      ^
                      |
        +--------+    |
num2 -->| value  |----+
        +--------+
```

Although there are now two structure objects (`num1` and `num2`), there is still only **one** integer object. Both pointers refer to the same memory location, so modifying the integer through either pointer affects the same object.

This behavior is known as a **shallow copy**.


---

## <font color='green'>3. Deep Copy</font>

In a **deep copy**, a new object is created for every pointer member in the structure. Instead of copying the pointer value, memory is allocated for a new object, and the data is copied into it.

The following example performs a deep copy of the previous structure.

```c
struct Number
{
    int *value;
};

int x = 100;

//Create one variable
struct Number num1;
num1.value = malloc(sizeof(int));
*num1.value = x;

//Create second variable (we must allocate space for this as well)
struct Number num2;
num2.value = malloc(sizeof(int));

//Copy the integer value
*num2.value = *num1.value;
```

Unlike the shallow copy example, `num1.value` and `num2.value` now point to two different integer objects. Although both integers initially contain the same value, they occupy different memory locations.

```text
        +--------+
num1 -->| value  |---------> +-----+
        +--------+           | 100 |
                             +-----+

        +--------+
num2 -->| value  |---------> +-----+
        +--------+           | 100 |
                             +-----+
```

Since each structure owns its own integer object, modifying one does not affect the other. Likewise, each object can be safely released without affecting the other.

This behavior is known as a **deep copy**.


---

## <font color='green'>4. Example: Shallow Copy vs Deep Copy</font>

Consider the following structure representing a student.

```c
struct Student
{
    int id;
    char *name;
};
```

The `id` member is an ordinary integer, whereas `name` is a pointer to dynamically allocated memory.


**Shallow Copy**

```c
struct Student s1;

s1.id = 101;

s1.name = malloc(20);  //allocate space of size 20
strcpy(s1.name, "Mujeeb");

struct Student s2 = s1;
```

After the assignment:

- `s2.id` is an independent copy of `s1.id`.
- `s2.name` contains the same address as `s1.name`.

```text
                 +----------------------+
s1 ------------->| id = 101             |
                 | name ----------------+----------+
                 +----------------------+          |
                                                   |
                                                   v
                                               +---------+
                                               | "Mujeeb" |
                                               +---------+
                                                   ^
                                                   |
                 +----------------------+          |
s2 ------------->| id = 101             |
                 | name -----------------+----------+
                 +----------------------+
```

Although there are two `Student` structures, there is only one copy of the string `"Mujeeb"`. Any modification to the string through either structure is reflected in the other. Likewise, freeing `s1.name` leaves `s2.name` pointing to invalid memory.

> <font color='red'>A shallow copy is appropriate only when sharing the pointed-to object is intentional. Otherwise, a deep copy should be used to ensure that each structure owns its own dynamically allocated memory. </font>


**Deep Copy**

```c
struct Student s2;

s2.id = s1.id;  //non-pointre data (int) can be copied as normal using = operator

//for pointer data, we must allocate space first 
s2.name = malloc(strlen(s1.name) + 1); // Allocate memory for a new string
strcpy(s2.name, s1.name); // Copy the string into the new memory
```

In this case:

- `id` is copied as before.
- A new block of memory is allocated for `name`.
- The string is copied into the newly allocated memory.

```text
                 +----------------------+
s1 ------------->| id = 101             |
                 | name ---------------------------> +---------+
                 +----------------------+            | "Mujeeb" |
                                                     +---------+

                 +----------------------+
s2 ------------->| id = 101             |
                 | name ---------------------------> +---------+
                 +----------------------+            | "Mujeeb" |
                                                     +---------+
```

The two structures are now completely independent. Modifying or freeing `s1.name` has no effect on `s2.name`, and vice versa.


---

## <font color='green'>5. Summary</font>

- Structure assignment copies every member.
- Ordinary data members are copied by value.
- Pointer members copy only the stored address.
- A **shallow copy** shares the pointed-to object.
- A **deep copy** allocates new memory and duplicates the pointed-to data, allowing each structure to manage its own resources independently.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
