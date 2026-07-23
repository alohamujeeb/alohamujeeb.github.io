---
hide:
  - navigation
  
tags:
  - Callback Patterns
  
  
---
# Callback Design Patterns in C

*This article is intended for intermediate and advanced C programmers. It explains how callback functions enable libraries to invoke application-defined behavior, introduces common callback design patterns, and demonstrates how they are used to build flexible and reusable C APIs.*

---
## <font color='green'>1. What Are Callbacks?</font>

A **callback** is a function that is passed as an argument to another function so that it can be invoked later. Instead of hard-coding a specific behavior, a function delegates part of its work to another function supplied by the caller.

Unlike an ordinary function call, where the application directly invokes a library function, a callback reverses this relationship. The application passes a function to the library, and the library invokes that function whenever appropriate.

```text
Ordinary Function Call

Application
     │
     ▼
Library Function
```

```text
Callback

Application
     │
     │  Passes Callback
     ▼
+----------------------+
|      Library         |
+----------------------+
            │
            │ Invokes Callback
            ▼
Application Function
```

This reversal is often referred to as **inversion of control** because the application temporarily gives the library control over when a particular function is executed.

For example, consider a library function that processes every element of an integer array. Rather than deciding what to do with each element, the library allows the application to provide a callback.

```c
void process(int *array,
             size_t size,
             void (*callback)(int));
```

Here:

- `array` specifies the data to process.
- `size` specifies the number of elements.
- `callback` specifies the function to invoke for each element.

The application defines the desired behavior.

```c
void printNumber(int value)
{
    printf("%d\n", value);
}
```

It then passes the callback to the library.

```c
int values[] = {10, 20, 30};

process(values, 3, printNumber);
```

During execution, the library repeatedly invokes the callback.

```text
process()

      │
      ├── callback(10)
      ├── callback(20)
      └── callback(30)
```

The library controls **when** the callback is executed, while the application controls **what** the callback does.

This separation makes the library independent of application-specific behavior. The same processing function can be reused with different callbacks without changing its implementation.

For example, one application might print each value, another might compute a sum, and a third might write the values to a file. The library performs the same traversal in every case; only the callback changes.

---
## <font color='green'>2. The Basic Callback Pattern</font>

The simplest callback pattern consists of a function that accepts another function as one of its parameters. Rather than performing a fixed operation, the function delegates part of its work to the callback.

A typical callback-based function has the following form.

```c
void process(int *array,
             size_t size,
             void (*callback)(int));
```

Here, `process()` is responsible for traversing the array, while the callback determines what action is performed for each element.

```text
                process()

      +-----------------------------+
      | Traverse Array              |
      +-----------------------------+
                 │
                 ├── callback(10)
                 ├── callback(20)
                 ├── callback(30)
                 └── callback(40)
```

A simple callback that prints each value might be written as follows.

```c
void printNumber(int value)
{
    printf("%d\n", value);
}
```

The callback is passed to `process()` when it is called.

```c
int values[] = {10, 20, 30, 40};

process(values, 4, printNumber);
```

Internally, `process()` invokes the callback for every element in the array.

```c
void process(int *array,
             size_t size,
             void (*callback)(int))
{
    for (size_t i = 0; i < size; i++)
    {
        callback(array[i]);
    }
}
```

The advantage of this design is that the traversal algorithm remains unchanged while the callback determines the behavior.

For example, a different callback can compute the sum of all elements.

```c
int sum = 0;

void addNumber(int value)
{
    sum += value;
}
```

The same `process()` function can now be reused.

```c
process(values, 4, addNumber);
```

Likewise, another callback could write each value to a file.

```c
void writeNumber(int value)
{
    fprintf(file, "%d\n", value);
}

process(values, 4, writeNumber);
```

```text
            Same Algorithm

          process(array)

                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 print()     add()     write()
```

In each case, `process()` performs exactly the same traversal. The only difference is the callback supplied by the application.

This separation between the algorithm and the operation being performed is the fundamental idea behind callback-based design. By allowing the caller to provide different callbacks, a single function can support many different behaviors without modifying its implementation.

---
## <font color='green'>3. Callback Design Patterns</font>

Callbacks are used in different ways depending on the problem a library is trying to solve. The following are some of the most common callback patterns used in C libraries.

### Iteration Callback

An iteration callback is invoked once for every element in a collection. The library performs the traversal, while the callback processes each element.

```c
/* Callback */

void print(int value)
{
    printf("%d\n", value);
}
```

```c
/* Library */

void process(int *array,
             size_t size,
             void (*callback)(int))
{
    for (size_t i = 0; i < size; i++)
    {
        callback(array[i]);
    }
}
```

```c
/* Application */

int values[] = {10, 20, 30};

process(values, 3, print);
```

Execution:

