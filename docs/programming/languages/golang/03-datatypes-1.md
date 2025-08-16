# **03-Data Types Part-1**

This section contains information about following topics:

- **data type**: boolean, int, float
- signed and unsigned integers
- variables of different size (8-bit, 16-bit, so on)
---

## 1. Boolean variables

- The **bool** type is one of the built-in types, and they represents boolean values — either true or false.

- They are cmmonly used for logical decisions, conditions, and flags (to be convered later in this tutorial series)

### Some examples of boolean
???+ "Click to view"

	=== "boolean example snippets"
		``` go
		//remeber that "go" is case sensitive...bool is not same as Bool
		
		var isReady bool
		fmt.Println(isReady)  // false (default value)

		//Declaration with initialization
		var isLoggedIn bool = true

		//Short variable declaration
		isAdmin := false

		//boolean expressions
		a := 10
		b := 5

		isGreater := a > b         // true
		isEqual := a == b          // false
		isValid := a > 0 && b > 0  // true
		```

	=== "A complete example"
		```
		package main

		import "fmt"

		func main() {
			var flag bool = true
			isEven := 10%2 == 0
			isEmpty := "" == ""
			
			fmt.Println("flag:", flag)
			fmt.Println("Is 10 even?", isEven)
			fmt.Println("Is string empty?", isEmpty)
		}
		```
	=== "Output"
		```
		flag: true
		Is 10 even? true
		Is string empty? true
		```

### Common usages of bool variables

|Use case|Example|
|---|---|
|Conditional logic |	```if isAdmin { ... }```|
|Loop control	|```for ok := true; ok; { ... }```|
|Function return	|```func isEven(n int) bool { return n % 2 == 0 }```|
|State/flags	|```vvar isConnected bool = false```|


## 1. integer variables
In Go, **int** is a built-in numeric type used to store whole numbers (integers). It supports both positive and negative values.

