# **06b Functions in Go (Part 2)**

Main topics:

- Variadic Functions
- Anonymous Functions
- Closures
- defer Statement
- Higher Order Functions


---
Part 2 covers some function-related features in Go that are uncommon in traditional languages but are commonly found in modern languages like Python and JavaScript.

---

## 9. Variadic functions
A variadic function is a function that can take any number of arguments of the same type. It allows you to call the function with zero, one, or many values.

- **This is different from C/C++, however, some languages like Python allow fucntions to take variable number of parameters.**

**Important**

- All variadic arguments must be of the same type
- Variadic parameter must be at the end
- Can pass slice with ...

Examples:

=== "Finding max number"
    ``` go
    func max(nums ...int) int {
    if len(nums) == 0 {
        return 0 // or panic/error if no input
    }
    maxVal := nums[0]
    for _, n := range nums {
        if n > maxVal {
            maxVal = n
        }
    }
    return maxVal
    }

    func main() {
        fmt.Println("Max:", max(3, 8, 2, 10, 5))  // Output: 10
        fmt.Println("Max:", max(1, 2, 12, 23, 36, 8, 2, 10, 5))  // Output: 36
    }
    ```
=== "More examples with fine details(WIP)"
    ``` go
    ```

## 10. Anonymous functions

Anonymous functions are functions without a name. They are defined inline and can be assigned to variables, passed as arguments, or invoked immediately. 

They’re very handy for quick, throwaway logic or closures.

=== "Create and Call"
    ``` go
    package main

    import "fmt"

    func main() {
        greet := func(name string) {
            fmt.Println("Hello,", name)
        }

        greet("Mujeeb")
        greet("Merlin")
    }

    ```
=== "IIFE"
    ``` go
    //IIFE - Immediately Invoked Function Expression
    package main

    import "fmt"

    func main() {
        func() {
            fmt.Println("This runs immediately!")
        }()
    }
    ```
=== "Anonymous function with return value"  
    ``` go
    package main

    import "fmt"

    func main() {
        func() {
            fmt.Println("This runs immediately!")
        }()
    }
    ```

### Function literals vs IIFE

=== "Functional literal example"
    The function is defined and stored in a variable for later use.
    ``` go
    package main

    import "fmt"

    func main() {
        greet := func(name string) {
            fmt.Println("Hello,", name)
        }

        // Function literal is called later
        greet("Mujeeb")
        greet("Merlin")
    }
    ```

=== "IIFE (Immediately Invoked Function Expression)"
    The function literal is defined and called immediately, without assigning it to a variable.
    ``` go
    package main

    import "fmt"

    func main() {
        func(name string) {
            fmt.Println("Hello immediately,", name)
        }("Mujeeb")  // Immediately invoked with "Mujeeb"
    }

    ```
    

## 11. Closures (Functions inside functions)
A closure in Go is an anonymous function that captures and "remembers" variables from its surrounding scope, even after that scope has finished executing.

### Rules of a closure data persistence
- It's a function (often anonymous).
- It uses variables declared outside of itself (from the surrounding function).
- Those outer variables persist as long as the closure is being used — even if the original function has finished executing.


Example:
=== "Example 1"
    ``` go

    package main

    import "fmt"

    func main() {
        counter := 0

        increment := func() int {
            counter++          // captures and modifies counter (outer variable!!!)
            return counter
        }

        fmt.Println(increment()) // 1
        fmt.Println(increment()) // 2  #remembers state from prvious call
        fmt.Println(increment()) // 3
    }
    ```
=== "A complex example"
    ``` go
    package main

    import "fmt"

    func main() {
        a := 0

        increment := func() int {
            a++         //again: a is an outer variable
            return a
        }

        fmt.Println(increment()) // 1

        a += 10                  // manually add 10 to 'a'

        fmt.Println(increment()) // ?
    }
    ```
    Note: the output is 12
=== "Global variable example"
    ``` go
    package main

    import "fmt"

    var counter int = 100  // global variable

    func main() {
        increment := func() int {
            counter++       //outer variable is the state
            return counter
        }

        fmt.Println(increment()) // 101
        fmt.Println(increment()) // 102

        counter += 50
        fmt.Println(increment()) // 153
    }

    ```
