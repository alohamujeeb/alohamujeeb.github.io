# **01-Getting Started**

	Go Installation

	Hello World

	Semicolons(;) in Go

---

## 1. **Go Installation**

=== "Linux (Ubuntu)"

	1. To installo: type following in the terminal
	```
    sudo apt update && sudo apt upgrade
    sudo apt install golang-go
    ```
    2. To check installation:
	
		type ```go version```
		
		Expected output:
		``` text
		go version go1.22.2 linux/amd64
		```


=== "Windows"

	1. Download MSI installer from Go website
	2. Open the MSI file you downloaded and follow the prompts to install Go. 
	By default, the installer will install Go to Program Files or Program Files (x86). You can change the location as needed.     
	3. Open the command prompt (or PowerShell)
		
		type ```go version```
		
		Expected output:
		``` text
		go version go1.24.4 windows/amd64
		```
	
---
## 2. **Hello World** 

This chapter describes how to write your first program in Go language.

Following is a **standalone** program in Go

In this exmple, we are printing some statements. We use **Println** and **Print**

- fmt.Print() prints output without a newline at the end.
- fmt.Println() prints output with a newline. 

Create a file with any name of your choice, e.g. **helloGo.go** and copy following contents in it.

=== "Println example"
	``` go
	//Single line comment

	/* 
	Multi-line comments
	line 2 of comments
	*/

	package main

	import "fmt"

	func main() {
		//fmt.Println() prints output with a newline. 
		fmt.Println("Hello World")
		fmt.Println("My name is Mujeeb")
	}
	```
	output:
	```
	Hello World
	My name is Mujeeb
	```

=== "Print example"
	``` go
	package main

	import "fmt"

	func main() {
		//fmt.Print() prints output without a newline at the end.
		fmt.Print("Hello World")
		fmt.Print("My name is Mujeeb")
	}
	```
	output:
	```
	Hello WorldMy name is Mujeeb
	```
### A note on comments

	Comments in Go can be single-line or multi-line, similar to how they are used in C++ or Java.


---
## **How to compile and run**
=== "Linux (Ubuntu)"

    1. Open the terminal.
    2. Compile the program by typing **go build helloGo.go**

        An executable file is generated with name **helloGo**
    3. Run the program by typing its name **./helloGo**


---
## 3. Semicolons(;) in Go

- Semicolons are required by the Go language (**internally**).  But you usually don’t write it yourself — the Go compiler inserts it for you automatically during parsing.


###  When you MUST write semicolons

- If you try to write multiple statements on one line without ;, it will cause a compile error:
``` go
x := 10 y := 20 // INVALID

x := 10; y := 20 // VALID, but discouraged
```

So, in practice:

- Semicolons are required by the spec, but Go handles them for you automatically
- You should avoid writing them manually, unless you're writing multiple short statements on the same line (which is not recommended)


---
## 4. **Points to remember**
- Go comment style is same as C/C++.
- A standalone application must inclue **pacakge main" statement on top
- **fmt.Println("Hello World")** is equivalent of **printf** statement in C/C++
- **Code indentation** is not required, but highly recommended for readability. We can use **tabs** or **spaces** (same as in C/C++ or Java)
- for prints and some other input/output statements, golang package is **fmt** which must be included
- **starting curly bracket **{** MUST be one same line** as the function name. Unlike C/C++ or Java, we cannot write it to the next line.
- **semicolons** are optional in Go, unless you are writing multiple statements on a single line (which is  discouraged)


=== "Incorrect"
      
    ``` go
    func main() 
    {
        fmt.Println("Hello World")
    }
    
    ```
    

=== "Correct"

    ``` go
    func main() {
        fmt.Println("Hello World")
    }
    
    ```

---
## 5. Check your understanding
??? question "What package should your main executable Go program be in?"
	Ans: package main

??? question "What is the significance of the main function in a Go program?"
	Ans: It’s the entry point where program execution starts.

??? question "How do you import other packages into your Go file?"
	Ans: Using the import keyword followed by the package name(s).
	``` go
	import (
    "fmt"
    "math"
	)
	```
??? question "What does fmt.Println do?"
	Ans: Prints text with a newline to the console.	

??? question "What package is needed to use Println?"
	Ans: fmt

??? question "What is the difference between Print and Println from the fmt package?"
	Ans: Print doesn’t add a newline; Println adds a newline at the end.

??? question "Is the main function mandatory for all Go programs?"
	Yes, for executable programs (i.e main package)
	No, for other packages

??? question "How do you write a comment in Go?"
	Ans: Use ```//``` for single-line comments, and ```/* */``` for multi-line comments
	``` go
	# single line comment: This is a comment statement
	
	/* multi-line comment
	line 2
	*/
	```

??? question "Can the main function take parameters or return values?"
	Ans: No, main must have no parameters or return values.

??? question "What are alternate ways to pass command line arguments and return code?"
	Ans: If you want to handle command-line arguments, 
	
	- use the os.Args slice instead.
	- To signal an exit status, use os.Exit(code).
	
	**(Note: They are not covered in this lesson)**

??? question "What happens if you try to declare main with a capital letter like Main?"
	Ans: It won’t be recognized as the entry point; program won’t run as expected.

??? question "How do you run a Go program in console?"
	Ans: Use ```go run filename.go``` 
	
	or build with ```go build <inputfile.go>`<outfile>```and run the generated executable by typing its name in the console
??? question "What is wrong (if any) with the following code?"
	Ans: Go  places the opening { on the same line as the function declaration; the correct code is following.
	``` go
	func main() {
		fmt.Println("Hello World")
	}
	```
``` go
func main() 
{
    fmt.Println("Hello World")
}
```