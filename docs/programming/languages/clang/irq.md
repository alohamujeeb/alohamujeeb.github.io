---
hide:
  - navigation
  
tags:
  - IRQ
  - Interrupt Service Routine

---

# <font color='green'> Interrupts and IRQs: How Hardware Gets the CPU's Attention </font>

*This article is intended for intermediate and advanced C programmers. It explains how interrupts allow hardware devices to notify the CPU when attention is required, the role of Interrupt Requests (IRQs), and why interrupt-driven systems are far more efficient than continuous polling.*

---
## <font color='green'>1. Why Do We Need Interrupts?</font>

When communicating with a hardware device, the CPU generally has two ways of determining whether the device requires attention:

1. **Polling**
2. **Interrupts**

Both techniques achieve the same goal, but they differ significantly in efficiency.

---

### 1.1 Polling

With **polling**, the CPU repeatedly checks the status of a hardware device to determine whether it needs servicing.

For example, consider a UART receiving data from another device.

```text
CPU

Loop Forever

    │
    ▼
+---------------------+
| UART has data?      |
+---------------------+
        │
   No ──┘
        │
       Yes
        │
        ▼
 Read Data

Repeat...
```

The CPU continuously asks:

> "Has data arrived?"

If the answer is **No**, it immediately asks again.

This process repeats over and over until data finally arrives.

Polling works, but it has one major disadvantage: **the CPU spends much of its time checking devices that have nothing to report.**

Now imagine a system with several hardware devices.

```text
CPU

Loop Forever

Keyboard?
Mouse?
UART?
ADC?
Timer?
GPIO?
Network?
Repeat...
```

Even if every device is idle, the CPU continues checking each one.

As the number of devices increases, more CPU time is wasted performing these repeated checks.

---

### 1.2 Interrupts

A more efficient approach is to let the **hardware device notify the CPU** whenever it requires attention.

Instead of constantly checking every device, the CPU simply continues executing its normal program.

```text
CPU

+------------------------------+
| Executing Application Code   |
+------------------------------+
```

When a hardware device needs servicing, it sends a signal to the CPU.

```text
Keyboard ----------------------► CPU

           "I need attention!"
```

The CPU temporarily pauses its current task, services the hardware device, and then resumes exactly where it left off.

This mechanism is called an **interrupt**.

Using interrupts allows the CPU to spend its time performing useful work instead of continuously checking devices that are idle. As a result, interrupt-driven systems are generally more efficient, more responsive, and consume less power than systems that rely solely on polling.

The next section explains what an interrupt is and what happens inside the CPU when one occurs.


---
## <font color='green'>2. Polling in Practice</font>

The previous section introduced **polling** as a technique in which the CPU repeatedly checks whether a hardware device requires attention.

Let's see what this looks like in a C program.

Suppose a UART provides the following function.

```c
bool UART_DataAvailable(void);
```

The function returns:

- `true` if data has been received.
- `false` otherwise.

A simple polling loop might look like this.

```c
while (1)
{
    if (UART_DataAvailable())
    {
        /* Read and process the data */
    }
}
```

Although this code appears simple, consider what actually happens.

```text
while (1)
{
    Is data available?
        No

    Is data available?
        No

    Is data available?
        No

    Is data available?
        No

    Is data available?
        Yes
}
```

The CPU continuously calls `UART_DataAvailable()`, even when no data has arrived.

Most of these function calls simply return `false`.

---

Now imagine that the program communicates with several hardware devices.

```c
while (1)
{
    if (UART_DataAvailable())
    {
        /* Process UART data */
    }

    if (Keyboard_KeyPressed())
    {
        /* Process keyboard input */
    }

    if (Timer_Expired())
    {
        /* Process timer event */
    }

    if (ADC_ConversionComplete())
    {
        /* Read ADC value */
    }
}
```

The CPU repeatedly checks every device, one after another.

```text
Loop

UART?
Keyboard?
Timer?
ADC?

Repeat...
```

Even if none of the devices require attention, the CPU continues executing this loop.

This constant checking wastes CPU time and power, especially when hardware events occur infrequently.

Polling is acceptable for simple applications and may even be the preferred solution in some situations. However, as the number of devices increases, continuously checking each one becomes increasingly inefficient.

