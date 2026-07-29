---
hide:
  - navigation
  
tags:
  - Function Pointers
  - Callback Functions
  - Dispatch Table
  
---

# C Structures: Building Class-Like Objects

*This article is intended for intermediate and advanced C programmers. It explores how C structures can encapsulate both data and the functions that operate on that data, enabling modular, object-oriented design principles without using C++ classes. It also highlights the similarities and differences between C structures and C++ classes, demonstrating how structures form the foundation of many large-scale C software systems.*

---

## <font color='green'>1. Why Think Beyond Data?</font>

When most programmers first learn the C language, they are introduced to structures as a convenient way to group related variables.

For example, instead of storing a rectangle's dimensions in separate variables,

```c
int width;
int height;
```

they are grouped into a single structure.

```c
typedef struct
{
    int width;
    int height;
} Rectangle;
```

This is certainly one of the primary purposes of a structure, and for many C programmers, that is where the story ends.

However, in professional software development, structures play a much larger role.

Rather than viewing a structure as simply a collection of related data, experienced C programmers often treat it as the **center of a software component**. The structure represents an entity, while a carefully designed set of functions defines everything that can be done with that entity.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Operations
    ├── Area()
    ├── Perimeter()
    ├── Union()
    ├── Intersection()
    └── Scale()
```

Instead of scattering unrelated functions throughout the program, all operations concerning a `Rectangle` are naturally grouped together.

This design offers several advantages:

- Improves code organization.
- Clearly separates responsibilities.
- Makes APIs easier to understand.
- Encourages modular software design.
- Simplifies maintenance as projects grow.

This concept is known as **encapsulation**—bringing together the data that represents an object and the operations that manipulate it.

Although C does not provide classes as a language feature, nothing prevents us from organizing our software in a similar way. By combining structures with well-designed functions, we can create reusable, object-like components that are easy to understand and maintain.

In fact, this design philosophy is widely used in many large C codebases, including operating systems, embedded firmware, networking libraries, graphics frameworks, and device drivers.

Throughout this article, we will see that a C structure is much more than a passive container for variables—it can serve as the foundation of a clean, modular, and class-like software design.


---
## <font color='green'>2. Structures as a Collection of Related Data</font>

Before exploring how structures can be used to build class-like objects, it is important to understand their original purpose.

A structure is a **user-defined data type** that groups multiple related variables into a single logical unit.

Without a structure, the properties of a rectangle might be stored as separate variables.

```c
int width  = 10;
int height = 5;
```

This approach is manageable for a single rectangle, but quickly becomes difficult when multiple rectangles are involved.

```c
int rect1_width,  rect1_height;
int rect2_width,  rect2_height;
int rect3_width,  rect3_height;
```

There is no relationship between these variables other than their names. The programmer must remember which width belongs to which height.

A structure solves this problem by grouping related data together.

```c
typedef struct
{
    int width;
    int height;
} Rectangle;
```

Now each rectangle is represented by a single object.

```c
Rectangle rect1;
Rectangle rect2;
Rectangle rect3;
```

Visually, the structure can be thought of as a blueprint.

```text
Rectangle
├── width
└── height
```

Each variable declared from this blueprint contains its own copy of the data.

```text
rect1
├── width  = 10
└── height = 5

rect2
├── width  = 25
└── height = 12

