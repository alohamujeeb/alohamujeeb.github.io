---
hide:
  - navigation
  
tags:
  - Function Pointers
  - Callback Functions
  - Dispatch Table
  
---

# Function Pointers (FP) in C: The Foundation of Callback Functions

*This article is intended for intermediate and advanced C programmers. It explains what function pointers are, how they enable indirect function calls, and why they are fundamental to implementing callback functions, dispatch tables, event-driven programming, state machines, and many other flexible software design techniques in C.*

---
## <font color='green'>1. Choosing a Function at Run Time</font>

In C, a function is normally called by writing its name followed by parentheses.

For example,

```c
add(10, 20);
```

Here, the function to be executed is decided **when the program is written**. Every function call explicitly specifies the function that should be invoked.

However, there are many situations where the function to execute is **not known in advance**.

For example:

- A menu-driven application may need to execute a different function depending on the user's selection.
- A sorting algorithm may require different comparison functions for different types of data.
- An embedded system may execute different interrupt handlers depending on the event that occurs.
- A communication library may notify an application when a message arrives, but it cannot know beforehand which function the application wants to execute.

> In all of these situations, the program must be able to **choose a function at run time** rather than at compile time.

### 1.1 Using Conditional Statements

One way to solve this problem is to use a sequence of `if...else` or `switch` statements.

```c
if(choice == 1)
    add();
else if(choice == 2)
    subtract();
else if(choice == 3)
    multiply();
...
```

Although this approach works, it becomes increasingly difficult to maintain as more functions are added. Every new operation requires modifying the conditional statements, making the code less flexible and harder to extend.

### 1.2 Using Function Pointers

A more flexible solution is to store the **address of a function** in a variable and invoke the function through that address. Such variables are called **function pointers**.

Instead of repeatedly testing conditions, the program can simply select the appropriate function, store its address in a function pointer, and invoke it whenever needed.

Function pointers make it possible to select and invoke functions dynamically, resulting in programs that are more modular, reusable, and easier to extend.

In the next section, we will see that every function has a memory address and learn how that address can be stored in a function pointer.


---
## <font color='green'>2. Functions Have Memory Addresses</font>

Like variables, every function in a C program occupies memory. When a program is loaded into memory, the machine instructions that implement each function are stored at a specific memory location.

Consequently, every function has a unique memory address.

Consider the following program.

```c
#include <stdio.h>

void display(void)
{
    printf("Hello, World!\n");
}

int main(void)
{
    printf("%p\n", (void *)display);

    return 0;
}
```

A typical output might be:

```text
0x401136
```

The exact address will vary from one program execution to another and from one system to another.

Notice that we did **not** write:

```c
display()
```

Instead, we simply wrote:

```c
display
```

This is because:

- `display()` **calls** the function.
- `display` **refers to the function itself**, which evaluates to its address in most expressions.

In other words, the function name can be used to identify the location of the function in memory without actually executing it.

Since a function has an address, that address can be stored in a variable.

A variable capable of storing the address of a function is called a **function pointer**. In the next section, we will learn how to declare function pointers and use them to invoke functions indirectly.

---
## <font color='green'>3. Steps in Creating and Using FP</font>


### <font color='green'>Step 1: Declaring FP</font>

Since every function has a memory address, we need a variable capable of storing that address. Such a variable is called a **function pointer**.

Unlike ordinary pointers, a function pointer stores the address of a **function** rather than the address of a data object.

Consider the following function.

```c
int add(int a, int b)
{
    return a + b;
}
```

A function pointer capable of storing the address of this function is declared as follows.

```c
int (*funcPtr)(int, int);
```

Although this declaration may look unusual at first, it follows the same general syntax used for other declarations in C.

It can be understood by reading it from the variable name outward.

```text
           (*funcPtr)
                │
                ▼
        funcPtr is a pointer
                │
                ▼
           to a function
                │
                ▼
     taking two int arguments
                │
                ▼
      and returning an int
```

Notice the parentheses around `*funcPtr`.

```c
int (*funcPtr)(int, int);
```

These parentheses are essential. Without them,

```c
int *funcPtr(int, int);
```

the declaration has an entirely different meaning.

It declares **a function named `funcPtr` that takes two `int` arguments and returns a pointer to an `int`**, not a pointer to a function.

Therefore, whenever declaring a function pointer, the parentheses around `*` and the pointer name must be included.

