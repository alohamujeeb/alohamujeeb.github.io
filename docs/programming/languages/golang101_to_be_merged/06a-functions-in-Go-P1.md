# **06a Functions in Go (Part 1)**

Main topics:

- Defining and Calling Functions
- Function Parameters
- Function Return Values
- Scope of Variables
- Recursion
- Variable Shadowing
- Function Signatures

---
Functions in Go work the same way as in other languages like Python, Java, C++, and JavaScript; They’re just a way to group code which we want to use many times.

The syntax might look different, but the basic idea is the same.

---
## 1. Defining and calling functions
The if statement in Go is used to execute code conditionally—only when a given boolean expression is true.

=== "Syntax"
	``` go
	func functionName(parameter1 type, parameter2 type, ...) returnType {
    // function body
    }
	```
    Note: Unlike C/C++ and Java, the **func** keyword is mandatory in Go
    
=== "A simple function example"
	``` go
    package main

    import "fmt"
    // Function definition
    func add(a int, b int) int {
        return a + b
    }

    func main() {
        // Function call
        result := add(5, 3)
        fmt.Println("Sum:", result)
    }
	```
    Again, function defining and calling is very similar as in other languages.

---
## 2. Function parameters
The if statement in Go is used to execute code conditionally—only when a given boolean expression is true.

Some exampls are shown below:

=== "String"
	``` go
    func greet(name string) {
        fmt.Println("Hello,", name)
    }
    ```
=== "Integer"
	``` go
    func add(a int, b int) int {
        return a + b
    }
    ```   
=== "Float"
	``` go
    func multiply(x float64, y float64) float64 {
        return x * y
    }
    ```
=== "Boolean"
    ``` go
    func checkStatus(active bool) {
        if active {
            fmt.Println("Status: Active")
        } else {
            fmt.Println("Status: Inactive")
        }
    }
    ``` 
---
## 3. Function return values
In Go, a function’s return type specifies the type of value it sends back to the caller after execution.

Some exampls are shown below:

=== "String"
	``` go
    func greet(name string) string {
        return "Hello, " + name
    }
    ```
=== "Integers"
	``` go
    func square(x int) int {
        return x * x
    }
    ```
=== "Float"
	``` go
    // Function that returns a float64
    func average(a, b float64) float64 {
        return (a + b) / 2
    }
    ```
### Multiple return values

Some examples

=== "Example(value, erro)"
    ``` go
    package main

    import (
        "errors"
        "fmt"
    )

    func divide(a, b float64) (float64, error) {
        if b == 0 {
            return 0, errors.New("cannot divide by zero")
        }
        return a / b, nil
    }

    func main() {
        result, err := divide(10, 2)
        if err != nil {
            fmt.Println("Error:", err)
        } else {
            fmt.Println("Result:", result)
        }
    }

    ```
=== "Example(swap values)"
    ``` go
    func swap(a, b string) (string, string) {
        return b, a
    }

    func main() {
        x, y := swap("hello", "world")
        fmt.Println(x, y)  // Output: world hello
    }
    ```

=== "Example(min and max)"
    ``` go
    func minMax(a, b int) (int, int) {
        if a < b {
            return a, b
        }
        return b, a
    }

    func main() {
        min, max := minMax(7, 3)
        fmt.Println("Min:", min, "Max:", max)
    }
    ```
### "error" package in Go
The **errors** package provides simple error handling primitives in Go. 

It’s part of the standard library and mainly helps you create and manipulate error values, which are used to indicate when something has gone wrong during program execution.

- **Creating errors:**
The most common way to create a new error is using 
    **errors.New()**,
which takes a string message describing the error.

- **Error type:**
In Go, error is an interface type with a single method:
    ``` go
    type error interface {
        Error() string
    }
    ```
Any type that implements this method is an error.

- **Error handling pattern:**
Functions often return an error as the last return value, which you check to see if something went wrong.

=== "Example 1"
    ``` go
    package main

    import (
        "errors"
        "fmt"
    )

    // Function that returns an error if input is negative
    func checkPositive(number int) error {
        if number < 0 {
            return errors.New("input cannot be negative")
        }
        return nil  // no error
    }

    func main() {
        nums := []int{10, -5, 0}

        for _, num := range nums {
            err := checkPositive(num)
            if err != nil {
                fmt.Println("Error:", err)
            } else {
                fmt.Println(num, "is positive or zero")
            }
        }
    }
    ```

=== "Example 2 (explicit declarion)"
    ``` go
    package main

    import (
        "errors"
        "fmt"
    )

    func divide(a, b float64) (float64, error) {
        var err error // explicitly declare an error variable
        var result float64

        if b == 0 {
            err = errors.New("cannot divide by zero")
            return 0, err
        }

        result = a / b
        return result, nil
    }

    func main() {
        var err error // explicitly declare error variable to hold function return

        result, err := divide(10, 0)
        if err != nil {
            fmt.Println("Error:", err)
        } else {
            fmt.Println("Result:", result)
        }

        result, err = divide(10, 2)
        if err != nil {
            fmt.Println("Error:", err)
        } else {
            fmt.Println("Result:", result)
        }
    }
    ```
### Named return values

Named return values are like pre-declared variables for the return values of a function. Instead of just specifying the types of the return values, you also give each return value a name in the function signature.

Example:
``` go
func divide(a, b float64) (result float64, err error) {
    if b == 0 {
        err = fmt.Errorf("cannot divide by zero")
        return  // returns result=0 (default float64), and err
    }
    result = a / b
    return  // returns the values of result and err
}

```
### Blank identifier
The blank identifier _ is a special placeholder used when you want to ignore a value. It tells the Go compiler that you don’t care about that particular value, and it prevents compilation errors about unused variables.

