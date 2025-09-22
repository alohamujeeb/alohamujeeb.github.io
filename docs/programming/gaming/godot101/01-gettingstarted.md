# **01-Getting Started**

Main topics:

- Godot installation
- Four key concepts in Godot
- Hello world program
- How to run

---
## 1. **Godot Installation**

=== "Windows"

	1. Download from ```https://godotengine.org/download/windows/```
       The downloaded file is like ```Godot_v4.5-stable_win64.exe.zip```
    2. Extract the file using ```7z``` or any other utility
    3. If you downloaded an EXE installer, run it and follow prompts (or if it’s a portable EXE, just keep it where you want).

---
## 2. Key concepts
There are following fundamental concepts that we need to understand to work with Godot.
**(Do not worry if you do not understand them fully. They will become clear as we work along)**

1. **Nodes:**

    - Think of nodes like building blocks. 
    - Each node does one thing — like showing an image, playing a sound, or detecting input.
    - Nodes are arranged in a tree (like folders inside folders), where some nodes are "parents" and others are "children".

2. **Scenes:** 
    A scene is a group of nodes that work together.
    It could be anything:

    - A player character
    - A weapon
    - A main menu
    - A full game level
    - Scenes are reusable and nestable (you can put one scene inside another like LEGO pieces.)


3. **Scene tree:** 
    - The scene tree is the overall structure of your game at any moment.
    - It’s a tree of all active scenes (and their nodes) running together.
    - This is what Godot shows you when your game runs — everything in one big hierarchy.

4. **Signals:** 
    - Signals are how nodes talk to each other.
    - Instead of constantly checking (“Hey, did something happen?”), a node can emit a signal when something happens (like a button being pressed or a character getting hit.)
    - Other nodes can listen and react.


---
## 3. Write a Hello World program 

### 3.1 Create a project ```hello-world```
1. Click New Project (top-left).
2. Project Name: type ```hello-world```.
3. Project Path: pick a folder where it will live (e.g., C:\MyGodot\HelloWorld).
4. Renderer: leave as Compatibility (default).
5. Click Create & Edit.

### 3.2 Create the scene

1. In the **Scene** panel (top-left), click ➕ to add a new root node.
2. Choose (by searching) ```Node2D``` (it’s the basic 2D container).
3. Rename the node to ```Main``` (optional, but good practice).

### 3.3 Add a label

- With ```Main```(created in previous step) selected, click ➕ to add a child node.
- Search for ```Label``` and select it.
- In the **Inspector** (right panel), find the **Text** property → type: 
```console
Hello World
```

(to be continued.....)