```text
process()

    │
    ├── print(10)
    ├── print(20)
    └── print(30)
```

### Comparison Callback

A comparison callback determines the ordering of two objects. Instead of assuming how objects should be compared, the library delegates that decision to the application.

```c
/* Callback */

int compare(const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    return (*x > *y) - (*x < *y);
}
```

```c
/* Library */

void sortArray(int *array,
               size_t size,
               int (*compare)(const void *, const void *))
{
    qsort(array,
          size,
          sizeof(int),
          compare);
}
```

```c
/* Application */

int values[] = {30, 10, 40, 20};

sortArray(values, 4, compare);
```

Execution:

```text
sortArray()

      │
      ▼

qsort()

      │
      ├── compare(30, 10)
      ├── compare(40, 20)
      ├── compare(10, 20)
      └── ...
```

The application provides the comparison logic, while the library invokes the callback whenever it needs to determine the relative ordering of two elements.


### Event Callback

An event callback is invoked when a particular event occurs. Unlike an iteration callback, the application does not know when the callback will be executed. Instead, the library invokes it whenever the corresponding event takes place.

```c
/* Callback */

void onButtonClick(void)
{
    printf("Button clicked!\n");
}
```

```c
/* Library */

static void (*buttonCallback)(void);

void registerButtonCallback(void (*callback)(void))
{
    buttonCallback = callback;
}

void buttonClicked(void)
{
    if (buttonCallback != NULL)
        buttonCallback();
}
```

```c
/* Application */

registerButtonCallback(onButtonClick);

/* ... */

buttonClicked();
```

Execution:

```text
Application

registerButtonCallback(onButtonClick)

            │
            ▼

        Library

Stores callback

            │

Button Clicked
            │
            ▼

buttonClicked()

            │
            ▼

onButtonClick()
```

The application registers a callback once, and the library invokes it whenever the event occurs. This pattern is commonly used for graphical user interfaces, keyboard and mouse events, timers, network events, and interrupt handlers.

### Notification Callback

A notification callback allows a library to report its progress or status while performing a long-running operation. Instead of waiting until the operation completes, the library periodically invokes the callback to notify the application.

```c
/* Callback */

void showProgress(int percent)
{
    printf("%d%% complete\n", percent);
}
```

```c
/* Library */

void downloadFile(const char *url,
                  void (*progress)(int))
{
    /* ... */

    progress(10);

    /* ... */

    progress(50);

    /* ... */

    progress(100);
}
```

```c
/* Application */

downloadFile("https://example.com/file.zip",
             showProgress);
```

Execution:

```text
downloadFile()

      │
      ├── showProgress(10)
      ├── showProgress(50)
      └── showProgress(100)
```

The application supplies the notification callback, while the library determines **when** progress updates are reported. This pattern is commonly used for file downloads, uploads, data compression, software installation, and other long-running operations.


### Filter Callback

A filter callback determines whether an object should be accepted or rejected. For each object, the library invokes the callback and uses its return value to decide whether to keep or discard the object.

```c
/* Callback */

int isEven(int value)
{
    return value % 2 == 0;
}
```

```c
/* Library */

void filter(int *array,
            size_t size,
            int (*predicate)(int))
{
    for (size_t i = 0; i < size; i++)
    {
        if (predicate(array[i]))
        {
            printf("%d\n", array[i]);
        }
    }
}
```

```c
/* Application */

int values[] = {10, 15, 20, 25, 30};

filter(values, 5, isEven);
```

Execution:

```text
filter()

      │
      ├── isEven(10) ──► Keep
      ├── isEven(15) ──► Discard
      ├── isEven(20) ──► Keep
      ├── isEven(25) ──► Discard
      └── isEven(30) ──► Keep
```

The application supplies the filtering criteria, while the library decides **when** the callback is invoked and what action to take based on its return value. This pattern is commonly used for searching, data filtering, validation, and custom selection criteria.



---
## <font color='green'>4. Designing Callback-Based APIs</font>

When designing a callback-based API, it is important to define a callback interface that is flexible, easy to use, and unambiguous. A poorly designed callback can make an API difficult to understand or limit its usefulness.

The following guidelines are commonly used when designing callback-based APIs.

### Keep Callback Signatures Simple

A callback should receive only the information needed to perform its task.

For example, a callback that processes an integer might be declared as:

```c
void callback(int value);
```

If additional information is required, it should be passed explicitly rather than relying on global variables.

Simple callback signatures are easier to understand, document, and reuse.

---

### Pass User Context

Many callbacks need access to application-specific data.

Instead of using global variables, a common design is to provide a user-defined context pointer.

```c
void process(int *array,
             size_t size,
             void (*callback)(int, void *),
             void *userData);
```

The library stores the `userData` pointer and passes it unchanged whenever the callback is invoked.

