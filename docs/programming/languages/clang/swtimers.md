---
hide:
  - navigation
  
tags:
  - Timers in C
  - Software Timers

---

# Software Timers: Extending Limited Hardware Timers

*This article is intended for intermediate and advanced C programmers. It explains why software timers are needed, how they overcome the limitations of hardware timers, and how to design and implement a software timer manager in C for bare-metal embedded systems.*

---
## <font color='green'>1. Hardware Timers</font>

Modern microcontrollers include dedicated hardware timer peripherals that provide precise timing and event generation. These peripherals operate independently of the CPU and are among the most versatile resources available in an embedded system.

Unlike software routines that consume processor cycles, hardware timers continue counting in the background while the CPU executes other instructions. They are driven by the microcontroller's clock and can generate events with high accuracy and minimal processor intervention.

A typical microcontroller provides only a small number of hardware timers. Depending on the device family, this may range from as few as two timers in low-end devices to several timers in high-performance microcontrollers. For many applications, having four hardware timers is quite common.

```text
Microcontroller

+---------+
| Timer 1 |
+---------+

+---------+
| Timer 2 |
+---------+

+---------+
| Timer 3 |
+---------+

+---------+
| Timer 4 |
+---------+
```

Although they all perform timing functions, hardware timers are capable of much more than simply measuring elapsed time. Common applications include:

- Generating periodic interrupts
- Producing PWM (Pulse Width Modulation) signals
- Measuring pulse widths and frequencies using input capture
- Generating precisely timed output signals using output compare
- Counting external events
- Measuring time intervals

Since hardware timers are implemented as dedicated peripherals, they are limited hardware resources. Once a timer is allocated for a particular purpose. For example, generating a PWM signal for a motor, it is generally unavailable for other tasks.

Consider a typical embedded application:

- One timer generates the system tick.
- Another produces PWM for motor speed control.
- A third measures the frequency of an incoming signal.
- A fourth generates a communication timeout.

At this point, all available hardware timers have been assigned specific functions.

However, the application may still require many additional timing operations, such as blinking multiple LEDs, debouncing buttons, scheduling sensor readings, implementing communication timeouts, periodically logging data, or triggering maintenance tasks.

Clearly, allocating a dedicated hardware timer for every timing requirement is neither practical nor possible.

So, what happens when an application needs 20, 50, or even 100 independent timers, but the microcontroller provides only four hardware timer peripherals?

This limitation leads directly to the concept of **software timers**, which allow a single hardware timer to support many independent logical timers.

---
## <font color='green'>2. Why Software Timers Exist</font>

As discussed in the previous section, hardware timers are limited resources. While a typical microcontroller may provide only four hardware timers, a real-world embedded application often requires dozens of independent timing operations.

Consider a simple embedded system controlling various peripherals:

- Blink a status LED every 500 ms.
- Sample a temperature sensor every second.
- Debounce multiple push buttons.
- Detect communication timeouts.
- Periodically transmit diagnostic data.
- Monitor sensor inactivity.
- Refresh a display.
- Trigger periodic maintenance tasks.

Each of these functions requires its own notion of time. If every timing requirement needed a dedicated hardware timer, the application would quickly exhaust the available timer peripherals.

Fortunately, this is **not** how embedded systems are designed.

The solution is **software timers**.

A software timer is **not** another hardware peripheral. It does **not** create additional timer hardware inside the microcontroller. Instead, software timers are logical timers implemented entirely in software.

Rather than assigning one hardware timer to every timing operation, a single hardware timer generates a periodic interrupt. Software then uses these periodic interrupts to maintain multiple independent timer objects.

```text
                One Hardware Timer
                       │
             Interrupt every 1 ms
                       │
                       ▼
         +---------------------------+
         | Software Timer Manager    |
         +---------------------------+
           │     │      │      │
           ▼     ▼      ▼      ▼
        Timer1 Timer2 Timer3 ... Timer100
```

In this design, the hardware timer acts as a **time base**. Every time it generates an interrupt, the software timer manager updates the state of all active software timers.

