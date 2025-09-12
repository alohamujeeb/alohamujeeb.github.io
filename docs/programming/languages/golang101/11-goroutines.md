# **11 Goroutines Part-1**

This section covers the theoretical concepts of ```goroutines``` in Go and concurrency in general. The next section will focus on hands-on practice.

---
Main topics:s

- Goroutines
- Threads vs goroutines vs asyncio

---
## 1. What is a Goroutine?

A goroutine is an independent function that runs concurrently with other functions in Go.
For those familiar with threads, you can think of a goroutine as a thread, with the following differences:

- Goroutines are lighter than threads (thousands or millions can run on few OS threads).
- They are managed by the Go runtime, not the operating system.
- They have smaller stack sizes (grow/shrink dynamically), unlike fixed-size thread stacks.
- They use channels (not shared memory) as the primary way to communicate safely.

## 2. main() is a Goroutine
In Go, even the main() function is executed as a goroutine — called the main goroutine.
That means every Go program always starts with at least one goroutine.

From there:

- We can create additional goroutines using the go keyword.
- All goroutines, including the **main** one, run concurrently.
- When the **main** goroutine ends, the whole program terminates; even if other goroutines are still running.

So, **every Go application is composed of at least one goroutine (main)**, and we can scale concurrency by adding more goroutines when needed.

## 3. Threads vs Goroutines

| Aspect              | OS Threads (Kernel-Managed)                                   | Goroutines (Go Runtime-Managed)                           |
|---------------------|---------------------------------------------------------------|-----------------------------------------------------------|
| **Management**      | Managed by the operating system kernel                        | Managed by the Go runtime scheduler (user space)          |
| **Stack Size**      | Fixed, usually 1–2 MB reserved per thread                     | Starts small (~2 KB) and grows/shrinks dynamically        |
| **Creation Cost**   | Expensive (system calls required)                             | Very cheap (just a function call + small runtime setup)   |
| **Context Switch**  | Handled by OS, involves saving/restoring registers & stacks   | Handled in user space by Go scheduler, much cheaper       |
| **Scheduling**      | Kernel schedules all system threads across processes         | Go runtime uses M:N scheduling (many goroutines on few OS threads) |
| **Scalability**     | Limited (hundreds or thousands, memory-heavy)                 | Extremely scalable (hundreds of thousands or millions)    |
| **Communication**   | Usually needs locks, mutexes, or shared memory               | Done via channels (safe, blocking, typed communication)   |
| **Overhead**        | Higher memory + kernel involvement                           | Low memory + efficient runtime management                 |


### M:N scheduling model
```code
                ┌──────────────────────────────┐
                │          OS Kernel         │
                └──────────────────────────────┘
                        ▲          ▲
                        │          │
             ┌───────────┘          └───────────┐
             │                                │
     ┌───────────────┐                  ┌───────────────┐
     │ OS Thread M1 │                  │ OS Thread M2 │
     └───────────────┘                  └───────────────┘
            ▲                                 ▲
   ┌─────────┼─────────┐              ┌─────────┼─────────┐
   │        │        │              │         │        │
 ┌───────┐ ┌───────┐ ┌───────┐    ┌───────┐ ┌───────┐ ┌───────┐
 │ G1    │ │ G2   │ │ G3   │    │ G4    │ │ G5   │ │ G6    │
 └───────┘ └───────┘ └───────┘    └───────┘ └───────┘ └───────┘

 Goroutine Goroutine Goroutine    Goroutine Goroutine Goroutine
```

## 4. How many threads a system can support
On Linux, threads are basically lightweight processes (tasks) managed by the kernel.

Each thread requires:

- Stack memory (typically 1–2MB per thread by default)
- Kernel data structures (task_struct, file descriptors, etc.)
- In practice, Linux can often handle several thousand threads per process
```text
Example: On an Intel PC
	
* Suppose we have 16GB RAM
* default 2MB stack per thread;

	Max threads ≈16GB​/2MB ≈8,000
```

### 4.1 How many goroutine
Goroutines are much lighter:

```text 
Example: On the same Intel PC 

* Suppose we have 16GB RAM.
* Initial stack ~2KB (grows dynamically)

	Max goroutines ≈16GB/2KB  ​≈8,000,000
```


## 5. Processor vs IO concurrency
Concurrency can be broadly categorized as:

- Processor-bound (CPU-bound) concurrency
- I/O-bound concurrency

