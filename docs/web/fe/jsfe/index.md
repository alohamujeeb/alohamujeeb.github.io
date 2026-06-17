---
hide:
  - navigation
  
tags:
  - JavaScript
---

# JavaScript in browser (A Reference)
This document is **not** meant for learning JavaScript from scratch. It serves as a **quick reference** for various JavaScript topics used in HTML programming.

---
## 1. JavaScript "Hello World"

| Topic | Code / Quick Reference | Description |
|-------|----------------------|------------|
| **Hello World** | `<script>console.log("Hello World")</script>` | Print message to browser console |
| **Alert Message** | `<script>alert("Hello World")</script>` | Show popup alert in browser |
| **Writing to Page** | `<script>document.write("Hello World")</script>` | Insert text directly into HTML page |
| **Basic Inline Script** | `<html><body><script>console.log("Hello")</script></body></html>` | Minimal HTML + JS example |
| **External Script** | `<!-- index.html --> <script src="main.js"></script>`<br>`// main.js`<br>`console.log("Hello World")` | Separate JS file included via script tag |

### Comments 
```JavaScript 
// This is a single-line comment
```

```JavaScript
/* 
   This is a
   multi-line comment 
*/
```

### Semicolons

- Optional in many cases, because JS automatically inserts them (ASI = Automatic Semicolon Insertion)
- Recommended to use for clarity and to avoid pitfalls.

```js
let x = 10;   // semicolon used
let y = 20    // semicolon omitted, still works
```

---
## 2. Variables & constants

| Topic | Code / Quick Reference | Description |
|-------|----------------------|------------|
| **Variable (var)** | `<script>var x = 10; console.log(x);</script>` | Declares a function-scoped variable |
| **Variable (let)** | `<script>let y = 20; console.log(y);</script>` | Declares a block-scoped variable |
| **Constant (const)** | `<script>const z = 30; console.log(z);</script>` | Declares a read-only block-scoped constant |
| **Multiple Variables** | `<script>let a = 1, b = 2, c = 3;</script>` | Declare multiple variables in one line |
| **Variable Reassignment** | `<script>let x = 5; x = 10; console.log(x);</script>` | Variables declared with `let` or `var` can be reassigned |
| **Constant Reassignment Error** | `<script>const pi = 3.14; pi = 3.141; // Error</script>` | `const` cannot be reassigned |

### Block-scoped Variables

```JavaScript
{
  let x = 10;   // x exists only inside this block
  const y = 20; // y exists only inside this block
}
console.log(x); // Error: x is not defined
console.log(y); // Error: y is not defined
```

## 3. Loops and conditions

### Loops

| Loop Type | Code / Quick Reference | Description |
|-----------|----------------------|------------|
| **For Loop** | `<script>for (let i = 0; i < 5; i++) { console.log(i); }</script>` | Loop with known start/end |
| **While Loop** | `<script>let i = 0; while(i < 5) { console.log(i); i++; }</script>` | Loop with condition checked each iteration |
| **Do...While Loop** | `<script>let i = 0; do { console.log(i); i++; } while(i < 5);</script>` | Executes block at least once, then checks condition |
| **For...of Loop** | `<script>const arr = [1,2,3]; for(const val of arr) { console.log(val); }</script>` | Iterates over iterable objects like arrays |
| **For...in Loop** | `<script>const obj = {a:1,b:2}; for(const key in obj) { console.log(key,obj[key]); }</script>` | Iterates over object keys |

### conditions

| Conditional Type | Code / Quick Reference | Description |
|-----------------|----------------------|------------|
| **If Statement** | `<script>if(x > 0){console.log("Positive");}</script>` | Conditional execution |
| **If...Else** | `<script>if(x>0){console.log("Positive");}else{console.log("Non-positive");}</script>` | Two-way conditional |
| **Else If** | `<script>if(x>0){...}else if(x<0){...}else{...}</script>` | Multi-branch conditional |
| **Switch Statement** | `<script>switch(day){case 1:console.log("Mon");break;default:console.log("Other");}</script>` | Multi-branch selection based on value |
| **Ternary Operator** | `<script>let msg = (x>0)? "Positive":"Non-positive";</script>` | Short conditional expression |

