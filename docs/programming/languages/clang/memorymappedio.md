---
hide:
  - navigation
  
tags:
  - Memory-Mapped IO
  - Memory Mapped IO
  
---

# Memory-Mapped I/O in C

*This article is intended for intermediate and advanced C programmers. It explains how embedded systems map peripheral registers into the processor's address space, allowing hardware devices to be accessed using ordinary C pointers and memory operations.*


---
## <font color='green'>1. What is Memory-Mapped I/O?</font>

In embedded systems, peripherals such as General-Purpose Input/Output (GPIO) ports, timers, Universal Asynchronous Receiver-Transmitter (UART) modules, and Analog-to-Digital Converters (ADCs) are controlled through **registers**. These registers store configuration settings, status information, and data exchanged between the processor and the peripheral.

Processors typically access these peripheral registers using one of two methods:

- **Memory-Mapped I/O**: Peripheral registers occupy locations within the processor's memory address space and are accessed using ordinary memory read and write operations.
- **Port-Mapped I/O (Isolated I/O)**: Peripheral registers reside in a separate I/O address space and are accessed using dedicated I/O instructions. <font color='red'> (this is the focus of this article)</font>

Most modern microcontrollers, including ARM Cortex-M devices, use **Memory-Mapped I/O**, allowing peripheral registers to be accessed using ordinary C pointers. This article focuses on this approach.

In Memory-Mapped I/O, peripheral registers are assigned fixed addresses within the processor's memory address space. From the perspective of a C program, these registers appear just like ordinary memory locations. Reading from or writing to a specific address accesses the corresponding hardware register.

For example, writing to a GPIO control register may configure a pin as an output, while reading from a status register may indicate whether a timer has expired or whether a character has been received by a UART.

Because peripheral registers occupy memory addresses, they can be accessed using ordinary C pointers and the standard memory access operators. This provides a simple and consistent programming model, allowing software to interact with hardware using the same language constructs used to access variables stored in memory.



---
## <font color='green'>2. The Processor's Memory Map</font>

A microcontroller has a finite **address space**, with each address corresponding to a unique memory location. This address space is divided into regions, each serving a specific purpose. Common regions include:

- **Flash Memory**: Stores the program code and constant data.
- **RAM**: Stores variables, the stack, and dynamically allocated memory.
- **Peripheral Registers**: Used to configure and communicate with hardware peripherals such as GPIO ports, timers, UARTs, and ADCs.

A simplified memory map might look like this:

| Address Range | Purpose |
|----------------|---------|
| `0x00000000` - `0x0007FFFF` | Flash Memory |
| `0x20000000` - `0x2001FFFF` | RAM |
| `0x40000000` - `0x5FFFFFFF` | Peripheral Registers |

The exact memory layout varies between microcontrollers, but the concept remains the same. Each peripheral is assigned a dedicated range of memory addresses within the processor's address space.

When the processor reads from or writes to an address within the peripheral region, it is not accessing RAM. Instead, it is communicating directly with the corresponding hardware device. For example, writing a value to one address may configure a GPIO pin, while reading another address may return the current state of a timer or UART.

Because peripheral registers occupy fixed memory addresses, software can access them using ordinary memory operations, making hardware control both simple and efficient.


---
## <font color='green'>3. Peripheral Registers</font>

Peripheral registers are special memory locations used to control and monitor the operation of hardware peripherals. Each register has a specific purpose, such as configuring a peripheral, reporting its status, or transferring data between the processor and the hardware.

For example, a GPIO peripheral may provide registers to:

- Configure a pin as an input or output.
- Read the current state of an input pin.
- Set or clear an output pin.

Similarly, a UART peripheral may include registers to:

- Configure the baud rate.
- Transmit data.
- Receive data.
- Report communication status.

Each register occupies a fixed address within the peripheral region of the processor's memory map. The microcontroller's datasheet or reference manual defines these addresses and describes the purpose of each register.

Unlike ordinary variables stored in RAM, peripheral registers represent hardware resources. Reading from a register retrieves information from the associated peripheral, while writing to a register changes the behaviour or configuration of the hardware.

Because these registers are mapped into the processor's address space, they can be accessed using the same pointer operations used to access ordinary memory. The next section demonstrates how memory-mapped registers are accessed in C.

---
## <font color='green'>4. Accessing Memory-Mapped Registers in C</font>

