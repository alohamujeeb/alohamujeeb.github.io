---
hide:
  - navigation
  
tags:
  - Finite State Machine
  
  
---
# Finite State Machines in C

*This article is intended for intermediate and advanced C programmers. It introduces the finite state machine (FSM) programming model, explains how states, events, and transitions are represented in C, and demonstrates common implementation techniques used to build predictable and maintainable applications, particularly in embedded systems.*

---
## <font color='green'>1. What Is a Finite State Machine?</font>

A **Finite State Machine (FSM)** is a programming model used to represent systems whose behavior depends on their current state. At any given time, the system is in exactly one state, and it changes to another state only when a specific event occurs.

For example, consider a simple automatic door.

```text
           Button Press
      Closed -----------> Opening
         ▲                   │
         │                   │ Door Opened
Door Closed                  ▼
         │                Open
         │                   │
         └------ Closing <---┘
               Timer Expired
```

At any moment, the door is in one of four states:

- Closed
- Opening
- Open
- Closing

Events such as pressing a button, the door fully opening, or a timer expiring cause the system to transition from one state to another.

An FSM consists of three fundamental components:

- **State** – The current operating mode of the system.
- **Event** – Something that occurs and may trigger a state change.
- **Transition** – The movement from one state to another in response to an event.

These components interact as follows:

```text
Current State
      │
      ▼
Receive Event
      │
      ▼
Transition
      │
      ▼
Next State
```

Unlike a sequence of unrelated `if` or `switch` statements, an FSM organizes behavior around the current state of the system. The same event can therefore produce different behavior depending on the active state.

For example, pressing the door button while the door is closed starts the opening process.

```text
State : Closed
Event : Button Press

↓

Next State : Opening
```

However, pressing the same button while the door is already open may instead start the closing process.

```text
State : Open
Event : Button Press

↓

Next State : Closing
```

The event is identical, but the outcome differs because the current state is different.

Finite state machines are widely used in embedded systems because many devices naturally operate as a series of well-defined states. Typical examples include:

- Traffic light controllers
- Elevators
- Washing machines
- Vending machines
- Communication protocols
- User interface menus

By explicitly modeling states and transitions, FSMs make program behavior easier to understand, implement, test, and maintain.

---
## <font color='green'>2. States, Events, and Transitions</font>

Every finite state machine is built from three fundamental components: **states**, **events**, and **transitions**. Together, they define how the system behaves as it responds to changing conditions.

### States

A **state** represents the current operating mode of the system. At any point in time, an FSM is in exactly one state.

For example, an automatic door may have the following states:

```text
Closed

Opening

Open

Closing
```

The active state determines how the system responds to incoming events.

---

### Events

An **event** is something that occurs while the system is operating. Events may originate from user input, hardware, timers, sensors, or communication interfaces.

Typical events include:

- Button Pressed
- Timer Expired
- Sensor Triggered
- Data Received
- Error Detected

An event simply informs the FSM that something has happened. Whether it causes a change in behavior depends on the current state.

---

### Transitions

A **transition** is the movement from one state to another in response to an event.

For example, if the door is currently closed, pressing the button causes it to begin opening.

```text
Current State      Event              Next State
------------------------------------------------
Closed        +  Button Pressed  ->   Opening
```

After the transition completes, **Opening** becomes the current state.

Likewise, once the door is fully open, a timer may cause it to begin closing.

```text
Current State      Event              Next State
------------------------------------------------
Open          +  Timer Expired   ->   Closing
```

---

### The Current State Matters

One of the defining characteristics of an FSM is that the same event can produce different results depending on the current state.

For example, consider the event **Button Pressed**.

```text
State = Closed

Button Pressed

↓

Next State = Opening
```

Now consider exactly the same event while the door is already open.

```text
State = Open

Button Pressed

↓

Next State = Closing
```

The event is identical, but the resulting transition is different because the FSM is in a different state.

