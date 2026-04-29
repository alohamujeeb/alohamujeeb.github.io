---
tags:
  - tmux
---

# TMUX (Terminal Multiplexer)
(This section is meant as a quick reference rather than a full tutorial)

---
## 1. What is tmux
- Normally, when we want to run programs, we use a terminal. If we want to run multiple programs, we open multiple terminal windows, and each one runs a separate program.

- tmux (short for terminal multiplexer) is a tool that lets us run and manage multiple terminal sessions inside a single terminal window.

- It allows us to organize our work into sessions, windows, and panes—all within one place.

---
## 2. Works like a background task
- With a normal terminal, if a user logs out or closes the session, the terminal is closed and any running programs will stop.

- However, tmux behaves differently. It keeps your sessions running in the background, even if you close the terminal or get disconnected.

- We can later reconnect to the same session and continue your work exactly where you left off.

---
## 3. Quick Reference

**Note: All shorthands start with Ctrl + b**

```
tmux

tmux new -s mysession	(Start a named session)

tmux ls

tmux attach -t mysession	(Attach to a session)

Ctrl + b, then d 	(Detach from a session)

Ctrl + b, then c	(Create a new window)

Ctrl + b, then n	(Switch to next window)

Ctrl + b, then p	(Switch to previous window)

Ctrl + b, then ,	(Rename a window)

Ctrl + b, then "	(Split pane horizontally)

Ctrl + b, then %	(Split pane vertically)

Ctrl + b, then arrow keys	(Move between panes)

exit	(Close a pane)

tmux kill-session -t mysession	(Kill a tmux session)

tmux kill-server	(Kill all servers)

```

---
## 4. Who is tmux useful for?

- Developers: Running editors, servers, logs, and builds at the same time without opening many terminals.

- System administrators / DevOps engineers: Managing remote servers over SSH, especially when connections may drop.

- Anyone running long tasks: Like scripts, data processing, or training jobs that should keep running even if the terminal is closed.

- People who prefer keyboard-driven workflows

- tmux helps avoid constantly switching between multiple terminal windows.

---
## 5. Why not use backgorund tasks instead of tmux?

- We start a process in the background; It keeps running after you close the terminal;

- **But we lose easy interaction with it**

- So, with background tasks, following are difficult:

	-see live output cleanly
	
	-interact with the program (menus, prompts, debugging)
	
	-manage multiple related processes together



