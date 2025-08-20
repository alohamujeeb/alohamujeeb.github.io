# **08 Arrays and Slices in Go**

Main topics:

- slicing
- slice literals
- reslicing and trimming
- slices for pass by reference of array

---
## 1. What is a slice?

- A slice is a special type of array, that grows automatically (under the hood) when new lement is added beyond the maximum size (i.e. capacity)

- If you are familiar with concept of **vectors** in C++, then you can relate this idea.

### Slice literal and slice from an existing array
=== "Example: slice litera"
	``` go
	package main

	import "fmt"

	func main() {
		// Create a slice using a slice literal
		nums := []int{10, 20, 30}

		// Print the slice
		fmt.Println(nums)       // Output: [10 20 30]
		fmt.Println(len(nums))  // Output: 3
		fmt.Println(cap(nums))  // Output: 3

		// Access and update an element
		nums[1] = 99
		fmt.Println(nums)       // Output: [10 99 30]

		// Append a new element
		nums = append(nums, 40)
		fmt.Println(nums)       // Output: [10 99 30 40]
		fmt.Println(len(nums))  // Output: 4 (elements)
		fmt.Println(cap(nums))  // Output: 6 (maximum capacity increased from 3 to 6)
	}
	```
	Output:
	```
	[10 20 30]
	3
	3
	[10 99 30]
	[10 99 30 40]
	4
	6
	```

=== "Example: slice from an existing array"
	``` go
	package main

	import "fmt"

	func main() {
		// Create an array
		arr := [5]int{10, 20, 30, 40, 50}

		// Create a slice referencing part of the array
		s := arr[1:4] // slice contains elements 20, 30, 40

		fmt.Println("Original array:", arr)    // [10 20 30 40 50]
		fmt.Println("Slice s:", s)             //[20 30 40]
		fmt.Println("Slice length = ", len(s)) //3
		fmt.Println("Slice cap= ", cap(s))     //4 (capacity = elements from starting index (i.e. 1) to end)

		// Modify an element in the slice
		s[1] = 99 // modifies the element at index 2 in the array

		fmt.Println("Modified slice:", s)
		fmt.Println("Array after slice modification:", arr)
		fmt.Println("Original array (after modificatio of slice):", arr) // [10 20 99 40 50]
	```
	Output:
	```
	Original array: [10 20 30 40 50]
	Slice s: [20 30 40]
	Slice length =  3
	Slice cap=  4
	Modified slice: [20 99 40]
	Array after slice modification: [10 20 99 40 50]
	Original array (after modificatio of slice): [10 20 99 40 50]
	```
	Note: Original array is also affected after the slice is modified. 
	
	**slice is actually a pointer to an array with extra information like length and capacity**

### Slice internals: three elements
The Three Elements of a Slice

- Pointer: points to the first element of the underlying array that the slice references.
- Length (len): the number of elements the slice currently holds — what you get from len(slice).
- Capacity (cap): the maximum number of elements the slice can grow to within the underlying array before needing a new allocation — what you get from cap(slice).

### append() 

- append is only applicable to slices, NOT arrays.
- It adds elements to the end of a slice, possibly increasing its capacity.

=== "Syntax"
	``` go 
	slice = append(slice, elem1, elem2, ...)
	```
=== "single element"
	``` go
	nums := []int{1, 2, 3}
	nums = append(nums, 4)
	fmt.Println(nums) // Output: [1 2 3 4]
	```

=== "multiple elements"
	``` go
	nums := []int{1, 2, 3}
	nums = append(nums, 4, 5, 6)
	fmt.Println(nums) // Output: [1 2 3 4 5 6]
	```

=== "two slices appended"
	``` go
	a := []int{1, 2}
	b := []int{3, 4}
	a = append(a, b...)
	fmt.Println(a) // Output: [1 2 3 4]
	
	var s []int
	s = append(s, 10)
	fmt.Println(s) // Output: [10]
	```

## 2. How much capacity increases
When you append an element and capacity is exceeded, Go allocates a new underlying array with larger capacity.

- The growth strategy depends on the current capacity:

	- for small slices (capacity < 1024 elements), capacity roughly doubles.
	- for large slices (capacity ≥ 1024), capacity grows by about 25% each time.