rect3
├── width  = 40
└── height = 18
```

Grouping related data offers several advantages:

- Improves readability.
- Reduces programming errors.
- Simplifies passing related data to functions.
- Makes programs easier to maintain.
- Allows the data to represent a real-world entity.

For example, instead of writing:

```c
draw_rectangle(width, height);
```

we can simply write:

```c
draw_rectangle(&rect1);
```

The function receives a single object rather than multiple independent variables.

At this point, the structure is still **nothing more than a collection of data**. It defines **what a rectangle is**, but not **what can be done with it**.

The next section takes the next logical step by associating functions such as calculating the area, perimeter, union, and intersection with the `Rectangle` structure, transforming it from a passive data container into a class-like software component.

---
## <font color='green'>3. Adding Behavior to Structures</font>

So far, our `Rectangle` structure only describes **what a rectangle is**.

```text
Rectangle
├── width
└── height
```

While this is useful, it tells us nothing about **what we can do with a rectangle**.

For example, given a rectangle, we may want to:

- Calculate its area.
- Calculate its perimeter.
- Determine whether a point lies inside it.
- Find the union of two rectangles.
- Find the intersection of two rectangles.
- Scale its dimensions.
- Move it to a new position.

These are all operations that naturally belong to the `Rectangle` entity.

Instead of creating unrelated functions throughout the program, a better approach is to associate these operations with the structure they manipulate.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Operations
    ├── Area()
    ├── Perimeter()
    ├── Contains()
    ├── Union()
    ├── Intersection()
    ├── Move()
    └── Scale()
```

Notice that although the functions are **not physically stored inside the structure**, they are conceptually part of its interface.

This is exactly how programmers begin thinking in terms of **objects** rather than merely **data**.

---

### 3.1 Associating Functions with a Structure

Consider the following declarations.

```c
typedef struct
{
    int width;
    int height;
} Rectangle;

int Rectangle_Area(const Rectangle *rect);
int Rectangle_Perimeter(const Rectangle *rect);
Rectangle Rectangle_Union(const Rectangle *r1,
                          const Rectangle *r2);
Rectangle Rectangle_Intersection(const Rectangle *r1,
                                 const Rectangle *r2);
```

Every function accepts one or more `Rectangle` objects and performs an operation that is meaningful for that type.

For example,

```c
Rectangle rect = {20, 10};

int area = Rectangle_Area(&rect);
int perimeter = Rectangle_Perimeter(&rect);
```

Even though these are ordinary C functions, they clearly belong to the `Rectangle` abstraction.

---

### 3.2 Treating the Structure as an Object

As the number of related operations grows, programmers naturally stop thinking of `Rectangle` as merely a collection of variables.

Instead, they begin thinking of it as an object that exposes a well-defined set of operations.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Interface
    ├── Rectangle_Area()
    ├── Rectangle_Perimeter()
    ├── Rectangle_Union()
    ├── Rectangle_Intersection()
    ├── Rectangle_Move()
    └── Rectangle_Scale()
```

This organization provides several benefits.

- Related code stays together.
- The API becomes easier to understand.
- New operations can be added without affecting unrelated modules.
- Other programmers immediately know where to find functionality related to a rectangle.

As projects grow from hundreds to thousands of source files, this organization becomes increasingly valuable.

---

### 3.3 Similar to Methods in a Class

If you have experience with C++, the design should look familiar.

In C++, you might write:

```cpp
Rectangle rect;

int area = rect.Area();
```

In C, the equivalent operation is typically written as:

```c
Rectangle rect;

int area = Rectangle_Area(&rect);
```

Although the syntax is different, the intent is the same.

Both statements ask the `Rectangle` abstraction to compute its area.

The difference is that C expresses this relationship through ordinary functions that accept a pointer to the structure, whereas C++ expresses it through member functions that are built into the language.

This simple design pattern forms the foundation of many object-like software architectures written entirely in C.


---
## <font color='green'>4. Encapsulation in C</font>

One of the fundamental principles of object-oriented programming is **encapsulation**.

Encapsulation means bringing together:

- The data that represents an object.
- The operations that manipulate that data.

In C++, the language enforces this relationship through classes.

In C, we achieve the same objective through **program organization** rather than language features.

---

### 4.1 Organizing Related Code

A common practice is to place the structure definition and all related function declarations into a single header file.

For example:

```text
rectangle.h
├── Rectangle structure
├── Rectangle_Create()
├── Rectangle_Area()
├── Rectangle_Perimeter()
├── Rectangle_Union()
├── Rectangle_Intersection()
└── Rectangle_Scale()
```

The corresponding implementation resides in a single source file.

```text
rectangle.c
├── Rectangle_Create()
├── Rectangle_Area()
├── Rectangle_Perimeter()
├── Rectangle_Union()
├── Rectangle_Intersection()
└── Rectangle_Scale()
```

Everything related to a rectangle is located in one module.

This makes the code easier to navigate and understand.

---

### 4.2 A Well-Defined Interface

Applications do not need to know how the rectangle operations are implemented.

They simply use the interface provided by the module.

```c
Rectangle rect = {20, 10};