### Example of loops in html using JavaScript

**Example 1: create a table of numbers and their squares**<br>

```html
<!DOCTYPE html>
<html>
<body>
  <table id="t"></table>

  <script>
    const t = document.getElementById("t");
    for(let i=1; i<=10; i++){
      const r = t.insertRow();
      r.insertCell(0).textContent = i;
      r.insertCell(1).textContent = i*i;
    }
  </script>
</body>
</html>
```

**Example 2: table using a condition to check even/odd:**<br>

```html
<!DOCTYPE html>
<html>
<body>
  <table id="t"></table>

  <script>
    const t = document.getElementById("t");
    for(let i=1; i<=10; i++){
      const r = t.insertRow();
      r.insertCell(0).textContent = i;
      r.insertCell(1).textContent = (i % 2 === 0) ? "Even" : "Odd";
    }
  </script>
</body>
</html>
```


### ```let``` vs ```var``` vs global 

| Feature | `var` | `let` | Global (undeclared) |
|---------|-------|-------|-------------------|
| **Scope** | Function-scoped | Block-scoped | Global-scoped |
| **Hoisting** | Hoisted, initialized as `undefined` | Hoisted, uninitialized (Temporal Dead Zone) | Created on first assignment, hoisted as global |
| **Reassignment** | Can reassign | Can reassign | Can reassign |
| **Redeclaration** | Allowed in same scope | Not allowed in same scope | Allowed (creates global property) |
| **Example** | ```js function f(){ var x=1; } console.log(x); // Error outside f ``` | ```js { let x=1; } console.log(x); // Error outside block ``` | ```js { x=1; } console.log(x); // Works globally ``` |
| **Best Use** | Older JS, function-level variables | Modern JS, recommended for block scope | Avoid — pollutes global scope |

**Key takeaway:**<br>

- Use **let** for loops and block variables, avoid undeclared globals
- use **var** only if maintaining legacy code.


---
## 3. Cautions in using variable/constants

### Using ```var```
```js
for (var i = 0; i < 5; i++) {
  console.log(i);
}
console.log(i); // i is accessible here (function-scoped)
```

- var is function-scoped, so the loop variable can leak outside the block.
- Works in all loops and conditionals.

### Using constants

```js
for (const i = 0; i < 5; i++) { // ❌ Error
  console.log(i);
}
```

- const is only for **values that do not change.**

### Omitting declaration (not recommended)

```js
for (i = 0; i < 5; i++) {
  console.log(i);
}
```
- Creates a global variable i (bad practice).
- Avoid in modern code; always use **let** or **const** for clarity and safety.


### Summary

- ```let```: recommended, block-scoped.
- ```var```: works but can leak outside loops.
- ```const```: only for loops where value does not change (rare).
- No declaration → works but pollutes global scope, avoid it.


---
## 4. Data types and operators

### Data types

| Data Type | Code / Example | Description |
|-----------|----------------|------------|
| **Number** | `let x = 10; let y = 3.14;` | JS has a single Number type for integers & floats |
| **String** | `let s = "Hello";` | Sequence of characters |
| **Boolean** | `let b = true; let f = false;` | true/false values |
| **Undefined** | `let u; console.log(u);` | Variable declared but not assigned |
| **Null** | `let n = null;` | Explicit “no value” |
| **Object** | `let obj = {a:1, b:2};` | Key-value pairs |
| **Array** | `let arr = [1,2,3];` | Ordered list of values |
| **Symbol** | `let sym = Symbol("id");` | Unique identifier, rarely used |


### Operators

| Operator Type | Examples | Description |
|---------------|---------|------------|
| **Arithmetic** | `+ - * / % **` | Addition, subtraction, multiplication, division, remainder, exponentiation |
| **Assignment** | `= += -= *= /= %= **=` | Assign and modify values |
| **Comparison** | `== === != !== > < >= <=` | Equality, strict equality, inequality, relational |
| **Logical** | `&& || !` | And, Or, Not |
| **Ternary** | `condition ? value1 : value2` | Short if-else expression |
| **Type Checking** | `typeof x` | Returns data type as string |

### **Object** type

In JavaScript, an Object is a collection of key-value pairs.