Now that we know how to declare a function pointer, the next step is to store the address of a function in it and invoke the function through the pointer.

---
### <font color='green'>Step 2: Assigning Functions to FP</font>

Once a function pointer has been declared, it can be assigned the address of a compatible function.

Consider the following function.

```c
int add(int a, int b)
{
    return a + b;
}
```

A function pointer capable of storing its address can be declared as follows.

```c
int (*funcPtr)(int, int);
```

The address of the function can then be assigned to the function pointer.

```c
funcPtr = add;
```

or equivalently,

```c
funcPtr = &add;
```

Both statements are valid and produce the same result.

This is because, in most expressions, the function name automatically evaluates to the address of the function. Therefore, explicitly using the address-of operator (`&`) is optional.

The following diagram illustrates the relationship.

```text
              +------------------+
add --------> |   Function Code  |
              +------------------+
                      ▲
                      │
                  funcPtr
```

A function pointer can only store the address of a function whose signature is compatible with its declaration.

For example,

```c
int (*funcPtr)(int, int);
```

can store the address of functions such as

```c
int add(int, int);
int subtract(int, int);
int multiply(int, int);
```

However, it cannot store the address of a function with a different return type or parameter list.

```c
void display(void);      // Incompatible
float average(int, int); // Incompatible
```

Now that the function pointer stores the address of a function, the next step is to invoke that function through the pointer.

---
### <font color='green'>Step 3: Calling Functions Through FP</font>

After assigning the address of a function to a function pointer, the function can be invoked through the pointer.

Consider the following program.

```c
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int (*funcPtr)(int, int);

    funcPtr = add;

    printf("%d\n", funcPtr(10, 20));

    return 0;
}
```

Output:

```text
30
```

Notice that the function is called using the function pointer rather than the function name.

```c
funcPtr(10, 20);
```

This statement invokes the function whose address is currently stored in `funcPtr`.

An equivalent way to call the function is

```c
(*funcPtr)(10, 20);
```

Both statements produce exactly the same result.

```c
funcPtr(10, 20);
```

is simply a more convenient notation for

```c
(*funcPtr)(10, 20);
```

Most C programmers prefer the shorter form because it is easier to read.

The following diagram illustrates the sequence of events.

```text
             +------------------+
funcPtr ---->| Address of add() |
             +------------------+
                       |
                       v
             +------------------+
             |   add(10, 20)    |
             +------------------+
                       |
                       v
                    returns 30
```

One important point to remember is that the function pointer does not contain the function itself. It merely stores the address of the function. When the function pointer is invoked, the program jumps to the function located at that address and executes it.


## <font color='green'>4. Callback Functions</font>

One of the most important applications of function pointers is the implementation of **callback functions**.

> A callback is a function whose address is passed to another function so that it can be invoked later when required.
> This allows a library or framework to perform a generic task while letting the application customize part of its behavior.


Consider the following example.

```c
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int subtract(int a, int b)
{
    return a - b;
}

void calculate(int x, int y, int (*operation)(int, int))
{
    int result = operation(x, y);

    printf("Result = %d\n", result);
}

int main(void)
{
    calculate(10, 5, add);
    calculate(10, 5, subtract);

    return 0;
}
```

Output:

```text
Result = 15
Result = 5
```

In this example,

```c
void calculate(int x,
               int y,
               int (*operation)(int, int))
```

accepts a function pointer as its third argument.

When `calculate()` is called,

```c
calculate(10, 5, add);
```

the address of the `add()` function is passed to `calculate()`.

Inside `calculate()`, the function pointer is used to invoke the callback.

```c
result = operation(x, y);
```

When the second call is made,

```c
calculate(10, 5, subtract);
```

the same `calculate()` function executes a completely different operation without requiring any modifications.

The following diagram illustrates the process.

```text
                  +----------------+
                  |   calculate()  |
                  +----------------+
                           |
                           |
                 operation(x, y)
                           |
              +------------+------------+
              |                         |
              |                         |
            add()                  subtract()
```

This demonstrates the primary advantage of callback functions: **the behavior of a function can be changed simply by passing a different function pointer**.

Instead of hardcoding the operation to perform, the function delegates that decision to the caller, making the program more flexible and reusable.

Many standard library functions, such as `qsort()`, rely on callback functions to allow user-defined behavior without modifying the library itself.