int area = Rectangle_Area(&rect);

Rectangle_Scale(&rect, 2);

Rectangle_Move(&rect, 15, 8);
```

Notice that the application interacts only with the published functions.

It does not need to know how the area is calculated or how scaling is performed internally.

This separation between **interface** and **implementation** is a key aspect of encapsulation.

---

### 4.3 Thinking in Terms of Modules

As software grows, each structure naturally evolves into its own software module.

```text
Project
├── rectangle.c
├── rectangle.h
├── circle.c
├── circle.h
├── line.c
├── line.h
├── polygon.c
└── polygon.h
```

Each module is responsible for a single entity.

For example:

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Operations
    ├── Create()
    ├── Area()
    ├── Perimeter()
    ├── Union()
    ├── Intersection()
    ├── Move()
    └── Scale()
```

This organization keeps related code together while minimizing dependencies between modules.

---

### 4.4 Encapsulation Without Classes

Unlike C++, C does not force data and functions to be bundled together.

Nothing prevents a programmer from writing unrelated functions that directly manipulate a structure.

However, disciplined C programmers follow a simple convention:

- Define a structure to represent an entity.
- Place all related functions in the same module.
- Expose only the operations that make sense for that entity.

Over time, other programmers naturally begin to think of the module as a single reusable component rather than as a collection of independent functions.

Although C structures are **not classes**, this disciplined approach achieves one of the primary goals of object-oriented programming: organizing related data and behavior into a coherent, reusable abstraction.


---
## <font color='green'>5. Public by Default</font>

One important difference between a C structure and a C++ class is **member accessibility**.

In C, every structure member is **public by default**.

```c
typedef struct
{
    int width;
    int height;
} Rectangle;
```

Any part of the program that has access to a `Rectangle` object can directly read or modify its members.

```c
Rectangle rect;

rect.width  = 100;
rect.height = 50;
```

Nothing prevents another function from writing:

```c
rect.width = -25;
```

even if a negative width is considered invalid.

Unlike C++, the language provides no mechanism to prevent such direct access.

---

### 5.1 C++ Provides Access Control

A C++ class can restrict access to its internal data.

```cpp
class Rectangle
{
private:
    int width;
    int height;

public:
    void SetWidth(int w);
    int Area() const;
};
```

Only the public interface is visible to users of the class.

```text
Rectangle
├── Private
│   ├── width
│   └── height
│
└── Public
    ├── SetWidth()
    ├── SetHeight()
    ├── Area()
    └── Perimeter()
```

This prevents external code from modifying the object's internal state arbitrarily.

---

### 5.2 Structures Do Not Enforce Encapsulation

Although we organize our code around structures and related functions, the compiler does not stop other code from accessing the structure members directly.

```c
Rectangle rect;

rect.width = -100;      /* Allowed */
rect.height = 5000;     /* Also allowed */
```

Whether these values are valid depends entirely on the programmer.

The compiler performs no access checks.

---

### 5.3 Achieving Data Hiding in C

Although C has no `private` keyword, data hiding is still possible.

A common technique is to expose only an **opaque pointer** in the public header while keeping the actual structure definition private.

