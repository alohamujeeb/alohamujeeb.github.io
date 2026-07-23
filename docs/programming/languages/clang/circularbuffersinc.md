---
hide:
  - navigation
  
tags:
  - Cicular Buffer
  - Ring Buffer
  
---
# Circular Buffers (Ring Buffers) in C

*This article is intended for intermediate and advanced C programmers. It explains what circular buffers are, how they efficiently reuse fixed-size memory, and how they are implemented in C for continuous data storage and retrieval.*

---
## <font color='green'>1. What Is a Circular Buffer?</font>

A **circular buffer**, also known as a **ring buffer**, is a fixed-size data structure that stores data in a continuous loop. Unlike a conventional linear buffer, a circular buffer reuses memory that becomes available after data has been removed, allowing continuous insertion and removal of data without reallocating memory.

Consider a linear buffer of size 8.

```text
+----+----+----+----+----+----+----+----+
| A  | B  | C  | D  |    |    |    |    |
+----+----+----+----+----+----+----+----+
```

Suppose the first two elements are removed.

```text
+----+----+----+----+----+----+----+----+
|    |    | C  | D  |    |    |    |    |
+----+----+----+----+----+----+----+----+
```

Although the first two locations are now free, a linear buffer typically continues writing at the end of the occupied region.

```text
+----+----+----+----+----+----+----+----+
|    |    | C  | D  | E  | F  | G  | H  |
+----+----+----+----+----+----+----+----+
```

At this point, no more elements can be inserted even though unused space exists at the beginning of the buffer. Reusing that space would require shifting the remaining elements toward the front, which is inefficient.

A circular buffer avoids this problem by treating the first and last positions as adjacent. When the end of the buffer is reached, the next insertion wraps around to the beginning, provided that space is available.

```text
          Wrap Around
               ▲
               │
+----+----+----+----+----+----+----+----+
| E  | F  | C  | D  | G  | H  |    |    |
+----+----+----+----+----+----+----+----+
  ▲                                        │
  └────────────────────────────────────────┘
```

Instead of moving existing elements, the buffer simply reuses locations that have already been consumed. As a result, insertion and removal operations remain efficient while the memory is continuously recycled.

Circular buffers are widely used when data is produced and consumed continuously, such as in communication systems, streaming applications, device drivers, and embedded systems.

---
## <font color='green'>2. How a Circular Buffer Works</font>

A circular buffer maintains two indices to manage its contents:

- **Head** – Points to the position where the next element will be inserted.
- **Tail** – Points to the position of the next element to be removed.

As elements are inserted and removed, the head and tail indices move forward independently. When either index reaches the end of the buffer, it wraps around to the beginning.

Consider an empty circular buffer of size 8.

```text
        H,T
         │
         ▼
+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+
```

Suppose four elements are inserted.

```text
                        H
                        │
                        ▼
+----+----+----+----+----+----+----+----+
| A  | B  | C  | D  |    |    |    |    |
+----+----+----+----+----+----+----+----+
  ▲
  │
  T
```

The head now points to the next available position for insertion, while the tail still points to the oldest element in the buffer.

Next, suppose two elements are removed.

```text
                        H
                        │
                        ▼
+----+----+----+----+----+----+----+----+
|    |    | C  | D  |    |    |    |    |
+----+----+----+----+----+----+----+----+
            ▲
            │
            T
```

Notice that the elements are **not shifted**. Instead, only the tail moves forward.

Now insert four more elements.

```text
                                    H
                                    │
                                    ▼
+----+----+----+----+----+----+----+----+
|    |    | C  | D  | E  | F  | G  | H  |
+----+----+----+----+----+----+----+----+
            ▲
            │
            T
```

At this point, the head has reached the end of the buffer. The next insertion wraps around to the beginning.

```text
            H
            │
            ▼
+----+----+----+----+----+----+----+----+
| I  | J  | C  | D  | E  | F  | G  | H  |
+----+----+----+----+----+----+----+----+
            ▲
            │
            T
```

The buffer continues to reuse previously freed locations without moving any existing elements.

Since the head and tail continuously move around the array, the buffer behaves like a ring, which is why it is commonly called a **ring buffer**.

