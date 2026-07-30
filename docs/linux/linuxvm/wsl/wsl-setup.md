---
hide:
  - navigation
  
  
tags:
  - WSL
  - Windows Subsystem for Linux
---

# Windows Subsystem for Linux (WSL) Quick Reference
This page provides quick-access cheat sheets for WSL installation and setup.

**Note: This is not an exhaustive guide—just a concise reference for commonly used commands.**

---
## 1. What is WSL
- Windows Subsystem for Linux (WSL) allows us to run a Linux environment directly on Windows without needing a virtual machine or dual boot.

- It lets you install and use Linux distributions (such as Ubuntu) alongside Windows tools, making it easy to run Linux commands, develop software, and manage files.

- This document is a quick reference of commands for installing and setting up WSL using Windows PowerShell.


---
## 2. Advantages and drawbacks

### 2.1 Advantages of WSL over VMware and VirtualBox

- WSL is lightweight and starts quickly, unlike traditional virtual machines (e.g., VMware or VirtualBox), which are more resource-heavy.

- Communication between Linux and Windows is much simpler in WSL (e.g., easy file access and command execution), compared to typical VM setups where integration can be more complex.

- WSL integrates well with Windows, allowing seamless switching between environments.

- We can install multiple WSL distributions (Ubuntu, Debian, custom ones, etc.); They run independently (each has its own filesystem, packages, users, etc.); They are lightweight compared to full VMs, so running many is usually feasible.



### 2.2 When NOT to use WSL

- When doing kernel-level development or modifications, since WSL does not provide full control over the Linux kernel.

- When you need full system virtualization (e.g., testing different OS kernels, custom drivers, or low-level system behavior).

- When running GUI-heavy Linux desktop environments or applications that require full GPU/driver control (a full VM may be more suitable depending on the use case).

- When strict isolation is required (e.g., security testing or sandboxing), where a full virtual machine is safer.


---
## 3. Installation 

**Set WSL 2 as default (recommended):**
```
wsl --set-default-version 2
```

| Description | Command / Method |
|------------|-----------------|
| Install WSL with default distro | `wsl --install` |
| Install a specific distro (PowerShell) | `wsl --install -d Ubuntu-20.04` |
| Install another distro (PowerShell) | `wsl --install -d Ubuntu-22.04` |
| Install another distro (PowerShell) | `wsl --install -d Ubuntu-24.04` |
| Install distro with custom name | `wsl --install -d Ubuntu-24.04 --name u24-mdc` |
| Start (launch) a distribution|wsl -d <DistroName>|
| Install distro via Microsoft Store | Open Store → search distro → Click Get / Install |


---
## 4. General commands

| Description | Command |
|------------|--------|
| List all installed distros (detailed: state + version) | `wsl -l -v` |
| List all installed distros (simple) | `wsl -l` |
| Launch a specific distro | `wsl -d Ubuntu-22.04` |
| Run a command in a specific distro | `wsl -d Ubuntu-22.04 ls -la` |
| Shut down all running distros | `wsl --shutdown` |
| Terminate a specific distro | `wsl --terminate Ubuntu-20.04` |
| Set default distro | `wsl --set-default Ubuntu-24.04` |
| Set default distro (custom name) | `wsl --set-default u24-mdc` |
| Set WSL version for a distro (1 or 2) | `wsl --set-version Ubuntu-22.04 2` |
| Set default WSL version for new installs | `wsl --set-default-version 2` |
| Show WSL status | `wsl --status` |
| Export a distro to a backup file | `wsl --export Ubuntu-22.04 backup.tar` |
| Import a distro from a backup | `wsl --import NewDistro C:\WSL\NewDistro backup.tar` |
| Unregister (delete) a distro ⚠️ | `wsl --unregister Ubuntu-20.04` |






