---
tags:

---

# 01. Getting started

---
## 1. Installation

### 1.1. Vue.js Installation Modes

Vue.js offers multiple installation modes to fit different development needs.
You can start instantly in the browser or set up a full project using modern build tools like Vite or the Vue (to be covered later)


| Mode | How it Works | When to Use | Pros | Cons |
|------|---------------|-------------|------|------|
| **1. CDN (Direct Script Tag)** | Add `<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>` in HTML | Quick demos, learning, small static pages | ✅ No setup<br>✅ Works instantly in browser | ❌ Needs internet (unless downloaded)<br>❌ No build system or modular code |
| **2. NPM / Vite (Module Mode)** | Install via `npm install vue` and import in JS (`import { createApp } from 'vue'`) | Real projects using bundlers like **Vite** or **Webpack** | ✅ Modern ES modules<br>✅ Works with build tools & frameworks | ❌ Requires Node.js and build setup |
| **3. Vue CLI (Legacy Tool)** | Use `npm install -g @vue/cli` → `vue create my-app` | Older Vue 2/early Vue 3 projects | ✅ Complete scaffolding (router, store, tests) | ❌ Heavier and slower than Vite<br>❌ Not preferred for new projects |

---
## 2. ```Hello World``` application

- We use CDN method (as describned in the previous section), which is simplest one.

- 





--- 
## Some relevant links

[vue official website](https://vuejs.org/)

[vue playground](https://play.vuejs.org)