```text
rectangle.h
├── typedef struct Rectangle Rectangle;
├── Rectangle_Create()
├── Rectangle_Destroy()
├── Rectangle_Area()
└── Rectangle_Scale()
```

The actual structure definition remains inside `rectangle.c`.

```text
rectangle.c
└── struct Rectangle
    ├── width
    ├── height
    └── ...
```

Since the application cannot see the structure members, it must interact with the object through the published API.

This effectively provides data hiding, even though the C language has no built-in access specifiers.

> **Note:** Opaque pointers are a widely used technique for implementing encapsulation in C. If you're unfamiliar with this approach, refer to the earlier article on **Opaque Pointers**, where the technique is discussed in detail.

---

### 5.4 Encapsulation Is a Design Discipline

One of the strengths of C is that it gives programmers complete freedom.

That freedom also comes with responsibility.

Unlike C++, the compiler does not enforce encapsulation. Instead, encapsulation is achieved through careful API design, disciplined programming practices, and well-defined module boundaries.

This flexibility is one of the reasons why experienced C programmers can build software that exhibits many object-oriented characteristics without requiring language-supported classes.

The next section demonstrates how function pointers can take this idea even further, allowing structures to simulate methods and enabling more dynamic object-oriented designs.

---
## <font color='green'>6. Taking It Further with Function Pointers</font>

So far, we have associated ordinary C functions with a structure.

```c
Rectangle_Area(&rect);
Rectangle_Perimeter(&rect);
Rectangle_Scale(&rect, 2);
```

This is the most common and recommended approach for building object-like software in C.

However, C offers another powerful feature that allows structures to become even more class-like: **function pointers**.

By storing function pointers inside a structure, each object can carry not only its data but also the operations that act upon it.

---

### 6.1 Functions as Structure Members

Unlike ordinary variables, a function pointer stores the address of a function.

This allows a structure to reference the functions associated with it.

```c
typedef struct Rectangle
{
    int width;
    int height;

    int (*Area)(const struct Rectangle *rect);
    int (*Perimeter)(const struct Rectangle *rect);

} Rectangle;
```

Now, in addition to its data members, the structure also contains references to its operations.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Function Pointers
    ├── Area()
    └── Perimeter()
```

---

### 6.2 Initializing the Function Pointers

The function pointers are assigned during object initialization.

```c
int Rectangle_Area(const Rectangle *rect);
int Rectangle_Perimeter(const Rectangle *rect);

Rectangle rect =
{
    .width = 20,
    .height = 10,

    .Area = Rectangle_Area,
    .Perimeter = Rectangle_Perimeter
};
```

Once initialized, the functions can be invoked through the object itself.

```c
int area = rect.Area(&rect);

int perimeter = rect.Perimeter(&rect);
```

Notice how the syntax begins to resemble a member function call in C++.

```cpp
rect.Area();
```

Although the C version still requires the object pointer to be passed explicitly, the overall programming style becomes very similar.

---

### 6.3 Why Use Function Pointers?

At first glance, this may appear unnecessary.

After all, writing

```c
Rectangle_Area(&rect);
```

is simpler than

```c
rect.Area(&rect);
```

The real advantage is not shorter syntax—it is **flexibility**.

Different objects of the same type can execute different implementations.

For example,

```text
Rectangle A
├── Area() ─────► Rectangle_Area()

