---
hide:
  - navigation
  
tags:
  - OOP Philosophy

---
# The Philosophy Behind Classes and Objects

Before learning the syntax of classes and objects in Python, it's useful to understand why programming languages provide them in the first place.


---
## <font color="green"> 1. Built-in Data Types</font>

Programming languages provide several built-in data types, such as:

- `int`
- `float`
- `bool`
- `str`

These data types represent common kinds of data.

For example:

```python
age = 25
salary = 85000.50
name = "Boris"
is_active = True
```

Each data type also comes with operations that can be performed on it.

For example, integers support arithmetic operations.

```python
a = 10
b = 5

print(a + b)
print(a * b)
```

Strings provide operations such as concatenation and searching.

```python
name = "Boris"

print(name.upper())
print(name.startswith("A"))
```

A data type is more than just data—it also provides operations for working with that data.

---

## <font color="green"> 2. Built-in Data Types Are Not Enough</font>

Real-world programs often work with things that are not built into Python.

For example:

- Students
- Employees
- Customers
- Books
- Bank Accounts
- Cars

Python does not provide data types for these concepts.

Suppose you're writing a school management system.

A student has information such as:

- Name
- Roll number
- Age
- Grade

You could store this information in separate variables.

```python
student_name = "Boris"
student_roll = 101
student_age = 20
student_grade = "A"
```

But these variables all belong to the same student.

They represent one logical entity.

---

## <font color="green">3. Grouping Related Data</font>

Instead of scattering related information across multiple variables, it is better to group it together.

Think of a student as a single unit that contains all of its related information.

```
Student
├── Name
├── Roll Number
├── Age
└── Grade
```

Now the entire student can be treated as one object rather than several unrelated variables.

---

## <font color="green">4. Data Also Needs Operations</font>

Storing data alone is not enough.

We also perform operations on that data.

For a student, we might:

- Display student details
- Calculate GPA
- Update the grade
- Check attendance

These operations naturally belong with the student's data.

Just as integers provide arithmetic operations,

```
10 + 20
30 * 5
```

a student data type can provide operations such as

```
display()
calculate_gpa()
update_grade()
```

The operations are part of the data type itself.

---

## <font color="green">5. Creating New Data Types</font>

Programming languages allow programmers to define their own data types.

A programmer can create a new data type called `Student`.

That data type contains:

- Data (attributes)
- Operations (methods)

```
Student
├── Data
│   ├── Name
│   ├── Roll Number
│   ├── Age
│   └── Grade
│
└── Operations
    ├── display()
    ├── calculate_gpa()
    └── update_grade()
```

Similarly, an `Employee` data type might contain

```
Employee
├── Data
│   ├── Name
│   ├── Employee ID
│   ├── Salary
│   └── Department
│
└── Operations
    ├── display()
    ├── calculate_bonus()
    └── promote()
```

---

## <font color="green"> 6. Classes and Objects</font>

A **class** defines a new data type.

An **object** is an individual value created from that data type.

For example, if `Employee` is a class, then

- Sergei is one employee object.
- Boris is another employee object.
- Charlie is another employee object.

Each object stores its own data, but they all share the same operations.

---

## <font color="green"> 7. Summary</font>

Built-in data types such as `int`, `float`, and `str` are suitable for common kinds of data. However, real-world programs often need to represent concepts such as students, employees, customers, and bank accounts.

Classes allow programmers to create their own data types by combining related data with the operations that work on that data.

An object is an individual instance of such a data type.



---
## **Relevant Links**

[Python Material on this website](../index.md)

