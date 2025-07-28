# **02-Some Fundamentals**

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
    
### Short declaration

``` go
name := "Alice"
name := "Bob" // ❌ ERROR: no new variables on left side of :=
```

##3. Built-in data types

???+ Basic tyes
    - bool
    - string

??? Integer types
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
    
???+ Float types
    - float32
    - float64

???+ Complex types
    - complex64
    - complex128
???+ Alias types
    - byte (alias for uint8)
    - rune (alias for int32)
---

##4. Zero values
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