Rectangle B
├── Area() ─────► Optimized_Rectangle_Area()
```

The calling code remains identical.

```c
rect.Area(&rect);
```

Only the implementation changes.

This technique forms the basis of many plug-in architectures, device drivers, callback systems, and object-oriented frameworks written in C.

---

### 6.4 A Word of Caution

Although function pointers make structures look more like classes, they are **not always the best solution**.

For many software components, ordinary functions are:

- Simpler
- Easier to understand
- More efficient
- Easier to maintain

Function pointers should be introduced only when multiple implementations or runtime behavior selection is actually required.

Otherwise, they simply add unnecessary complexity.

For this reason, many C libraries expose an object-like API using ordinary functions, reserving function pointers for cases where dynamic behavior is essential.


---
## <font color='green'>7. How C Structures Differ from C++ Classes</font>

By now, it should be clear that C structures can be used to build software components that closely resemble classes.

Both organize related data and operations into a single abstraction, making programs easier to understand and maintain.

However, despite these similarities, **a C structure is not a C++ class**.

Several important language features found in C++ are not available in C.

---

### 7.1 Similarities

Both C structures and C++ classes allow programmers to model real-world entities.

For example, both can represent a rectangle.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Operations
    ├── Area()
    ├── Perimeter()
    ├── Move()
    └── Scale()
```

In both languages, software can be organized around objects instead of unrelated variables and functions.

This encourages:

- Better code organization
- Modular design
- Reusable components
- Easier maintenance

From a design perspective, the overall architecture can look remarkably similar.

---

### 7.2 Constructors and Destructors

One major difference is object lifetime management.

A C++ class can automatically initialize and clean up an object.

```cpp
Rectangle rect(20, 10);
```

The constructor is called automatically when the object is created.

Likewise, the destructor is automatically invoked when the object goes out of scope.

C provides no equivalent language feature.

Initialization and cleanup must be performed explicitly.

```c
Rectangle rect;

Rectangle_Init(&rect, 20, 10);

/* Use the object */

Rectangle_Destroy(&rect);
```

Whether these functions are called correctly depends entirely on the programmer.

---

### 7.3 Access Control

As discussed in the previous section, C++ supports:

- `private`
- `protected`
- `public`

These keywords allow the compiler to enforce encapsulation.

C structures have no such capability.

Every member is publicly accessible unless the programmer deliberately hides the structure using techniques such as opaque pointers.

---

### 7.4 Inheritance

One of the defining features of C++ is **inheritance**.

A new class can extend an existing class by inheriting its data and behavior.

```text
Shape
├── Draw()
└── Move()
     │
     ├──────────────┐
     ▼              ▼
Rectangle        Circle
```

C has no built-in mechanism for inheritance.

If code reuse is required, it must be achieved through composition or other design techniques.

---

### 7.5 Polymorphism

C++ also supports **runtime polymorphism** through virtual functions.

A program can invoke the same function on different objects, with each object providing its own implementation.

```text
Shape
│
├── Rectangle
│     └── Draw()
│
└── Circle
      └── Draw()
```

The calling code remains identical.

```cpp
shape->Draw();
```

In C, similar behavior can be implemented manually using function pointers, but the language provides no built-in support for polymorphism.

---

### 7.6 Comparison

| Feature | C Structure | C++ Class |
|----------|:-----------:|:---------:|
| Group related data | ✓ | ✓ |
| Associate functions with data | ✓ | ✓ |
| Encapsulation | ✓ (by design) | ✓ (language support) |
| Access control | ✗ | ✓ |
| Constructors / Destructors | ✗ | ✓ |
| Inheritance | ✗ | ✓ |
| Runtime Polymorphism | ✗ (manual implementation) | ✓ |

Although C lacks several object-oriented language features, it is still capable of producing highly modular and maintainable software.

By combining structures, carefully designed APIs, opaque pointers, and, where appropriate, function pointers, C programmers can build software architectures that exhibit many of the same design principles found in object-oriented languages.

---
## <font color='green'>8. Where This Design Is Used</font>

If you've followed this design pattern throughout the article, you might wonder whether it is merely an academic exercise.

The answer is **no**.

Organizing software around structures and their associated functions is a well-established practice in C programming. Many of the world's largest and most successful C codebases rely on this approach because it produces software that is modular, maintainable, and easy to extend.

Let's look at a few examples.

---

### 8.1 Linux Kernel

The Linux kernel makes extensive use of structures to represent kernel objects.

Examples include:

- Processes
- Devices
- File systems
- Network sockets
- Memory regions