> A better approach is to let the hardware device notify the CPU **only when it actually needs attention**.

This is the purpose of an **interrupt**, which is discussed in the next section.

---
## <font color='green'>3. What Is an Interrupt?</font>

> An **interrupt** is a signal sent by a hardware device to inform the CPU that it requires immediate attention.

> Instead of the CPU repeatedly asking a device whether something has happened, the device simply notifies the CPU when an event occurs.

For example, consider a keyboard.

With polling, the CPU repeatedly checks whether a key has been pressed.

```text
CPU

Keyboard?
Keyboard?
Keyboard?
Keyboard?
Keyboard?
...
```

With interrupts, the CPU does not need to perform these repeated checks.

Instead, it continues executing its current program.

```text
CPU

+------------------------------+
| Executing Application Code   |
+------------------------------+
```

When a key is pressed, the keyboard sends an interrupt signal.

```text
              Key Pressed

Keyboard ------------------------► CPU
```

The CPU then temporarily pauses the currently executing program and responds to the interrupt.

---

### 3.1 What Does the CPU Do?

The CPU does **not** stop immediately when an interrupt occurs.

Instead, it first completes the instruction that it is currently executing.

```text
Current Program

Instruction 1
Instruction 2
Instruction 3   ← Interrupt occurs
Instruction 4

        ↓

CPU completes Instruction 3

        ↓

CPU responds to the interrupt
```

Completing the current instruction ensures that the processor remains in a consistent state before handling the interrupt.

---

### 3.2 Saving the Program State

Before servicing the interrupt, the CPU must save enough information so that the interrupted program can continue later.

Typically, this includes:

- The Program Counter (PC)
- Processor status information
- CPU registers (depending on the processor architecture)

Conceptually, the sequence is:

```text
Running Program

        │
        ▼

+----------------------+
| Save CPU State       |
+----------------------+
        │
        ▼
+----------------------+
| Handle Interrupt     |
+----------------------+
        │
        ▼
+----------------------+
| Restore CPU State    |
+----------------------+
        │
        ▼

Continue Program
```

Once the CPU state has been saved, the processor begins executing a special function designed to handle the interrupt.

This function is called an **Interrupt Service Routine (ISR)**.

The ISR performs whatever work is necessary for the hardware device.

For example:

- Read a received UART byte.
- Record a keyboard key press.
- Update a timer tick.
- Read the result of an ADC conversion.

After the ISR finishes, the CPU restores the saved state and resumes execution of the interrupted program.

```text
Program Execution

=============================

        Interrupt

=============================

Execute ISR

=============================

Resume Program

=============================
```

From the program's point of view, execution simply pauses for a very short time before continuing exactly where it left off.

The next section explains how hardware devices request the CPU's attention using an **Interrupt Request (IRQ)**.

---
## <font color='green'>4. Common Sources of Interrupts</font>

Almost any hardware device can generate an interrupt whenever it requires the CPU's attention.

The signal sent by the device is known as an **Interrupt Request**, or **IRQ**.

Instead of waiting for the CPU to repeatedly check its status, the device raises an IRQ whenever an important event occurs.

Some common examples are shown below.

| Hardware Device | Typical IRQ Event |
|-----------------|-------------------|
| Keyboard | A key is pressed or released. |
| Mouse | The mouse moves or a button is clicked. |
| Timer | A timer interval expires. |
| UART | A byte has been received or transmitted. |
| Network Interface | A network packet has arrived. |
| GPIO | An external signal changes state. |
| ADC | An analog-to-digital conversion completes. |
| DMA Controller | A data transfer finishes. |

Let's look at a few of these in more detail.

---

### 4.1 Keyboard Interrupt

When a user presses a key, the keyboard immediately generates an IRQ.

```text
Key Pressed

Keyboard
     │
     ▼
    IRQ
     │
     ▼
    CPU
```

The CPU executes the keyboard's Interrupt Service Routine (ISR), which reads the key information before returning to the interrupted program.

Without interrupts, the CPU would need to continuously ask:

```text
Key pressed?
Key pressed?
Key pressed?
Key pressed?
...
```

---

### 4.2 Timer Interrupt

Timers are one of the most common sources of interrupts.

