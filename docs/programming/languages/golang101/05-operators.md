# **05 Operators and Typecasting**
- Arithmetic Operators
- Comparision Operators
- Logtical Operators
- Bitwise Operators
- Typecasting 
---

## 1. Arithmetic Operators
Arithmetic operations in Go (Golang) are the basic mathematical operations you can perform on numbers. These include addition, subtraction, multiplication, division, and modulus (like most languages). 

=== "Some examples"
	``` go
	////Be careful about (:= or =) assignment operations

	a := 10
	b := 5
	sum := a + b // sum is 15
	diff := a - b // diff is 5
	product := a * b // product is 50


	//integer division
	a := 10
	b := 3
	quotient := a / b // quotient is 3 (integer division)

	//float division
	x := 10.0
	y := 3.0
	floatQuotient := x / y // floatQuotient is 3.3333333 (float division)

	//Modulus (remainder) operation
	a := 10
	b := 3
	remainder := a % b // remainder is 1

	```
	
=== "A full example"
	``` go
	
	package main

	import "fmt"

	func main() {
		a := 15
		b := 4

		fmt.Println("Addition:", a+b)        // 19
		fmt.Println("Subtraction:", a-b)     // 11
		fmt.Println("Multiplication:", a*b)  // 60
		fmt.Println("Division:", a/b)         // 3 (integer division)
		fmt.Println("Modulus:", a%b)          // 3

		// For floating point division:
		x := 15.0
		y := 4.0
		fmt.Println("Float Division:", x/y)  // 3.75
	}
	```
## 2. Comparision Operators
Comparison operators in Go are used to compare two values and return a Boolean result (true or false). These operators are commonly used in conditions such as if statements or loops.

=== "Some examples"
	``` go
	////Be careful about (:= or =) assignment operations
	
	a := 5
	b := 5
	fmt.Println(a == b) // true
	
	a := 5
	b := 3
	fmt.Println(a != b) // true

	a := 7
	b := 5
	fmt.Println(a > b) // true
	
	a := 7
	b := 10
	fmt.Println(a < b) // true
	
	a := 7
	b := 7
	fmt.Println(a >= b) // true

	a := 7
	b := 7
	fmt.Println(a <= b) // true
	```

=== "A full example"
	``` go
	
	package main

	import "fmt"

	func main() {
		a := 10
		b := 20

		fmt.Println("a == b:", a == b)   // false
		fmt.Println("a != b:", a != b)   // true
		fmt.Println("a > b:", a > b)     // false
		fmt.Println("a < b:", a < b)     // true
		fmt.Println("a >= b:", a >= b)   // false
		fmt.Println("a <= b:", a <= b)   // true
	}
	```

## 3. Logical operators

Logical operators in Go let you combine or invert Boolean expressions (true or false). 

| Operator | Name        | Description |
|---|---|---|
| `&&`     | Logical AND | True if **both** operands are true|
| `||`     | Logical OR | True if **atleast ONE** operand is true|
| `!`     | Logical NOT | Inverts the Boolean value|

**An example**
``` go
//Be careful about (:= or =) assignment operations

package main

import "fmt"

func main() {
    a := true
    b := false

    fmt.Println("a && b:", a && b)  // false
    fmt.Println("a || b:", a || b)  // true
    fmt.Println("!a:", !a)          // false
}
```


## 4. Bitwise operators

- Bitwise operators in Go allow you to perform operations directly on the binary representation of integers. 
- These are very useful in systems programming, hardware control, flags, and performance-critical code.

???+ warning "Do not confuse with logical operators"

- **logical operators (&&, ||, !) operate on boolean data, wherease bitwise operators (&, | ) operate on bits** 

|Operator |Name		|Description|
|---|---|---|
|`&`	|AND	|1 if both bits are 1 \
| `|`|OR||1 if both bits are 1|
|`^`|XOR (binary)	|1 if bits are different|
|`^`|NOT (unary)	|Inverts all bits|
|`&^`|	AND NOT (bit clear)	|Clears bits set in second operand|
|`<<`|Left Shift	|Shifts bits to the left|
|`>>`|Right Shift	|Shifts bits to the right|