Each software timer maintains its own countdown value, expiration state, and configuration. Although all timers share the same hardware timer, they operate independently from the application's perspective.

This approach effectively multiplexes one physical timer into many logical timers.

The practical limit is no longer the number of hardware timer peripherals available on the microcontroller. Instead, it depends primarily on:

- Available RAM for storing timer objects
- CPU time required to update the timers
- The efficiency of the timer manager implementation

Consequently, an application can manage tens or even hundreds of software timers using a single hardware timer interrupt.

The obvious question is: **If software timers are implemented entirely in software, why do desktop applications rarely need to implement them?**

The answer lies in the services provided by operating systems, which is the topic of the next section.

---
## <font color='green'>3. How Software Timers Work</font>

A software timer cannot measure time on its own. It depends on a **hardware timer** to provide a regular time reference.

Typically, one hardware timer is configured to generate a periodic interrupt at a fixed interval, commonly every 1 ms, although other intervals such as 10 ms or 100 μs may also be used depending on the application's timing requirements.

```text
              Hardware Timer

      1 ms    1 ms    1 ms    1 ms
        │       │       │       │
        ▼       ▼       ▼       ▼
      +---+   +---+   +---+   +---+
      |IRQ|   |IRQ|   |IRQ|   |IRQ|
      +---+   +---+   +---+   +---+
```

Each interrupt represents the passage of a fixed amount of time, commonly referred to as a **tick**.

Whenever a tick occurs, the interrupt service routine (ISR) invokes the software timer manager. The timer manager then updates every active software timer.

```text
                One Hardware Timer
                       │
             Interrupt every 1 ms
                       │
                       ▼
         +---------------------------+
         | Software Timer Manager    |
         +---------------------------+
           │     │      │      │
           ▼     ▼      ▼      ▼
        Timer1 Timer2 Timer3 ... Timer100
```

Internally, each software timer maintains information such as:

- Whether the timer is active
- The remaining time before expiration
- Whether it is a one-shot or periodic timer
- The action to perform when it expires (if callbacks are used)

Suppose a timer is started with a duration of **500 ms**. If the system tick occurs every **1 ms**, the timer manager initializes its countdown value to **500**.

Every tick, the timer manager decrements the countdown.

```text
Tick      Remaining Time

Start     500
1         499
2         498
3         497
...
499       1
500       0  ← Timer expires
```

When the countdown reaches zero, the timer is considered **expired**. Depending on the implementation, the timer manager may:

- Set an expiration flag
- Invoke a callback function
- Restart the timer automatically (for periodic timers)

Notice that only **one** hardware timer generated all 500 interrupts. The remaining work was performed entirely in software.

This approach allows a single hardware timer to maintain many independent software timers simultaneously. Every active timer is updated during each tick, giving the illusion that each timer is operating independently.

As a result, the application is no longer constrained by the number of hardware timer peripherals. Instead, the number of software timers is determined primarily by available memory and the processing time required to update them.


---
## <font color='green'>4. Software Timers in Operating Systems</font>

The next question naturally follows: **If software timers are so useful, why don't desktop applications usually implement their own timer managers?**

Software timers are not unique to embedded systems. In fact, they are a fundamental service provided by virtually every modern operating system.

Suppose you are writing a desktop application on Linux. If your application needs to execute a task after one second or perform an operation every 100 ms, you simply use one of the operating system's timer APIs. The operating system takes care of creating, managing, and expiring the timer.

From the application's perspective, using a software timer is straightforward.

```text
Application
      │
      ▼
Timer API
```

However, much more happens behind the scenes.

When an application creates a timer, it is not communicating directly with the hardware timer peripheral. Instead, the request passes through several layers of the operating system.

```text
Application
      │
      ▼
Timer API
      │
      ▼
Operating System
      │
      ▼
Kernel Timer Manager
      │
      ▼
Hardware Timer
```

The operating system is responsible for:

