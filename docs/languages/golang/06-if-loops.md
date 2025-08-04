# **06 Conditions and Loops**
- if statements
- switch statements
- loops
- break and continue
---

## 1. If statements
The if statement in Go is used to execute code conditionally—only when a given boolean expression is true.

=== "Syntax"
	``` go
	if condition {
		// code to execute if condition is true
	}
	```
	
=== "if Examples"
	``` go
	if x > 0 {
		fmt.Println("x is positive")
	}
	
	//conditions can be put within (), but this is optional
	if (x > 0) {
		fmt.Println("x is positive")
	}
	```

=== "if-else Examples"
	``` go
    if age >= 18 {
        fmt.Println("You are an adult.")
    } else {
        fmt.Println("You are a minor.")
    }
	```
	
=== "Incorrect syntax"

	``` go
	//INCORRECT because no {} (it works in C, but not in GO)
	if (x > 0) 
		fmt.Println("x is positive")
	
	//corrected is following (must use curly brackets to enclose the code block)
	if (x > 0) {
		fmt.Println("x is positive")
	}
	
	//correct
	if x > 0 {
		fmt.Println("x is positive")
	}
	
	```

### if-else statements
The if-else statement lets your program choose between two paths based on a condition.

- If the condition is true, the code inside the if block runs.
- Otherwise (condition is false), the code inside the else block runs.

=== "Syntax"
	``` go
	if condition {
		// run this if condition is true
	} else {
		// run this if condition is false
	}
	```
	
=== "if-else Examples"
	``` go
	age := 20

	if age >= 18 {
		fmt.Println("You are an adult.")
	} else {
		fmt.Println("You are a minor.")
	}
	```

### if-else ladder (chain)
An if-else ladder (also called an if-else-if chain) is a series of multiple conditions checked one after another.

- The program tests the first condition.
- If it’s false, it moves to the next condition.
- This continues until one condition is true, or it reaches the final else block (which runs if all conditions are false).

=== "Syntax"
	``` go
	if condition1 {
    // code if condition1 is true
	} else if condition2 {
		// code if condition2 is true
	} else if condition3 {
		// code if condition3 is true
	} else {
		// code if none of the above conditions are true
	}

	```
	
=== "Example"
	``` go
	score := 75

    if score >= 90 {
        fmt.Println("Grade: A")
    } else if score >= 80 {
        fmt.Println("Grade: B")
    } else if score >= 70 {
        fmt.Println("Grade: C")
    } else if score >= 60 {
        fmt.Println("Grade: D")
    } else {
        fmt.Println("Grade: F")
    }
	```

### ==switch statement
- A switch statement in Go is like an if-else ladder—both let you choose between multiple options based on conditions.

- But a switch is usually clearer and easier to read when you’re comparing one value against many possible cases.

- The default case in a switch works like the final else in an if-else ladder—it runs when none of the other cases match.


=== "Syntax"
	``` go
	switch expression {
	case value1:
		// code if expression == value1
	case value2:
		// code if expression == value2
	default:
		// code if no case matches
	}

	```
	
=== "Example"
	``` go

    day := "Tuesday"
    switch day {
    case "Monday":
        fmt.Println("Start of the week")
    case "Tuesday":
        fmt.Println("Second day")
    case "Friday":
        fmt.Println("Almost weekend!")
    default:
        fmt.Println("Just another day")
    }
	```
### When to use if-else and when to use switch?
**Use if-else for complex conditions or ranges; use switch when comparing one value against many fixed options for cleaner, easier-to-read code.**

## 2. **select** statement

**select** statements in GO are used for  concurrency to wait on multiple channel operations. It’s like a switch but for channels.
**We will cover this topic in the chapter on concurrency**

## 3. **Loops** in Go
Loops are statements which are used to repeat a block of code multiple times until a condition is met. They help automate repetitive tasks.

### **for** loops

