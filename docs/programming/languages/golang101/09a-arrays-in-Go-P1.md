# **08 Arrays and Slices in Go**

Main topics:

- arrays
- multidimensional arrays
- passing arrays as parameters
- passing arrays as return types
- operations on arrays
- make a copy of an array
---
## 1. What is an array

- An array in Go is a fixed-size, ordered collection of elements of the same type. Once an array is created, its size cannot be changed.

- Think of it like a container with a set number of boxes, each holding a value of the same type (like all integers, or all strings).

- The concept of arrays in Go is same as in strong types languages like C/C++ and Java (not like Python)

### Features

- Fixed size (decided at the time of declaration)
- Stores values of the **same type**
- Stored in contiguous memory
- indexng start from 0 (not from 1)
- Passed by value to functions (i.e., copied): **this is different than what happens in C/C++, where arrays are passed by reference**

---
## 2. Syntax and examples

Syntax:

``` go var arrayName [size]Type```

=== "local arrays example"
	``` go
	package main

	import "fmt"

	func main() {
		var nums [3]int            // declares an array of 3 integers
		nums[0] = 10               // assign values
		nums[1] = 20
		nums[2] = 30

		fmt.Println(nums)          // Output: [10 20 30]
		fmt.Println(nums[1])       // Output: 20
	}
	```
	output:
	```
	[10 20 30]
	20
	```
=== "Global arrays example"
	``` go
	package main

	import "fmt"

	// Global array with inferred length
	var colors = [...]string{"Red", "Green", "Blue"}

	func main() {
		fmt.Println(colors)           // Output: [Red Green Blue]
		fmt.Println(len(colors))     // Output: 3
	}
	```
	Output:
	```
	[Red Green Blue]
	3
	```
	



### Short initialization 
Similar to short initialization of variables.

=== "short initialization"	
	``` go
	func main() {
		fruits := [3]string{"Apple", "Banana", "Cherry"}
		fmt.Println(fruits)        // Output: [Apple Banana Cherry]
	}
	```
	
### inferred lengths (short-declaration)

**similar to short-declaration for variables**

=== "compiler inferred"	
	``` go
	func main() {
		primes := [...]int{2, 3, 5, 7, 11}
		fmt.Println(primes)        // Output: [2 3 5 7 11]
	}
	```
**Note: Inferred type with := is not allowed at package (global) level**
(same as variables, where := can only be used for local (within function) variables)

---
## 3. Multidimentional Arrays
Declaring and Initializing 2D Arrays

``` go
var matrix [3][3]int

OR
matrix := [3][3]int{
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
}
```

---
## 4. Processing arrays

### Reading and wrting values

=== "Read example"
	``` go
	nums := [4]int{10, 20, 30, 40}
	fmt.Println(nums[0]) // Outputs: 10
	fmt.Println(nums[2]) // Outputs: 30
	```
=== "Update example"
	``` go
	nums := [4]int{10, 20, 30, 40}
	nums[1] = 50          // Update the second element
	fmt.Println(nums[1])  // Outputs: 50
	fmt.Println(nums)     // Outputs: [10 50 30 40]
	```

### loop through arrays

=== "Using len()"

	```
	package main

	import "fmt"

	func main() {
		nums := [4]int{1, 2, 3, 4}

		// Using classic for loop with len()
		for i := 0; i < len(nums); i++ {
			fmt.Println(nums[i])
		}
	}
	```
	Output:
	```
	1
	2
	3
	4
	```

=== "Using range"

	```
	package main

	import "fmt"

	func main() {
		nums := [4]int{1, 2, 3, 4}

		// Using range to iterate
		for index, value := range nums {
			fmt.Printf("Index %d = %d\n", index, value)
		}
	}
	```
	Output:
	```
	Index 0 = 1
	Index 1 = 2
	Index 2 = 3
	Index 3 = 4
	```

### Iterating over multidimensional arrays

=== "Using len()"
	```go 
	matrix := [3][3]int{
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
	}

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			fmt.Printf("%d ", matrix[i][j])
		}
		fmt.Println()
	}
	```
	Output:
	```
	1 2 3 
	4 5 6 
	7 8 9 
	```
	
=== "Using range"
	```go 
	matrix := [3][3]int{
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
	}
	
	for i, row := range matrix {
		for j, val := range row {
			fmt.Printf("%d ", val)
		}
		fmt.Println()
	}
	```
	Output:
	```
	1 2 3 
	4 5 6 
	7 8 9 
	```