- Keys (also called properties) are strings or symbols.
- Values can be any data type, including numbers, strings, arrays, functions, or even other objects.

```js
let person = {
  name: "Alice",   // key: name, value: "Alice"
  age: 25,         // key: age, value: 25
  isStudent: true, // key: isStudent, value: true
  greet: function(){ console.log("Hello!"); } // method
};

// Accessing values
console.log(person.name);   // Alice
console.log(person["age"]); // 25

// Calling a method
person.greet(); // Hello!
```


### Objecs, Arrays, and Primitives

| Type | Example | Description | Access |
|------|---------|------------|--------|
| **Object** | `let obj = {name:"Alice", age:25}` | Collection of key-value pairs; values can be any type | `obj.name` or `obj["age"]` |
| **Array** | `let arr = [1,2,3]` | Ordered list of values; special object with numeric keys | `arr[0]` |
| **Number** | `let x = 10` | Single numeric value | `x` |
| **String** | `let s = "Hello"` | Sequence of characters | `s` |
| **Boolean** | `let b = true` | true/false | `b` |
| **Undefined** | `let u;` | Declared but not assigned | `u` |
| **Null** | `let n = null` | Explicit “no value” | `n` |
| **Symbol** | `let sym = Symbol("id")` | Unique identifier | `sym` |

- Objects and Arrays are reference types — assigning them to another variable copies the reference, not the value.

- Numbers, Strings, Booleans, Undefined, Null, Symbol are primitive types — assigning them copies the

---
## 5. Creating classes

```js
class Person {
  constructor(name, age) {  // Constructor method runs when a new object is created
    this.name = name;
    this.age = age;
  }

  greet() {                 // Method
    console.log("Hi, I'm " + this.name);
  }
}

// Creating an instance
let p1 = new Person("Alice", 25);
p1.greet(); // Hi, I'm Alice
```

### 5.1 Inheritance (Subclassing)

```js
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);     // Call parent constructor
    this.grade = grade;
  }

  study() {
    console.log(this.name + " is studying in grade " + this.grade);
  }
}

let s1 = new Student("Bob", 16, 10);
s1.greet(); // Hi, I'm Bob
s1.study(); // Bob is studying in grade 10
```

---
## 6. Functions

| Concept | Description | Example |
|----------|--------------|----------|
| **Function Declaration** | Traditional named function, hoisted (usable before definition). |     function greet(name) { return "Hello, " + name; }<br>console.log(greet("Mujeeb")); |
| **Function Expression** | Stored in a variable; not hoisted. |     const greet = function(name) { return "Hi, " + name; };<br>console.log(greet("Mujeeb")); |
| **Arrow Function** | Shorter syntax; inherits `this` from outer scope. |     const square = n => n * n;<br>console.log(square(4)); // 16 |
| **Default Parameters** | Values used if none provided. |     function add(a, b = 5) { return a + b; }<br>console.log(add(3)); // 8 |
| **Return Value** | `return` sends a value back to caller. |     function multiply(a, b) { return a * b; } |
| **Anonymous Function** | Function without a name, often used in callbacks. |     setTimeout(function() { console.log("Done!"); }, 1000); |
| **Immediately Invoked Function (IIFE)** | Runs right away, used to create isolated scope. |     (function() { console.log("Runs instantly!"); })(); |
| **Function in Function** | Functions can be nested. |     function outer(x){ function inner(y){ return y * 2; } return inner(x); }<br>console.log(outer(5)); // 10 |
| **Arrow Function vs Normal** | Arrow keeps `this` from parent; normal defines its own. |     const obj = { value: 10, arrow: () => console.log(this.value), normal() { console.log(this.value); } };<br>obj.arrow(); // undefined<br>obj.normal(); // 10 |


### 6.1 Pass by value and pass by reference

| Type | Description | Example |
|-------|--------------|----------|
| Pass by Value | Primitive types (number, string, boolean, null, undefined, symbol, bigint) are copied — changing one doesn’t affect the other. | let a = 10; let b = a; b = 20; console.log(a); // 10 |
| Pass by Reference | Objects (arrays, functions, plain objects) are referenced — both variables point to the same memory location. | let x = {num: 5}; let y = x; y.num = 99; console.log(x.num); // 99 |
| Tip | To clone objects safely, use spread or structuredClone. | let newObj = {...x}; |

