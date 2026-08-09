---
date:
  created: 2026-08-09
  posted: 2026-08-09

author:
  name: Mujeeb
  description: Creator

readtime: 5

categories:
  - Embedded Systems
  
tags:
  - Polling
  - Interrupt
   
---

# <font color='green'>Polling vs. Interrupts</font>

This article is intended for intermediate and advanced C programmers. It explains the two primary techniques used by embedded systems to detect and respond to hardware events, comparing their operation, advantages, limitations, and typical applications.


<!-- more -->

---
## <font color='green'>1. Why Do Embedded Systems Need to Detect Events?</font>

An embedded system continuously interacts with the outside world.

It monitors sensors, communicates with other devices, responds to user inputs, and controls hardware peripherals. To perform these tasks, the processor must detect when an event has occurred.

Typical events include:

- A button is pressed.
- A timer expires.
- A UART receives a character.
- An ADC completes a conversion.
- A CAN message arrives.

Once an event occurs, the application must respond appropriately. For example, it may read incoming data, update an output, or execute a control algorithm.

The question is:

> **How does the processor know that an event has occurred?**

There are two common techniques used in embedded systems:

- **Polling**, where the processor repeatedly checks whether an event has occurred.
- **Interrupts**, where the hardware automatically notifies the processor when an event occurs.

Both approaches are widely used in embedded systems, and each has its own advantages and limitations.

---
## <font color='green'>2. Polling</font>

**Polling** is the simplest technique for detecting hardware events.

In polling, the processor repeatedly checks the status of a peripheral to determine whether an event has occurred.

For example, suppose an application is waiting for a button to be pressed.

Instead of waiting for the hardware to notify it, the processor continuously checks the button's status.

```text
Read Button Status
        │
        ▼
Button Pressed?
   │         │
  No         Yes
   │          │
   └──────────┘
        │
Repeat Check
```

The same approach can be used with other peripherals.

For example, an application may repeatedly check whether:

- A UART has received a character.
- An ADC conversion is complete.
- A timer has expired.
- A communication packet has arrived.

The processor keeps checking until the required event occurs.

---

### Advantages of Polling

Polling offers several benefits:

- Simple to understand and implement.
- Easy to debug.
- No interrupt handling is required.
- Suitable for small applications.

---

### Limitations of Polling

The main drawback of polling is that the processor spends time checking for events even when nothing has happened.

For example, if a button is pressed only once every few seconds, the processor may perform thousands of unnecessary checks before detecting the event.

As a result:

- CPU time is wasted.
- Response time depends on how frequently the event is checked.
- Multiple peripherals become difficult to monitor efficiently.

For simple applications, polling is often sufficient.

However, when faster response or better CPU utilization is required, **interrupts** provide a more efficient solution.


---
## <font color='green'>3. Interrupts</font>

While polling requires the processor to continuously check for events, **interrupts** take the opposite approach.

Instead of the processor asking,

> **"Has anything happened yet?"**

the hardware simply notifies the processor **when an event actually occurs**.

When a peripheral generates an interrupt, the processor temporarily suspends its current execution and automatically executes an **Interrupt Service Routine (ISR)** to handle the event.

After the ISR completes, the processor resumes executing the program from exactly where it left off.

```text
Program Running
       │
       ▼
Hardware Event
       │
       ▼
Interrupt Generated
       │
       ▼
Execute ISR
       │
       ▼
Resume Program
```

Because the processor responds only when necessary, interrupts eliminate the need for continuous polling.

For example, a UART peripheral can generate an interrupt whenever a character is received. Rather than repeatedly checking the UART status register, the processor simply continues executing the application until the interrupt occurs.

---

### Advantages of Interrupts

Interrupts provide several important benefits:

- Fast response to hardware events.
- Better CPU utilization.
- Suitable for asynchronous events.
- Ideal for time-critical applications.

---

### Limitations of Interrupts

Interrupts also introduce additional complexity.

The developer must:

- Write interrupt service routines (ISRs).
- Handle shared data safely between ISRs and the main application.
- Keep ISRs short to avoid delaying other interrupts.

For this reason, interrupt-driven applications are generally more difficult to design and debug than polling-based applications.

