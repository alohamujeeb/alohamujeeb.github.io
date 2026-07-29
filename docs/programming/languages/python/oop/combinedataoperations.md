---
hide:
  - navigation
  
tags:
  - OOP Philosophy
  - Encapsulation

---

# Why Combine Data and Operations?

When creating a new data type, we don't just group related data together—we also group the operations that work on that data.

This idea of combining related data and operations into a single unit is known as **encapsulation**.

Encapsulation provides several important advantages.

---

## <font color='green'>1. A Rectangle Is More Than Its Data</font>

Consider a rectangle as an example.

It has data such as:

- Length
- Width

However, we rarely store a rectangle just to remember its dimensions.

We also want to perform operations on it.

For example:

- Calculate its area
- Calculate its perimeter
- Find the union of two rectangles
- Find the intersection of two rectangles

Instead of writing these operations repeatedly throughout a program, it makes sense to define them once as part of the `Rectangle` data type.

```
Rectangle
├── Data
│   ├── Length
│   └── Width
│
└── Operations
    ├── area()
    ├── perimeter()
    ├── union()
    └── intersection()
```
**A sample code is following:**

```python

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def union(self, other):
        print("Union of two rectangles")

    def intersection(self, other):
        print("Intersection of two rectangles")


rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

rect1.union(rect2)
rect1.intersection(rect2)
```



By combining related data and the operations that work on that data into a single unit, the `Rectangle` becomes a complete data type. This principle is called **encapsulation**.

---

## <font color='green'>2. Write the Operations Once</font>

Operations such as `area()` and `perimeter()` are usually written by the designer of the data type.

Once these operations have been tested, every programmer on the team can use them with confidence.

Without predefined operations, different programmers might implement the same calculation in different ways, leading to duplicate code and inconsistent results.

---

## <font color='green'>3. Convenience</font>

Another advantage is convenience.

A data type can provide the operations that programmers are most likely to need.

For example, a `Rectangle` can provide methods such as `area()` and `perimeter()`, while an `Employee` can provide operations such as `calculate_bonus()` or `promote()`.

Instead of writing these operations every time they are needed, programmers simply use the ones provided by the data type.

---

## <font color='green'>4. Can New Operations Be Added?</font>

Yes.

A data type is not limited to the operations originally provided by its designer.

Although a data type provides a useful set of built-in operations, programmers can extend its functionality by adding new operations when needed.

For example, new functionality can be added using techniques such as **inheritance**, **composition**, and **polymorphism**. Some programming languages also support **extension methods**.

We'll learn about these techniques in later articles.

---

## <font color='green'>5. Preventing Honest Mistakes</font>

Grouping operations with data also helps teams write more reliable software.

The goal is not to protect the program from malicious users.

Instead, it is to reduce honest programming mistakes.

If every programmer writes their own version of an operation such as `area()` or `calculate_bonus()`, small differences or bugs can easily appear.

By providing well-tested operations as part of the data type, every programmer uses the same implementation, making the code more consistent, easier to maintain, and less error-prone.

---

## <font color='green'>6. Summary</font>

Encapsulation is the practice of combining related data and the operations that work on that data into a single unit.

This approach avoids duplicate implementations, provides convenient and well-tested operations, promotes consistency across a team, and reduces the chance of honest programming mistakes. Additional operations can still be added when needed using techniques such as inheritance, composition, and polymorphism.


---
## **Relevant Links**

[Python Material on this website](../index.md)