For example, a hardware timer may be configured to generate an interrupt every 1 millisecond.

```text
Time

0 ms     1 ms     2 ms     3 ms

 |---------|---------|---------|
     IRQ       IRQ       IRQ
```

Each timer interrupt allows the operating system or embedded application to perform periodic tasks such as:

- Updating the system clock
- Scheduling tasks
- Reading sensors
- Toggling LEDs

---

### 4.3 Network Interrupt

A network controller generates an IRQ whenever a network packet arrives.

```text
Network Packet

Ethernet Controller
        │
        ▼
       IRQ
        │
        ▼
       CPU
```

Instead of continuously checking whether new data has arrived, the CPU is notified only when a packet is actually received.

---

### 4.4 GPIO Interrupt

Many embedded systems use General-Purpose Input/Output (GPIO) pins to detect external events.

For example, pressing a push button connected to a GPIO pin can generate an interrupt.

```text
Push Button

Button
   │
   ▼
GPIO Pin
   │
   ▼
 IRQ
   │
   ▼
 CPU
```

This allows the application to respond immediately to user input without continuously polling the GPIO pin.

---

These examples illustrate the primary purpose of IRQs: **allowing hardware devices to notify the CPU only when an event occurs**.

Whether the event is a key press, a timer expiration, a completed ADC conversion, or the arrival of a network packet, the overall sequence remains the same:

1. A hardware event occurs.
2. The device raises an IRQ.
3. The CPU temporarily pauses its current task.
4. The appropriate Interrupt Service Routine (ISR) executes.
5. The CPU resumes the interrupted program.


---
## <font color='green'>5. IRQ vs Interrupt Service Routine (ISR)</font>

The terms **IRQ** and **Interrupt Service Routine (ISR)** are closely related, but they refer to two completely different things.

An **IRQ (Interrupt Request)** is a **hardware-generated signal** that informs the CPU a device requires attention.

An **Interrupt Service Routine (ISR)** is a **software function** that the CPU executes to handle that interrupt.

In simple terms:

- **IRQ** = "Something happened!"
- **ISR** = "Here's how to handle it."

---

### 5.1 IRQ: A Hardware-Generated Signal

When a hardware device detects an event that requires the CPU's attention, it generates an **Interrupt Request (IRQ)**.

For example:

- A keyboard generates an IRQ when a key is pressed.
- A timer generates an IRQ when it expires.
- A UART generates an IRQ when new data is received.
- A network controller generates an IRQ when a packet arrives.

Conceptually:

```text
Hardware Device

      Event Occurs
            │
            ▼
     Generate IRQ
            │
            ▼
           CPU
```

An IRQ is **not code**.

It is simply a hardware signal that tells the CPU:

> "I need your attention."

---

### 5.2 ISR: A Software Function

After receiving the IRQ, the CPU executes a special function called an **Interrupt Service Routine (ISR)**.

The ISR contains the code that services the hardware device.

For example, a keyboard ISR might read the key that was pressed.

```c
void Keyboard_ISR(void)
{
    /* Read the pressed key */

    /* Process the key */
}
```

Similarly, a UART ISR may read a received byte.

```c
void UART_ISR(void)
{
    /* Read received data */

    /* Store it in a buffer */
}
```

Unlike an IRQ, an ISR is **ordinary program code** written in C or assembly language.

The CPU executes the ISR just as it would execute any other function, except that it is invoked automatically in response to an interrupt.

---

### 5.3 IRQ and ISR Working Together

The sequence of events is illustrated below.

```text
Hardware Event
      │
      ▼
Generate IRQ
      │
      ▼
CPU Receives IRQ
      │
      ▼
Execute ISR
      │
      ▼
Service the Device
      │
      ▼
Resume Interrupted Program
```

The following table summarizes the difference.

| IRQ | ISR |
|-----|-----|
| Hardware-generated signal | Software function |
| Generated by a hardware device | Executed by the CPU |
| Requests CPU attention | Handles the interrupt |
| Electrical or hardware event | C or assembly code |
| Occurs first | Executes after the IRQ is accepted |

An easy way to remember the difference is:

- **IRQ asks for attention.**
- **ISR performs the work.**

> <font color='red'>The IRQ is the notification sent by the hardware, while the ISR is the code that responds to that notification.</font>