| Feature                     | Processor-bound (CPU-bound)               | I/O-bound                                  |
|-----------------------------|------------------------------------------|-------------------------------------------|
| **Definition**               | Tasks limited by CPU computation          | Tasks limited by waiting for I/O          |
| **Characteristics**          | Heavy computations, minimal waiting       | Mostly waiting for external resources     |
| **Concurrency model**        | OS threads or goroutines on multiple cores | Lightweight threads, goroutines, or async/event loop |
| **Parallelism**              | True parallelism improves throughput     | Parallelism mostly logical (many tasks waiting concurrently) |
| **CPU usage**                | High                                      | Low                                        |
| **Example tasks**            | Image/video processing, simulations, math computations | Web servers, network requests, database queries |
| **Optimization focus**       | Maximize CPU core usage                  | Maximize concurrency, minimize blocking  |


```text
CPU-bound (Processor Heavy)                I/O-bound (Waiting Heavy)
──────────────────────                   ──────────────────────
   ┌───────────┐                               ┌─────────────┐
   │CPU Core 1│                               │ Event Loop │
   └─────┬─────┘                               └─────┬───────┘
         │                                         │
 ┌───────┼────────┐                       ┌──────────┼─────────┐
 │       │       │                       │         │        │
┌─────┐ ┌─────┐ ┌─────┐                ┌─────┐   ┌─────┐    ┌─────┐
│ T1  │ │ T2 │ │ T3  │                │ G1  │  │  G2 │    │ G3 │
└─────┘ └─────┘ └─────┘                └─────┘   └─────┘    └─────┘
  Thread Thread Thread                   Goroutine Goroutine Goroutine
  doing  CPU heavy                        mostly waiting for I/O

 ┌─────┐ ┌─────┐ ┌─────┐                ┌─────┐ ┌─────┐ ┌─────┐
 │ T4  │ │T5  │ │ T6  │                │ G4 │ │ G5  │ │ G6  │
 └─────┘ └─────┘ └─────┘                └─────┘ └─────┘ └─────┘
  Thread Thread Thread                   Goroutine Goroutine Goroutine
  doing  CPU heavy                        mostly waiting for I/O

```
Note:

- CPU-bound: Threads / goroutines doing heavy computations mapped directly to cores
- I/O-bound: Goroutines or async tasks multiplexed over few OS threads or a single event loop

### 5.1 Event loop (in IO-bound)

An event loop is a programming construct that repeatedly checks for and dispatches events or tasks. It allows a program to handle many I/O-bound operations concurrently on a single thread by switching between tasks whenever one is waiting for I/O.

```text
            ┌──────────────────────────────┐
            │        Event Loop            │
            │  (Single Thread Execution)  │
            └─────────────┬────────────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
      ┌───────┐       ┌───────┐        ┌───────┐
      │ Task1 │       │ Task2 │        │ Task3 │
      └───┬───┘       └───┬───┘        └───┬───┘
          │               │                │
          ▼               ▼                ▼
   Waiting for I/O   Waiting for I/O  Waiting for I/O
          │               │                │
          └───── Event Loop polls ────────┘
                     repeatedly
```

- The Event Loop is a single thread that repeatedly checks tasks.
- Each task that is waiting for I/O yields control.
- The loop continues to poll and schedule ready tasks, allowing high concurrency without multiple threads.

## 6. Where do Goroutines fit?

**Goroutines are general-purpose lightweight concurrency units**.

- They are excellent for I/O-bound workloads, 
- but they can also handle CPU-bound workloads up to the number of available CPU cores.

### 6.1 I/O-bound:

- Goroutines are **more suited** here. 
- We can run thousands of concurrent I/O operations (network calls, disk reads, etc.) very efficiently. 
- This is similar to asyncio or Node.js’s event loop, but with a simpler model (you just write normal-looking code with goroutines + channels).

### 6.2 CPU-bound:

- Goroutines also work well, 
- However, they’re limited by the number of CPU cores. The Go runtime maps goroutines onto OS threads, and the OS threads onto cores. 
- So, if you have an 8-core machine, you’ll get at most 8 CPU-heavy goroutines truly running in parallel. 

### 6.3 Async-io loop:

- ```asyncio``` is mainly for I/O-bound concurrency (single thread can juggle many tasks, but CPU-heavy work will block it).

- Goroutines, being mapped onto OS threads, can do both I/O and CPU-bound concurrency.

### 6.4 Comparision

| Technique           | Best For                          | Characteristics                                | Example Scenarios                                   |
|---------------------|-----------------------------------|-----------------------------------------------|----------------------------------------------------|
| **OS Threads**      | CPU-heavy parallelism             | Heavyweight, limited in number, managed by OS  | Video rendering, physics simulations, game engines |
| **Goroutines (Go)** | Mixed CPU + I/O, scalable tasks   | Lightweight, multiplexed on OS threads, simple API | Web servers, microservices, proxies, IoT collectors |
| **Asyncio / Event Loop** | I/O-heavy concurrency (low CPU) | Single-threaded, cooperative multitasking      | Chat servers, web scrapers, GUIs, lightweight web apps |