Some events may not cause any transition at all.

```text
State = Closed

Event = Door Closed

↓

Remain in Closed
```

Since the door is already closed, the event has no effect.

---

The relationship between states, events, and transitions can be summarized as follows.

```text
                +---------------+
                | Current State |
                +---------------+
                        │
                        ▼
                  Receive Event
                        │
                        ▼
          Is a Transition Defined?
                 │            │
              Yes│            │No
                 ▼            ▼
          Change State   Stay in State
```

Every finite state machine follows this same principle. It continuously waits for events, determines whether the current state defines a valid transition for that event, and either changes state or remains where it is.

---
## <font color='green'>3. Event-Driven State Machines</font>

In many embedded systems, events do not occur in a fixed sequence. Instead, they are generated by external sources such as interrupts, timers, communication peripherals, or user input. An **event-driven state machine** waits for these events and processes them as they occur.

A typical embedded application follows this pattern.

```text
+------------+
| Initialize |
+------------+
       │
       ▼
+----------------------+
| Wait for an Event    |
+----------------------+
       │
       ▼
+----------------------+
| Process the Event    |
+----------------------+
       │
       ▼
+----------------------+
| Update the State     |
+----------------------+
       │
       └───────────────┐
                       ▼
             Wait for Next Event
```

Rather than continuously checking every possible condition, the application reacts only when an event is available.

---

### Event Sources

Events can originate from many parts of an embedded system.

For example:

- A button is pressed.
- A timer expires.
- A UART receives a character.
- An ADC conversion completes.
- A sensor detects an object.

Each of these occurrences generates an event that is delivered to the state machine.

```text
Button
        │
Timer   │
        │
UART    │
        ▼
    Event Queue
         │
         ▼
 State Machine
```

Regardless of their source, all events are processed in the same way.

---

### The Main Event Loop

Many embedded applications spend most of their time waiting for events.

```c
while (1)
{
    Event event = getEvent();

    processEvent(event);
}
```

The function `getEvent()` retrieves the next available event, while `processEvent()` updates the current state based on that event.

This separates **event detection** from **state processing**, making the program easier to understand and maintain.

---

### Interrupts and State Machines

In embedded systems, interrupts often detect events, but they typically do **not** implement the state machine.

Instead, the interrupt records that an event occurred.

```text
Interrupt

      │

Detect Event

      │

Queue Event

      │

Return
```

The main application loop later removes the event from the queue and passes it to the FSM.

```text
Interrupt

      │
      ▼
Queue Event

      │
      ▼
Main Loop

      │
      ▼
processEvent()
```

Keeping interrupt service routines short improves responsiveness and avoids performing complex processing at interrupt level.

---

An event-driven architecture naturally complements finite state machines. Interrupts, timers, and peripherals generate events, while the main application loop processes those events and updates the current state. This separation results in firmware that is modular, predictable, and easier to maintain.


---
## <font color='green'>4. Implementing an FSM in C</font>

Once the states and events have been identified, implementing a finite state machine in C is relatively straightforward. The most common approach is to represent states and events using enumerations and use a `switch` statement to determine how each event is handled.

### Defining the States

The possible states are typically represented using an enumeration.

```c
typedef enum
{
    STATE_CLOSED,
    STATE_OPENING,
    STATE_OPEN,
    STATE_CLOSING
} State;
```

A variable stores the current state of the system.

```c
State currentState = STATE_CLOSED;
```

At any point during execution, `currentState` identifies the system's operating mode.

---

### Defining the Events

Events are also commonly represented using an enumeration.

```c
typedef enum
{
    EVENT_BUTTON_PRESSED,
    EVENT_DOOR_OPENED,
    EVENT_TIMER_EXPIRED,
    EVENT_DOOR_CLOSED
} Event;
```

Whenever something happens, the corresponding event is passed to the state machine.

---

### Processing Events

A typical implementation uses a function that accepts an event and updates the current state.