---
## <font color='green'>6. Advantages of Interrupts Over Polling</font>

Both **polling** and **interrupts** enable the CPU to communicate with hardware devices. However, interrupt-driven systems are generally more efficient because the CPU responds **only when an event occurs**.

The following table compares the two approaches.

| Polling | Interrupts |
|---------|------------|
| CPU repeatedly checks device status. | Device notifies the CPU when an event occurs. |
| CPU time is spent checking idle devices. | CPU performs other work until interrupted. |
| Higher CPU utilization. | Better CPU utilization. |
| Generally consumes more power. | Often consumes less power. |
| Simple to implement. | More complex to implement. |

---

### 6.1 Better CPU Utilization

With polling, the CPU repeatedly executes code to check whether a device requires attention.

```text
CPU

UART?
Keyboard?
Timer?
UART?
Keyboard?
Timer?
...
```

Most of these checks find nothing to do.

With interrupts, the CPU spends its time executing useful work.

```text
CPU

+------------------------------+
| Executing Application Code   |
+------------------------------+

          │
          │ Interrupt Occurs
          ▼

+------------------------------+
| Execute ISR                  |
+------------------------------+

          │
          ▼

+------------------------------+
| Resume Application           |
+------------------------------+
```

The CPU responds only when necessary.

---

### 6.2 Faster Response to Hardware Events

Polling can only detect an event when the program reaches the next polling operation.

For example, if a program checks a keyboard every 100 milliseconds, a key press may not be detected immediately.

```text
Polling

Check -------- Check -------- Check
      ↑
 Key Press

Detected at next check
```

With interrupts, the hardware immediately notifies the CPU.

```text
Key Press
     │
     ▼
Generate IRQ
     │
     ▼
CPU Executes ISR
```

This results in much faster response times.

---

### 6.3 Lower Power Consumption

Polling keeps the CPU active because it is constantly checking hardware devices.

Interrupt-driven systems allow the CPU to continue useful work or even enter a low-power sleep mode until an interrupt occurs.

This is one of the reasons interrupts are widely used in embedded systems, battery-powered devices, and mobile electronics.

---

### 6.4 When Is Polling Still Useful?

Although interrupts are generally preferred, polling is not obsolete.

Polling may still be appropriate when:

- the hardware must be checked continuously,
- events occur very frequently,
- the application is simple,
- minimizing software complexity is more important than maximizing efficiency.

For example, a simple microcontroller application that periodically reads a temperature sensor every second may use polling without any noticeable performance issues.


> Interrupts provide a more efficient mechanism for communicating with hardware because devices notify the CPU only when attention is required. This allows the processor to spend more time performing useful work, respond quickly to important events, and reduce unnecessary CPU activity.

---
## <font color='green'>7. Summary</font>

Interrupts provide an efficient mechanism for communication between hardware devices and the CPU. Instead of continuously checking whether a device requires attention, the CPU allows the hardware to notify it only when an important event occurs.

The two common approaches to communicating with hardware are:

- **Polling**, where the CPU repeatedly checks the status of each device.
- **Interrupts**, where the hardware notifies the CPU whenever service is required.

An interrupt begins when a hardware device generates an **Interrupt Request (IRQ)**. After receiving the IRQ, the CPU temporarily pauses the currently executing program, saves its state, and executes an **Interrupt Service Routine (ISR)** to service the device. Once the ISR completes, the CPU restores the saved state and resumes the interrupted program.

The key distinction between these terms is:

- **IRQ** – A hardware-generated signal requesting the CPU's attention.
- **ISR** – A software function executed by the CPU to handle that request.

Interrupts are generated by many hardware devices, including:

- Timers
- Keyboards
- Mice
- UARTs
- Network interfaces
- GPIO peripherals
- ADCs
- DMA controllers

Compared to polling, interrupt-driven systems offer several advantages:

- Better CPU utilization
- Faster response to hardware events
- Lower power consumption
- Improved scalability as more hardware devices are added

For these reasons, interrupts are a fundamental feature of modern operating systems, desktop computers, and embedded systems, enabling hardware devices to communicate efficiently with the processor while allowing the CPU to spend most of its time performing useful work.




---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
