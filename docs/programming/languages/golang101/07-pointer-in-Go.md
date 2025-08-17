# **07 Pointers in Go**
---

A pointer is a variable that stores the memory address of another variable.

It is used to:

- Share and modify values without copying them
- Optimize performance (especially with structs)
- Pass large data structures efficiently

---

## 1. Basic pointer syntax
``` go
var x int = 10
var p *int = &x  // p is a pointer to x

fmt.Println(x)   // 10
fmt.Println(p)   // memory address of x
fmt.Println(*p)  // dereferencing p — prints 10
```
### What is dereferencing
Dereferencing means accessing the value stored at a memory address held by a pointer.

- In Go, you use the * operator to dereference a pointer.
- A pointer stores a memory address, not the actual value.
- Dereferencing allows you to read or modify the value at that address.

``` text
&x → “Give me the address of x”
*p → “Give me the value stored at address p”
```

## 2. Modifying a value through a pointer

``` go
func change(val *int) {
    *val = *val + 5
}

func main() {
    x := 10
    change(&x)
    fmt.Println(x)  // Output: 15
}
```
## 3. Comparison with C/C++ pointers


In Comparison to C/C++:

- Go does not support pointer arithmetic (e.g., p++, p+1 are not allowed).
- Go does not have NULL; instead, it uses nil for uninitialized or zero-value pointers.
- No malloc or free
    - Go has automatic garbage collection, so you don't need to manually free memory for unreferenced pointers.



## 4. uninitialized or unreferenced pointers

-  Zero Value of a Pointer is nil (**see topic on data types for 'zero values', which are default values of a variable**)

=== "Example 1"
    ``` go
    var p *int
    fmt.Println(p)  // Output: <nil>
    
    //You must check for nil before dereferencing:
    if p != nil {
        fmt.Println(*p)
    }
    ```
## 5. Pointer comparison
Go does not support pointer arithmetic (e.g., p++, p+1 are not allowed).
But, we can compare pointers directly:

``` go
if ptr1 == ptr2 {
    fmt.Println("Same address")
}
```

## 6. Pointers and structures

Pointers are often used when:

- Modifying struct fields in methods
- Avoiding large struct copies
(**more on this in the chapter on struc**)


    
