---
search:
  exclude: true
---

## 99. VueJS topics
(For my reference only)

---

### 1) JavaSCript in browser (Quick refeence)--not a full course
Prerequisite: Any programming experience (like Python)

| Topic | Quick Reference / Example |
|-------|---------------------------|
| **Hello World** | `<script>console.log("Hello World")</script>` |
| **Variables & Constants** | `var x = 1; let y = 2; const z = 3;` |
| **Data Types** | `string, number, boolean, array, object` |
| **Operators** | `+ - * / %`, `== === != !==`, `&& || !` |
| **Loops** | `for (let i=0;i<5;i++) {}`, `while(condition){}`, `for (const x of arr){}` |
| **Conditional Statements** | `if(condition){}`, `else if`, `else`, `switch(value){}` |
| **Functions** | `function f(){}`, `const f = () => {}` |
| **Scope & Closures** | Block scope (`let/const`) vs function scope (`var`), basic closure example |
| **DOM Manipulation** | `document.getElementById('id')`, `querySelector()`, `innerHTML`, `textContent` |
| **Event Handling** | `element.onclick = fn;`, `element.addEventListener('click', fn)` |
| **Forms & Inputs** | `input.value`, basic validation |
| **Arrays & Methods** | `push(), pop(), map(), filter(), forEach()` |
| **Objects** | `obj.key`, `obj['key']`, adding/updating properties, methods |
| **Template Literals** | `` `Hello ${name}` `` |
| **Console & Debugging** | `console.log()`, `console.table()`, breakpoints |
| **Basic ES6+ Features** | Destructuring, default params, spread/rest operators |
| **Timers** | `setTimeout(fn, ms)`, `setInterval(fn, ms)` |
| **Basic JSON** | `JSON.parse(str)`, `JSON.stringify(obj)` |



### 2) JavaSCript for HTML DOM

| Topic | Quick Reference / Example |
|-------|---------------------------|
| **Selecting Elements** | `document.getElementById('id')`, `document.querySelector('.class')`, `document.querySelectorAll('div')` |
| **Reading & Writing Content** | `element.textContent`, `element.innerHTML`, `element.value` |
| **Modifying Attributes** | `element.setAttribute('attr', 'value')`, `element.getAttribute('attr')`, `element.removeAttribute('attr')` |
| **Styling Elements** | `element.style.color = 'red'`, `element.classList.add('class')`, `element.classList.remove('class')` |
| **Creating Elements** | `document.createElement('div')`, `element.appendChild(child)` |
| **Removing Elements** | `element.remove()`, `parent.removeChild(child)` |
| **Event Handling** | `element.addEventListener('click', fn)`, `element.onclick = fn` |
| **Form & Input Handling** | `input.value`, `input.checked`, `select.value` |
| **Traversing DOM** | `element.parentNode`, `element.children`, `element.nextElementSibling`, `element.previousElementSibling` |
| **Cloning Elements** | `element.cloneNode(true)` |
| **Scrolling & Position** | `element.scrollIntoView()`, `element.offsetTop`, `element.getBoundingClientRect()` |
| **Timers & Animation** | `setTimeout(fn, ms)`, `setInterval(fn, ms)`, `requestAnimationFrame(fn)` |
| **Data Attributes** | `element.dataset.key`, `element.setAttribute('data-key', 'value')` |
| **Event Delegation** | `parent.addEventListener('click', e => { if(e.target.matches('button')) ... })` |

### 3. DOM in HTML

| Topic | Quick Reference / Notes |
|-------|------------------------|
| **What is DOM** | Document Object Model: a tree-like representation of HTML where each element is a node/object |
| **DOM in HTML** | Exists in all HTML pages; can be styled with CSS; structure is static without JS |
| **Why JavaScript is Needed** | To dynamically read/update content (`textContent`, `innerHTML`), modify attributes/styles, handle events, create/remove elements |
| **Selecting Elements** | `document.getElementById('id')`, `document.querySelector('.class')`, `document.querySelectorAll('div')` |
| **Traversing Elements** | `parentNode`, `children`, `nextElementSibling`, `previousElementSibling` |
| **Event Handling** | `element.addEventListener('click', fn)`, `element.onclick = fn` |
| **Creating/Removing Elements** | `document.createElement('div')`, `element.appendChild(child)`, `element.remove()` |
| **Attributes & Styling** | `element.setAttribute('attr', 'value')`, `element.getAttribute('attr')`, `element.style.color = 'red'`, `element.classList.add('class')` |
| **Common DOM Elements** | Text/Headings: `<h1>-<h6>`, `<p>`, `<span>`, `<div>`; Links: `<a>`, `<nav>`; Images/Media: `<img>`, `<video>`, `<audio>`; Lists: `<ul>`, `<ol>`, `<li>`; Forms/Inputs: `<form>`, `<input>`, `<textarea>`, `<select>`, `<option>`, `<button>`; Tables: `<table>`, `<tr>`, `<td>`, `<th>`; Sections/Layout: `<section>`, `<article>`, `<header>`, `<footer>`, `<aside>`; Embedded: `<iframe>`; Interactive/Semantic: `<label>`, `<fieldset>`, `<legend>`, `<details>`, `<summary>` |
| **Notes** | DOM exists even without JS; JS is needed for dynamic interaction |

