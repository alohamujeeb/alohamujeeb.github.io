---
hide:
    - navigation
  
tags:
    - TCP Programming
    - Byte Stream vs. Message in TCP
    - Websocket
    
---

# <font color='tomato'>TCP is Reliable. TCP is Not Message-Oriented</font>
*Concepts, architectures, and practical considerations for computing and content delivery at the edge.*


---
## <font color='green'>1. What Does “Reliable” Actually Mean? </font>

When we say **TCP is reliable**, it doesn't mean:

> “Whatever message I send will arrive exactly as I sent it.”

TCP provides reliability at the **byte-stream level**.

It ensures that data is:

- **Delivered**: lost data is retransmitted.
- **Ordered**: bytes are delivered to the application in the correct order.
- **Not duplicated**: duplicate data is handled by TCP before it reaches the application.

For example, if an application sends:

```text
HELLO
```

TCP ensures that the receiver sees the same sequence of bytes:

```text
HELLO
```

But there is an important detail:

**TCP does not know that `HELLO` is a message.**

To TCP, it is simply:

```text
H   E   L   L   O
```

TCP sees a **stream of bytes**, not a collection of messages.



---
## <font color='green'>2. TCP Is a Byte Stream, Not a Message Stream</font>

This is one of the most important things to understand when programming with TCP.

Suppose the application sends two messages:

```text
HELLO
WORLD
```

It is tempting to think TCP will preserve them as two separate messages:

```text
HELLO
WORLD
```

But TCP doesn't work that way.

TCP combines everything into a continuous stream of bytes:

```text
H E L L O W O R L D
```

There is no concept of:

```text
Message 1 = HELLO
Message 2 = WORLD
```

as far as TCP is concerned.

The receiving application simply reads bytes from the stream.

It might receive:

```text
HEL
```

followed by:

```text
LOWORLD
```

Or:

```text
HELLOW
```

followed by:

```text
ORLD
```

Or even the entire:

```text
HELLOWORLD
```

All of these are valid from TCP's perspective.

**TCP guarantees the order of the bytes. It does not preserve the boundaries between the data writes made by the application.**



---
## <font color='green'>3. The `send()` / `recv()` Surprise</font>

This is where the difference between a **byte stream** and a **message stream** becomes important.

Suppose the sender does this:

```text
send("HELLO")
send("WORLD")
```

A common assumption is that the receiver will do:

```text
recv() -> "HELLO"
recv() -> "WORLD"
```

TCP does not guarantee that.

The receiver could get:

```text
recv() -> "HEL"
recv() -> "LOW"
recv() -> "WORLD"
```

Or:

```text
recv() -> "HELLOWORLD"
```

Or:

```text
recv() -> "HELLOW"
recv() -> "ORLD"
```

All of these are perfectly valid.

The reason is simple:

**`send()` and `recv()` operate on a byte stream, not on application messages.**

TCP is responsible for delivering the bytes reliably and in order.

It is not responsible for preserving how those bytes were grouped by the sender.

So this assumption is wrong:

```text
send()  <->  recv()
message <-> message
```

The correct mental model is:

```text
Sender                          Receiver

send()                          recv()
   |                               |
   v                               v
+---------------------------------------+
|          TCP byte stream              |
+---------------------------------------+
```

If our application needs messages, **we need a way to define where one message ends and the next begins.**



---
## <font color='green'>4. So How Does the Receiver Know Where a Message Ends?</font>

If TCP doesn't preserve message boundaries, the receiver needs some way to figure out:

> **“Where does this message end?”**

The answer is: **the application protocol must define it.**

For example, suppose we want to send:

```text
HELLO
WORLD
```

We could define a simple rule:

> Every message ends with a newline.

Now the stream could look like:

```text
HELLO\nWORLD\n
```

The receiver reads bytes until it finds `\n`.

Or we could define another rule:

> The first 4 bytes contain the length of the message.

For example:

```text
0005HELLO
0005WORLD
```

Now the receiver knows exactly how many bytes belong to each message.

The important point is that **TCP itself doesn't define these boundaries**; Our application protocol does.

This is called **message framing**.

```text
TCP
    ↓
Reliable byte stream

Application protocol
    ↓
Message boundaries
```

TCP gives us the stream. **Our protocol decides how that stream is divided into messages.**


---
## <font color='green'>5. Message Framing: How Applications Solve It</font>

Once we understand that TCP gives us only a byte stream, the next question is:

> **How do we turn that stream back into messages?**

The application needs a **framing mechanism**.

There are several common approaches.

### 1. Fixed-Length Messages

Every message has the same size.

```text
[1024 bytes][1024 bytes][1024 bytes]
```

The receiver always knows where a message ends.

Simple, but wasteful when messages have different sizes.

### 2. Delimiter-Based Messages

A special sequence marks the end of each message.

```text
HELLO\n
WORLD\n
```

The receiver reads until it finds `\n`.

Simple and useful for text-based protocols, but the delimiter cannot appear unescaped inside the message.

### 3. Length-Prefixed Messages

The message length is sent before the actual data.

```text
[5][HELLO]
[5][WORLD]
```

The receiver first reads the length, then knows exactly how many bytes to read for the message.

This is a common approach for binary protocols.

The important thing is not which framing method we choose. The important thing is that **TCP doesn't choose one for us**.

Our application protocol must decide how bytes in the TCP stream become messages.


---
## <font color='green'>6. TCP vs UDP: Stream vs Message</font>

This is where TCP and UDP differ in a way that matters directly to application developers.

With TCP, if we send:

```text
HELLO
WORLD
```

the receiver sees a continuous byte stream:

```text
HELLOWORLD
```

The original boundaries are not preserved.

With UDP, each `send()` creates a separate datagram:

```text
send("HELLO")
send("WORLD")
```

The receiver gets:

```text
recv() -> "HELLO"
recv() -> "WORLD"
```

The message boundary is preserved.

So the mental models are:

```text
TCP

Application
    ↓
Byte stream
    ↓
TCP
```

```text
UDP

Application
    ↓
Datagram
    ↓
UDP
```

But this doesn't mean UDP is simply "TCP without reliability".

They make different trade-offs around reliability, ordering, congestion control, message boundaries, and delivery behavior.

**TCP gives us a reliable byte stream. UDP gives us datagrams.**


--- 
## <font color='green'>What About WebSocket?</font>

WebSocket is a good example of a protocol that adds **message semantics on top of a TCP connection**.

TCP gives WebSocket a reliable, ordered byte stream.

WebSocket adds its own framing so the application can work with messages rather than having to define its own framing on top of raw TCP.

```text
Application
    ↓
WebSocket messages
    ↓
WebSocket framing
    ↓
TCP byte stream
```

So when we say **TCP is not message-oriented**, it doesn't mean applications cannot use messages over TCP.

It means **TCP itself doesn't define those messages**.

WebSocket is one example of a protocol that does.

---
## <font color='green'>7. Summary</font>

TCP provides a **reliable, ordered byte stream**, but it does not preserve application-level message boundaries.

If an application needs messages, it must define its own framing mechanism. Common approaches include:

- **Fixed-length messages**
- **Delimiter-based messages**
- **Length-prefixed messages**

> This is why a single `send()` does not necessarily correspond to a single `recv()`.

Protocols such as **WebSocket** solve this at a higher level by providing message framing over a TCP connection.


---
## Relevant Link(s)

[TCP/IP and Network Progamming Page](../tcpip-networkprogramming.md)