### **An example**
``` go
package main

import "fmt"

func main() {
	a := 10 // binary: 00001010
	b := 6  // binary: 00000110

	fmt.Println("a & b:", a&b)   // 2  -> 00001010 & 00000110 = 00000010  // Bitwise AND
	fmt.Println("a | b:", a|b)   // 14 -> 00001010 | 00000110 = 00001110  // Bitwise OR
	fmt.Println("a ^ b:", a^b)   // 12 -> 00001010 ^ 00000110 = 00001100  // Bitwise XOR
	fmt.Println("^a   :", ^a)    // -11 -> ^00001010 = 11110101           // Bitwise NOT (inversion)
	fmt.Println("a &^ b:", a&^b) // 8  -> 00001010 &^ 00000110 = 00001000 // Bit Clear (AND NOT)
	fmt.Println("a << 1:", a<<1) // 20 -> 00001010 << 1 = 00010100        // Left Shift (×2)
	fmt.Println("a >> 1:", a>>1) // 5  -> 00001010 >> 1 = 00000101        // Right Shift (÷2)
}

```
## 5. Typecasting (type conversion)
Typecasting (more properly called type conversion in Go) is the process of converting a value of one data type into another. This is useful when you want to assign a value from one type to a variable of a different type or perform operations that require matching types.

### Implicit typecasting
Implicit typecasting (also called implicit conversion) is when a programming language automatically converts a value from one data type to another without you having to write extra code.

=== "Implicit type conversion example"

	``` go
	var a int = 42          // int literal 42 implicitly converted to int
	var b float64 = 42      // int literal 42 implicitly converted to float64
	var c byte = 42         // int literal 42 implicitly converted to byte

	var x float32 = 3.14    // floating-point literal implicitly converted to float32
	var y float64 = 3.14    // floating-point literal implicitly converted to float64
	
	let x = 5;       // integer
	let y = 3.14;
	
	#IMPORTANT
	let z = x + y;   // implicit conversion of x (int) to float for addition
	```

### Explicity typecasting
Explicit typecasting (or explicit type conversion) is when the programmer manually converts a value from one type to another by specifying the target type in the code.

**syntax**
T(value)

===  "Explicity type conversion example"
	``` go
	package main

	import "fmt"

	func main() {
		var i int = 42
		var f float64 = float64(i) // int → float64
		fmt.Println(f)             // Output: 42

		var x float64 = 3.99
		var y int = int(x) // float64 → int (decimal truncated)
		fmt.Println(y)     // Output: 3

		var b byte = byte(i) // int → byte
		fmt.Println(b)       // Output: 42
	}
	```
### Some pitfalls of typecasting
Here are some common pitfalls of explicit typecasting

- Loss of Data:
Converting from a larger or more precise type to a smaller or less precise type (e.g., float64 to int) truncates or loses information.
Example: int(3.99) becomes 3, decimal part lost.

- Overflow / Underflow:
Converting a value that doesn't fit into the target type’s range can cause unexpected results.
Example: Casting int(300) to byte results in overflow because byte is 0–255.

- Silent Errors:
Typecasting won’t raise errors or warnings when data loss or overflow occurs; it just happens silently.

- Unexpected Sign Changes:
Casting between signed and unsigned types can change the sign and produce surprising results.

- Performance Overhead:
Although generally small, unnecessary or excessive conversions can add performance cost.

- Code Readability:
Excessive explicit casting can make code harder to read and understand.

### Finding type of a variable
In Go, there are two common ways to check or print the type of a variable:

1. reflect.TypeOf(x)
2. fmt.Printf("%T", x)

### "reflect" pacakge
!!! note "What is reflect package"
	The reflect package in Go provides runtime reflection, which means it allows a program to inspect and manipulate values, types, and even structures at runtime, even if you don’t know their exact types when writing the code.

**Type Inference**
===+ "Basic Examples"
	```
	const pi = 3.14

	var a float32 = pi     // pi becomes float32
	var b float64 = pi     // pi becomes float64
	var c complex128 = pi  // pi becomes complex128 (real part)
	```

===+ "reflect.TypeOf(x)"
	``` go
	package main

	import (
		"fmt"
		"reflect"
	)

	const pi = 3.14

	func main() {
		var a float32 = pi
		fmt.Println("Type of a (after assigning pi):", reflect.TypeOf(a)) // float32

		var b float64 = pi
		fmt.Println("Type of b (after assigning pi):", reflect.TypeOf(b)) // float64

		var c complex128 = pi
		fmt.Println("Type of c (after assigning pi):", reflect.TypeOf(c)) // complex128
	}
	```
===+ "fmt.Printf("%T", x)"
	``` go
	package main

	import "fmt"

	const pi = 3.14

	func main() {
		var a float32 = pi
		fmt.Printf("Type of a (after assigning pi): %T\n", a) // float32

		var b float64 = pi
		fmt.Printf("Type of b (after assigning pi): %T\n", b) // float64

		var c complex128 = pi
		fmt.Printf("Type of c (after assigning pi): %T\n", c) // complex128
	}
	```