---
## 7. Cloning/Copying and object

**Shallow copy**:<br>

- Top-level properties are copied.
- But if any property is itself an object, it’s not copied, only the reference is.

**Deep copy**:<br>
A deep copy means a complete duplication of an object — including all nested objects and arrays, not just the top level.

**Comparision**:<br>

| Type | What It Does | Independent from Original? | Example | Notes |
|------|---------------|-----------------------------|----------|--------|
| **Assignment** | Copies only the *reference* (both point to same object). | ❌ No | let a = {x:1}; let b = a; b.x = 5; console.log(a.x); // 5 | Fast but linked; both refer to same memory. |
| **Shallow Copy** | Copies only top-level properties. Nested objects are still shared. | ⚠️ Partially | let a = {p:{q:1}}; let b = {...a}; b.p.q = 5; console.log(a.p.q); // 5 | Fine for flat objects only. |
| **Deep Copy** | Duplicates the entire object and all nested structures. | ✅ Yes | let a = {p:{q:1}}; let b = structuredClone(a); b.p.q = 5; console.log(a.p.q); // 1 | Safest; independent copy of everything. |



```js
// Using spread syntax (shallow copy)
let a = {x: 1, y: 2};
let b = {...a};
b.x = 99;
console.log(a.x); // 1 (unchanged)

// Using structuredClone (deep copy)
let c = {p: {q: 10}};
let d = structuredClone(c);
d.p.q = 50;
console.log(c.p.q); // 10 (unchanged)
```

- Spread ({...obj}) → good for simple, shallow copies.
- structuredClone(obj) → better for deep copies (nested objects).


---
## 8. Arrays

| Concept | Description | Example |
|---------|-------------|---------|
| Create an Array | Use square brackets or Array() constructor | let nums = [1,2,3]; let names = new Array("Ali","Zara"); |
| Access Elements | Indexed from 0 | console.log(nums[0]); |
| Modify Elements | Assign new value by index | nums[1] = 10; |
| Length | .length gives size | console.log(nums.length); |
| Add / Remove (end) | push() adds; pop() removes last | nums.push(4); nums.pop(); |
| Add / Remove (start) | unshift() adds; shift() removes first | nums.unshift(0); nums.shift(); |
| Loop Through | Use for, for...of, or forEach | for(let n of nums){ console.log(n); } |
| Find / Filter / Map | Built-in methods for processing | nums.filter(n => n>2); nums.map(n => n*2); |
| Combine / Slice | concat() joins; slice() copies part | nums.concat([4,5]); nums.slice(1,3); |
| Sort / Reverse | Sort or reverse order | nums.sort(); nums.reverse(); |

### [] vs new Array()

| Syntax | Description | Example | Notes |
|--------|-------------|---------|-------|
| `[]` | Array literal; most common, concise | let nums = [1,2,3]; | Recommended for almost all cases |
| `new Array()` | Array constructor | let nums = new Array(3); | Creates empty slots; use `[]` instead to avoid confusion |
| `new Array(values...)` | Array constructor with elements | let nums = new Array(1,2,3); | Same as `[1,2,3]` |


- Use [] for regular arrays.
- Only use new Array(size) if you explicitly need an empty array of a fixed length.

---
## 9. DOM events

### 9.1 What is DOM

- DOM (Document Object Model) is like a **tree structure** of a web page.
- Every part of the page such as headings, paragraphs, buttons, images  is a **node** in this tree.
JavaScript can look at, change, add, or remove these nodes, making the page **interactive**.

**Analogy**<br>

- Think of a web page as a family tree.
- HTML elements are family members.
- The DOM is the map of relationships, and JS is like a person who can update the tree anytime.

### 9.2 What are events
DOM events are things that happen on a web page that JavaScript can respond to. The concept is similar to  **even handling** system in any other GUI.

**Examples:**

- Clicking a button (click)
- Moving the mouse over an element (mouseover)
- Typing in an input box (keydown)
- Submitting a form (submit)

### 9.3 List of events

