# *11 Goroutines**

Main topics:

- Goroutines
- Channels
- Threads vs goroutines

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








