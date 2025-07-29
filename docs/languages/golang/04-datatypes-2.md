# **04 Data Types-2: Strings in Go**

---

## Two types of strings
In Go, strings can be defined in two distinct ways, each offering unique benefits depending on the use-case:

**Regular Strings** – defined using double quotes ("...")

- These support escape sequences like \n, \t, \", etc.
- Ideal for **short, dynamic** strings or when using special characters.

**Raw Strings** – defined using backtick characters (\`...\`)

- These do not support escape sequences.
- Useful for multiline text, embedded code, or preserving exact formatting.



- Regular Strings (defined within double quotes)
- Backtick Strings (defined within backtick characters)


## Regular Strings
- Regular strings are defined within double quotes, like C/C++, Java, and other languages.
- They can contain escape characters such as \t, \n...

|Escape Sequence|Description | Output	| 
|----|----|----|
|\n|Newline	|Moves to next line|
|\t|Horizontal tab|Adds tab spacing|
|\\\	|Backslash (\)	| \ |
|\"	|Double quote (")|"
|\'	|Single quote (')	|(used in runes)|
|\r	|Carriage return	|Resets cursor to line start|
|\b	|Backspace-Deletes previous char |(in some terminals)|


## Raw Strings
They are especially helpful for writing strings that should appear visually as they are typed.

- Raw strings are enclosed in a pair of backtick characters ( \`...\` ).
- They do not support escape sequences — characters like \n, \t, or \\\ are treated literally.
- Raw strings are useful when you want to preserve formatting exactly as written, including spacing, indentation, and line breaks.


### Example of a raw string
```
html := `<html>
  <body>Hello, World!</body>
</html>`
```

### Example 2
=== "Code"
	``` go
	package main

	import "fmt"

	func main() {
		var s1 string = "Hello, world!"
		s2 := `Line 1
				 \n\tLine 2
			Line3`

		fmt.Println(s1)
		fmt.Println(s2)
	}
	```

=== "Output"
	```
	Hello, world!
	Line 1
				 \n\tLine 2
			Line3
	```

### Why use raw Strings
Raw strings are especially useful in modern web-based and systems programming. Go includes raw stringsto make working with complex, formatted text easier and cleaner. 

- They are quite handy for embedding code such as regular expressions, HTML, JSON, or SQL, without needing escape characters.
- They simplify writing multiline strings — no need to manually insert \n, \t, \\ etc.
- They preserve formatting exactly as written, including spaces, indentation, and line breaks.
- They are more readable and visually clear, especially for large blocks of text.


## UTF-8 Format Coding
- Strings in Go (both regular strings and raw strings) use UTF-8 encoding by default.
- UTF-8 is the most widely used character encoding for representing text from various languages, symbols, and special characters.
- It is a variable-length encoding, using 1 to 4 bytes per character, depending on the character's Unicode code point.
- UTF-8 is ASCII-compatible, meaning all standard ASCII characters (values 0–127) have the same representation in UTF-8.