---
## <font color='green'>3. Implementing a Circular Buffer in C</font>

A circular buffer is typically implemented using a fixed-size array together with two indices:

- **Head** – Points to the position where the next element will be inserted.
- **Tail** – Points to the position of the next element to be removed.

The following structure implements a circular buffer for storing integers.

```c
#define BUFFER_SIZE 8

typedef struct
{
    int data[BUFFER_SIZE];
    int head;
    int tail;
} CircularBuffer;
```

Initially, both indices are set to the beginning of the buffer.

```c
void initBuffer(CircularBuffer *cb)
{
    cb->head = 0;
    cb->tail = 0;
}
```

### Checking Whether the Buffer Is Empty

The buffer is empty when the head and tail point to the same location.

```c
int isEmpty(const CircularBuffer *cb)
{
    return cb->head == cb->tail;
}
```

### Checking Whether the Buffer Is Full

A common implementation reserves one array element to distinguish a full buffer from an empty one.

```c
int isFull(const CircularBuffer *cb)
{
    return ((cb->head + 1) % BUFFER_SIZE) == cb->tail;
}
```

With this approach, a buffer of size **N** can store at most **N - 1** elements.

### Inserting an Element (Enqueue)

Before inserting an element, the buffer must be checked to ensure it is not already full.

```c
int enqueue(CircularBuffer *cb, int value)
{
    if (isFull(cb))
        return 0;

    cb->data[cb->head] = value;
    cb->head = (cb->head + 1) % BUFFER_SIZE;

    return 1;
}
```

The following example illustrates the insertion of three elements.

```text
Initially

Head,Tail
    │
    ▼
+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+
```

```text
enqueue(A)
enqueue(B)
enqueue(C)

                  Head
                   │
                   ▼
+----+----+----+----+----+----+----+----+
| A  | B  | C  |    |    |    |    |    |
+----+----+----+----+----+----+----+----+
  ▲
  │
 Tail
```

Notice that only the **head** advances after each insertion.

### Removing an Element (Dequeue)

Before removing an element, the buffer must be checked to ensure it is not empty.

```c
int dequeue(CircularBuffer *cb, int *value)
{
    if (isEmpty(cb))
        return 0;

    *value = cb->data[cb->tail];
    cb->tail = (cb->tail + 1) % BUFFER_SIZE;

    return 1;
}
```

Suppose two elements are removed.

```text
dequeue()
dequeue()

                  Head
                   │
                   ▼
+----+----+----+----+----+----+----+----+
|    |    | C  |    |    |    |    |    |
+----+----+----+----+----+----+----+----+
            ▲
            │
          Tail
```

Notice that the elements are **not shifted**. Only the **tail** advances to the next element.

### Wrap-Around

When the head reaches the end of the array, it wraps around to the beginning.

```text
Before Wrap

                                    Head
                                      │
                                      ▼
+----+----+----+----+----+----+----+----+
|    |    | C  | D  | E  | F  | G  |    |
+----+----+----+----+----+----+----+----+
            ▲
            │
          Tail
```

The next insertion causes the head to wrap around.

```text
enqueue(H)

        Head
          │
          ▼
+----+----+----+----+----+----+----+----+
| H  |    | C  | D  | E  | F  | G  |    |
+----+----+----+----+----+----+----+----+
            ▲
            │
          Tail
```

This wrap-around behavior allows the circular buffer to continuously reuse previously freed locations without moving any existing elements.

---
## <font color='green'>4. Advantages and Limitations</font>

Circular buffers are widely used because they provide an efficient way to manage a continuous stream of data using a fixed amount of memory. However, they also have some limitations that should be considered when choosing an appropriate data structure.

### Advantages

#### Constant-Time Operations

Insertion and removal operations are performed in **constant time**, i.e., **O(1)**. Since elements are never shifted, each operation simply updates the head or tail index.

#### Fixed Memory Usage

A circular buffer allocates a fixed amount of memory during initialization. No additional memory allocation is required while the buffer is in use, making its memory usage predictable.

This characteristic makes circular buffers well suited for embedded and real-time systems where memory is limited.

#### Efficient Memory Reuse

Instead of leaving unused space at the beginning of the buffer, a circular buffer automatically reuses locations that have already been consumed.

