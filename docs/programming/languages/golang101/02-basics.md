# **02-Some Fundamentals**

- importing packages
- creating variables 
- short declarations
- constant declaration (immutable)
- zero values

---

##1. **Importing packages**
- In the previous chapter, we used a package "import fmt".
- In Go, a package is a collection of related source files that are compiled together.

    For example, the "fmt" package provides functions for formatted input and output, such as **fmt.Println()** and **fmt.Printf()**.
    
- In Go, a program must import a package at the beginning of the source file to access and use the functionality defined in that package.


``` go
//To import a single package:
import "fmt"

//To import multiple packages:
import (
    "fmt"
    "math"
)

```
### **An example**

``` go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Floor(2.75))
}
```

---

##2. Declaring Variables

Syntax to create a variable is
```
var <name> <type>
```

For example, 
=== "Declaration"
    ``` go
    var quantity int
    var height float64
    var name string
    var length, width int
    ```
=== "Assigning Values"
    ``` go
    quantity = 23
    name "Mujeeb"
    length, width = 10, 14
    ```
=== "Assining and Declaring togetghar"
    ``` go
    //go decides on the type based on the value
    message := "Ronaldo"
    age := 25
    
    //or
    var quantity = 23
    var length, width = 10,14 //both are integer
    var length, width = 10.0, 14 //can you guess types?
    ```
    
##3. Built-in data types

!!! note "Basic types"
    - bool
    - string

!!! note "Integer types"
    - int
    - int8
    - int16
    - int32 (alias: rune)
    - int64
    - uint
    - uint8 (alias: byte)
    - uint16
    - uint32
    - uint64
    - uintptr
    
???+ note "Float types"
    - float32
    - float64

???+ note "Complex types"
    - complex64
    - complex128
	
???+ note "Alias types"
    - byte (alias for uint8)
    - rune (alias for int32)
---

##4. Short variable declaration

- The short variable declaration syntax uses := to declare and initialize a variable in one concise statement.
- It automatically infers the variable’s type from the value on the right-hand side.
-It can only be used inside functions (not at the package level).

**Syntax**
``` go 
//variableName := value
func main() {
    age := 25        // int inferred
    fmt.Println(age) // Output: 25
}
```

### Important points about **short variable declation**
- Variable type is inferred automatically.
- You cannot use := without initialization (no zero value-only declarations).
- Very handy for quick and readable code inside functions.
- **You cannot declare a variable without initialization**

We can change the value of the variable, but then we have to use "=" instead of ":="
``` go

func main() {
    x := 10          // Declare and initialize x with 10
    fmt.Println(x)   // Output: 10

	//x :=20   COMPILATION ERROR
    x = 20           // Reassign a new value to x
    fmt.Println(x)   // Output: 20
}
```

``` go
name := "Alice"
name := "Bob" // ❌ ERROR: no new variables on left side of :=
```

### 'short declaration' outside functions not allowed

- **You cannot do this at the package level (outside functions)**
- At the package level (outside any function), Go requires explicit var declarations at the top level.
(This point will be discussed in more details in the section of Packages later.)


### 'short declaration' summary:

|context|allowed|
|---|---|
|inside functions| YES|
|outside function (e.g. package level)| NO|
|value update|NO|




##5. Constants in Go (Immutables)
The const keyword in Go is used to declare constant values — these are values that cannot change after they're defined.

``` go
const pi = 3.14 
const pi float64 = 3.14159 // inferred as float64
```


##6. Zero values
In Go, "zero values" are the default values assigned to variables when they are declared but not explicitly initialized.

|Type| Zero Value|
|----|----|
|bool| false|
|int, float|0, 0.0|
|string| empty string (not Nil)|
|pointer, func, interface{}, map, slice, chan| Nil |
|struct| 	Fields = zero values|

**Note:**

- Some of the above data types are not explained in this chapter (such as struct, pointer...). They will be described in the subsequent chapters.
- nil is used with reference types, not value types (to be explained in coming chapters)