Note: In the example in previous section, the capacity increased from  3 to 6 (i.e. doubled) when a new element was added after exceeding the capacity


## 3. What happens to original array when capacity exceeds

When you append to a slice and its length reaches its capacity, Go allocates a new, bigger underlying array.

- The existing elements are copied to this new array, and the slice now points to this new array.
- The original array remains unchanged because the slice no longer references it.

Example:
``` go
package main

import "fmt"

func main() {
	// Original array
	arr := [3]int{10, 20, 30}

	// Create a slice referencing the array
	s := arr[:]
	fmt.Println("Before append:")
	fmt.Println("Slice s:", s)                  // [10 20 30]
	fmt.Println("Array arr:", arr)              // [10 20 30]
	fmt.Println("len:", len(s), "cap:", cap(s)) // len:3 cap:3

	// Append element beyond capacity
	s = append(s, 40)

	fmt.Println("\nAfter append:")
	fmt.Println("Slice s:", s)                        // [10 20 30 40]
	fmt.Println("original Array arr:", arr)           // [10 20 30]  (unchanged)
	fmt.Println("slice len:", len(s), "cap:", cap(s)) // len:4 cap:6 (capacity grows)

	// Edit the first lement
	s[1] = 99 //this element is within the range of original array length
	fmt.Println("\nAfter Editing:")
	fmt.Println("Slice s:", s)                        // [10 20 30 40]
	fmt.Println("original Array arr:", arr)           // [10 20 30]  (unchanged)---hence once exceeded the original array stops reflecting the slice (but before exceeding it reflects slice)
	fmt.Println("slice len:", len(s), "cap:", cap(s)) // len:4 cap:6 (capacity grows)
}
```
```
Before append:
Slice s: [10 20 30]
Array arr: [10 20 30]
len: 3 cap: 3

After append:
Slice s: [10 20 30 40]
original Array arr: [10 20 30]
slice len: 4 cap: 6

After Editing:
Slice s: [10 99 30 40]
original Array arr: [10 20 30]
slice len: 4 cap: 6
```
Note: 
- Once exceeded the original array stops reflecting the slice 
- but before exceeding it reflects slice.

### Sharing underlying array (more detail)
As shown in example above:

- When you create a slice from an array or another slice, the new slice shares the same underlying array. This means:
- Changes made through the slice will reflect in the original array (or other slices from the same array).
- This saves memory and is efficient, but can lead to unintended side effects if you're not careful.

Example:
``` go
package main

import "fmt"

func main() {
    arr := [5]int{10, 20, 30, 40, 50}

    s1 := arr[1:4]  // s1 = [20 30 40]
    s2 := s1[1:]    // s2 = [30 40]

    s2[0] = 999     // modifies arr[2]

    fmt.Println("Array:", arr) // [10 20 999 40 50]
    fmt.Println("s1:", s1)     // [20 999 40]
    fmt.Println("s2:", s2)     // [999 40]
}
```
Note:

- s1 and s2 both reference the same original array (arr).
- A change through s2 modified the array and was visible through s1 as well.


## 4. Reslicing
What is Reslicing?

- Reslicing means creating a new slice from an existing slice by slicing it again.
- We are creating a view/window over a portion of the original slice’s elements.
- Reslicing does not copy data; the new slice still points to the same underlying array.

=== "syntax"
	``` go
	newSlice := oldSlice[start:end]
	```

=== "Example"
	``` go
	package main

	import "fmt"

	func main() {
		s := []int{10, 20, 30, 40, 50}

		// Original slice
		fmt.Println("Original slice:", s)  // [10 20 30 40 50]

		// Reslice from index 1(inclusive) to 4(exclusive) (elements 20,30,40)
		sub := s[1:4]
		fmt.Println("Resliced slice:", sub)  // [20 30 40]

		// Modify resliced slice
		sub[1] = 99

		// Both slices share underlying array, so original changes too
		fmt.Println("Modified resliced slice:", sub)  // [20 99 40]
		fmt.Println("Original slice after modification:", s)  // [10 20 99 40 50]
	}
	```
	