### "range" vs len()
len() and range are two built-in features in Go used to work with arrays and other collections — len() returns the number of elements, while range is used to iterate through them.

- **len()** is a built-in function in Go — it’s part of the language and doesn’t require importing any library.

- **range** is a keyword used in for loops to iterate over elements.

- range produces two values during iteration:
	- Index (or key): the position or key of the current element
	- Value: the element at that index or key

- The “index” returned by range is not always a numeric position.
	- For arrays and slices, it is a zero-based integer index.
	
	- For maps (dictionaries), it is the key, which can be of any comparable type (string, int, etc.).
(more on indexes in the topic of collections)

---
## 5. Zero values

- This concept in arrays is same as zero-values for variables.

- when you declare an array without explicitly initializing its elements, all elements are automatically set to their zero value.

-The zero value depends on the element’s type:
	- For numbers (int, float), zero value is 0
	- For booleans, zero value is false
	- For strings, zero value is "" (empty string)
	- For pointers, interfaces, slices, maps, channels, functions, zero value is nil
	

---
## 6. Array Operations

### Copy, Compare
==="Copy Arrays"
	``` go
	a := [3]int{1, 2, 3}
	b := a          // copy
	b[0] = 10
	fmt.Println(a)  // [1 2 3]
	fmt.Println(b)  // [10 2 3]
	```
	
==="Compare Arrays"
	``` go
	a := [3]int{1, 2, 3}
	b := [3]int{1, 2, 3}
	c := [3]int{4, 5, 6}
	fmt.Println(a == b)  // true
	fmt.Println(a == c)  // false
	```

### Pass by value to functions
Arrays are passed by value to functions, meaning a copy is made. Changes inside the function do not affect the original array.

``` go
func modify(arr [3]int) {
    arr[0] = 100
}

func main() {
    a := [3]int{1, 2, 3}
    modify(a)
    fmt.Println(a)  // [1 2 3], unchanged
}
```

### What to do for pass by reference?
If we want to pass array as parameter to a function by reference (and not by value), then we can use slices

(as explained in the next section)


### Return values from functions
The array is copied when returned (not by reference as in C/C++)
``` go
func createArray() [3]int {
    return [3]int{7, 8, 9}
}

func main() {
    arr := createArray()
    fmt.Println(arr)  // [7 8 9]
}
```

---
## 7. Shallow and deep copy

To make a copy of an array, elements are copied one by one manually:

### Deep copy: Method 1 (one by one manually)
``` go
package main

import "fmt"

func main() {
    // Original array
    original := [5]int{1, 2, 3, 4, 5}

    // Copy array (same size)
    var copy [5]int

    // Copying elements manually
    for i, v := range original {
        copy[i] = v
    }

    // Output
    fmt.Println("Original array:", original)
    fmt.Println("Copied array:  ", copy)

    // Modify the copy to show they're independent
    copy[0] = 99

    fmt.Println("\nAfter modifying the copied array:")
    fmt.Println("Original array:", original)
    fmt.Println("Copied array:  ", copy)
}
```
Output:
```
Original array: [1 2 3 4 5]
Copied array:   [1 2 3 4 5]

After modifying the copied array:
Original array: [1 2 3 4 5]
Copied array:   [99 2 3 4 5]
```
### Method-2: use of = operator

=== "Shallow copy of array"
	``` go
	package main

	import "fmt"

	func main() {
		original := [5]int{1, 2, 3, 4, 5}

		// Shallow copy via pointer
		ptrCopy := &original

		ptrCopy[0] = 99

		fmt.Println("Original array:", original)   // [99 2 3 4 5]
		fmt.Println("Pointer copy:  ", *ptrCopy)   // [99 2 3 4 5]
	}
	```

=== "Deep copy of array"
	``` go
	package main

	import "fmt"

	func main() {
		original := [5]int{1, 2, 3, 4, 5}

		// Deep copy: regular assignment copies all values
		copyArray := original

		copyArray[0] = 99

		fmt.Println("Original array:", original)   // [1 2 3 4 5]
		fmt.Println("Copy array:    ", copyArray)  // [99 2 3 4 5]
	}
	```

## 8. A note about make() and copy() for Arrays

- We cannot use make() with arrays.

- Arrays are fixed-size, value types, and their size must be known at compile time — they do not support make().

make() is only for:
- Slices
- Maps
- Channels

- copy() works with slices, not raw arrays.
	- However, you can copy an array into a slice, or convert arrays to slices, and then use copy().