| Event Type | Description | Example |
|------------|-------------|---------|
| click | Mouse click on an element | button.addEventListener("click", () => console.log("Clicked")); |
| dblclick | Mouse double-click | element.addEventListener("dblclick", () => console.log("Double Clicked")); |
| mouseover | Mouse moves over an element | element.addEventListener("mouseover", () => console.log("Hovered")); |
| mouseout | Mouse leaves an element | element.addEventListener("mouseout", () => console.log("Left")); |
| keydown | Key is pressed down | input.addEventListener("keydown", (e) => console.log(e.key)); |
| keyup | Key is released | input.addEventListener("keyup", (e) => console.log(e.key)); |
| change | Value of input or select changes | select.addEventListener("change", () => console.log("Changed")); |
| submit | Form is submitted | form.addEventListener("submit", (e) => e.preventDefault()); |
| focus | Element gains focus | input.addEventListener("focus", () => console.log("Focused")); |
| blur | Element loses focus | input.addEventListener("blur", () => console.log("Blurred")); |

### 9.4 Ways to handle events

| Concept | Description | Example |
|---------|-------------|---------|
| Inline Event | Assign event directly in HTML | `<button onclick="alert('Hi')">Click</button>` |
| Using JS Property | Assign event handler in JavaScript | `const btn = document.getElementById("btn"); btn.onclick = () => alert("Hello");` |
| addEventListener | Modern approach; allows multiple handlers | `btn.addEventListener("click", () => console.log("Clicked"));` |
| Event Object | Provides info about the event | `btn.addEventListener("click", (e) => console.log(e.type, e.target));` |
| Mouse Events | click, dblclick, mousedown, mouseup, mouseover, mouseout | `element.addEventListener("mouseover", () => console.log("Hovered"));` |
| Keyboard Events | keydown, keyup, keypress | `input.addEventListener("keydown", (e) => console.log(e.key));` |
| Form Events | submit, change, input | `form.addEventListener("submit", (e) => { e.preventDefault(); console.log("Form submitted"); });` |
| Removing Event | Remove previously added handler | `const handler = () => console.log("Hi"); btn.addEventListener("click", handler); btn.removeEventListener("click", handler);` |


---
## 10. Dynamic HTML

- Dynamic HTML (DHTML) means a web page can change without reloading.
- Using JavaScript, the page can add, remove, or modify content on the fly — like showing a new message, updating a table, or highlighting a button when clicked.


| Concept | Description | Example |
|---------|-------------|---------|
| Create Element | Create a new HTML element | `let div = document.createElement("div");` |
| Set Content | Add text or HTML | `div.textContent = "Hello";`<br>`div.innerHTML = "<b>Bold</b>";` |
| Set Attributes | Add attributes to element | `div.setAttribute("id", "myDiv");`<br>`div.className = "box";` |
| Append to DOM | Add element to page | `document.body.appendChild(div);` |
| Insert Before | Insert element before another | `let ref = document.getElementById("ref"); document.body.insertBefore(div, ref);` |
| Remove Element | Delete element from DOM | `div.remove();` |
| Clone Element | Copy an element | `let copy = div.cloneNode(true); document.body.appendChild(copy);` |
| Modify Styles | Change CSS dynamically | `div.style.color = "red"; div.style.backgroundColor = "yellow";` |
| Access Children | Work with nested elements | `div.children[0]`<br>`div.firstChild`<br>`div.lastChild` |


### Dynamic HTML vs event handling

| Aspect | Dynamic HTML | DOM Event Handling |
|--------|--------------|-----------------|
| Purpose | Change the content, structure, or style of the page dynamically | Respond to things that happen on the page (clicks, keypresses, form submits) |
| How it works | Use JavaScript to create, modify, or remove elements and attributes | Use JavaScript to listen for events and run code when they occur |
| Trigger | Can be triggered by any JS code, timers, or events | Triggered specifically by user actions or browser events |
| Overlap | Often uses event handling to know *when* to change the page | Often changes the page in response to an event, so DOM manipulation is involved |
| Analogy | Whiteboard: you can write, erase, or update anything anytime | Doorbell: rings when pressed, and you react to it |


---
## 11. Form handling

### 11.1 What are forms

