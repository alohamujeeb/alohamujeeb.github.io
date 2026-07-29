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

Learn how to define classes, create objects (instances), and access their attributes in Python. This article assumes you're already familiar with the concepts of classes and objects.


---
## <font color='green'>1. Accessing Object Attributes</font>

An object stores data in the form of **attributes**.

In Python, attributes are accessed using the **dot (`.`) operator**.

Unlike languages such as Java and C++, attributes **do not have to be declared when the class is defined**. They can be created dynamically by assigning values to an object.

For example:

```python
class Employee:
    pass

emp = Employee()

emp.name = "Sergei"
emp.age = 25
emp.department = "Engineering"
```

Here:

- `emp.name` creates the `name` attribute and assigns it the value `"Alice"`.
- `emp.age` creates the `age` attribute and assigns it the value `25`.
- `emp.department` creates the `department` attribute and assigns it the value `"Engineering"`.

The same dot (`.`) operator is used to access attribute values.

```python
print(emp.name)
print(emp.age)
print(emp.department)
```

Output

```text
Alice
25
Engineering
```

### Attributes Are Created Dynamically

Since attributes are created when values are assigned, different objects of the same class can have different attributes.

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

In this example:

- `emp1` has the attributes `name` and `age`.
- `emp2` has the attributes `name` and `salary`.

Although both objects belong to the same class, they do not contain the same set of attributes.

<font color='red'>This behavior is different from languages such as Java and C++, where the data members of a class are typically declared when the class is defined.</font>

### Accessing a Non-Existent Attribute

Trying to access an attribute that hasn't been created raises an `AttributeError`.

```python
class Employee:
    pass

emp = Employee()

print(emp.age)
```

Output

```text
AttributeError: 'Employee' object has no attribute 'age'
```

Since the `age` attribute was never assigned a value, it doesn't exist.

> **Note:** Although Python allows attributes to be created dynamically, most Python programs define the expected attributes when an object is created using the `__init__()` constructor. You'll learn about constructors in the next article.


---
## <font color='green'>2. Defining Attributes Within a Class</font>

In the previous section, attributes were created by assigning values to an object.

```python
class Employee:
    pass

emp = Employee()

emp.name = "Sergei"
emp.age = 25
emp.department = "Engineering"
```

Python also allows attributes to be defined directly within the class.

```python
class Employee:
    name = ""
    age = 0
    department = ""

emp = Employee()

print(emp.name)
print(emp.age)
print(emp.department)
```

Output

```text

0

```

Here, the attributes `name`, `age`, and `department` are defined when the class is created.

As a result, every object created from the `Employee` class has access to these attributes.

```python
emp1 = Employee()
emp2 = Employee()

print(emp1.name)
print(emp2.name)
```

Output

```text


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

Although the attributes are defined within the class, each object appears to maintain its own values.


---
## <font color='green'>3. Initializing Object: Constructor</font>

In the previous section, the attributes `name`, `age`, and `department` were defined within the class.

```python
class Employee:
    name = ""
    age = 0
    department = ""
```

Although this works, it has a limitation.

Every object initially contains the same default values.

```python
emp1 = Employee()
emp2 = Employee()

print(emp1.name, emp1.age, emp1.department)
print(emp2.name, emp2.age, emp2.department)
```

Output

```text

0

```

**A better approach is to initialize an object's attributes when the object is created.**

Python provides a special method named `__init__()` for this purpose. This method is known as the **constructor**.

```python
class Employee:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.department = ""

emp1 = Employee()
emp2 = Employee()
```

Whenever an object is created, Python automatically calls the `__init__()` method.

As a result, every object starts with its own `name`, `age`, and `department` attributes.

You can assign values to these attributes in the usual way.

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

The `__init__()` method is executed automatically for every object created from the class.

Although the constructor in this example initializes the attributes with default values, it can also accept values as arguments. This allows each object to be initialized with different data at the time it is created.


---
## <font color='green'>4. Understanding the `self` Parameter</font>

The `__init__()` method always has at least one parameter named `self`.

```python
class Employee:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.department = ""
```

The `self` parameter refers to the object that is currently being created.

When you write:

```python
emp = Employee()
```

Python automatically passes the newly created object as the first argument to the `__init__()` method.

Although `self` appears in the method definition, you never pass it explicitly.

```python
emp = Employee()      # Correct
```

Not

```python
emp = Employee(emp)   # Incorrect
```

The `self` parameter is used to create and access attributes that belong to the current object.

For example:

```python
class Employee:

    def __init__(self):
        self.name = "Sergei"
        self.age = 25

emp1 = Employee()
emp2 = Employee()

print(emp1.name)
print(emp2.name)
```

Output

```text
Sergei
Sergei
```

Here, `self.name` and `self.age` create attributes for the object being initialized.


---
## <font color='green'>5. Passing Arguments to the Constructor</font>

In the previous section, every object was initialized with the same default values.

```python
class Employee:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.department = ""
```

Often, you want each object to be initialized with different values.

The `__init__()` constructor can accept additional parameters for this purpose.

```python
class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
```

When creating an object, pass the required values as arguments.

```python
emp1 = Employee("Sergei", 25, "Engineering")
emp2 = Employee("Boris", 30, "Sales")
```

The arguments are assigned to the constructor's parameters.

For `emp1`:

- `"Sergei"` → `name`
- `25` → `age`
- `"Engineering"` → `department`

The constructor then stores these values in the object's attributes.

```python
print(emp1.name)
print(emp1.age)
print(emp1.department)

print(emp2.name)
print(emp2.age)
print(emp2.department)
```

Output

```text
Sergei
25
Engineering
Boris
30
Sales
```

By accepting arguments, the constructor allows every object to be initialized with its own data at the time it is created.


---
## <font color='green'>Summary</font>

In this article, we learned the basics of creating classes and objects in Python. You learned how to define a class, create objects, access and modify attributes, define attributes within a class, and initialize object attributes using the `__init__()` constructor.

These concepts provide the foundation for object-oriented programming in Python.



---
## **Relevant Links**

[Python Material on this website](../index.md)

