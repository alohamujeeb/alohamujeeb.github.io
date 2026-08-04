---
hide:
  - navigation
  
tags:
  - bash
  - linux scripting
---

#Bash Scripting

---
## 1. Introduction

- **Bash** (Born Again Shell) is a command-line utility used to interact with Unix and Linux systems. 
- We use **CLI commands** that are executed by the Bash. 

- This typing of commands could be a tedious task if many commands are to be executed with various parameter options. We need a way to **automate** the long processes such as managing files, installing software, or configuring systems.

- A **Bash script** is a text file that contains a series of Bash commands, allowing users to automate tasks they would normally type manually in the terminal.

- Bash is not just a command-line utility; it's also a **simple programming language**. It includes constructs like variables, arrays, loops, and conditional statements, which allow users to run commands in a structured and logical way.

- In this module, we describe various Bash scripting techniques, each explained with practical examplesd.

---
## 2. echo and comments

- echo is one of the simplest and most useful commands in Bash.
- It displays text or variable values on the screen — or sends them to a file.

=== "print text"
	```console
	echo "Hello, world!"
	```
	"Output is"<br>
	```Hello, world!```

=== "print variable"

	```console
	name="Mujeeb"
	echo "Hello, $name!"
	```
	Output:<br>
	```Hello, Mujeeb!```

=== "Comment example"
	In Bash, comments are simple and start with the # symbol. Everything after # on the same line is ignored by the shell.

	```console
	# This is a single-line comment
	echo "Hello, Bash!"  # This is an inline comment
	```

### 2.1 Special Characters and Escapes

- By default, echo doesn’t interpret escape sequences like \n (newline) 
- The ```-e``` option in echo enables interpretation of escape sequences 

=== "Without  -e"
	```console
	echo "Line1\nLine2"
	```
	ouput:<br>
	```Line1\nLine2```

=== "WITH  -e"
	```console
	echo -e "Line1\nLine2"
	```
	ouput:<br>
	```
	Line1
	Line2
	```
=== "Multiline text"
	```console
	echo -e "Bash scripting basics:\n1. Variables\n2. Loops\n3. Conditions"
	```
	Output:
	```
	Bash scripting basics:
	1. Variables
	2. Loops
	3. Conditions
	```
	