- Maintaining a list of active timers
- Updating timers as time passes
- Detecting timer expiration
- Waking sleeping threads or tasks
- Executing callbacks or delivering timer events
- Managing the underlying hardware timer

As a result, application developers rarely need to think about how timers are actually implemented. They simply request a timer, and the operating system handles the rest.

This abstraction offers two important advantages.

First, applications can create many independent timers without worrying about the limited number of hardware timer peripherals available on the system.

Second, the timer implementation is shared by every application running on the system. Instead of each application implementing its own timer manager, the operating system provides a common, well-tested timing service.

For desktop and server software, this architecture is taken for granted because the operating system is always present.

Embedded systems, however, are often very different. Many microcontroller-based applications run **without an operating system**, meaning none of these timer management services are available.

In such systems, if the application requires multiple software timers, someone has to implement the timer manager.

That "someone" is usually the embedded software developer.

---
## <font color='green'>5. Software Timers in Bare-Metal Embedded Systems</font>

Unlike desktop and server computers, many embedded systems operate without an operating system. Such systems are commonly referred to as **bare-metal systems** because the application executes directly on the hardware without an intermediate software layer.

In a bare-metal application, there is no kernel, no scheduler, and no operating system services. The firmware is responsible for interacting directly with the microcontroller's peripherals.

```text
Application
      │
      ▼
Hardware
```

This simple architecture is one of the reasons embedded systems are efficient and predictable. However, it also means that services commonly provided by an operating system simply do not exist.

One such missing service is **software timer management**.

Suppose an application requires:

- A status LED to blink every 500 ms
- A sensor to be sampled every second
- A communication timeout of 100 ms
- A periodic diagnostic task every five seconds

Unlike Linux or an RTOS, there is no timer API that can be called to create these timers. There is no kernel maintaining timer queues or notifying the application when a timer expires.

Someone must implement these capabilities.

The typical solution is to dedicate one hardware timer to generate a periodic system tick and build a **software timer manager** on top of it.

```text
Bare-Metal Firmware

Application
      │
      ▼
Software Timer Manager
      │
      ▼
Hardware Timer
```

The software timer manager becomes an essential part of the firmware. It keeps track of all active software timers, updates them on every system tick, and determines when each timer has expired.

From the application's perspective, this timer manager provides functionality similar to that offered by an operating system. The difference is that **you** are responsible for designing and implementing it.

Fortunately, the underlying idea is straightforward. Once a periodic tick is available, the timer manager simply maintains a collection of software timers and updates their state every time the hardware timer interrupt occurs.


---
## <font color='green'>6. Advantages and Disadvantages</font>

The remainder of this article focuses on building such a timer manager in C. Starting with a simple software timer, we will gradually extend the design to efficiently manage multiple independent timers suitable for bare-metal embedded applications.

Like any engineering solution, software timers offer significant benefits, but they also introduce certain trade-offs. Understanding these advantages and limitations helps in deciding when software timers are appropriate and how they should be designed.

### Advantages

#### Efficient Use of Hardware

The most significant advantage of software timers is that they allow a single hardware timer to support many independent timing operations.

Instead of consuming a dedicated hardware timer for every timeout or periodic task, one timer peripheral provides the time base for the entire application.

#### Highly Scalable

A microcontroller may provide only four hardware timers, but a software timer manager can maintain dozens or even hundreds of software timers.

The practical limit depends primarily on:

- Available RAM
- CPU processing time
- Efficiency of the timer manager

rather than the number of timer peripherals available on the microcontroller.

#### Flexible

Software timers can easily support different operating modes, such as:

- One-shot timers
- Periodic timers
- Restartable timers
- Infinite repeating timers

New features can often be added by modifying software rather than requiring additional hardware.

#### Portable

Since software timers are implemented entirely in C, the timer manager can usually be reused across different microcontrollers.

Only the hardware timer initialization and interrupt configuration are typically device-specific.

This makes software timer libraries highly portable between projects.

---

### Disadvantages

#### CPU Overhead

Unlike hardware timers, software timers require processor time.

On every system tick, the timer manager must update each active timer.

