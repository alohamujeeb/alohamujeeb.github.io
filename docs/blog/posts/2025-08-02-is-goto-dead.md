---
date: 
  created: 2025-08-02
  posted:  2025-08-01
author:
  name: Mujeeb
  description: Creator
readtime: 10

categories: 
  - Programming
tags:
  - goto
  - structured programming
---

# Is **goto** statement dead?

---
Structured programming became mainstream in the 1970s and 1980s. It  is a programming paradigm that emphasizes writing clear, logical, and well-organized code using:

1. Sequence – code runs in order
2. Selection – decisions using if, else, switch
3. Loops – repetition using for, while, etc.
<!-- more -->

## goto statment
A fourth type of statement, the **goto** statement, was widely used before structured programming. However, it is considered harmful because it makes code harder to understand and maintain.

Consider the following two examples—one using a goto statement and one without—to illustrate how goto can impact code readability.

=== "code WITH goto"
	``` c
	#include <stdio.h>

	int a = 48, b = 18;  // global for simplicity
	int result;

	int main() {
		goto compute_gcd;

	return_point:
		printf("GCD is: %d\n", result);
		return 0;

	// "Simulating a function call"
	compute_gcd:
		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}
		result = a;
		goto return_point;  // simulate "return"
	}
	
	```
	Note the following about the program (goto version):

	- It uses two labels: compute_gcd and return_point.
	- The code first jumps to compute_gcd, and after calculating the result, it jumps back to return_point using another goto.
	- If this kind of jumping occurs hundreds of times in a program, it quickly becomes difficult to follow the flow.
	- Moreover, using unclear or unintuitive label names can make the code even harder to understand.
	- In contrast, consider the version of the code that uses functions exclusively — it’s much clearer and easier to maintain.
	

=== "code WITHOUT goto"
	``` c
	#include <stdio.h>

	int gcd(int a, int b) {
		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}
		return a;
	}

	int main() {
		int result = gcd(48, 18);
		printf("GCD is: %d\n", result);
		return 0;
	}
	```
	
	Note the following about the program (without goto):

	- the main() function uses only one statement to perform the task—calling gcd() and then continuing after it returns.

	- instead of using goto jumps, we simply call the function by its name. Although the underlying mechanism involves jumps at the machine level, from the programmer’s perspective it’s just a straightforward statement without explicit jumps or goto.

	- this approach greatly improves the readability and clarity of the code.		
		

## goto statments replaced by functions
From the examples above, you can see that the same task can be accomplished with a single statement—a function call.

From a code reviewer’s perspective, it’s just one statement, even though the function itself may contain dozens or hundreds of lines of code.

This is why structured programming emphasizes using only three types of statements:

1. Sequential (organized through functions)
2. Conditional (if, if-else, switch, etc.)
3. Loops (for, while, etc.)

The following code snippet (taken from the example above) demonstrates how creating a function instead of using a goto statement leads to a purely sequential code flow, thereby improving code clarity.

``` c
    // the code now becomes a sequntial code of three statemetns only
int main() {
	int result = gcd(48, 18);  	
    printf("GCD is: %d\n", result);
    return 0;
}
```

Note:

**In the early days, programmers found it difficult to write code without using goto. However, today we understand that avoiding goto is not a problem at all.**


## goto is not always bad

- there are certain situations where using goto (or an equivalent) can simplify the code.

- one such example is breaking out of nested loops.

- while a break statement exits only the innermost loop, it can be tricky to exit multiple levels of nested loops.

- using a goto statement with a labeled target allows you to jump out of one or more loops easily, **providing a clean way to handle such cases** (which was ironically the orignal purpose of AVOIDING goto).


=== "break out of nested loops(without goto)"
	``` c
	#include <stdio.h>

	int main() {
		int i, j;
		int done = 0;  // flag to indicate when to break outer loop

		for (i = 0; i < 5; i++) {
			for (j = 0; j < 5; j++) {
				printf("i=%d, j=%d\n", i, j);
				if (i == 2 && j == 3) {
					done = 1;  // set flag
					break;     // break inner loop
				}
			}
			if (done) {
				break; // break outer loop if flag is set
			}
		}

		printf("Exited nested loops\n");
		return 0;
	}
	```

	```
	- In this example, to break out of the outer loop, a flag variable done is used. The outer loop checks this flag, and if it’s set to true, it breaks as well.

	- However, this approach isn’t very intuitive.

	- The same behavior can be achieved more simply using a goto statement.
	```
	


=== "break out of nested loops(WITH goto)"
	``` c
	#include <stdio.h>

	int main() {
		int i, j;

		for (i = 0; i < 5; i++) {
			for (j = 0; j < 5; j++) {
				printf("i=%d, j=%d\n", i, j);
				if (i == 2 && j == 3) {
					goto exit_loops;  // Jump out of both loops
				}
			}
		}

	exit_loops:
		printf("Exited nested loops\n");
		return 0;
	}
	```

	```
	- in this example using goto, breaking out of the outer loop is  more intuitive and cleaner compared to the version without goto.
	 
	- therefore, the goto statement can be helpful in situations like this.
	- The same behavior can be achieved more simply using a goto statement.
	```


## Should we use goto?

- A pedantic programmer might argue that goto should never be used.

- However, it’s important to understand that goto was discouraged mainly because it often led to confusing and hard-to-follow code.

- In certain cases—like the nested loop example above—goto actually improves readability and simplifies the logic.

- Therefore, there’s no strong reason to oppose its use outright.

- Jumping **ACROSS** function boundaries was the primary (mis)use that led to goto being discouraged. However, there is no reason why it should NEVER be used even within a single function comprising very few lines.


## goto in Go (Golang) language 

- goto has actually made a come back in the case nested loop breaks in Go language.

- to break out of nested loops we use the "labels" (and not explicitly goto). However, the logic is still the same (i.e. jumps to certain label, which is what traditional goto statment does).

=== "Example 1: break WITHOUT label"
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
	**This code 'breaks' from the current loop only (not from all)**



=== "Example 2:  break WITH labels"
	``` go
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
	**This code 'breaks' from the ALL loops**

	
=== "Example 3:  break MIDDLE loop (WITH labels)"
	
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
	**This code 'breaks' from two loops out of three loops (hence more refined control)
	
**It can much more complicated to break out of selected loop by using flag variables at different levels. A cleaner logic would be to use labels (i.e. hidden goto statements)**

## Inter-Function vs. Intra-Function use of goto
```goto``` was originally discouraged at the **cross-function** level because jumping between functions breaks modularity and disrupts structured control flow, making the code harder to understand and maintain. However, when used within a single function—especially in small functions—it generally doesn't harm readability and can even simplify error handling or cleanup in some cases.


## Summary
- goto is a discouraged programming construct and has become nearly obsolete in most cases since the rise of structured programming in the late 1970s.

- The main reason for this is its negative impact on code readability.

- However, in certain scenarios—such as breaking out of nested loops—it can actually improve readability and give finer control over program flow.

- A relatively new and popular language, Go (Golang), does not have traditional goto statements but supports labeled breaks, which serve a similar purpose for exiting loops.

- These "labelled breaks" in Go are intended for more localized use within functions or loops, unlike traditional goto which could jump anywhere in the program.

- So, while goto itself is rarely used today, its adapted form—label-based breaks—still finds practical use in specific situations. 

---
**To Reiterate:**

 Jumping **ACROSS** function boundaries was the primary (mis)use that led to goto being discouraged; there is no reason why it should NEVER be used even within a single function comprising very few lines.
