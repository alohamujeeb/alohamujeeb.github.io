---
hide:
  - navigation
  
tags:
  - Classes in Python
  - Objects in Python
  - __init__ 
  - Constructor in Python
  - Self parameter in Python

---

# Creating Classes and Objects in Python

let us see how to define classes, create objects (instances), and work with their attributes in Python. This article assumes we're already familiar with the concepts of classes and objects.

---

## <font color='green'>1. Defining a Class and Creating Objects</font>

A **class** defines a new data type, while an **object** (or **instance**) is an individual value created from that data type.

A class is defined using the `class` keyword.

```python
class Employee:
    pass
```

The `pass` statement indicates that the class currently contains no attributes or methods.

Once a class has been defined, objects can be created by calling the class name like a function.

```python
emp1 = Employee()
emp2 = Employee()
```

Here:

- `Employee` is the class.
- `emp1` and `emp2` are two different objects (instances) of the `Employee` class.

Each call to `Employee()` creates a new object.

```python
print(type(emp1))
print(type(emp2))
```

Output

```text
<class '__main__.Employee'>
<class '__main__.Employee'>
```

Although `emp1` and `emp2` belong to the same class, they are independent objects.

---

## <font color='green'>2. Defining Attributes Within a Class</font>

An **attribute** is a piece of data that belongs to an object.

For example, an `Employee` object might store attributes such as:

- `name`
- `age`
- `department`

One way to define these attributes is to declare them directly within the class.

```python
class Employee:
    name = ""
    age = 0
    department = ""

emp1 = Employee()
emp2 = Employee()
```

Here, the class defines three attributes:

- `name`
- `age`
- `department`

Every object created from the `Employee` class has access to these attributes.

```python
print(emp1.name)
print(emp1.age)
print(emp1.department)
```

Output

```text

0

```

Each object can assign its own values to these attributes.

```python
emp1.name = "Sergei"
emp1.age = 25
emp1.department = "Engineering"

emp2.name = "Boris"
emp2.age = 30
emp2.department = "Sales"

print(emp1.name, emp1.age, emp1.department)
print(emp2.name, emp2.age, emp2.department)
```

Output

```text
Sergei 25 Engineering
Boris 30 Sales
```

This approach is similar to languages such as Java and C++, where the expected data members are declared when the class is defined.

---

## <font color='green'>3. Creating Attributes Dynamically</font>

**Unlike many programming languages, Python also allows attributes to be created dynamically.**

Instead of defining attributes within the class, they can be created simply by assigning values to an object.

```python
class Employee:
    pass

emp = Employee()

emp.name = "Sergei"
emp.age = 25
emp.department = "Engineering"
```

Each assignment creates a new attribute for the object.

The same dot (`.`) operator is used to access the attribute values.

```python
print(emp.name)
print(emp.age)
print(emp.department)
```

Output

```text
Sergei
25
Engineering
```

Since attributes are created dynamically, different objects can contain different sets of attributes.

```python
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.name = "Sergei"
emp1.age = 25

emp2.name = "Boris"
emp2.salary = 75000
```

Here:

- `emp1` has the attributes `name` and `age`.
- `emp2` has the attributes `name` and `salary`.

Trying to access an attribute that doesn't exist raises an `AttributeError`.

```python
print(emp1.salary)
```

Output

```text
AttributeError: 'Employee' object has no attribute 'salary'
```

Although Python supports dynamic attributes, most Python programs initialize an object's attributes using a constructor.

---

## <font color='green'>4. Initializing Attributes Using the Constructor</font>

Python provides a special method named `__init__()` to initialize an object's attributes.

This method is called the **constructor**.

```python
class Employee:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.department = ""
```

Whenever an object is created, Python automatically calls the constructor.

```python
emp1 = Employee()
emp2 = Employee()
```

Each object begins with its own `name`, `age`, and `department` attributes.

```python
emp1.name = "Sergei"
emp1.age = 25
emp1.department = "Engineering"

emp2.name = "Boris"
emp2.age = 30
emp2.department = "Sales"

print(emp1.name, emp1.age, emp1.department)
print(emp2.name, emp2.age, emp2.department)
```

Output

```text
Sergei 25 Engineering
Boris 30 Sales
```

The constructor can also accept arguments so that each object is initialized with different values.

```python
class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

emp1 = Employee("Sergei", 25, "Engineering")
emp2 = Employee("Boris", 30, "Sales")
```

---

---

## <font color='green'>5. Complete Example</font>

The following `Employee` class combines everything we've learned so far.

```
Employee
├── Attributes
│   ├── name
│   ├── age
│   └── department
│
└── Constructor
    └── __init__(name, age, department)
```

The class defines three attributes and initializes them using the `__init__()` constructor.

```python
class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


emp1 = Employee("Sergei", 25, "Engineering")
emp2 = Employee("Boris", 30, "Sales")

print(emp1.name, emp1.age, emp1.department)
print(emp2.name, emp2.age, emp2.department)
```

Output

```text
Sergei 25 Engineering
Boris 30 Sales
```

In this example:

- `Employee` defines a new data type.
- `emp1` and `emp2` are objects of the `Employee` class.
- The `__init__()` constructor initializes each object with its own data.
- The attributes are accessed using the dot (`.`) operator.


---

## <font color='green'>6. Understanding the `self` Parameter</font>

The first parameter of every instance method, including the constructor, is usually named `self`.

```python
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The `self` parameter refers to the object that is currently being created or accessed.

When we create an object,

```python
emp = Employee("Sergei", 25)
```

Python automatically passes the newly created object as the first argument to the constructor.

Although `self` appears in the method definition, we never pass it explicitly.

```python
emp = Employee("Sergei", 25)      # Correct
```

Not

```python
emp = Employee(emp, "Sergei", 25) # Incorrect
```

The `self` parameter is used to create and access attributes that belong to the current object.

```python
print(emp.name)
print(emp.age)
```

Output

```text
Sergei
25
```

---

## <font color='green'>Summary</font>

In this article, we learned how to define a class, create objects, define attributes within a class, create attributes dynamically, initialize objects using the `__init__()` constructor, and understand the purpose of the `self` parameter.

These concepts provide the foundation for working with classes and objects in Python.






---
## **Relevant Links**

[Python Material on this website](../index.md)