> Callback functions are widely used in software because they allow one piece of code to execute functionality defined elsewhere. Typical applications include:

- **Sorting algorithms**, where the comparison logic is supplied by the caller (for example, `qsort()`).
- **Graphical user interfaces (GUIs)**, where functions are invoked in response to button clicks, mouse movements, or keyboard events.
- **Embedded systems**, where interrupt service routines (ISRs) or device drivers invoke user-defined callback functions when hardware events occur.
- **Communication libraries**, which notify applications when data is received, a connection is established, or an error occurs.
- **Operating systems**, where timers and asynchronous events trigger callback functions at a later time.

In each of these cases, the library or operating system does not know in advance which function should be executed. Instead, it simply invokes the callback function whose address was previously provided by the application.

---
## <font color='green'>5. Dispatch Tables</font>

A callback allows a function to choose one of several operations by receiving a function pointer as an argument. Another common technique is to store multiple function pointers together in a table, allowing the program to select the required function by using an index.

Such a collection of function pointers is commonly known as a **dispatch table**.

Instead of writing a long sequence of `if...else` or `switch` statements, the program simply looks up the appropriate function in the table and invokes it.

> A dispatch table is conceptually similar to a **Lookup Table (LUT)**. In a LUT, an index is used to retrieve a precomputed **data value**. In a dispatch table, an index is used to retrieve the **address of a function**. Instead of looking up data, the program looks up which function should be executed and then invokes it.

This approach makes the code easier to extend because adding a new operation often requires only inserting another function into the table rather than modifying the program's control logic.

The following example demonstrates a simple dispatch table.

```c
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int subtract(int a, int b)
{
    return a - b;
}

int multiply(int a, int b)
{
    return a * b;
}

int divide(int a, int b)
{
    return a / b;
}

int main(void)
{
    int (*dispatchTable[])(int, int) =
    {
        add,
        subtract,
        multiply,
        divide
    };

    int choice = 2;

    int result = dispatchTable[choice](20, 5);

    printf("Result = %d\n", result);

    return 0;
}
```

Output:

```text
Result = 100
```

The dispatch table is simply an array whose elements are function pointers.

```c
int (*dispatchTable[])(int, int)
```

Each element stores the address of a function having the same signature.

```text
Index      Function
-----      --------
0   -----> add()
1   -----> subtract()
2   -----> multiply()
3   -----> divide()
```

When the expression

```c
dispatchTable[choice](20, 5);
```

is executed, the program first retrieves the function pointer stored at index `choice` and then invokes the corresponding function.

Since `choice` is `2`, the function `multiply()` is selected and executed.

```text
choice = 2
     |
     v
+-----+------------+
|  0  | add()      |
+-----+------------+
|  1  | subtract() |
+-----+------------+
|  2  | multiply() |  <----
+-----+------------+
|  3  | divide()   |
+-----+------------+
       |
       v
multiply(20, 5)
       |
       v
     Result = 100
```

---
## <font color='green'>6. State Machines Using FP`</font>

Many embedded systems and real-time applications are organized as **state machines**. Examples include traffic light controllers, vending machines, washing machines, elevators, communication protocols, and user interface menus.

In a state machine, the behavior of the program depends on its **current state**. Instead of repeatedly testing the current state using long `if...else` or `switch` statements, each state can be represented by a function. A function pointer is then used to invoke the function corresponding to the current state.

This approach makes the program modular, easier to understand, and easier to extend as additional states are introduced.

```c
typedef enum
{
    STATE_IDLE,
    STATE_RUNNING,
    STATE_ERROR
} State;

void idle(void)
{
    printf("Idle\n");
}

void running(void)
{
    printf("Running\n");
}

void error(void)
{
    printf("Error\n");
}

int main(void)
{
    void (*stateTable[])(void) =
    {
        idle,
        running,
        error
    };

    State currentState = STATE_RUNNING;

    stateTable[currentState]();

    return 0;
}
```

```text0
           Current State
                 |
                 v
          STATE_RUNNING
                 |
                 v
        +----------------+
        |   stateTable   |
        +----------------+
        | idle()         |
        | running() <----+
        | error()        |
        +----------------+
                 |
                 v
          running()
```

> By representing each state as a separate function, the program avoids complex conditional logic. Changing the current state simply changes which function is executed, resulting in code that is easier to maintain and extend.