Each structure has a well-defined set of functions that operate on it.

```text
struct file
├── Data Members
│   ├── f_pos
│   ├── f_flags
│   └── ...
│
└── Operations
    ├── open()
    ├── read()
    ├── write()
    ├── close()
    └── ioctl()
```

Rather than exposing unrelated global functions, the kernel groups operations around the object they manipulate.

---

### 8.2 Embedded Software

Embedded software often follows exactly the same design philosophy.

A peripheral driver typically consists of a structure representing the device together with a set of functions that operate on it.

```text
UART
├── Data
│   ├── Baud Rate
│   ├── Buffer
│   └── Status
│
└── Operations
    ├── Init()
    ├── Send()
    ├── Receive()
    ├── Flush()
    └── DeInit()
```

To the application developer, the driver behaves much like an object.

---

### 8.3 Graphics and GUI Libraries

Graphics libraries frequently model graphical objects using structures.

Examples include:

- Windows
- Buttons
- Images
- Fonts
- Rectangles
- Circles

Each object exposes operations that naturally belong to it.

```text
Image
├── width
├── height
├── pixels
├── Load()
├── Save()
├── Resize()
└── Draw()
```

This organization makes the API intuitive because related functionality is grouped together.

---

### 8.4 Networking Libraries

Networking stacks also organize their software around structures.

A socket, for example, is more than just a collection of variables.

```text
Socket
├── Address
├── Port
├── State
├── Connect()
├── Send()
├── Receive()
└── Close()
```

Once again, the structure represents the object, while the associated functions define its behavior.

---

### 8.5 Why This Design Scales

As software projects grow, organizing code around structures provides several advantages.

Instead of thinking about hundreds of independent functions, developers think in terms of reusable software components.

```text
Project
├── Rectangle
│   ├── Data
│   └── Operations
│
├── Circle
│   ├── Data
│   └── Operations
│
├── Image
│   ├── Data
│   └── Operations
│
└── Socket
    ├── Data
    └── Operations
```

Each component has:

- A clearly defined purpose.
- A well-defined interface.
- A dedicated implementation.
- Minimal dependency on unrelated modules.

This modular organization is one of the primary reasons why large C codebases remain maintainable even after decades of development.

Although C structures are not classes, they allow programmers to organize software in a remarkably similar way. Combined with disciplined API design, they provide a practical and effective foundation for building reusable, object-like software components.

---
## <font color='green'>9. Summary</font>

When C structures are first introduced, they are often presented simply as a way to group related variables.

While this is certainly their primary purpose, it is only the beginning.

Throughout this article, we have seen that a structure can become the foundation of a much larger software component by associating it with the functions that operate on its data.

```text
Rectangle
├── Data
│   ├── width
│   └── height
│
└── Operations
    ├── Area()
    ├── Perimeter()
    ├── Union()
    ├── Intersection()
    ├── Move()
    └── Scale()
```

This organization allows programmers to think in terms of **objects** rather than isolated variables and functions.

We also explored how this approach naturally leads to:

- Better code organization
- Modular software design
- Well-defined interfaces
- Easier maintenance
- Reusable software components

Although C does not provide language features such as classes, constructors, inheritance, or built-in polymorphism, it still allows developers to apply many object-oriented design principles through disciplined programming and careful API design.

For applications requiring even greater flexibility, function pointers can be used to simulate methods and enable runtime behavior selection, further strengthening the object-oriented style.

Perhaps the most important takeaway is this:

> **A C structure is not merely a collection of related data—it is the foundation upon which an entire software abstraction can be built.**

This philosophy has been successfully applied for decades in operating systems, embedded firmware, graphics libraries, networking stacks, and countless other large C projects.

Mastering this way of thinking transforms structures from simple data containers into powerful building blocks for writing clean, modular, and maintainable software in C.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory management, pointers, embedded C programming etc.)