Since peripheral registers occupy fixed locations within the processor's address space, they can be accessed using ordinary C pointers. A register's address is cast to a pointer of the appropriate type, and dereferencing that pointer reads from or writes to the register.

For example, suppose a GPIO control register is located at address `0x40020000`.

```c
#define GPIO_DIR (*(volatile uint32_t *)0x40020000)
```

This declaration consists of three parts:

- `0x40020000` is the address of the peripheral register.
- `(volatile uint32_t *)` casts the address to a pointer to a 32-bit unsigned integer.
- `*` dereferences the pointer, allowing the register to be accessed like an ordinary variable.

The register can then be read from or written to using normal assignment statements.

```c
/* Configure the GPIO pins */
GPIO_DIR = 0x00000001;

/* Read the current register value */
uint32_t value = GPIO_DIR;
```

Although the syntax resembles reading from or writing to a normal variable, the processor is actually communicating with a hardware peripheral.

Notice the use of the `volatile` qualifier. Unlike ordinary variables, the value stored in a peripheral register may change independently of the executing program. Declaring the register as `volatile` ensures that every read and write is performed exactly as written in the source code. The `volatile` qualifier is discussed in detail in the next article.

---
## <font color='green'>5. Why <code>volatile</code> Is Required</font>

Memory-mapped peripheral registers are different from ordinary variables stored in RAM. Their values may change independently of the executing program. For example, a timer register increments automatically as the timer runs, and a UART status register may change when new data is received.

The compiler, however, assumes that ordinary variables do not change unless the program modifies them. Based on this assumption, it may optimize the generated code by caching values in CPU registers or eliminating repeated memory accesses ([**Read: volatile key word in C**](volatilekeyword.md)).

Such optimizations are undesirable when accessing hardware registers because every read and write must interact with the peripheral.

For this reason, memory-mapped registers are typically declared using the `volatile` qualifier.

```c
#define GPIO_DIR (*(volatile uint32_t *)0x40020000)
```

The `volatile` qualifier instructs the compiler not to optimize accesses to the register. Every read retrieves the current value from the hardware, and every write is performed exactly as specified in the source code.

A detailed discussion of the `volatile` qualifier, including when it should and should not be used, is provided in the next article.


---
## <font color='green'>6. Benefits of Memory-Mapped I/O</font>

Memory-Mapped I/O is widely used in modern microcontrollers because it provides a simple and efficient mechanism for software to communicate with hardware peripherals.

Some of its key benefits include:

- **Unified Address Space**: Program memory, RAM, and peripheral registers all reside within the processor's address space, providing a consistent method of accessing both memory and hardware.

- **Simple Programming Model**: Peripheral registers are accessed using ordinary C pointers and standard memory read and write operations. No special programming constructs are required.

- **Efficient Hardware Access**: The processor uses the same load and store instructions for both memory and peripheral accesses, simplifying the processor architecture.

- **Language Independence**: Since peripherals appear as memory locations, any programming language capable of reading from and writing to memory can access hardware registers.

- **Portable Programming Techniques**: Although register addresses vary between microcontrollers, the underlying programming model remains largely the same across many embedded processor families.

Because of these advantages, Memory-Mapped I/O has become the preferred method of interfacing with hardware in most modern embedded systems. It provides a straightforward abstraction that allows software to configure peripherals and exchange data with hardware using familiar memory access operations.


---
## <font color='green'>7. Summary</font>

Memory-Mapped I/O allows embedded software to communicate with hardware peripherals by mapping their registers into the processor's memory address space. As a result, peripherals can be accessed using ordinary memory read and write operations.

The key concepts covered in this article are summarized below.

| Concept | Description |
|---------|-------------|
| Memory-Mapped I/O | Maps peripheral registers into the processor's memory address space. |
| Port-Mapped I/O | Uses a separate I/O address space accessed with dedicated instructions. |
| Memory Map | Organizes the processor's address space into regions such as Flash, RAM, and peripherals. |
| Peripheral Register | A hardware register used to configure, control, or monitor a peripheral. |
| Pointer Access | Registers are accessed by casting their address to a pointer and dereferencing it. |
| `volatile` | Ensures every register access is performed exactly as written by preventing unwanted compiler optimizations. |

Memory-Mapped I/O is a fundamental concept in embedded systems programming. Understanding how hardware registers are mapped into memory provides the foundation for configuring peripherals, developing device drivers, and writing efficient low-level embedded software.



---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