```c
void processEvent(Event event)
{
    switch (currentState)
    {
        case STATE_CLOSED:

            if (event == EVENT_BUTTON_PRESSED)
            {
                currentState = STATE_OPENING;
            }

            break;

        case STATE_OPENING:

            if (event == EVENT_DOOR_OPENED)
            {
                currentState = STATE_OPEN;
            }

            break;

        case STATE_OPEN:

            if (event == EVENT_TIMER_EXPIRED)
            {
                currentState = STATE_CLOSING;
            }

            break;

        case STATE_CLOSING:

            if (event == EVENT_DOOR_CLOSED)
            {
                currentState = STATE_CLOSED;
            }

            break;
    }
}
```

The `switch` statement selects the current state, while the `if` statements determine whether the received event causes a transition.

---

### Example Execution

Suppose the state machine begins in the **Closed** state.

```text
Current State = Closed
```

The following events occur.

```text
Button Pressed

↓

Door Opened

↓

Timer Expired

↓

Door Closed
```

The state machine processes each event in sequence.

```text
STATE_CLOSED
      │
      │ EVENT_BUTTON_PRESSED
      ▼
STATE_OPENING
      │
      │ EVENT_DOOR_OPENED
      ▼
STATE_OPEN
      │
      │ EVENT_TIMER_EXPIRED
      ▼
STATE_CLOSING
      │
      │ EVENT_DOOR_CLOSED
      ▼
STATE_CLOSED
```

Each event updates the current state, and that new state determines how the next event will be processed.

---

Representing states and events with enumerations, combined with a `switch` statement for state processing, is one of the simplest and most widely used techniques for implementing finite state machines in C. It is easy to understand, easy to debug, and suitable for many embedded applications.

The next section introduces **table-driven finite state machines**, an alternative implementation that replaces large `switch` statements with transition tables.

---
## <font color='green'>5. Table-Driven Finite State Machines</font>

As a state machine grows, the number of states and events increases, and a large `switch` statement can become difficult to read and maintain. An alternative approach is to represent state transitions as a table.

Instead of embedding the transition logic directly in code, each transition is stored as a table entry.

### Transition Table

Consider the automatic door example.

```text
Current State      Event                  Next State
----------------------------------------------------
Closed             Button Pressed         Opening
Opening            Door Opened            Open
Open               Timer Expired          Closing
Closing            Door Closed            Closed
```

Each row defines a valid transition.

---

### Representing a Transition

A transition can be represented using a structure.

```c
typedef struct
{
    State currentState;
    Event event;
    State nextState;
} Transition;
```

The complete state machine is then described as an array.

```c
Transition transitions[] =
{
    { STATE_CLOSED,  EVENT_BUTTON_PRESSED, STATE_OPENING },
    { STATE_OPENING, EVENT_DOOR_OPENED,    STATE_OPEN     },
    { STATE_OPEN,    EVENT_TIMER_EXPIRED,  STATE_CLOSING  },
    { STATE_CLOSING, EVENT_DOOR_CLOSED,    STATE_CLOSED   }
};
```

Rather than writing a separate `case` for every state, the application searches the table for a matching state and event.

---

### Processing an Event

When an event occurs, the FSM searches the transition table.

```text
Current State = Open

Event = Timer Expired

            │
            ▼

Search Transition Table

            │
            ▼

Open + Timer Expired

            │
            ▼

Next State = Closing
```

If no matching entry exists, the current state remains unchanged.

---

### Advantages

A table-driven implementation separates the **definition** of the state machine from the code that executes it.

```text
Transition Table

        │

        ▼

FSM Engine

        │

        ▼

Current State
```

This offers several advantages:

- Adding a new transition often requires only adding another table entry.
- The state machine is easier to visualize.
- Transition logic is centralized.
- Large state machines become easier to maintain.

---

### Choosing an Implementation

Both implementation techniques are widely used.

A `switch` statement is often preferred for:

- Small state machines.
- Performance-critical code.
- State-specific processing.

A transition table is often preferred for:

- Large state machines.
- Frequently changing transition rules.
- Applications where the FSM definition should be easy to modify.

The choice depends on the complexity of the application rather than on correctness.

The next section discusses the advantages and limitations of using finite state machines in C.

---
## <font color='green'>6. Advantages and Limitations</font>

Finite state machines are widely used in embedded software because they provide a structured way to model system behavior. By explicitly defining states and transitions, they simplify many control-oriented applications. However, like any design technique, they also have limitations.

### Advantages

#### Predictable Behavior

An FSM can only be in one state at a time, and every state transition is explicitly defined.

```text
Current State
      │
      ▼
Receive Event
      │
      ▼
Defined Transition
      │
      ▼
Next State
```

This makes the behavior of the system deterministic and easy to reason about.

---

#### Easy to Debug

Because the current state is always known, debugging often becomes much simpler.

For example, logging state transitions can reveal exactly how the system reached its current condition.

```text
Closed
   │
   ▼
Opening
   │
   ▼
Open
```

Following the sequence of transitions is usually easier than tracing deeply nested conditional statements.

---

#### Modular Design

An FSM separates the application's behavior into well-defined states.

Instead of scattering conditional logic throughout the program, state-specific behavior is organized into a single state machine.

This improves readability and makes the code easier to maintain.

---

#### Well Suited for Embedded Systems

Many embedded applications naturally operate as a collection of states driven by external events.

Examples include:

- Communication protocols
- User interfaces
- Motor controllers
- Traffic light controllers
- Industrial automation

FSMs provide a natural way to model these systems.

### Limitations

#### State Explosion

As a system becomes more complex, the number of states and transitions can increase rapidly.

```text
Few States

      │

Simple FSM

      ▼

Many States

      │

Many Transitions

      ▼

Complex FSM
```

Large state machines can become difficult to visualize and maintain.

---

#### Complex State Logic

Some applications require significant processing within each state.

As the amount of state-specific logic grows, the state machine itself can become harder to understand.

---

#### Limited Support for Concurrent Behavior

A basic finite state machine represents only one active state at a time.

Applications that perform multiple independent activities simultaneously may require multiple cooperating state machines or a more advanced design.

---

Finite state machines provide a simple and effective way to model event-driven behavior. They produce predictable, maintainable code for many embedded applications, but very large or highly concurrent systems may require additional design techniques to manage their complexity.

The next section summarizes the key concepts discussed in this article.

---
## <font color='green'>7. Summary</font>

A **Finite State Machine (FSM)** is a programming model used to represent systems whose behavior depends on their current operating state. Instead of relying on complex conditional logic, an FSM organizes behavior into well-defined states and explicitly specifies how events cause transitions between those states.

Throughout this article, the following key concepts were introduced:

- An FSM is always in exactly one state.
- Events trigger state transitions.
- The same event can produce different behavior depending on the current state.
- States, events, and transitions form the core of every finite state machine.
- A `switch` statement is a common technique for implementing FSMs in C.
- Transition tables provide an alternative implementation that scales well for larger state machines.

The overall operation of an FSM can be summarized as follows.

```text
Current State
      │
      ▼
Receive Event
      │
      ▼
Is Transition Defined?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Change   Remain in
 State     Current State
 │
 ▼
Wait for Next Event
```

Finite state machines are particularly valuable in embedded systems because many real-world devices naturally operate as a sequence of discrete states. By explicitly modeling these states and their transitions, FSMs produce software that is easier to understand, debug, test, and maintain.

Although very large systems may require multiple cooperating state machines or more advanced architectural techniques, the FSM remains one of the most widely used design patterns for implementing predictable, event-driven behavior in C.






---
## **Relevant Links**

[C/C++ Material on this website](index.md)

(such as memory managment, pointers, embedded C programming etc.)