- IMPORTANT: Go language has only ONE type of loop construct (i.e. **for** loops);  In other words Go doesn’t have while, do-while, or foreach. Everything is done using **for**.
- **while** and **do-while** type of loop constructs as found in other languages are implemented using **for** loops only. 

=== "fixed iterations"
	``` go 
	//to execute a code block for a fixed number of times
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
	```

=== "while-styled"
	``` go
	//to perform a loop until a certain condition is met
	//number of iterations may not be known in advance
	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}
	```

=== "do-while-styled"
	``` go
	//to perform a loop until a certain condition is met
	//number of iterations may not be known in advance
	//ADDITIONALLY, code must be executed ATLEAST ONCE
	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}
	```

### when to use which style
1. **traditional for loop**:  execute a code block for a fixed number of times
2. **while-styled loop**: to perform a loop until a certain condition is met. The number of iterations may not be known in advance
3. **while-styled loop**: to perform a loop until a certain condition is met. The number of iterations may not be known in advance. ADDITIONALLY, code must be executed ATLEAST ONCE.

### infinite loops

=== "Basic example"
	``` go
	for {
		fmt.Println("loop forever")
	}
	```

=== "More examples"
	``` go
	//EXAMPLE 1: break out of infinite loop when a condition is met
	i := 0
	for {
		if i >= 5 {
			break
		}
		fmt.Println(i)
		i++
	}
	fmt.Println("Loop ended")

	//Example 2
	i := 0
	for {
		i++
		if i%2 == 0 {
			continue // Skip even numbers
		}
		fmt.Println(i)
		if i >= 9 {
			break
		}
	}

	//Example 3: time delay 
	for {
        fmt.Println("Tick")
        time.Sleep(1 * time.Second)
    }

	```
### Nested loops
- A nested loop is a loop placed inside another loop.
It’s used when you need to repeat actions in a multi-level structure (like rows and columns).
- (No of iterations becomes N X M: where N is the outer loop count, and M is the inner loop count)

### Example- Multiplication Table (1 to 3)
``` go
package main

import "fmt"

func main() {
    for i := 1; i <= 3; i++ {
        for j := 1; j <= 3; j++ {
            fmt.Printf("%d x %d = %d\n", i, j, i*j)
        }
    }
}
- The outer loop (i) runs from 1 to 3.
- For each value of i, the inner loop (j) runs from 1 to 3.
- The inner loop completes all its iterations for every single iteration of the outer loop.
```




## 4. Some fine points about loops
### break (exit the loop) statement  in a loop

Example of **break**
``` go
for i := 0; i < 10; i++ {
    if i == 3 {
        break
    }
    fmt.Println(i)
}

//Example 2: Find the first match in a list
//Efficiently exit when you find the first match.
nums := []int{3, 7, 9, 12, 18}
for _, n := range nums {
    if n%6 == 0 {
        fmt.Println("Found divisible by 6:", n)
        break
    }
}
```



### continue statement in a loop
The continue statement is used to skip the rest of the current loop iteration and move directly to the next iteration.

Example of **continue**
``` go
for i := 1; i <= 5; i++ {
    if i%2 == 0 {
        continue
    }
    fmt.Println(i) // prints only odd numbers
}
```