- It is a signed integer type (unless explicitly defined as **unsigned**.
- The size of int is platform-dependent:
	- 32 bits on 32-bit systems
	- 64 bits on 64-bit systems

### signed integers

|Type|	Description	|Size|
|---|---|---|
|int|	Platform-dependent integer|	32 or 64 bits|
|int8|	8-bit signed integer|	−128 to 127|
|int16|	16-bit signed integer|	−32,768 to 32,767|
|int32|	32-bit signed integer|	−2^31 to 2^31−1|
|int64|	64-bit signed integer|	−2^63 to 2^63−1|

### unsinged integers

|Type|	Description|	Value Range|
|---|---|---|
|uint|	Platform-dependent unsigned integer|	0 to 2³²−1 or 2⁶⁴−1
|uint8|	8-bit unsigned integer|	0 to 255
|uint16|	16-bit unsigned integer|	0 to 65,535
|uint32|	32-bit unsigned integer| 0 to 4,294,967,295
|uint64|	64-bit unsigned integer| 0 to 18,446,744,073,709,551,615

### signed and unsigned integer examples
???+ "Click to view"

	=== "signed int"
		``` go
		//basic example
		var age int = 30
		balance := -1500
		fmt.Println("Age:", age)
		fmt.Println("Balance:", balance)

		//int8 (Range: -128 to 127)
		var temperature int8 = -20
		fmt.Println("Temperature:", temperature)

		//int16 (Range: -32,768 to 32,767)
		var altitude int16 = 1200
		fmt.Println("Altitude:", altitude)

		//int32 (Range: -2,147,483,648 to 2,147,483,647)
		var population int32 = 1500000
		fmt.Println("Population:", population)
		
		//5. int64 (Range: Very large range, 64-bit)
		var nationalDebt int64 = -900000000000
		fmt.Println("National Debt:", nationalDebt)
		```
	=== "A complete program"
		``` go
		//a working program to demonstrate signed int (int)
		package main

		import "fmt"

		func main() {
			var x int = -100
			var y int8 = 127
			var z int16 = -32768
			var a int32 = 2000000
			var b int64 = 9223372036854775807

			fmt.Println("int:", x)
			fmt.Println("int8:", y)
			fmt.Println("int16:", z)
			fmt.Println("int32:", a)
			fmt.Println("int64:", b)
		}
		```
	=== "unsigned int"
		``` go
		//Basic uint Example
		var distance uint = 150
		fmt.Println("Distance:", distance)

		//uint8 (Range: 0 to 255)
		var brightness uint8 = 200
		fmt.Println("Brightness:", brightness)
		
		//uint16 (Range: 0 to 65,535)
		var port uint16 = 8080
		fmt.Println("Port:", port)
		
		//uint32 (Range: 0 to 4,294,967,295)
		var views uint32 = 2500000
		fmt.Println("Views:", views)
		
		//uint64 (Range: 0 to 18,446,744,073,709,551,615)
		var totalSupply uint64 = 1000000000000000
		fmt.Println("Total Supply:", totalSupply)
		```
	=== "A complete example (unsinged)"
		```
		//a working program to demonstrate unsigned int (uint)
		package main

		import "fmt"

		func main() {
			var a uint = 100
			var b uint8 = 255
			var c uint16 = 60000
			var d uint32 = 4000000000
			var e uint64 = 1234567890123456789

			fmt.Println("uint:", a)
			fmt.Println("uint8:", b)
			fmt.Println("uint16:", c)
			fmt.Println("uint32:", d)
			fmt.Println("uint64:", e)
		}
		```
## 3. floating point variables

- Floating-point numbers are used to represent real numbers (i.e., numbers with decimal points), including both fractions and very large/small values.
- In Go, floating-point numbers are represented using the built-in types:

|Type|	Precision|	Range|
|---|---|---|
|float32|	~6 decimal digits|	±1.18×10⁻³⁸ to ±3.4×10³|
|float64|	~15 decimal digits|	±2.23×10⁻³⁰⁸ to ±1.8×10³|

**float64 is the default type when you write a floating-point literal.**

### floating point examples

???+ "Click to view"

	=== "float32"
		``` go
		//Declare and initialize
		var temperature float32 = 36.6
		fmt.Println("Temperature:", temperature)
		
		//Short variable declaration
		height := float32(5.9)
		fmt.Println("Height:", height)
		
		//arithmetic operations on float
		var a float32 = 10.5
		var b float32 = 3.2

		sum := a + b        // 13.7
		diff := a - b       // 7.3
		product := a * b    // 33.6
		quotient := a / b   // ~3.28125

		fmt.Println("Sum:", sum)
		fmt.Println("Difference:", diff)
		fmt.Println("Product:", product)
		fmt.Println("Quotient:", quotient)

		```
	=== "A complete example"
		``` go
		//a working program to demonstrate float32
		package main

		import "fmt"

		func main() {
			var temp float32 = 37.5
			weight := float32(65.2)
			bmi := weight / (1.7 * 1.7) // assuming height in meters

			fmt.Println("Temperature:", temp)
			fmt.Println("Weight:", weight)
			fmt.Println("Estimated BMI:", bmi)
		}

		/* output is following:
		Temperature: 37.5
		Weight: 65.2
		Estimated BMI: 22.560553
		*/
		
		```
		
	=== "float64"
		``` go
		
		//declare and initaliaze
		var temperature float64 = 36.6
		fmt.Println("Temperature:", temperature)
		
		//Short variable declaration
		height := 5.9  // inferred as float64 by default
		fmt.Println("Height:", height)
		
		var a float64 = 10.5
		var b float64 = 3.2

		sum := a + b        // 13.7
		diff := a - b       // 7.3
		product := a * b    // 33.6
		quotient := a / b   // ~3.28125

		fmt.Println("Sum:", sum)
		fmt.Println("Difference:", diff)
		fmt.Println("Product:", product)
		fmt.Println("Quotient:", quotient)
		```
	=== "A complete example"
		``` go
		//a working program to demonstrate float64
		package main

		import "fmt"

		func main() {
			var temp float64 = 37.5
			weight := 65.2
			bmi := weight / (1.7 * 1.7) // assuming height in meters

			fmt.Println("Temperature:", temp)
			fmt.Println("Weight:", weight)
			fmt.Println("Estimated BMI:", bmi)
		}
		/* generated out is
		Temperature: 37.5
		Weight: 65.2
		Estimated BMI: 22.560553633217992
		*/
		
		```
		