```text
Application

userData
    │
    ▼
+-------------------+
|     Library       |
+-------------------+
          │
          ▼
callback(value, userData)
```

This allows the callback to maintain state while keeping the library independent of application-specific data.

---

### Define the Callback's Return Value

Some callbacks simply perform an action and return nothing.

```c
void callback(int value);
```

Others return a value to influence the library's behavior.

For example, a callback may indicate whether processing should continue.

```c
int callback(int value);
```

```text
callback()

     │
     ├── 0 → Stop
     └── 1 → Continue
```

Clearly documenting the meaning of the callback's return value avoids ambiguity.

---

### Document Invocation Rules

Applications need to know when and how callbacks are invoked.

For example, documentation should specify:

- When the callback is called.
- How often it may be called.
- Whether it may be called multiple times.
- Whether it may terminate the operation early.

Well-defined invocation rules help prevent incorrect assumptions by API users.

---

### Define Ownership Responsibilities

If a callback receives pointers, the API should clearly specify their ownership.

For example:

- Is the callback allowed to modify the object?
- Is it allowed to retain the pointer after returning?
- Is it responsible for freeing the memory?

Clearly documenting ownership prevents misuse and memory management errors.


By following these guidelines, callback-based APIs become easier to understand, safer to use, and more flexible. A well-designed callback interface allows the library to remain generic while giving applications complete control over their custom behavior.



---
## <font color='green'>5. Advantages and Limitations</font>

Callback-based design is widely used in C because it enables libraries to remain generic while allowing applications to customize their behavior. However, this flexibility comes with some trade-offs.

### Advantages

#### Reusable Algorithms

Callbacks separate an algorithm from the operation it performs.

For example, a single array traversal function can support many different operations simply by changing the callback.

```text
           process()

               │
      ┌────────┼────────┐
      ▼        ▼        ▼
   print()   sum()   write()
```

The traversal logic is written once and reused with different callbacks.

---

#### Flexible Behavior

A library does not need to know what an application wants to do with the data it processes.

Instead, the application supplies the desired behavior through a callback.

This makes the library adaptable to many different use cases without requiring changes to its implementation.

---

#### Decoupling

Callbacks reduce the dependency between a library and the applications that use it.

The library focuses on **how** an operation is performed, while the application decides **what** should happen at specific points during execution.

```text
Library
    │
    │ Calls
    ▼
Application Callback
```

This separation makes both the library and the application easier to develop and maintain.

---

#### Extensible APIs

New application behavior can often be added by writing a new callback rather than modifying the library itself.

As a result, the same API can support a wide variety of applications without increasing the complexity of the library.

### Limitations

#### Indirect Control Flow

With callbacks, the flow of execution is no longer strictly linear.

```text
Application
      │
      ▼
Library
      │
      ▼
Callback
      │
      ▼
Library
      │
      ▼
Application
```

This indirect flow can make programs more difficult to understand, especially when callbacks invoke additional library functions.

---

#### More Difficult Debugging

Because control repeatedly switches between the library and the application, following program execution during debugging may require stepping through multiple functions and source files.

---

#### Lifetime of Callback Data

If a callback receives pointers or user-defined context, those objects must remain valid for as long as the library may invoke the callback.

Using pointers to objects that have already been destroyed results in undefined behavior.

---

#### More Complex API Design

Designing callback-based APIs requires careful consideration of:

- Callback signatures
- Return values
- Invocation rules
- Ownership of callback data

Poorly designed callback interfaces can be difficult to understand and use correctly.

Despite these challenges, callback-based design remains one of the most effective techniques for building flexible and reusable C libraries. It allows a single implementation to support a wide range of application-specific behavior without sacrificing modularity.

The next section summarizes the key concepts discussed in this article.

---
## <font color='green'>6. Summary</font>

Callbacks are a fundamental technique for designing flexible and reusable C libraries. Rather than hard-coding application-specific behavior, a library allows the application to provide one or more callback functions that are invoked when needed.

In this article, you learned:

- A callback is a function passed as an argument to another function so that it can be invoked later.
- Callbacks reverse the normal direction of function calls, allowing a library to invoke application-defined behavior.
- The basic callback pattern separates an algorithm from the operation performed on the data, making the algorithm reusable.
- Common callback design patterns include iteration callbacks, comparison callbacks, event callbacks, notification callbacks, and filter callbacks.
- Well-designed callback-based APIs use clear callback signatures, provide user context when needed, define callback return values, document invocation rules, and specify ownership responsibilities.
- Callback-based design improves flexibility, reusability, and extensibility, but also introduces indirect control flow and requires careful API design.

Although callbacks are implemented using ordinary function pointers, they represent an important API design technique. By allowing applications to supply custom behavior, callback-based libraries remain generic while supporting a wide variety of use cases without modifying their core implementation.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
