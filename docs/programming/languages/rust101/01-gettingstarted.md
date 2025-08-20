# **01-Getting Started**

Main topics: 

- Rust Installation
- Hello World example
- Caro in Rust

---
## 1. **Rust Installation**

=== "Linux (Ubuntu)"
	Type the following command.
	
	``` bash
	curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
	```
	The command downloads a script and starts the installation of the rustup tool, which installs the latest stable version of Rust. 
	
	If everything goes well, you’ll see a large message containing follwoing text:
	
	```Rust is installed now. Great!```
	
### Verify the Installation
Type followin in the terminal:
``` bash
rustc --version
```
And you should see something like this:

```rustc 1.89.0 (29483883e 2025-08-04)```

---
## 2. **Hello World** in Rust

- Create a fle "hello.rs" with following contents
``` rust
fn main() {
    println!("Hello, world from Rust!");
}
```

### **How to compile and run the program**
=== "Linux (Ubuntu)"

	To compile, type:
	``` bash 
	rustc main.rs
	```
	A file ```main``` is generated which is an executable program.

	To run, type:
	``` bash
	./main
	```
	You should see following message on the screen:
	```
	Hello, world from Rust!
	```
	
## Cargo in Rust

Cargo is Rust’s **build system** and **package manager**, and it does following:

- building your code

- downloading the libraries your code depends on, and building those libraries. 

(We call the libraries that your code needs dependencies.)

The concept of "cargo" is not new. It is already part of many languages and tools, such as Golang, Docker, and frameworks like Djiango.

- In Go language, we called this concept as **Go Modules** (in case you are interested).

- We'll cover "cargo" in more details in coming chapters.

### Creating a new project using Cargo

To create a project, such as "Project-1":

``` bash
cargo new Project-1
```
You see a message like this:

warning: the name `Project-1` is not snake_case or kebab-case which is recommended for package names, consider `project-1`

Reason:
Rust recommends using:

	- **snake_case:** like project_one
	- or **kebab-case:** like project-1

so change the project name to saye ```project-1```
``` bash
cargo new project-1
```

- A directory **project-1** is created with some files and folders inside it.

- We are particularly interested in **src** folder at this stage.

Type following in src/main.rs (same code that we used in the previous section)
``` rust
fn main() {
	println!("Hello, world from Rust!");
}
```

### Building and running cargo project
In the project-1 folder, Type

``` bash
cargo build
```

- Cargo utility uses the file **Cargo.toml** to build the project and generate the output executable.
(more on Cargo.toml later)

type followin to run,
``` bash
cargo run
```
Out will be like following:
```
Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.05s
     Running `target/debug/project-1`
Hello, world from Rust!
```

## Summary: two ways to write and execute programs

1) Single file approach (used for simple testing)

2) Caro projects: Used for real-world projects with multiple files and dependencies.