- start is the starting index (inclusive)
- end is the ending index (exclusive)
- Both start and end must be within the slice’s length (not capacity)

### Trimming
Trimming is a special case of reslicing where you're dropping elements from the start or end of the slice.

``` go
s := []int{10, 20, 30, 40, 50}

// Trim first two elements
trimStart := s[2:]     // [30 40 50]

// Trim last two elements
trimEnd := s[:3]       // [10 20 30]

// Trim both sides
trimBoth := s[1:4]     // [20 30 40]
```

Note:

- We are not deleting anything; we are just narrowing the view.
- The underlying array remains the same.
- This is very memory-efficient, but:
	- The backing array may still keep the "trimmed" elements
	- Can cause memory leaks if the backing array is large and not needed

### About memory leaks in trimming

- Go has garbage collection (GC) — it will automatically free memory that is no longer referenced.
But GC can only collect memory that is truly unreachable.

- When you reslice or trim a slice, the new slice still points to the original underlying array — even if you only use a small part of it.

- The entire array stays in memory, because a portion of it is still referenced.
	- If the original array is large, this causes memory to be retained unnecessarily.
	- This isn’t a memory leak in the classical sense (like in C/C++), but it’s wasted memory; often called a “semileak”.

``` go
func leak() []int {
    // Create a large array (e.g., 1 million elements)
    large := make([]int, 1_000_000)

    // Trim and return a small slice
    return large[999_990:]  // Just the last 10 elements
}
```

We  might think that we are only keeping a slice of 10 elements, but:

- The slice still points to the full 1-million-element array.
- So Go cannot free that array, because 10 elements are still referenced.
- This can quietly accumulate over time — especially in long-running services.


## 5. make() and copy()
- make() and copy() are two built-in functions in Go used primarily to work with slices, maps, and channels (not arrays directly).

- make() is used to create and allocate memory for slices, maps, and channels.
- copy() copies elements between slices.

- Unlike range(), which is a language keyword used for iteration, make() and copy() are standard library functions.

``` go
src := []int{1, 2, 3}
dst := make([]int, len(src))  // create a new slice with the same length
copy(dst, src)                // copy data from src to dst

dst[0] = 99                  // modify dst
fmt.Println("src:", src)     // [1 2 3]  (unchanged)
fmt.Println("dst:", dst)     // [99 2 3] (changed)
```

## 6. Shallow vs deep copy of slices

Deep copy:	

- Copying the actual data into a new underlying array.
- The new slice is completely independent of the original.
- Changes to one will not affect the other.

Shallow copy:

- Only copies the slice header (pointer, length, capacity).
- Both original and shallowCopy point to the same underlying array.
- So, changing one affects the other.


=== "Slice- shallow copy"
	``` go
	package main

	import "fmt"

	func main() {
		// Original slice
		original := []int{1, 2, 3, 4, 5}

		// Shallow copy: just assign the slice
		shallowCopy := original

		// Modify the "copy"
		shallowCopy[0] = 99

		// Print both slices
		fmt.Println("Original slice:", original)     // [99 2 3 4 5]
		fmt.Println("Shallow copy:  ", shallowCopy)  // [99 2 3 4 5]
	}
	```

=== "Slice- deep copy"
	``` go
	package main

	import "fmt"

	func main() {
		// Original slice
		original := []int{1, 2, 3, 4, 5}

		// Create a new slice with same length
		copySlice := make([]int, len(original))

		// Copy data from original to copySlice
		copy(copySlice, original)

		// Modify the copy
		copySlice[0] = 99

		// Print both slices
		fmt.Println("Original slice:", original)   // [1 2 3 4 5]
		fmt.Println("Copy slice:    ", copySlice)  // [99 2 3 4 5]
	}
	```
## 7. Multidimentional slices

=== "An empty 2D slice"
	``` go
	var matrix [][]int
	fmt.Println(matrix) // Output: []
	```
=== "2D slice (literal)"
	``` go
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println(matrix)
	// Output:
	// [[1 2 3]
	//  [4 5 6]
	//  [7 8 9]]
	```
	