- Forms are an **HTML feature**, not JavaScript.
- HTML defines form elements like ```<form>, <input>, <textarea>, <select>, <button>,``` etc.
- Forms by themselves can **submit data to a server** using **HTML attributes (action, method)**.

### 11.2 Javascript and forms

JavaScript comes in as an addition:

- To enhance forms, make them interactive, or prevent page reloads.
- Examples of JS handling forms:

	- Validate input before submission
	- Dynamically add/remove form fields
	- Capture form data and process it without reloading (e.preventDefault())
	- Respond to events like submit, change, input, focus, blur

**So, forms belong to HTML, and JavaScript is used to enhance, control, or automate them.**

### 11.2 Form evens and JS interactions


| Concept | Description | Example |
|---------|-------------|---------|
| submit | Fired when a form is submitted | `form.addEventListener("submit", (e) => { e.preventDefault(); console.log("Form submitted"); });` |
| change | Fired when an input, select, or textarea value changes | `input.addEventListener("change", () => console.log(input.value));` |
| input | Fired on every change while typing | `input.addEventListener("input", () => console.log(input.value));` |
| focus | Fired when an element gains focus | `input.addEventListener("focus", () => console.log("Focused"));` |
| blur | Fired when an element loses focus | `input.addEventListener("blur", () => console.log("Blurred"));` |
| reset | Fired when a form is reset | `form.addEventListener("reset", () => console.log("Form reset"));` |
| preventDefault | Prevent default form submission | `form.addEventListener("submit", (e) => e.preventDefault());` |
| access values | Read values of form fields | `let name = document.getElementById("name").value;` |
| set values | Change form field values dynamically | `document.getElementById("name").value = "Mujeeb";` |

---
## 12. Why use a framework (like vue)?

**Why use Vue instead of plain JavaScript?**

| Feature | Plain JavaScript | Vue |
|---------|-----------------|-----|
| Automatic DOM updates | Must manually find elements and update them | Updating a variable automatically updates the page wherever it’s used |
| Declarative templates | Must write code to manipulate DOM | Describe what the page should look like; Vue updates DOM automatically |
| Event handling | Attach `onclick` or `addEventListener` | Use `@click` or `v-on:click` in the template |
| Two-way form binding | Manually get/set input values | `v-model` keeps input and data in sync automatically |
| Reactive data | No automatic tracking; must update manually | Vue “watches” data; changes trigger automatic DOM updates |
| Component structure | All code in one script or scattered functions | Organize code into reusable components |
| Boilerplate | More lines of code for updates and DOM manipulation | Fewer lines; focus on app logic instead of DOM handling |

### 12.1 HTML/JavaScript example

**Task:** to display and update a counter on the page when the button is clicked.

**Explaination:**<br>

- ```<span id="count">```: the text showing the current number
- ```<button id="inc">```: the clickable button
- Every time the button is clicked, JS manually sets countEl.textContent = ++count;, which changes the content inside the <span>.



```html
<button id="inc">+</button>
<span id="count">0</span>
```

```js
let count = 0;
const countEl = document.getElementById("count");
document.getElementById("inc").onclick = () => {
  countEl.textContent = ++count;
};
```

### 12.2 HTML/VueJS example

**Task:** to display and update a counter on the page when the button is clicked.

**Explaination:**<br>

- ```<span>{{ count }}</span>```: this is bound to the count variable via Vue’s template syntax
- ```<button @click="count++">```: Vue listens for clicks and updates count
- When count changes, Vue’s reactivity system automatically updates the content of the <span> in the DOM.


```html
<div id="app">
  <button @click="count++">+</button>
  <span>{{ count }}</span>
</div>
```

```js
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
Vue.createApp({
  data() {
    return { count: 0 }
  }
}).mount('#app')
</script>
```

**Differences:**<br>

Both are modifying the same visible counter (<span>), but the mechanism is different:

- Plain JS → manual DOM manipulation
- Vue → automatic DOM update via reactive binding

---
(This page would be updated in future on need basis)


## Relevant Links

#### [Vanialla JavaScript vs Frameworks](../../../blog/posts/2026-05-19-Frameworks_vs_JavascripVanila.md)
#### [Frameworks vs. Vanilla JS in the Age of AI](../../../blog/posts/2025-10-22-JSframework_vs_Vanilla_AI.md)