Nevertheless, interrupts are the preferred approach for many modern embedded systems because they provide efficient and responsive event handling.

---
## <font color='green'>4. Coparision</font>

Both polling and interrupts are used to detect hardware events. The difference lies in **how the processor becomes aware of those events**.

In polling, the processor repeatedly checks whether an event has occurred.

In an interrupt-driven system, the hardware notifies the processor only when an event actually occurs.

The following table summarizes the main differences.

| Feature | Polling | Interrupts |
|---------|----------|------------|
| Event Detection | CPU repeatedly checks the peripheral | Hardware notifies the CPU |
| CPU Usage | Higher | Lower |
| Response Time | Depends on polling frequency | Usually immediate |
| Software Complexity | Simple | More complex |
| Suitable For | Simple applications | Event-driven and real-time applications |

---

### Polling Example

Suppose a UART receives one character every few seconds.

With polling, the processor repeatedly checks the UART status register, even when no data has arrived.

```text
Check UART
     │
No Data?
     │
    Yes
     │
Repeat
```

Most of these checks are unnecessary, consuming processor time without performing useful work.

---

### Interrupt Example

With interrupts, the processor continues executing the application normally.

Only when a character actually arrives does the UART generate an interrupt.

```text
Application Running
        │
        ▼
UART Receives Data
        │
        ▼
Interrupt
        │
        ▼
Read Character
        │
        ▼
Resume Application
```

This allows the processor to spend its time performing useful work instead of continuously checking peripheral status.

---

Neither approach is universally better.

Polling is often sufficient for **simple or infrequent events**, while interrupts are generally preferred for **time-critical or asynchronous events** where fast response and efficient CPU utilization are important.

---
## <font color='green'>5. When Should You Use Polling or Interrupts?</font>

Choosing between polling and interrupts depends on the application's timing requirements, complexity, and resource constraints.

As a general guideline, **polling** is suitable when events occur infrequently or when response time is not critical. **Interrupts** are preferred when events require immediate attention or occur unpredictably.

---

### Use Polling When:

Polling is often a good choice for:

- Simple embedded applications.
- Slow-changing inputs, such as switches or push buttons.
- Periodic status monitoring.
- Non-time-critical operations.

Because polling is straightforward to implement and debug, it is commonly used in small bare-metal applications.

---

### Use Interrupts When:

Interrupts are generally preferred for:

- UART, SPI, I²C, and CAN communication.
- Timer events.
- ADC conversion completion.
- External sensors.
- Time-critical control systems.

In these applications, responding quickly to an event is often more important than continuously checking whether it has occurred.

---

### Many Systems Use Both

In practice, most embedded systems use a combination of polling and interrupts.

For example, a simple data acquisition system might:

- Use **interrupts** to detect when an ADC conversion is complete.
- Use **polling** to periodically check the status of user buttons.
- Use **interrupts** for UART communication.
- Use **polling** to update an LCD display every few hundred milliseconds.

By selecting the appropriate technique for each task, developers can build systems that are both efficient and easy to maintain.

The choice is therefore **not** between polling *or* interrupts, it is often a matter of deciding **where each technique is most appropriate**.


---
## <font color='green'>6. Summary</font>

Polling and interrupts are the two primary techniques used by embedded systems to detect and respond to hardware events.

Although they serve the same purpose, they differ significantly in how they operate and where they are most effective.

The key points discussed in this article are summarized below:

- **Polling** continuously checks whether an event has occurred.
- **Interrupts** allow hardware to notify the processor only when an event occurs.
- Polling is simple to implement but may waste CPU time checking for events that have not occurred.
- Interrupts improve CPU utilization by allowing the processor to perform other work until an event requires attention.
- Polling is often suitable for simple or non-time-critical applications.
- Interrupts are generally preferred for communication peripherals, timers, sensors, and other time-critical events.
- Most embedded systems use a combination of both techniques rather than relying exclusively on one.

The most important takeaway is this:

> **Polling asks, "Has anything happened?" while interrupts say, "Something has happened."**

Choosing the appropriate technique depends on the application's timing requirements, complexity, and performance needs. Understanding the strengths and limitations of both approaches enables developers to design embedded systems that are both responsive and efficient.