As the number of software timers increases, so does the amount of processing performed during every tick.

#### Limited Resolution

A software timer cannot provide finer resolution than the system tick.

For example, if the hardware timer generates an interrupt every 1 ms, software timers can generally expire only at 1 ms intervals.

If higher timing precision is required, the tick interval must be reduced, increasing interrupt frequency and CPU overhead.

#### Timing Jitter

Software timers do not always expire at the exact instant requested.

Interrupt latency, interrupt masking, higher-priority ISRs, and application processing can introduce small variations in the actual expiration time.

For most embedded applications, this jitter is negligible. However, applications requiring extremely precise timing, such as high-speed motor control or digital communication protocols, often rely directly on hardware timers instead.

#### Additional Software Complexity

A software timer manager introduces another subsystem into the firmware.

The developer must design and maintain:

- Timer data structures
- Timer update logic
- Start and stop operations
- Expiration handling
- Periodic timer management

Although these components are relatively straightforward, they still increase the complexity of the application.

---

Despite these limitations, software timers have become the standard solution for implementing multiple independent timing operations in embedded systems.

They provide an excellent balance between flexibility, scalability, and efficient hardware utilization, making them one of the most widely used building blocks in embedded software.

---
## <font color='green'>7. Common Use Cases</font>

Software timers are one of the most frequently used building blocks in embedded systems. Any operation that must occur after a specified delay or at regular intervals is a candidate for implementation using a software timer.

The following are some common applications.

### LED Blinking

Blinking status LEDs is perhaps the simplest and most recognizable use of software timers.

Instead of blocking the CPU with delay loops, a periodic software timer toggles the LED at the required interval while allowing the processor to perform other tasks.

```text
Every 500 ms

Tick ─────────► Timer Expires ─────────► Toggle LED
```

---

### Button Debouncing

Mechanical push buttons do not produce clean transitions. When pressed or released, the contacts bounce for several milliseconds, generating multiple unwanted transitions.

A software timer is commonly started when a button state changes. The button is considered valid only after the debounce interval has elapsed.

```text
Button Press
      │
      ▼
Start 20 ms Timer
      │
      ▼
Timer Expires
      │
      ▼
Validate Button State
```

---

### Communication Timeouts

Many communication protocols require a response within a specified time.

For example, after transmitting a command over UART, SPI, I²C, or CAN, the firmware starts a timeout timer.

If no response is received before the timer expires, the communication is considered unsuccessful, allowing the application to retry the operation or report an error.

---

### Periodic Sensor Sampling

Many sensors do not require continuous sampling.

Instead, they are sampled at fixed intervals such as:

- Every 10 ms
- Every 100 ms
- Every second

A periodic software timer schedules these measurements without blocking the processor.

---

### Display Updates

Graphical displays, LCDs, and OLED modules often require periodic refreshing.

Rather than continuously updating the display inside the main loop, a periodic software timer determines when the next refresh should occur.

---

### Periodic Diagnostics

Embedded applications frequently perform background maintenance tasks such as:

- Checking battery voltage
- Monitoring system health
- Measuring processor temperature
- Logging diagnostic information
- Updating runtime statistics

These activities typically execute at regular intervals using periodic software timers.

---

### Watchdog Servicing

Many systems periodically refresh (or *feed*) the watchdog timer to indicate that the application is operating correctly.

A periodic software timer can schedule this operation at the required interval, ensuring the watchdog is serviced consistently without scattering timing logic throughout the application.

---

### State Machine Timeouts

Finite state machines often require a state transition after a specified period.

For example:

- Exit an initialization state after five seconds.
- Leave an error state after a timeout.
- Retry communication every second.

Instead of manually checking elapsed time, each state can simply start a software timer and respond when it expires.

---

These examples illustrate why software timers are so widely used in embedded systems. Rather than writing custom timing logic for every feature, developers create a single timer manager that provides a common timing service for the entire application.

The next section begins building such a timer manager by implementing a simple software timer in C.