### 2.2 List of escape Characters
| Escape Sequence | Description | Example Command | Example Output |
|-----------------|--------------|-----------------|----------------|
| `\n` | New line | `echo -e "Line1\nLine2"` | Line1<br>Line2 |
| `\t` | Horizontal tab | `echo -e "Col1\tCol2"` | Col1    Col2 |
| `\v` | Vertical tab | `echo -e "A\vB"` | A<br><br>B |
| `\r` | Carriage return (moves cursor to line start) | `echo -e "Hello\rWorld"` | World |
| `\b` | Backspace (deletes previous character) | `echo -e "abc\b"` | ab |
| `\a` | Alert (system bell sound) | `echo -e "Beep\a"` | *(beep sound)* |
| `\\` | Prints a single backslash (`\`) | `echo -e "\\n"` | \n |
| `\"` | Prints double quotes | `echo -e "\"Hello\""` | "Hello" |
| `\0NNN` | Character with octal value `NNN` | `echo -e "\041"` | ! |

### 2.3 Basic file creation with ```echo```

```console
echo "Hello, Bash world!" > hello.txt
```

This creates (or overwrites) a file named hello.txt with the text:
```console
Hello, Bash world!
```

### 2.4 ```printf``` vs ```echo```

| Feature | `echo` | `printf` |
|----------|---------|----------|
| Purpose | Prints text or variables to the terminal | Prints formatted text with control over layout |
| Automatic newline | Adds newline automatically | Does **not** add newline unless specified (`\n`) |
| Escape sequences | Needs `-e` option to interpret (`\n`, `\t`) | Always interprets escape sequences |
| Formatting | Limited | Powerful (supports `%s`, `%d`, `%f`, etc.) |
| Portability | Behavior can vary between shells | More consistent across systems |
| Error handling | Always returns 0 | Returns nonzero on output error |
| Typical use | Simple messages or logs | Structured, aligned, or formatted output |

Example:

```bash
echo "Hello, World!"
printf "Hello, %s!\n" "World"
```
Output:
```
Hello, World!
Hello, World!
```

---
## 3. Creating variables

| Topic | Description | Example |
|-------|-------------|---------|
| **Creating a Variable** | In Bash, variables are created by assigning a value without spaces around `=`. | `name="Mujeeb"` |
| **Printing a Variable** | Use `$` before the variable name or `${}` for clarity. | `echo $name` → Mujeeb <br> `echo ${name}` → Mujeeb |
| **Reading Input from Keyboard** | Use the `read` command to take input from the user. | `read username` <br> `echo "Hello, $username!"` |
| **Variable Naming Rules** | - Must start with a letter or underscore `_` <br> - Can contain letters, numbers, underscores <br> - Case-sensitive | Valid: `_var1`, `name` <br> Invalid: `1name`, `my-var` |
| **Types of Variables** | Bash has only **strings** by default. Numbers are treated as strings unless used in arithmetic. <br> Special types: arrays, associative arrays, environment variables | `num=10` <br> `declare -a arr=(1 2 3)` <br> `declare -A assoc=([key1]=val1 [key2]=val2)` |
| **Unsetting Variables** | Remove a variable using `unset`. | `unset name` |
| **Default Values** | Use `${var:-default}` to provide a default if variable is empty/unset | `echo ${username:-Guest}` → prints `Guest` if `username` is empty |


---
## 4. Arithmetics 

### 4.1 Variables are **Strings** by default
Bash has only **strings** by default. Numbers are treated as strings.

Example 1: Assign a number to a variable
```
num="10"
```

Example 2: Add two values
```
result="$num + 5"
echo "Result without arithmetic: $result"
```
Output:
```
Result without arithmetic: 10 + 5
```

### 4.2 Perform arithmetic

**Using $(( )), Bash interprets the variable as a number and performs the calculation.**


```
# Arithmetic evaluation
num=10
sum=$((num + 5))
echo "Result with arithmetic: $sum"
```
Output:
```
Result with arithmetic: 15
```

### 4.3 **<font color = 'red'> Caution </font>**

| Expression | Description | Output / Behavior |
|------------|-------------|------------------|
| `result=$num + 5` | No quotes, no arithmetic | `result` becomes `10`; Bash tries to run `+ 5` as a command → Error: `bash: +: command not found` |
| `result="$num + 5"` | Quotes around expression | `result` becomes the **string** `10 + 5` (no calculation) |
| `result=$((num + 5))` | Arithmetic context | `result` becomes `15` (calculation performed) |
| `echo $result` | Display the value | Prints the value of `result` depending on above assignment |

### 4.4 List of arithmetic operation

| Operation | Symbol | Example | Output |
|-----------|--------|---------|--------|
| Addition | `+` | `a=10; b=5; sum=$((a + b)); echo $sum` | 15 |
| Subtraction | `-` | `a=10; b=5; diff=$((a - b)); echo $diff` | 5 |
| Multiplication | `*` | `a=10; b=5; prod=$((a * b)); echo $prod` | 50 |
| Division | `/` | `a=10; b=5; div=$((a / b)); echo $div` | 2 |
| Modulus (remainder) | `%` | `a=10; b=3; mod=$((a % b)); echo $mod` | 1 |
| Exponentiation | `**` | `a=2; b=3; pow=$((a ** b)); echo $pow` | 8 |
| Increment | `++` | `a=5; ((a++)); echo $a` | 6 |
| Decrement | `--` | `a=5; ((a--)); echo $a` | 4 |

---
(Under construction)









