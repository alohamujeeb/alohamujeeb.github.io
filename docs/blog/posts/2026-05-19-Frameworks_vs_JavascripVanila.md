---
date: 
  created: 2026-05-18
  posted:  2025-05-18
author:
  name: Mujeeb
  description: Creator
readtime: 10

categories: 
  - Programming
tags:
   - vanilla JavaScript
   - frontend

---
# Vanialla JavaScript vs Frameworks

- This writing compares frontend frameworks such as Angular, React, and Vue.js with traditional web pages built using pure JavaScript (Vanilla JS).
<!-- more -->
- It highlights differences in development approach, structure, and scalability.

---
## 1. What is Vanilla JS 

- The DOM (Document Object Model) represents the structure of a web page as a tree of elements such as buttons, text, images, and containers.

- Web development is built using:

		HTML (structure)
		CSS (style)
		JavaScript (behavior)

- In plain JavaScript (commonly called Vanilla JS), we directly:
		read the DOM structure
		select elements
		attach event listeners
		update DOM elements manually when state changes

- In Vanilla JavaScript, we directly interact with the DOM by:
		sselecting elements
		listening to events
		updating the UI manually when data changes

<br> **So Vanilla JS simply means building web applications without using frontend frameworks.**



---
## 2. Why Vanilla JS becomes difficult

- As applications grow:

		- the DOM structure becomes more complex
		
		- multiple UI components depend on shared data
		
		- updates must stay consistent across different parts of the page
		
		- DOM manipulation logic gets repeated and harder to manage

- The main challenge is not writing JavaScript itself, but:
<br> **keeping application state and UI consistent as complexity increases.**


---
## 3. Why frameworks exist (an analogy)

We already accept this idea in other areas of computing:

		- We do not write everything in assembly language
		
		- We use higher-level languages like C/C++ for productivity and maintainability
		
		- We do not manually manage database storage at disk level

		- We use database systems like MySQL to handle complexity for us

- Similarly in frontend development, frameworks like **React, Vue.js, and Angular** provide a higher-level way to manage UI logic.

- They introduce abstractions that:
		
		- reduce manual DOM updates

		- help manage state consistently

		- provide structure for large applications

### Core idea

- We trade (actually throw-away) low-level control for:

		- structure
		
		- scalability
		
		- maintainability
		
		- predictable state management

This tradeoff becomes valuable when applications grow in size and complexity.

- In low-level programming:
	
		- we could write everything in assembly

		- but we use C/C++ and higher-level languages for productivity and safety

- In system design:

		- we could manage everything at raw machine/network level

		- but we use abstractions like databases, and web frameworks

- Similarly in frontend development:

		- we could manage DOM updates manually (Vanilla JS)

		- but we use frameworks like React, Vue.js, and Angular


---
## 4. Abstraction principle

- We trade low-level control for higher-level structure, productivity, and consistency.

- This tradeoff is only worth it when:

		- the system becomes large
		
		- coordination becomes complex
		
		- multiple parts depend on shared state

---
## 5. A practical example

<br> **Problem: Shopping cart with live UI updates**

- Imagine a simple e-commerce page with:

		- A list of products
		- A “Add to cart” button on each product
		- A cart icon in the navbar showing item count
		- A cart panel showing selected items
		- A total price display
		
- Now here is the key requirement:
	**Every change in the cart must update multiple parts of the UI instantly and consistently.**
	
	
### 5.1 Vanilla JS approach

- In Vanilla JavaScript, you typically do something like this:

		- Store cart data in a variable
		- Manually update the DOM whenever cart changes


``` JavaScript

let cart = [];

function addToCart(product) {
  cart.push(product);

  // update cart count
  document.getElementById("cartCount").textContent = cart.length;

  // update cart list
  const list = document.getElementById("cartList");
  list.innerHTML = "";

  cart.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item.name;
    list.appendChild(li);
  });

  // update total
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  document.getElementById("totalPrice").textContent = total;
}
```

- What is happening here? Every time state changes:
		
		we manually update cart count

		we manually rebuild cart list

		we manually recalculate and update total

		we must remember every place the UI depends on state
		

<br><font color='red'> **The real problem (not complexity, but coupling)**</font>


### 5.2 Vue approach

(Now the same logic using Vue.js)

``` html
<div id="app">

  <button v-for="product in products"
          @click="addToCart(product)">
    Add {{ product.name }}
  </button>

  <h3>Cart ({{ cart.length }})</h3>

  <ul>
    <li v-for="item in cart">
      {{ item.name }}
    </li>
  </ul>

  <p>Total: {{ total }}</p>

</div>

<script>
Vue.createApp({
  data() {
    return {
      products: [
        { name: "iPhone", price: 1000 },
        { name: "MacBook", price: 2000 }
      ],
      cart: []
    };
  },

  computed: {
    total() {
      return this.cart.reduce((sum, item) => sum + item.price, 0);
    }
  },

  methods: {
    addToCart(product) {
      this.cart.push(product);
    }
  }
}).mount("#app");
</script>

```

### 5.3 What is fundamentally different?

<br> **1. We stop describing UI updates**

| Vanilla JS                                             | Vue                         |
| ------------------------------------------------------ | --------------------------- |
| - update cart count<br>- update list<br>- update total | we only update state (cart) |



<br> **2. UI becomes a function of state**

| Vanilla JS                                     | Vue                             |
| ---------------------------------------------- | ------------------------------- |
| “When cart changes → manually update 3 places” | “UI is derived from cart state” |


---
## 6. Summary
In summary, Vanilla JavaScript requires developers to manually manage the relationship between application state and the user interface by directly updating the DOM whenever data changes. 

- As applications grow, this leads to repeated and tightly coupled UI update logic that becomes harder to maintain and keep consistent. In contrast, frameworks like React, Vue, and Angular shift this responsibility by allowing developers to focus on state, while the framework automatically keeps the UI in sync.

- Vanilla JS: 
		
		- manually updates multiple DOM elements whenever state changes
		
		- Complexity increases due to repeated and scattered UI update logic
		
		- Harder to maintain consistency as application grows

- Frameworks: 

		-UI is derived from state rather than manually updated
		
		-Developer focuses on state, framework handles UI synchronization automatically

---
## Relevant links

#### [JavaScript in Browser](../../web/fe/jsfe/index.md)
#### [Frameworks vs. Vanilla JS in the Age of AI](2025-10-22-JSframework_vs_Vanilla_AI.md)