=== "Example: Ignoring an error"
    ``` go
    package main

    import (
        "fmt"
        "strconv"
    )

    func main() {
        number, _ := strconv.Atoi("123") // ignoring the error here
        fmt.Println("Number:", number)
    }
    ```

=== "Example: Ignoring a return value"
    ``` go
    func divide(a, b int) (int, int) {
        return a / b, a % b
    }

    func main() {
        quotient, _ := divide(10, 3)  // ignore remainder
        fmt.Println("Quotient:", quotient)
    }
    ``` 
---
## 4. Pass by value or pass by pointer

- Go always passes function arguments by value. This means the function gets a copy of the argument.

- If you want the function to modify the original variable, you need to pass a pointer to that variable (**same concept as pointer parameters or reference parameter in C/C++**)

=== "Example (passing by value)"
    The function receives a copy of the argument. Changes inside the function don’t affect the original variable.
    ``` go
    package main

    import "fmt"

    func incrementByValue(n int) {
        n = n + 1
        fmt.Println("Inside incrementByValue:", n) // 11
    }

    func main() {
        a := 10
        incrementByValue(a)
        fmt.Println("After incrementByValue:", a)   // 10 (unchanged)
    }
    ```
    
=== "Example (passing by pointer)"
    We pass the address of the variable (*int), so the function can modify the original value.

    ``` go
    package main

    import "fmt"

    func incrementByPointer(n *int) {
        *n = *n + 1            // Dereference pointer to change actual value
        fmt.Println("Inside incrementByPointer:", *n) // 11
    }

    func main() {
        a := 10
        incrementByPointer(&a)    // Pass address of a
        fmt.Println("After incrementByPointer:", a)  // 11 (changed)
    }

    ```

## 5. Scope of variables
In Go, scope refers to where a variable can be accessed within your code.

- A local variable is declared inside a function and can only be used within that function.

- A global variable is declared outside of any function (usually at the top of the file) and is accessible from any function in the same package.

- **Rules are very similar to C/C++**

=== "Local variables"
    ``` go
    package main

    import "fmt"

    func greet() {
        message := "Hello from greet!" // local variable
        fmt.Println(message)
    }

    func main() {
        greet()
        // fmt.Println(message) // ❌ ERROR: message is not accessible here
    }
    ```
=== "Global variables"
    ``` go
    package main

    import "fmt"

    var globalMessage = "Hello from global!" // global variable

    func printMessage() {
        fmt.Println(globalMessage) // accessible here
    }

    func main() {
        fmt.Println(globalMessage) // accessible here too
        printMessage()
    }

    ```
Note: Prefer local variables when possible to avoid unwanted side effects and make your code easier to debug.


## 6. Recursion in Go
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem. It continues until it reaches a base case that stops further calls.

Examples:
=== "Factorial"
    ``` go
    package main

    import (
        "fmt"
    )

    func factorial(n int) int {
        if n == 0 {
            return 1
        }
        return n * factorial(n-1)
    }

    func main() {
        fmt.Println("Factorial of 5 is:", factorial(5)) // Output: 120
    }
    ```

## 7. Variable shadowing
Variable shadowing occurs when a new variable declared in a nested (inner) scope has the same name as a variable in an outer scope. The inner variable "shadows" or hides the outer one within its scope.

This can lead to confusion if not handled carefully.

=== "Simple shadowing example"
    ``` go
    package main

    import "fmt"

    func main() {
        x := 10
        fmt.Println("Outer x:", x)

        {
            x := 20  // This x shadows the outer x
            fmt.Println("Inner x:", x)
        }

        fmt.Println("Outer x again:", x)
    }
    ```
    Output:
    ``` text
    Outer x: 10
    Inner x: 20
    Outer x again: 10
    ```
=== "Shadowing a parameter"
    ``` go
    package main

    import "fmt"

    func printDouble(x int) {
        fmt.Println("Original x:", x)

        x := x * 2  // ❌ Shadowing here
        fmt.Println("Shadowed x:", x)
    }

    ```
    🛑 This code won't compile!
    
    **Error:** : no new variables on left side of :=
   
### Shadowing if or for block 

Example if or for block
``` go
package main

import "fmt"

func main() {
    x := 5
    fmt.Println("Before if:", x)

    if x := 100; x > 0 {  // New x shadows outer x
        fmt.Println("Inside if:", x)
    }
        fmt.Println("After if:", x)  // Still refers to the original x
}
```

Output
``` text
Before if: 5
Inside if: 100
After if: 5
```

## 8. Function types and signature
This is same concept as **function prototype** C/C++ or "function signature" in Java.

A function signature defines:

- The parameter types
- The return type(s)
- It tells you what a function expects and returns — like a contract.

**This improves code readability, especially when passing functions around.**

Example
``` go
func add(a int, b int) int
```

=== "Example 2"
    ``` go
    package main

    import "fmt"

    func add(a int, b int) int {
        return a + b
    }

    func main() {
        var op func(int, int) int  // Declare a function variable with a specific signature
        op = add                   // Assign the add function to it

        fmt.Println(op(3, 4))      // Output: 7
    }
    ```
=== "Example 2: defining a custom function"
    ``` go
    package main

    import "fmt"

    type operation func(int, int) int  // Define a named function type

    func multiply(x, y int) int {
        return x * y
    }

    func main() {
        var op operation = multiply
        fmt.Println(op(5, 6))  // Output: 30
    }
    ```
=== "Example 3: passing function types as arguments"
    ``` go
    package main

    import "fmt"

    type operation func(int, int) int

    func compute(op operation, a int, b int) int {
        return op(a, b)
    }

    func add(x, y int) int {
        return x + y
    }

    func main() {
        result := compute(add, 2, 3)
        fmt.Println(result)  // Output: 5
    }
    ```
    


    