---
## <font color='green'>7. Simplifying FP Declarations Using `typedef`</font>

Although function pointers are extremely useful, their declarations can become difficult to read, especially when multiple function pointers share the same signature.

For example, consider the following declaration.

```c
int (*funcPtr)(int, int);
```

While correct, this syntax is not immediately obvious to many programmers.

The `typedef` keyword allows a function pointer type to be given a meaningful name.

```c
typedef int (*Operation)(int, int);
```

The new type can then be used just like any other data type.

```c
Operation funcPtr;
```

The function pointer can be assigned and used in exactly the same way.

```c
funcPtr = add;

printf("%d\n", funcPtr(10, 20));
```

Using `typedef` becomes even more beneficial when declaring arrays of function pointers.

Without `typedef`

```c
int (*dispatchTable[])(int, int) =
{
    add,
    subtract,
    multiply,
    divide
};
```

With `typedef`

```c
typedef int (*Operation)(int, int);

Operation dispatchTable[] =
{
    add,
    subtract,
    multiply,
    divide
};
```

The second version is considerably easier to read because the complex function pointer declaration appears only once in the `typedef`. After that, `Operation` can be used wherever a function pointer of that type is required.

For this reason, many C libraries and large software projects use `typedef` extensively when working with function pointers.


---
## <font color='green'>8. Common Mistakes and Best Practices</font>

Although function pointers are powerful, they are also a common source of programming errors. The following are some of the most frequent mistakes made when working with function pointers.

### 8.1 Missing Parentheses in the Declaration

One of the most common mistakes is forgetting the parentheses around the pointer name.

Correct:

```c
int (*funcPtr)(int, int);
```

Incorrect:

```c
int *funcPtr(int, int);
```

The incorrect declaration defines a function that returns a pointer to an `int`, not a function pointer.

---

### 8.2 Assigning an Incompatible Function

A function pointer should only store the address of a function whose signature is compatible with its declaration.

For example,

```c
int (*funcPtr)(int, int);
```

is compatible with

```c
int add(int, int);
```

but not with

```c
void display(void);
```

Using incompatible function pointers results in undefined behavior.

---

### 8.3 Calling an Uninitialized Function Pointer

A function pointer must be assigned a valid function address before it is invoked.

Incorrect:

```c
int (*funcPtr)(int, int);

funcPtr(10, 20);      // Undefined behavior
```

Correct:

```c
funcPtr = add;

funcPtr(10, 20);
```

---

### 8.4 Calling a NULL Function Pointer

Sometimes a function pointer may intentionally be set to `NULL` to indicate that no function has been assigned.

Before invoking the function pointer, it is good practice to verify that it is not `NULL`.

```c
if (funcPtr != NULL)
{
    funcPtr(10, 20);
}
```

This prevents attempts to execute an invalid function address.

---

### 8.5 Remember That `funcPtr()` and `(*funcPtr)()` Are Equivalent

The following statements perform exactly the same operation.

```c
funcPtr(10, 20);
```

```c
(*funcPtr)(10, 20);
```

Although both are valid, the first form is more commonly used because it is shorter and easier to read.


---
## <font color='green'>9. Summary</font>

Function pointers are variables that store the addresses of functions, enabling programs to invoke functions indirectly at run time. This provides a level of flexibility that cannot be achieved with direct function calls alone.

In this article, we learned that:

- Every function occupies memory and has a unique address.
- A function pointer stores the address of a compatible function.
- Function pointers must be declared with the correct syntax, including the required parentheses.
- Functions can be assigned to function pointers and invoked indirectly.
- Callback functions allow libraries and applications to execute user-defined functionality.
- Dispatch tables use collections of function pointers to efficiently select and execute operations at run time.
- State machines can use function pointers to represent states, resulting in modular and maintainable code.
- The `typedef` keyword simplifies complex function pointer declarations and improves code readability.
- Care should be taken to use compatible function signatures, initialize function pointers before use, and avoid invoking `NULL` or uninitialized function pointers.

Function pointers are one of the most powerful features of the C language. They form the foundation of callback functions, dispatch tables, state machines, event-driven programming, operating systems, embedded software, communication libraries, and many other flexible software architectures. Although their syntax may initially appear intimidating, understanding the underlying concepts makes them an invaluable tool for writing modular, reusable, and extensible C programs.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory management, pointers, embedded C programming etc.)
