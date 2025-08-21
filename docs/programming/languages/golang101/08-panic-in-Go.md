# **08 Panic and Reover in Go**
(A request to crash the program ...)

---
## 1. What is ```panic```
```panic``` in Go is a built-in function that abruptly stops the execution of the current function when a serious, **unrecoverable error** occurs.

It's intended to stop execution in an unrecoverable situation (like a bug or critical failure).

---
## 2. Some possible scenarios
	
- **Scenario-1**: A Go app that tries to connect to a database right when it starts. If the connection messes up because of some wrong settings, the app just can’t keep running properly.

- **Scenario-2**: A program needs to read a config file from the system when it boots up. If that file’s missing, panicking makes sense since there’s no point in going on without it.

- **Scenario-3**: An app wants to listen on a TCP port (like a web server). If it can’t get that port because it’s already taken or we don’t have permission, then throwing a panic is a good option.

---
## 3. A simple "panic" example

=== "Example"
	``` go
	package main

	func main() {
		panic("Something went wrong!")
	}
	```
=== "Output"
	```
	panic: Something went wrong!

	goroutine 1 [running]:
	main.main()
		/tmp/sandbox1751277971/prog.go:4 +0x25
	```

---
## 4. More examples

=== "File missing example"
	``` go
	package main

	import (
		"os"
	)

	func main() {
		file, err := os.Open("config.json")
		if err != nil {
			panic("Failed to open config file: " + err.Error())
		}
		defer file.Close()

		// Continue with program...
	}
	```
	
	Output
	```
	panic: Failed to open config file: open config.json: no such file or directory

	goroutine 1 [running]:
	main.main()
		/tmp/sandbox1863475642/prog.go:10 +0x9f
	```

=== "panic outside main"
	``` go
	package main

	import "fmt"

	func checkPositive(n int) {
		if n <= 0 {
			panic("Number must be positive!")
		}
	}

	func main() {
		fmt.Println("Checking 5...")
		checkPositive(5)  // no panic
		fmt.Println("5 is positive!")

		fmt.Println("Checking -1...")
		checkPositive(-1) // will panic here
		fmt.Println("-1 is positive!") // This line won't run
	}
	```
	
	Output
	```
	Checking 5...
	5 is positive!
	Checking -1...
	panic: Number must be positive!

	goroutine 1 [running]:
	main.checkPositive(...)
		/tmp/sandbox1849315842/prog.go:7
	main.main()
		/tmp/sandbox1849315842/prog.go:17 +0xd1
	```
---
## 5. What happens with ```panic```?


- Normal execution stops immediately at the point where panic is called.

- **Deferred functions run** — Go executes all deferred functions in the current goroutine in reverse order 
For more info about [Deferred functions](06b-functions-in-Go-P2.md)

- After all deferred functions finish, if the panic is not recovered (via r), the program:

- Prints the panic message and a stack trace to the console.

- Terminates execution — the program crashes.

---
## 6. "recover" in Go

- recover() is a built-in function that can catch (recover from) a panic, stopping the program from crashing.

- It only works if called **inside a deferred function.** [Deferred functions](06b-functions-in-Go-P2.md)

- When recover() catches a panic, it returns the panic value (the error/message), and the program resumes normal execution after the deferred function.

Example
``` go
package main

import "fmt"

func safeCheck(n int) {

	// This is the deferred function
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from panic:", r)
        }
    }()

	// Panic will happen here if n <= 0
    if n <= 0 {
        panic("Number must be positive!")
    }
    fmt.Println("Number is", n)
}

func main() {
    safeCheck(10)
    safeCheck(-5)
    fmt.Println("Program continues after panic recovery")
}
```
Output:
```
Number is 10
Recovered from panic: Number must be positive!
Program continues after panic recovery
```

## 7. Multiple "defer" with "recover"

In the following example:

- Two defer statements are registered:
	First: the recover() block
	Second: the fmt.Println("Deferred: End of safeCheck") line

- Panic is triggered (n <= 0)

- Go starts unwinding the stack, and executes defers in reverse order:

	- 2nd defer runs first: prints Deferred: End of safeCheck
	
	- 1st defer runs second: runs recover(), catches the panic, and prints Recovered from panic:


Example:
``` go
package main

import "fmt"

func safeCheck(n int) {
    defer fmt.Println("Deferred: End of safeCheck") // 2nd defer

    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from panic:", r)
        }
    }() // 1st defer

    if n <= 0 {
        panic("Number must be positive!")
    }

    fmt.Println("Number is", n)
}

func main() {
    safeCheck(10)
    safeCheck(-5)
    fmt.Println("Program continues after panic recovery")
}
```
Output:
```
Number is 10
Deferred: End of safeCheck
Recovered from panic: Number must be positive!
Deferred: End of safeCheck
Program continues after panic recovery
```


## 8. Stack unwinding

-In Go (and many other programming languages), function calls are tracked on a **call stack** — a structure that keeps track of what functions were called.

- stacks are data structures that work on Last-In-First-Out (LIFO) principle. They are used to call functions in orderly manner.

- When a panic happens, Go **doesn't just stop immediately**. It "unwinds the stack", which means:

	- It goes backward through the list of function calls

	- Executes all defer statements in LIFO order

	- Gives each function a chance to clean up or recover

- **This process is called stack unwinding.**

## 9. Try-catch vs panic-recover
Go's panic/recover with defer is similar to try/catch in other languages like Java, Python, or JavaScript — but with some key differences in philosophy and mechanics.

| Feature                | Go (`panic`/`recover`)                   | Other languages (`try`/`catch`)        |
|------------------------|------------------------------------------|----------------------------------------|
| **Error signal**       | `panic("message")`                       | `throw new Error("message")`           |
| **Error handler**      | `recover()` inside `defer`               | `catch` block                          |
| **Cleanup**            | `defer` runs during panic stack unwind   | `finally` block                        |
| **Where it's used**    | Rare, for serious failures               | Common for handling expected or unexpected errors |
| **Control flow**       | Not meant for normal error handling      | Often used for flow control            |
| **Syntax**             | Manual setup with `defer` and `recover()`| Native `try { } catch { }` block       |