### breaking out of nested loops (i.e. MULTIPLE loop)
- **break** statement exits from the current loop only (so if we currently in the code of inner loop, only inner loop will be exited. 
- In many situations, we would like to break out of ALL loop. 
- We achieve this by using a "label"

=== "Example: Correct"
	``` go
	package main
	import "fmt"

	func main() {
	outer: // label is here
		for i := 1; i <= 3; i++ {
			for j := 1; j <= 3; j++ {
				if i == 2 && j == 2 {
					fmt.Println("Breaking out of both loops")
					break outer // exits the outer loop entirely
				}
				fmt.Printf("i = %d, j = %d\n", i, j)
			}
		}

		fmt.Println("This runs after both loops")
	}
	```
	Following is the output
	```
	i = 1, j = 1
	i = 1, j = 2
	i = 1, j = 3
	i = 2, j = 1
	Breaking out of both loops
	This runs after both loops
	```

=== "ERROR (important)"
	``` go
	import "fmt"

	func main() {
	outer: // label is here
		//print("loop starts") : ERROR...CANNOT PUT A STATEMENT BETWEENA LABLE AND LOOP
		for i := 1; i <= 3; i++ {
			for j := 1; j <= 3; j++ {
				if i == 2 && j == 2 {
					fmt.Println("Breaking out of both loops")
					break outer // exits the outer loop entirely
				}
				fmt.Printf("i = %d, j = %d\n", i, j)
			}
		}

		fmt.Println("This runs after both loops")
	}
	``` 
=== " Breaking out of two inner loops (but not the outermost)"
	``` go
	package main

	import "fmt"

	func main() {
		for x := 1; x <= 2; x++ {
			fmt.Println("Outer loop x =", x)

		middle:
			for y := 1; y <= 3; y++ {
				for z := 1; z <= 3; z++ {
					if y == 2 && z == 2 {
						fmt.Println("Breaking from middle and inner loops")
						break middle // only breaks middle and inner
					}
					fmt.Printf("  y = %d, z = %d\n", y, z)
				}
			}
		}

		fmt.Println("Done.")
	}
	```
	Output is:
	```
	Outer loop x = 1
	  y = 1, z = 1
	  y = 1, z = 2
	  y = 1, z = 3
	  y = 2, z = 1
	Breaking from middle and inner loops
	Outer loop x = 2
	  y = 1, z = 1
	  y = 1, z = 2
	  y = 1, z = 3
	  y = 2, z = 1
	Breaking from middle and inner loops
	Done.
	```


Note:

- The outer loop does not restart (AFTER the break statement). It ends right after break outer is called.
- Execution resumes after the whole loop block.
- **do not be confused about the position of label. It is written before the loops, but the after breaking, the loops will not be executed**


### continue in nested loops (multiple loops)

=== "Example 1: Skip CURRENT loop only"
	``` go
	for i := 1; i <= 2; i++ {
		for j := 1; j <= 3; j++ {
			if j == 2 {
				continue // skip when j == 2
			}
			fmt.Printf("i = %d, j = %d\n", i, j)
		}
	}
	```
	Output:
	``` 
	i = 1, j = 1
	i = 1, j = 3
	i = 2, j = 1
	i = 2, j = 3
	```

=== "Example 2:  Skip ALL loops"
	outer:
	for i := 1; i <= 3; i++ {
		for j := 1; j <= 3; j++ {
			if j == 2 {
				fmt.Println("Skipping to next outer loop iteration")
				continue outer // skip remaining inner loop and go to next outer i
			}
			fmt.Printf("i = %d, j = %d\n", i, j)
		}
	}
	```
	
	Output:
	```
	i = 1, j = 1
	Skipping to next outer loop iteration
	i = 2, j = 1
	Skipping to next outer loop iteration
	i = 3, j = 1
	Skipping to next outer loop iteration
	```

=== "Example 3:  Skip FEW loops"
	``` go
	for i := 1; i <= 2; i++ {
	middle:
		for j := 1; j <= 2; j++ {
			for k := 1; k <= 3; k++ {
				if k == 2 {
					fmt.Println("Continuing middle loop")
					continue middle
				}
				fmt.Printf("i=%d j=%d k=%d\n", i, j, k)
			}
		}
	}
	```
	
	Output:
	```
	i=1 j=1 k=1
	Continuing middle loop
	i=1 j=2 k=1
	Continuing middle loop
	i=2 j=1 k=1
	Continuing middle loop
	i=2 j=2 k=1
	Continuing middle loop
	```

## range statement in loops
This topic will be covered in chapter of "Collectoins" ater.