=== "Closure with persistent data"
    ``` go
    package main

    import "fmt"

    // counter returns a function that keeps track of a count
    func counter() func() int {
        //Note: it is outer variable that will be used by inner
        count := 0  // This variable is captured by the closure

        //the inner function remembers the outer variable "count"
        return func() int {
            count++      // modify the captured variable
            return count // return updated count
        }
    }

    func main() {
        //closure state will remain till "next" variable is destroyed
        next := counter()  // get the closure

        fmt.Println(next()) // 1
        fmt.Println(next()) // 2
        fmt.Println(next()) // 3

        another := counter() // a new closure with its own count
        fmt.Println(another()) // 1
        
    }
    ```
    
    - counter() returns an anonymous function (closure).
    - That returned function captures the count variable from its surrounding scope.
    - Even though counter() finishes executing, count remains alive inside the returned function.
    - Each call to next() updates and uses the same count — this is persistent state.
    

## 12. **defer** statements

- The defer statement schedules a function call to run later, just before the surrounding function returns.

- Deferred calls execute in last-in, first-out (LIFO) order.

- Useful for tasks like cleanup, closing files, unlocking resources, etc.

=== "Basic example"
    Note:
    
    - defer statements don’t run immediately.

    - They run after main() finishes, in reverse order of their declaration.

    - So "Deferred call 2" runs before "Deferred call 1".
    
    ```go
    package main

    import "fmt"

    func main() {
        fmt.Println("Start")

        defer fmt.Println("Deferred call 1")
        defer fmt.Println("Deferred call 2")

        fmt.Println("End")
    }
    ```
    Output:
    ```
    Start
    End
    Deferred call 2
    Deferred call 1
    ```

    
=== "A practical example"
    Note:

    - The file.Close() call is registered immediately, but it does not run yet.

    - It runs automatically at the end of the current function (e.g., main())—just before main()  exits.

    - This ensures the file is always closed, even if your function returns early or encounters an error.

    ```go
    package main

    import (
        "fmt"
        "os"
    )

    func main() {
        file, err := os.Open("example.txt")
        if err != nil {
            fmt.Println("Error opening file:", err)
            return
        }

        defer file.Close()  // ensures file is closed when main exits

        // Work with the file here
        fmt.Println("File opened successfully")
    }
    ```
##13. Higher function

A Higher-Order Function is a function that does at least one of the following:

- Takes another function as an argument

- Returns a function as its result

(Functions are first-class citizens in Go, meaning you can treat them like variables—assign them, pass them, return them.)

### Three examples

=== "Example 1: Passing a function as an argument"
    ``` go
    package main

    import "fmt"

    // A higher-order function that applies a function to two numbers
    func apply(op func(int, int) int, a int, b int) int {
        return op(a, b)
    }

    // A basic function to pass in
    func add(x, y int) int {
        return x + y
    }

    func main() {
        result := apply(add, 3, 4)
        fmt.Println("Result:", result) // Output: Result: 7
    }

    ```
=== "Example 2: Returning a function from another function"  
    ``` go
    package main

    import "fmt"

    // A higher-order function that returns another function
    func multiplier(factor int) func(int) int {
        return func(x int) int {
            return x * factor
        }
    }

    func main() {
        double := multiplier(2)
        triple := multiplier(3)

        fmt.Println(double(5)) // Output: 10
        fmt.Println(triple(5)) // Output: 15
    }
    ```
=== "Example 3: Anonymous function as argument"
    ``` go
    package main

    import "fmt"

    func compute(fn func(int) int, val int) int {
        return fn(val)
    }

    func main() {
        result := compute(func(x int) int {
            return x * x
        }, 6)

        fmt.Println("Squared:", result) // Output: Squared: 36
    }

    ```
### Why Use Higher-Order Functions?

- Clean, reusable, and composable code
- Common in functional-style patterns (map, filter, reduce)
- Enables callbacks and dynamic behaviour