```text
Before Reuse

+----+----+----+----+----+----+----+----+
|    |    | C  | D  | E  | F  | G  |    |
+----+----+----+----+----+----+----+----+

After Wrap-Around

+----+----+----+----+----+----+----+----+
| H  | I  | C  | D  | E  | F  | G  |    |
+----+----+----+----+----+----+----+----+
```

This eliminates the need to move existing elements, resulting in efficient use of memory.

### Limitations

#### Fixed Capacity

A circular buffer cannot grow dynamically. Once the buffer becomes full, one of the following actions must be taken:

- Reject new data until space becomes available.
- Overwrite the oldest data.
- Allocate a larger buffer and copy the existing contents.

The appropriate strategy depends on the application's requirements.

#### Full and Empty Detection

Because both the head and tail indices wrap around, additional logic is required to distinguish between a full and an empty buffer.

Common solutions include:

- Reserving one array element.
- Maintaining a separate element count.
- Using a dedicated "full" flag.

#### Not Suitable for Random Insertions

Circular buffers are designed for **First-In, First-Out (FIFO)** access.

They are efficient for inserting at the head and removing from the tail, but they are not suitable for arbitrary insertions, deletions, or random access operations within the buffer.

The next section explores some common applications of circular buffers.

---
## <font color='green'>5. Common Applications</font>

Circular buffers are widely used in systems that continuously produce and consume data. Their constant-time operations and fixed memory usage make them particularly suitable for embedded, real-time, and high-performance applications.

### Producer-Consumer Systems

One of the most common uses of a circular buffer is to exchange data between a **producer** and a **consumer**.

The producer inserts data into the buffer, while the consumer removes it for processing.

```text
          Produce                 Consume
             │                       ▲
             ▼                       │
        +-------------------------------+
        |        Circular Buffer        |
        +-------------------------------+
```

Examples include sensor data acquisition, logging systems, and multithreaded applications.

### Serial Communication

Circular buffers are commonly used in **UART**, **USB**, and other serial communication interfaces.

As bytes arrive from the hardware, an interrupt service routine (ISR) stores them in the circular buffer. The application later removes and processes the received bytes.

```text
UART
  │
  ▼
+----------------+
| Circular Buffer|
+----------------+
        │
        ▼
Application
```

Using a circular buffer prevents incoming data from being lost while the application is busy performing other tasks.

### Audio and Video Streaming

Streaming applications continuously receive and process data.

A circular buffer temporarily stores incoming audio or video samples so that playback can continue smoothly even if the producer and consumer operate at slightly different speeds.

### Network Packet Buffering

Network software often receives packets faster than they can be processed.

A circular buffer provides temporary storage for incoming packets until the networking stack or application is ready to handle them.

### Embedded and Real-Time Systems

Circular buffers are extensively used in embedded systems because they require a fixed amount of memory and avoid dynamic memory allocation.

Typical applications include:

- Sensor data collection
- Keyboard input buffering
- GPS receivers
- Data loggers
- Industrial control systems

In all of these applications, circular buffers provide an efficient mechanism for handling continuous streams of data while keeping memory usage predictable.

---
## <font color='green'>6. Summary</font>

A **circular buffer**, also known as a **ring buffer**, is a fixed-size data structure that stores data in a continuous loop. By treating the beginning and end of the buffer as adjacent, it efficiently reuses memory without shifting existing elements.

In this article, you learned:

- A circular buffer uses a fixed-size array together with **head** and **tail** indices.
- The **head** identifies where the next element will be inserted, while the **tail** identifies the next element to be removed.
- When either index reaches the end of the array, it wraps around to the beginning, allowing the buffer to reuse previously freed locations.
- Insertion (**enqueue**) and removal (**dequeue**) operations execute in **O(1)** time because they only update the head or tail index.
- A circular buffer has a fixed capacity, so applications must decide how to handle a full buffer, such as rejecting new data or overwriting the oldest data.
- Circular buffers are commonly used in producer-consumer systems, serial communication, network packet buffering, streaming applications, and embedded systems.

Because of their simplicity, predictable memory usage, and constant-time operations, circular buffers are one of the most widely used data structures for managing continuous streams of data in systems programming.


---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
