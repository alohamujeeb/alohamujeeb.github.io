# **01-Getting Started**

## **Go Installation**




=== "Linux (Ubuntu)"

    Type following in the terminal

    ```
    sudo apt update && sudo apt upgrade
    sudo apt install golang-go
    
    ```
    to check the instllation:
    type **go version**
    
=== "Windows"

   1. Download MSI installer from Go website
    2. Open the MSI file you downloaded and follow the prompts to install Go. 
        
        By default, the installer will install Go to Program Files or Program Files (x86). You can change the location as needed. 
        
    3. Open the command prompt (or PowerShell)
        
        type **go version**
    
        If everything is OK, you should see go version information.



## **Hello World**

This chapter describes how to write your first program in Go language.

Following is a **standalone** program in Go

Create a file with any name of your choice, e.g. **helloGo.go** and copy following contents in it.


``` go
//Single line comment

/* 
Multi-line comments
line 2 of comments
*/

package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

## **How to compile and run the program**
=== "Linux (Ubuntu)"

    1. Open the terminal.
    2. Compile the program by typing **go build helloGo.go**

        An executable file is generated with name **helloGo**
    3. Run the program by typing its name **./helloGo**




## **Points to remember**
- Go comment style is same as C/C++.
- A standalone application must inclue **pacakge main" statement on top
- ** fmt.Println("Hello World")** is equivalent of **printf** statement in C/C++
- **Code indentation** is not required, but highly recommended for readability. We can use **tabs** or **spaces** (same as in C/C++ or Java)
- for prints and other IOs, golang package is **fmt** which must be included
- **starting curly bracket **{** MUST be one same line** as the function name. Unlike C/C++ or Java, we cannot write it to the next line.


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