---
## <font color='green'>8. Building a Simple Software Timer</font>

Having understood why software timers exist and where they are used, let's build a simple software timer in C.

Our objective is modest: create a timer that can be started with a specified duration, updated periodically by the system tick, and indicate when it has expired.

To keep the design simple, this first implementation manages **only one timer**. In the next section, we will extend the design to support multiple timers through a timer manager.

### Designing the Timer

A software timer needs to store only a small amount of information:

- Whether the timer is active
- How much time remains before expiration
- Whether the timer has expired

One possible implementation is shown below.

```c
typedef struct
{
    uint32_t remaining;
    bool     active;
    bool     expired;
} software_timer_t;
```

Each member has a specific purpose:

- **remaining** stores the countdown value.
- **active** indicates whether the timer is currently running.
- **expired** indicates that the timer has reached zero.

---

### Starting the Timer

Starting a timer simply initializes its countdown value and marks it as active.

```c
void timer_start(software_timer_t *timer, uint32_t duration)
{
    timer->remaining = duration;
    timer->active    = true;
    timer->expired   = false;
}
```

For example,

```c
timer_start(&led_timer, 500);
```

starts a timer that expires after **500 system ticks**.

If the system tick period is **1 ms**, the timer expires after **500 ms**.

---

### Updating the Timer

The timer itself does nothing automatically.

Instead, it must be updated periodically by the software timer manager (or directly by the system tick ISR in this simple example).

```c
void timer_update(software_timer_t *timer)
{
    if (!timer->active)
        return;

    if (timer->remaining > 0)
    {
        timer->remaining--;
    }

    if (timer->remaining == 0)
    {
        timer->active  = false;
        timer->expired = true;
    }
}
```

Every call decreases the remaining time by one tick.

Suppose the timer was started with a duration of five ticks.

```text
Tick     Remaining

Start       5
1           4
2           3
3           2
4           1
5           0  ← Expired
```

Once the countdown reaches zero, the timer stops and sets the expiration flag.

---

### Updating from the System Tick

The hardware timer interrupt should invoke the update function once every tick.

```c
void SysTick_Handler(void)
{
    timer_update(&led_timer);
}
```

Every interrupt advances the timer by one tick.

Notice that the interrupt routine does very little work. It simply updates the timer state and returns immediately.

---

### Detecting Timer Expiration

The main application can periodically check whether the timer has expired.

```c
if (led_timer.expired)
{
    led_timer.expired = false;

    toggle_led();

    timer_start(&led_timer, 500);
}
```

This creates a repeating 500 ms LED blink by restarting the timer after each expiration.

---

### Limitations of This Design

Although this implementation demonstrates the basic concept, it has an obvious limitation. It manages only **one** software timer.

A real embedded application typically requires many independent timers operating simultaneously.

Creating separate update functions for every timer would quickly become difficult to maintain.

A better approach is to maintain a collection of timers and update them all from a single software timer manager.


---
## <font color='green'>9. Managing Multiple Software Timers</font>

The software timer developed in the previous section demonstrates the basic concept, but it is not practical for real-world applications.

An embedded system rarely requires just one timer. It may need independent timers for LEDs, communication timeouts, sensor sampling, display updates, button debouncing, and many other tasks.

Creating a separate update function for every timer would result in duplicated code and quickly become difficult to maintain.

A more scalable solution is to introduce a **software timer manager**.

Instead of updating a single timer, the timer manager maintains a collection of software timers and updates all active timers whenever the system tick occurs.

```text
             Hardware Timer
                    │
          Interrupt every 1 ms
                    │
                    ▼
        +-------------------------+
        |  Software Timer Manager |
        +-------------------------+
          │     │      │      │
          ▼     ▼      ▼      ▼
      Timer1 Timer2 Timer3 Timer4
```

The timer manager becomes the central component responsible for all timing operations in the application.

---

### Storing Multiple Timers

One simple approach is to store all timers in an array.

```c
#define MAX_TIMERS 10

software_timer_t timers[MAX_TIMERS];
```

