# **01- Go Modules**
(Under construction)

Main topics:

- Modules in Go

---
## 1. What is a module in Go

- In modern Go (1.17+), creating a Go module is necessary for almost all development, when you're:
	- Importing third-party packages (like quic-go)
	- Building projects with multiple files
	- Using dependency/version tracking

- A Go module is simply a project with a go.mod file at its root. It tells Go:
	- What your module is called
	- What dependencies it uses (and their versions)
	- How to build and fetch those dependencies

**A side note:** This concept is quite common, e.g. if you have worked with dockers, we create a project similar to the one we are discussing here.

### When we do not need a module:
- If you're writing a one-file script with only Go standard library packages
- If you’re just experimenting and not using go get or go build

(under construnction)