=== "zero initialized with make()"
	``` go
	rows, cols := 3, 4

	matrix := make([][]int, rows)    // Create outer slice with 3 rows

	for i := range matrix {
		matrix[i] = make([]int, cols)  // Initialize each row with 4 columns
	}

	// Now matrix is 3x4 filled with zeros (default int value)

	fmt.Println(matrix)
	/* Output:
	[[0 0 0 0]
	 [0 0 0 0]
	 [0 0 0 0]]
	*/
	```
	

### Some examples for variety

=== "variety example-1"
	``` go
	package main

	import "fmt"

	func main() {
		// Existing arrays (each represents a row)
		row1 := [3]int{1, 2, 3}
		row2 := [3]int{4, 5, 6}
		row3 := [3]int{7, 8, 9}

		// Convert arrays to slices and combine into a 2D slice
		matrix := [][]int{
			row1[:],
			row2[:],
			row3[:],
		}

		fmt.Println(matrix)
		// Output:
		// [[1 2 3]
		//  [4 5 6]
		//  [7 8 9]]
	}

	```

=== "variety example-2"
	``` go
	package main

	import "fmt"

	func main() {
		// Define a 2D array (3x3)
		var arr [3][3]int = [3][3]int{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		}

		// Create a 2D slice from the 2D array by slicing each row
		matrix := make([][]int, len(arr))
		for i := range arr {
			matrix[i] = arr[i][:]  // slice each row of the array
		}

		fmt.Println(matrix)
		// Output:
		// [[1 2 3]
		//  [4 5 6]
		//  [7 8 9]]
	}
	```

### Slices are only 1D (2D copy not allowed)	

**Important**:In Go, we cannot directly slice a multidimensional array as a whole into a multidimensional slice. Slicing works only on one-dimensional arrays or slices.

Given an array of:

```var arr [3][3]int```

Following is INVALID:
```
// Error: arr is [3][3]int, can't slice like this directly
slice := arr[:]  
```

=== "Solution 1"
	``` go
		//Solution-1: Create a 2D slice from a 2D array (row-by-row slicing)
		package main

		import "fmt"

		func main() {
			arr := [3][3]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			}

			// Create 2D slice from 2D array
			matrix := make([][]int, len(arr))
			for i := range arr {
				matrix[i] = arr[i][:]  // slice each row (array -> slice)
			}

			fmt.Println(matrix)
			// Output:
			// [[1 2 3]
			//  [4 5 6]
			//  [7 8 9]]
		}
	```

=== "Solution 2"
	``` go
	//Solution 2: Flatten 2D array into 1D slice
	package main

	import "fmt"

	func main() {
		arr := [3][3]int{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		}

		flat := make([]int, 0, len(arr)*len(arr[0]))
		for i := range arr {
			flat = append(flat, arr[i][:]...)
		}

		fmt.Println(flat)
		// Output: [1 2 3 4 5 6 7 8 9]
	}
	```
## 8. Slices for pass-by-reference 

=== "Example(literal slice)"
	``` go
	package main

	import "fmt"

	// modifySlice changes the first element of the slice
	func modifySlice(s []int) {
		s[0] = 100
	}

	func main() {
		nums := []int{1, 2, 3}
		fmt.Println("Before:", nums)

		modifySlice(nums)  // passing slice (reference to underlying array)

		fmt.Println("After:", nums)
	}
	```
	Output:
	```
	Before: [1 2 3]
	After: [100 2 3]
	```

=== "Example (underlying array)"
	``` go
	package main

	import "fmt"

	// Function modifies the slice
	func modifySlice(s []int) {
		s[0] = 100 // this will affect the original array
	}

	func main() {
		// Original array
		arr := [3]int{1, 2, 3}

		// Create a slice from the array
		slice := arr[:] // full slice of array

		fmt.Println("Before:")
		fmt.Println("Array:", arr)
		fmt.Println("Slice:", slice)

		// Pass slice to function (modifies underlying array)
		modifySlice(slice)

		fmt.Println("\nAfter:")
		fmt.Println("Array:", arr)   // changed!
		fmt.Println("Slice:", slice) // also changed
	}
	```
	Output:
	```
	Before:
	Array: [1 2 3]
	Slice: [1 2 3]

	After:
	Array: [100 2 3]
	Slice: [100 2 3]
	```