Each element represents an independent software timer.

```text
+-------+-------+-------+-------+-------+
|Timer 0|Timer 1|Timer 2|Timer 3|  ...  |
+-------+-------+-------+-------+-------+
```

The array size determines the maximum number of timers that can exist simultaneously.

---

### Updating All Timers

Instead of calling `timer_update()` for a single timer, the timer manager simply iterates through the array.

```c
void timer_manager_update(void)
{
    for (int i = 0; i < MAX_TIMERS; i++)
    {
        timer_update(&timers[i]);
    }
}
```

Now the system tick interrupt updates every active timer.

```c
void SysTick_Handler(void)
{
    timer_manager_update();
}
```

This design is simple, easy to understand, and works well for many embedded applications.

---

### One-Shot Timers

A **one-shot timer** expires only once.

After reaching zero, it stops automatically.

```text
Start

5 → 4 → 3 → 2 → 1 → 0
                     │
                     ▼
                 Stop Timer
```

One-shot timers are commonly used for:

- Communication timeouts
- Startup delays
- Button debouncing
- Delayed operations

---

### Periodic Timers

A **periodic timer** automatically restarts after expiration.

```text
5 → 4 → 3 → 2 → 1 → 0
                     │
                     ▼
                Reload = 5
                     │
                     ▼
5 → 4 → 3 → 2 → 1 → 0
```

Periodic timers are useful for:

- LED blinking
- Sensor sampling
- Display refresh
- Background maintenance
- Periodic diagnostics

Supporting periodic timers typically requires storing an additional **reload value** so the timer can automatically restart after reaching zero.

---

### Polling vs. Callbacks

Once a timer expires, the application must be notified.

Two approaches are commonly used.

#### Polling

The application periodically checks whether a timer has expired.

```c
if (timer_expired(&led_timer))
{
    toggle_led();
}
```

This approach is simple and predictable, making it popular in bare-metal applications.

---

#### Callbacks

Instead of polling, the timer manager can invoke a user-defined function when the timer expires.

```text
Timer Expires
      │
      ▼
Invoke Callback
      │
      ▼
Application Function
```

For example,

```c
void led_timeout(void)
{
    toggle_led();
}
```

The timer manager automatically calls `led_timeout()` when the timer expires.

Callbacks eliminate explicit polling and often produce cleaner application code. However, they also increase the complexity of the timer manager and require careful consideration if callbacks execute within an interrupt context.

---

The timer manager presented here is intentionally simple, but it demonstrates the fundamental architecture used in many embedded systems.

The next section discusses important design decisions that influence the performance, accuracy, and scalability of a software timer manager.


---
## <font color='green'>10. Design Considerations</font>

The software timer manager presented in the previous section is sufficient for many small embedded applications. However, as firmware grows in complexity, several design decisions become increasingly important.

A well-designed timer manager should be accurate, efficient, scalable, and easy to maintain.

The following are some of the most important considerations.

---

### Choosing the Tick Period

The first design decision is selecting the system tick interval.

Common choices include:

- 100 μs
- 1 ms
- 10 ms

The tick period determines both the timer resolution and the interrupt frequency.

For example, a **1 ms** tick generates:

```text
1000 interrupts per second
```

while a **10 ms** tick generates:

```text
100 interrupts per second
```

A shorter tick provides finer timing resolution but increases CPU overhead because interrupts occur more frequently.

Conversely, a longer tick reduces processor load but also decreases timer accuracy.

Selecting an appropriate tick interval is therefore a balance between precision and efficiency.

---

### Timer Resolution

A software timer cannot expire between system ticks.

Suppose the tick period is **1 ms**.

A timer can expire after:

```text
1 ms
2 ms
3 ms
...
```

but not after:

```text
1.5 ms
2.3 ms
2.75 ms
```

Applications requiring sub-millisecond precision generally rely on dedicated hardware timers instead of software timers.

---

### Timer Data Type

The countdown value is typically stored in an unsigned integer.

For example:

```c
uint16_t
```

or

```c
uint32_t
```

The choice determines the maximum timeout that can be represented.

For a **1 ms** system tick:

| Data Type | Maximum Timeout |
|-----------|----------------:|
| `uint16_t` | ≈ 65 seconds |
| `uint32_t` | ≈ 49.7 days |

Long-running applications often prefer `uint32_t` to accommodate extended delays without additional logic.

---

### Polling or Callbacks

Earlier, we discussed two methods for handling timer expiration.

**Polling**

- Simpler implementation
- Easy to debug
- Application decides when to process events

**Callbacks**

- Cleaner application code
- Immediate notification
- More flexible
- Increased implementation complexity

Neither approach is universally better. The choice depends on the application's architecture and responsiveness requirements.

---

### Interrupt Context

The system tick interrupt should complete as quickly as possible.

A common design is:

```text
Hardware Timer Interrupt
           │
           ▼
Update Timer Counters
           │
           ▼
Return Immediately
```

Avoid performing lengthy processing, communication, or complex calculations inside the interrupt service routine.

Instead, allow the ISR to update timer state and let the main application process expired timers.

Keeping ISRs short improves system responsiveness and reduces interrupt latency.

---

### Memory Usage

Each software timer occupies RAM.

For example, if a timer structure consumes **16 bytes**, then:

```text
10 timers   → 160 bytes
50 timers   → 800 bytes
100 timers  → 1600 bytes
```

While this is acceptable for many modern microcontrollers, memory usage should always be considered on devices with limited RAM.

---

### Scalability

The simple timer manager presented earlier updates every timer during every system tick.

```text
for each timer
    update timer
```

This approach is easy to implement and performs well for small and medium-sized applications.

As the number of timers grows, more sophisticated data structures. Such as linked lists, priority queues, or timer wheels can reduce the processing required on each tick. These techniques are commonly used in real-time operating systems and high-performance embedded software but are generally unnecessary for most bare-metal applications.

---

There is no single "best" software timer implementation.

The most appropriate design depends on factors such as the number of timers, required timing accuracy, available memory, processor performance, and overall application complexity.

For many embedded systems, a simple timer manager built around a periodic hardware timer interrupt provides an effective balance between simplicity, efficiency, and scalability.


---
## <font color='green'>11. Summary</font>

Hardware timers are among the most valuable peripherals in a microcontroller. They provide precise timing, generate interrupts, produce PWM signals, measure external events, and perform many other timing-related functions. However, the number of hardware timers is limited, making them a scarce resource in many embedded applications.

As embedded software grows in complexity, the demand for independent timing operations often exceeds the number of available hardware timers. Rather than dedicating one hardware timer to every timeout or periodic task, developers use **software timers** to multiplex a single hardware timer into many logical timers.

A software timer manager uses periodic interrupts generated by one hardware timer as its time base. On every system tick, it updates the state of all active software timers, detects timer expiration, and notifies the application when required. This approach allows dozens or even hundreds of independent timers to coexist while using only a single hardware timer peripheral.

On desktop and server systems, this functionality is usually provided by the operating system. Applications simply create timers through an API, leaving the operating system to manage timer queues, expiration, and callback execution.

Bare-metal embedded systems are different. Without an operating system, there is no built-in timer manager or timer service. If an application requires multiple independent timers, the firmware itself must implement this functionality.

In this article, we explored:

- The limitations of hardware timers
- Why software timers are necessary
- How software timers are driven by a periodic hardware timer interrupt
- How operating systems provide timer management services
- Why bare-metal systems require their own timer manager
- How to implement a simple software timer in C
- How to extend it into a scalable software timer manager
- The key design considerations involved in building an efficient timer subsystem

Software timers are a fundamental component of modern embedded software. Once implemented, they become a reusable infrastructure that simplifies application development by providing a consistent and scalable mechanism for managing time-based operations.

Although the implementation presented in this article is intentionally simple, the same principles form the foundation of timer managers used in embedded frameworks, real-time operating systems, and commercial firmware libraries.










---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
